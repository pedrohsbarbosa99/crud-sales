import csv
from typing import List

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from crud_sales.core.models import Sale
from crud_sales.djninja.schema import (
    NotFoundSchema,
    SaleByStateSchema,
    SaleIdSchema,
    SaleSchema,
)

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

@api.get("/sales/state", response=List[SaleByStateSchema], auth=JWTAuth())
def sales_by_state(request):
    print(request.user)
    sales = (
        Sale.objects.values("state")
        .annotate(total_price=Sum("total"))
        .order_by("total_price")
        .filter(status="COMPRA")
    )
    data = [
        {"state": item["state"], "total": float(item["total_price"])} for item in sales
    ]
    return data


@api.get("/download_csv", auth=JWTAuth())
def download_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="sales.csv"'},
    )
    writer = csv.writer(response)
    sales = sales_by_state(request)
    writer.writerow(["Estado", "Total vendido"])
    for sale in sales:
        writer.writerow(
            [
                sale["state"],
                round(sale["total"], 2),
            ]
        )
    return response


@api.get("/sales", response=List[SaleIdSchema], auth=JWTAuth())
def get_sales(request, limit: int = 100):
    return Sale.objects.all()[:limit]


@api.get("/sales/{sale_id}", response={200: SaleIdSchema, 404: NotFoundSchema})
def get_sale(request, sale_id: int):
    try:
        return Sale.objects.get(id=sale_id)
    except Sale.DoesNotExist as e:
        return 404, {"message": f"Sale does not exist"}


@api.post("/sales", auth=JWTAuth())
def create_sale(request, data: SaleSchema):
    qs = Sale.objects.create(**data.dict())
    return {"sale": qs.id}


@api.put("/sales/{sale_id}", auth=JWTAuth())
def update_sale(request, sale_id: int, payload: SaleIdSchema):
    sale = get_object_or_404(Sale, id=sale_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(sale, attr, value)
    sale.save()
    return {"Success": True}


@api.delete("/sales/{sale_id}", auth=JWTAuth())
def delete_sale(request, sale_id: int):
    Sale.objects.filter(id=sale_id).delete()
    return {"Success": sale_id}

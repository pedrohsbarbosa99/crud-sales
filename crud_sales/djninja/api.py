import csv
from typing import List

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from django.db.utils import IntegrityError

from crud_sales.core.models import Sale
from crud_sales.djninja.schema import NotFoundSchema, SaleByStateSchema, SaleSchema

api = NinjaAPI()


@api.get("/sales_by_state", response=List[SaleByStateSchema])
def sales_by_state(request):
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


@api.get("/download_csv")
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
                sale["total"],
            ]
        )
    return response


@api.get("/sales", response=List[SaleSchema])
def get_sales(request):
    return Sale.objects.all()


@api.get("/sales/{sale_id}", response={200: SaleSchema, 404: NotFoundSchema})
def get_sale(request, sale_id: int):
    try:
        return Sale.objects.get(id=sale_id)
    except Sale.DoesNotExist as e:
        return 404, {"message": "Sale does not exist"}


@api.post("/sales")
def create_sale(request, data: SaleSchema):
    try:
        qs = Sale.objects.create(**data.dict())
    except IntegrityError as e:
        return {"Failed": "Sale id already exists"}
    return {"sale": qs.id}


@api.put("/sales/{sale_id}")
def update_sale(request, sale_id: int, payload: SaleSchema):
    sale = get_object_or_404(Sale, id=sale_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(sale, attr, value)
    sale.save()
    return {"Success": True}


@api.delete("/sales/{sale_id}")
def delete_sale(request, sale_id: int):
    Sale.objects.filter(id=sale_id).delete()
    return {"Success": sale_id}

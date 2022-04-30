import csv
from typing import List

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from crud_sales.core.models import Sale
from crud_sales.djninja.schema import SaleByStateSchema, SaleSchema

api = NinjaAPI()


@api.get("/sales_by_state", response=List[SaleByStateSchema])
def sales_by_state(request):
    sales = (
        Sale.objects.values("state")
        .annotate(total_price=Sum("total"))
        .order_by("total_price")
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
    sales = Sale.objects.all()
    for sale in sales:
        writer.writerow(
            [
                sale.sale_id,
                sale.created_at,
                sale.total,
                sale.status,
                sale.products_count,
                sale.state,
            ]
        )
    return response


@api.get("/sales", response=List[SaleSchema])
def get_sales(request):
    return Sale.objects.all()

@api.get("/sales/{sale_id}", response=SaleSchema)
def get_sale(request, sale_id: int):
    return Sale.objects.get(sale_id=sale_id)


@api.post("/sales")
def create_sale(request, data: SaleSchema):
    qs = Sale.objects.create(**data.dict())
    return {"sale": qs.sale_id}


@api.put("/sales/{sale_id}")
def update_sale(request, sale_id: int, payload: SaleSchema):
    sale = get_object_or_404(Sale, sale_id=sale_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(sale, attr, value)
    sale.save()
    return {"Success": True}


@api.delete("/sales/{sale_id}")
def delete_sale(request, sale_id: int):
    Sale.objects.filter(sale_id=sale_id).delete()
    return {"Success": sale_id}

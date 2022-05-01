import pytest
from crud_sales.core.models import Sale
from django.utils.timezone import make_aware
from datetime import datetime


@pytest.fixture
def single_sale(db):
    sale_date = datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    return Sale.objects.create(
        id=123,
        created_at=make_aware(sale_date),
        total=100.99,
        status="COMPRA",
        products_count=5,
        state="Pará",
    )

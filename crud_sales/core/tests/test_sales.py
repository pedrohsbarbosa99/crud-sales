from crud_sales.core.models import Sale

from .fixtures import single_sale


def test_insert_single_sale(single_sale):
    get_sale = Sale.objects.all().first()
    assert single_sale == get_sale

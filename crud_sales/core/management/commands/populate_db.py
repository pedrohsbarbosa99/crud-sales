from datetime import datetime
import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware


from crud_sales.core.models import Sale


def build_data(row):
    sale_date = datetime.strptime(f"{row[2]} {row[3]}", "%Y-%m-%d %H:%M")
    return {
        "sale_id": int(f"{row[0]}{row[1]}"),
        "created_at": make_aware(sale_date),
        "total": row[4],
        "status": row[5],
        "products_count": row[6],
        "state": row[7],
    }

def skip_rows(reader, rows=1):
    [next(reader) for _ in range(rows)]

class Command(BaseCommand):
    help = "Create sales from csv file"

    def handle(self, *args, **kwargs):
        datafile = os.path.join(
            settings.BASE_DIR, "data", "data-HQvSmRz8z8RCA5aFm4Jj5.csv"
        )

        sales = []
        with open(datafile) as file:
            reader = csv.reader(file)
            skip_rows(reader, rows=3)
            for row in reader:
                if len(row) == 8 and row[1].isdigit():
                    try:
                        data = build_data(row)
                    except ValueError:
                        pass
                    sales.append(Sale(**data))
        
        Sale.objects.bulk_create(sales)

from django.db import models
class Sale(models.Model):
    sale_id = models.IntegerField()
    created_at = models.DateTimeField()
    total = models.FloatField()
    status = models.CharField(max_length=50)
    products_count = models.IntegerField()
    state = models.CharField(max_length=50)

    class Meta:
        db_table = "sales"
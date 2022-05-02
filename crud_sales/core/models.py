from django.db import models
class Sale(models.Model):
    created_at = models.DateTimeField(verbose_name='Data de Criacao')
    total = models.FloatField(verbose_name="Total venda")
    status = models.CharField(max_length=50, verbose_name="Status Venda")
    products_count = models.IntegerField(verbose_name='Quantidade de produtos')
    state = models.CharField(max_length=50, verbose_name='Estado')

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        db_table = "sales"
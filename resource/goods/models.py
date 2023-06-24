from django.db import models

# Create your models here.
class Goods(models.Model): #ตารางเก็บรายละเอียดสินค้า
    id = models.CharField(primary_key=True, db_column='Goods_id', max_length=10)
    name = models.CharField(db_column="Goods_name", max_length=30)
    cost = models.DecimalField(max_digits=8, decimal_places=2, db_column="cost_unit" ,default=0)

    class Meta:
        verbose_name_plural  = "Goods"
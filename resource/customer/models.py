from django.db import models

class Customer(models.Model):  #ตารางเก็บรายละเอียดลูกค้า
    id = models.CharField(primary_key=True, db_column="Cus_id", max_length=5)
    name = models.CharField(db_column="Cus_name", max_length=30)
# Create your models here.

from django.db import models

from customer.models import Customer
from goods.models import Goods


class Order(models.Model):  
    """เก็บรายละเอียดคำสั่งซื้อ""" 
    id = models.CharField(primary_key=True, db_column='Order_no', max_length=4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='Cus_id' )
    date = models.DateTimeField(auto_created=True, db_column="Order_Date")

    class Meta:
        db_table = "H_ORDER"


class Detail(models.Model): 
    order = models.ForeignKey(Order, db_column='Order_no', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, db_column='Goods_id',on_delete=models.CASCADE)
    order_date = models.DateTimeField(db_column='Ord_date')
    send_date = models.DateTimeField(db_column='Fin_date')
    amount = models.DecimalField(db_column='Amount', max_digits=8, decimal_places=2)
    cost = models.DecimalField(db_column='COST_UNIT', max_digits=8, decimal_places=2)
    total = models.DecimalField(db_column='TOT_PRC', max_digits=10, decimal_places=2)

    class Meta:
        db_table = "D_ORDER"
        constraints = [
            models.UniqueConstraint(fields=['order', 'goods'], name='order_goods_uniq'),
        ]


class Masterorder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='Cus_id')
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE, db_column='Goods_id')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # date_doc = models.DateTimeField(db_column='Doc_date')
    
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    # date_order = models.DateTimeField(db_column='Ord_date')
    # date_send = models.DateTimeField(db_column='Fin_date')
    
    date_sys = models.DateTimeField(db_column='Sys_date')
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)
    cost = models.DecimalField(db_column='cost_tot', max_digits=10, decimal_places=2)

    class Meta:
        db_table = "M_ORDER"

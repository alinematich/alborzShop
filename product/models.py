from django.db import models

class Product(models.Model):

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    name = models.CharField('شرح کالا', max_length=200)
    base_price = models.IntegerField('قیمت پایه')
    off_cash_percent = models.IntegerField('درصد تخفیف نقدی')
    customer_price = models.IntegerField('قیمت مصرف‌کننده')
    description = models.CharField('توضیحات',max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def off_cash_price(self):
        return self.base_price * (100-self.off_cash_percent) / 100.0
    off_cash_price.short_description='قیمت نهایی'

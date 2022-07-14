from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Product

admin.site.site_header = 'مدیریت فروشگاه البرز'
class BasePriceListFilter(admin.SimpleListFilter):
    title = _('قیمت پایه')
    parameter_name = 'basePriceFilter'

    def lookups(self, request, model_admin):
        return (
            ('0-20000', _('0-20000')),
            ('20000-40000', _('20000-40000')),
            ('40000-60000', _('40000-60000')),
            ('60000-80000', _('60000-80000')),
            ('80000-500000', _('80000-500000')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-20000':
            return queryset.filter(base_price__gte=0, base_price__lte=20000)
        if self.value() == '20000-40000':
            return queryset.filter(base_price__gte=20000, base_price__lte=40000)
        if self.value() == '40000-60000':
            return queryset.filter(base_price__gte=40000, base_price__lte=60000)
        if self.value() == '60000-80000':
            return queryset.filter(base_price__gte=60000, base_price__lte=80000)
        if self.value() == '80000-500000':
            return queryset.filter(base_price__gte=80000, base_price__lte=500000)


class CustomerPriceListFilter(admin.SimpleListFilter):
    title = _('قیمت مصرف‌کننده')
    parameter_name = 'customerPriceFilter'

    def lookups(self, request, model_admin):
        return (
            ('0-20000', _('0-20000')),
            ('20000-40000', _('20000-40000')),
            ('40000-60000', _('40000-60000')),
            ('60000-80000', _('60000-80000')),
            ('80000-500000', _('80000-500000')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-20000':
            return queryset.filter(customer_price__gte=0, customer_price__lte=20000)
        if self.value() == '20000-40000':
            return queryset.filter(customer_price__gte=20000, customer_price__lte=40000)
        if self.value() == '40000-60000':
            return queryset.filter(customer_price__gte=40000, customer_price__lte=60000)
        if self.value() == '60000-80000':
            return queryset.filter(customer_price__gte=60000, customer_price__lte=80000)
        if self.value() == '80000-500000':
            return queryset.filter(customer_price__gte=80000, customer_price__lte=500000)


class NameListFilter(admin.SimpleListFilter):
    title = _('نام کالا')
    parameter_name = 'nameFilter'

    def lookups(self, request, model_admin):
        return (
            ('ا', _('ا')),
            ('ب', _('ب')),
            ('پ', _('پ')),
            ('ت', _('ت')),
            ('ث', _('ث')),
            ('ج', _('ج')),
            ('چ', _('چ')),
            ('ح', _('ح')),
            ('خ', _('خ')),
            ('د', _('د')),
            ('ذ', _('ذ')),
            ('ر', _('ر')),
            ('ز', _('ز')),
            ('ژ', _('ژ')),
            ('س', _('س')),
            ('ش', _('ش')),
            ('ص', _('ص')),
            ('ض', _('ض')),
            ('ط', _('ط')),
            ('ظ', _('ظ')),
            ('ع', _('ع')),
            ('غ', _('غ')),
            ('ف', _('ف')),
            ('ق', _('ق')),
            ('ک', _('ک')),
            ('گ', _('گ')),
            ('ل', _('ل')),
            ('م', _('م')),
            ('ن', _('ن')),
            ('و', _('و')),
            ('ه', _('ه')),
            ('ی', _('ی')),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(name__startswith=self.value())

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'base_price', 'off_cash_percent', 'customer_price', 'description']
    list_display = ('name', 'base_price', 'off_cash_percent', 'off_cash_price','customer_price', 'description')
    search_fields = ['name', 'base_price', 'off_cash_percent', 'customer_price', 'description']
    list_filter = (BasePriceListFilter, CustomerPriceListFilter, 'off_cash_percent', NameListFilter)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Product, ProductAdmin)
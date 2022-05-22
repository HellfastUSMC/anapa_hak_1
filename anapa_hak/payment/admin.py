from django.contrib.admin import ModelAdmin, register

from payment.models import *


@register(Good)
class GoodAdmin(ModelAdmin):
    pass
@register(Transaction)
class TransactionAdmin(ModelAdmin):
    pass
@register(Wallet)
class WalletAdmin(ModelAdmin):
    pass
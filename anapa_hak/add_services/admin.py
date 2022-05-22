from django.contrib.admin import ModelAdmin, register

from add_services.models import *


@register(Poll)
class PollAdmin(ModelAdmin):
    pass
@register(News)
class NewsAdmin(ModelAdmin):
    pass
@register(Menu)
class MenuAdmin(ModelAdmin):
    pass
@register(Activity)
class ActivityAdmin(ModelAdmin):
    pass
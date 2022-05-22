from django.contrib.admin import ModelAdmin, register

from users.models import *

# TODO: initial data
#from .models import User
#admin.site.register(User, UserAdmin)

@register(Shift)
class ShiftAdmin(ModelAdmin):
    pass
@register(Team)
class TeamAdmin(ModelAdmin):
    pass
@register(Placement)
class PlacementAdmin(ModelAdmin):
    pass
@register(Achivements)
class AchivementsAdmin(ModelAdmin):
    pass
@register(Administrator)
class AdministratorAdmin(ModelAdmin):
    pass
@register(Supervisor)
class SupervisorAdmin(ModelAdmin):
    pass
@register(Parent)
class ParentAdmin(ModelAdmin):
    pass
@register(Kid)
class KidAdmin(ModelAdmin):
    pass
from django.contrib import admin
from core.models import Cohort, Day, AgendaItem, GuestLecture


# Register your models here.
admin.site.register(Cohort)
admin.site.register(Day)
admin.site.register(AgendaItem)
admin.site.register(GuestLecture)


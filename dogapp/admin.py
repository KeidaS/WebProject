from django.contrib import admin
from dogapp import models

admin.site.register(models.Dog)
admin.site.register(models.Vaccine)
admin.site.register(models.Refuge)
admin.site.register(models.Adoption)
#admin.site.register(models.Race)


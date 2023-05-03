from django.contrib import admin
from mainapp.models import(
    Company, Jobs, Events, Video
) 

admin.site.register(Company)
admin.site.register(Jobs)
admin.site.register(Events)
admin.site.register(Video)
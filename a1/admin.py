from django.contrib import admin

# Register your models here.
from .models import ImageList,PostNews,VideoList,PostCompetition,ImageList1,VideoList1

admin.site.register(VideoList1)
admin.site.register(ImageList1)
admin.site.register(PostCompetition)
admin.site.register(ImageList)
admin.site.register(PostNews)
admin.site.register(VideoList)
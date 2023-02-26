from django.contrib import admin
from .models import Female,Male,User,Product

# Register Your Models Here
admin.site.register(Female)
admin.site.register(Male)
admin.site.register(User)
admin.site.register(Product)
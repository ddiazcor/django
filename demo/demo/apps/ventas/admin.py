from django.contrib import admin

# Register your models here.

from demo.apps.ventas.models import cliente, producto

admin.site.register(cliente)
admin.site.register(producto)

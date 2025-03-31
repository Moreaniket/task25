from django.contrib import admin

# Register your models here.
from .models import student,address,skill,candidate,author,book,shubham
admin.site.register([student,address,skill,candidate,author,book,shubham])

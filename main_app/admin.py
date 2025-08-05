from django.contrib import admin
from .models import Expense, Deposit

# Register your models here.
admin.site.register(Expense)
admin.site.register(Deposit)

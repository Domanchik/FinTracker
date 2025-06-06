from django.contrib import admin
from .models import Category, Expense, Income

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'description', 'date')
    list_filter = ('category', 'date')
    search_fields = ('description',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'source', 'date')
    list_filter = ('date',)
    search_fields = ('source',)

from rest_framework import serializers
from .models import Category, Expense, Income


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Expense
        exclude = ('user',)


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        exclude = ('user',)

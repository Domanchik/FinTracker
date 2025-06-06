import django_filters
from .models import Expense, Income

class ExpenseFilter(django_filters.FilterSet):
    date_after = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    date_before = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['category', 'date_after', 'date_before', 'description']


class IncomeFilter(django_filters.FilterSet):
    date_after = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    date_before = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    source = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Income
        fields = ['source', 'date_after', 'date_before', 'description']

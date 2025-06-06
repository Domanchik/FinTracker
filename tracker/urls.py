from django.urls import path
from .views import ExpenseCreateAPIView, IncomeCreateAPIView, SummaryAPIView

urlpatterns = [
    path('expenses/create/', ExpenseCreateAPIView.as_view(), name='expense-create'),
    path('incomes/create/', IncomeCreateAPIView.as_view(), name='income-create'),
    path('summary/', SummaryAPIView.as_view(), name='summary'),
]

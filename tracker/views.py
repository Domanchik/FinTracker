from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters, views, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from .filters import ExpenseFilter, IncomeFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum


@extend_schema(summary='Создание расхода')
class ExpenseCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. Создание дохода
@extend_schema(summary='Создание дохода')
class IncomeCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ExpenseFilter  # для примера, смотри ниже
    search_fields = ['description']

    def get(self, request):
        user = request.user

        # Фильтры по GET параметрам
        date_after = request.GET.get('date_after')
        date_before = request.GET.get('date_before')

        expenses = Expense.objects.filter(user=user)
        incomes = Income.objects.filter(user=user)

        if date_after:
            expenses = expenses.filter(date__gte=date_after)
            incomes = incomes.filter(date__gte=date_after)
        if date_before:
            expenses = expenses.filter(date__lte=date_before)
            incomes = incomes.filter(date__lte=date_before)

        # Поиск по описанию (пример)
        search = request.GET.get('search')
        if search:
            expenses = expenses.filter(description__icontains=search)
            incomes = incomes.filter(description__icontains=search)

        total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
        total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
        total = total_income - total_expense

        # Можно дополнительно вернуть список расходов и доходов, если нужно

        return Response({
            "total_expense": total_expense,
            "total_income": total_income,
            "net_total": total,
        })

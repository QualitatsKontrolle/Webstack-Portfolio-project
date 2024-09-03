from rest_framework import serializers
from .models import Expense, Income, Budget, FinancialReport

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Budget
        fields = '__all__'


class FinancialReportSerializer(serializers.Modelserializer):
    class Meta:
        model = FinancialReport
        fields = '__all__'
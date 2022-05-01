
from django.urls import path 
from .views import (ListExpense, DetailExpense)

urlpatterns = [
    path('', ListExpense.as_view()),
    path('<int:id>', DetailExpense.as_view()),
]
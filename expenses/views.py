from cgitb import lookup
from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from .models import Expense
from .permissions import Is_owner
from .serializer import ExpenseSerializer

class ListExpense(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, Is_owner, )

    def perform_create(self, serializer):
        owner = self.request.user
        return self.serializer.save(owner = owner)

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field =  ('id')

    def perform_create(self, serializer):
        owner = self.request.user
        return self.serializer.save(owner = owner)

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

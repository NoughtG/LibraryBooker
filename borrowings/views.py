from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

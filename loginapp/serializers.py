from rest_framework import serializers
from myapp.models import Rating
from .models import Studentsregistration,tblSalesman

class Ratingform(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = ['rat']

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Studentsregistration
        fields=['name','email','phoneno','district','gender','dob','profileimg','football','cricket']

class salesmanserializer(serializers.ModelSerializer):
    class Meta:
        model=tblSalesman
        fields=['salesmanname','salesmancode','branch','profileimg']

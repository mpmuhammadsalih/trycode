from django import forms
from myapp.models import Registration
from .models import Employeedetails
from .models import tblSalesman,Studentsregistration

class Registrationform(forms.ModelForm):
    class Meta:
        model =Registration
        fields = ['name','address','phoneno','profileimg']
        # exclude =['phoneno']
class Employeedetailsform(forms.ModelForm):
    class Meta:
        model=Employeedetails
        fields=['employeename','employeeage','designation']


class salesmanform(forms.ModelForm):
    class Meta:
        model=tblSalesman
        fields=['salesmanname','salesmancode','branch','profileimg']

class studentsform(forms.ModelForm):
    class Meta:
        model=Studentsregistration
        fields=['name','email','phoneno','district','gender','dob','profileimg']


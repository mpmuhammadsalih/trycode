from django.contrib import admin
from .models import Employeedetails,tblSalesman,Studentsregistration,UserProfile,Token

# Register your models here.
admin.site.register(Employeedetails)
admin.site.register(tblSalesman)
admin.site.register(Studentsregistration)
admin.site.register(UserProfile)
admin.site.register(Token)

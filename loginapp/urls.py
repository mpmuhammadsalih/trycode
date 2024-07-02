

from django.urls import path,include
from .views import *

urlpatterns = [
    
     
     path('Registration/',Registratione.as_view()),
     path('Emplyeedetails/',Employeedetailsview.as_view()),
     path('Reglist/',Registrationlist.as_view(),name='abc'),
     path('Reglistdelete/<id>',Regdelete.as_view()),
     path('Regupdate/<data>',Regupdate.as_view(),name='regupdate'),
     path('Emplist/',Employeeslist.as_view()),
     path('salesman/',salesman.as_view()),
     path('salesmanlist/',salesmanlist.as_view(),name='sman'),
     path('salesmandelete/<id>',salesmandelete.as_view()),
     path('salesmandeletesoft/<id>',salesdeletesoft.as_view()),
     path('salesmanupdate/<id>',salesmanupdate.as_view(),name='salesupdate'),
     path('Studentsreg/',studentregistrationview.as_view()),
     path('Studentslist/',studentsnlist.as_view(),name='slist'),
     path('studentregupdate/<id>',Studentslistupdate.as_view(),name='supdate'),
     path('salesmanhome/',salesmanhomeview.as_view()),
     path('studentshome/',studentshomeview.as_view(),name='studenthome'),

     path('login/',UserLogin.as_view()),
     ## API PATH
     path('ratingadd/',Ratingadd.as_view()),
     path('studentsapi/',studentserializerview.as_view()),
     path('studentsapi/<id>',studentserializerview.as_view()),
     path('salesmanapi/',salesmanserializerview.as_view()),
     path('salesmanapi/<id>',salesmanserializerview.as_view())

     
     
]

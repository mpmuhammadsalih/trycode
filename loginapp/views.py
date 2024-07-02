from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from .forms import Registrationform,Employeedetailsform,salesmanform,studentsform
from .serializers import Ratingform,studentserializer,salesmanserializer
from myapp.models import Registration # type: ignore
from .models import Employeedetails,tblSalesman,Studentsregistration,UserProfile,Token
# from .forms import Employeedetails
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.contrib import messages
import json


class Myuser(View):
    def get(self,request):
        return HttpResponse('my user')

# Create your views here.
# class Mylogin(View):
#     def get(self,request):
#         return render(request,'common/login.html')
    
class Registratione(View):
    def get(self,request):
        return render(request,'common/registration.html')
    def post(self,request):
     form = Registrationform(request.POST,request.FILES)
     if form.is_valid():
        form.save()
        return render(request,'common/registration.html')
     
class Employeedetailsview(View):
    def get(self,request):
        return render(request,'common/employees.html')
    def post(self,request):
     form = Employeedetailsform(request.POST)
     if form.is_valid():
        form.save()
        return render(request,'common/employees.html')

class Registrationlist(View):
   def get(self,request):
        print("hello")
        reglist=Registration.objects.filter(is_active=True).all()
        print(reglist)
        return render (request,'common/Registrationlist.html',{'re':reglist})
   
class Employeeslist(View):
   def get(self,request):
        # print("hello")
        reglist=Employeedetails.objects.all()
        # print(reglist)
        return render (request,'common/Employeeslist.html',{'re':reglist})

class salesman(View):
    def get(self,request):
         return render(request,'common/salesman.html')
    def post(self,request):
     form = salesmanform(request.POST,request.FILES)
     if form.is_valid():
          st=form.save(commit=False)
          us=UserProfile.objects.create_user(username=request.POST.get("username"),password=request.POST.get("password"),user_type=request.POST.get("Roles"))
          st.user=us
          form.save()
          return render(request,'common/salesman.html')
    
class salesmanlist(View):
    def get(self,request):
         reglist=tblSalesman.objects.filter(is_active=True).all()
         return render (request,'common/salesmanlist.html',{'re':reglist})
    
class Regdelete(View):
    def get(self,request,id):
        reglist=Registration.objects.filter(id=id,is_active=True).first()
        return render(request,'common/reglistdeleteconfirm.html',{'reg':reglist})
    def post(self,request,id):
        reglist=Registration.objects.filter(id=id,is_active=True).first()
        reglist.is_active=False
        reglist.save()
        reglist=Registration.objects.filter(is_active=True).all()
        # print(reglist)
        return render (request,'common/Registrationlist.html',{'re':reglist})
    
class Regupdate(View):
    def get(self,request,data):
        print("hhhhhh",id)
        reglist=Registration.objects.filter(id=data,is_active=True).first()
        return render(request,'common/regupdate.html',{'reg':reglist})
    def post(self,request,data):
        reglist=Registration.objects.filter(id=data,is_active=True).first()
        form=Registrationform(request.POST,request.FILES,instance=reglist)
        if form.is_valid():
            form.save()
            return redirect('abc')

    
class salesmandelete(View):
    def get(self,request,id):
        saleslist=tblSalesman.objects.filter(id=id).first()
        return render (request,'common/salesmanlistdelete.html',{'reg':saleslist})
    def post(self,request,id):
        saleslist=tblSalesman.objects.filter(id=id).first()
        saleslist.delete()
        saleslist=tblSalesman.objects.all()
        return render (request,'common/salesmanlist.html',{'re':saleslist})
    
class salesdeletesoft(View):
    def get(self,request,id):
        reglist=tblSalesman.objects.filter(id=id,is_active=True).first()
        print(reglist)
        return render(request,'common/salesmandeletesoft.html',{'reg':reglist})
    def post(self,request,id):
        reglist=tblSalesman.objects.filter(id=id,is_active=True).first()
        reglist.is_active=False
        reglist.save()
        reglist=tblSalesman.objects.filter(is_active=True).all
        # print(reglist)
        return render (request,'common/salesmanlist.html',{'re':reglist})  

class salesmanupdate(View) :
    def get(self,request,id):
        reglist=tblSalesman.objects.filter(id=id,is_active=True) .first()
        print(reglist.salesmanname)
        return render(request,'common/salesmanupdate.html',{'reg':reglist})
    def post(self,request,id):
        reglist=tblSalesman.objects.filter(id=id,is_active=True).first()
        form=salesmanform(request.POST,request.FILES,instance=reglist)
        if form.is_valid():
            form.save()
            return redirect('sman')
        
class studentregistrationview(View):
    def get (self,request):
        return render(request,'common/Studentregistration.html')
    def post(self,request):
        # if (request.POST.get("Roles")=="STUDENT"):
            form = studentsform(request.POST,request.FILES)
            if form.is_valid():
                st=form.save(commit=False)
                st.football=request.POST.get("football")=='on'
                st.cricket=request.POST.get("cricket")=='on'
                print(request.POST.get("football"))
                print(request.POST.get("Roles"))
                us=UserProfile.objects.create_user(username=request.POST.get("username"),password=request.POST.get("password"),user_type=request.POST.get("Roles"))
                st.user=us
                st.save()
                return render(request,'common/Studentregistration.html')
            

        
class studentsnlist(View):
    def get(self,request):
         reglist=Studentsregistration.objects.filter(is_active=True).all()
         return render (request,'common/studentslist.html',{'re':reglist})
        

class Studentslistupdate(View):
    def get(self,request,id):
        reglist=Studentsregistration.objects.filter(id=id,is_active=True).first()
        return render(request,'common/studentregupdate.html',{'reg':reglist})
    def post(self,request,id):
        reglist=Studentsregistration.objects.filter(id=id,is_active=True).first()
        form=studentsform(request.POST,request.FILES,instance=reglist)
        if form.is_valid():
            st=form.save(commit=False)
            st.football=request.POST.get("football")=='on'
            st.cricket=request.POST.get("cricket")=='on'
            print(request.POST.get("football"))
            st.save()
            return redirect('slist') 

class studentsdeletesoft(View):
    def get(self,request,id):
        reglist=Studentsregistration.objects.filter(id=id,is_active=True).first()
        print(reglist)
        return render(request,'common/studentsdelete.html',{'reg':reglist})
    def post(self,request,id):
        reglist=Studentsregistration.objects.filter(id=id,is_active=True).first()
        reglist.is_active=False
        reglist.save()
        reglist=Studentsregistration.objects.filter(is_active=True).all
        # print(reglist)
        return render (request,'common/salesmanlist.html',{'re':reglist})    

class Ratingadd(APIView):
    def post(self,request):
        serializer=Ratingform(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class studentserializerview(APIView):
    def get(self,request,id=None):
        if id is not None:
            reglist=Studentsregistration.objects.filter(is_active=True,id=id).first()
            serializer=studentserializer(reglist)
            return Response(serializer.data)
        else:
            reglist=Studentsregistration.objects.filter(is_active=True).all()
            serializer=studentserializer(reglist,many=True)
            return Response(serializer.data)

    def post(self,request,id=None):
        serializer=studentserializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,id):
        reg=Studentsregistration.objects.filter(is_active=True,id=id).first()
        serializer=studentserializer(reg,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def patch(self,request,id):
        reg=Studentsregistration.objects.filter(is_active=True,id=id).first()
        serializer=studentserializer(reg,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class salesmanserializerview(APIView):
    def get(self,request,id=None):
        if id is not None:
            reglist=tblSalesman.objects.filter(is_active=True,id=id).first()
            serializer=salesmanserializer(reglist)
            return Response(serializer.data)
        else:
            reglist=tblSalesman.objects.filter(is_active=True).all()
            serializer=salesmanserializer(reglist,many=True)
            return Response(serializer.data)

    def post(self,request,id=None):
        serializer=salesmanserializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,id):
        reg=tblSalesman.objects.filter(is_active=True,id=id).first()
        serializer=salesmanserializer(reg,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def patch(self,request,id):
        reg=tblSalesman.objects.filter(is_active=True,id=id).first()
        serializer=salesmanserializer(reg,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
from django.contrib.auth.mixins import LoginRequiredMixin        
class salesmanhomeview(LoginRequiredMixin, View):
    login_url = '/user/login/'  # URL to redirect to if not logged in
    redirect_field_name = 'studenthome'  # Field name for the redirect URL

    def get(self, request):
        print("loginrequired")
        return render(request, 'common/salesmanhome.html')
    
class studentshomeview(LoginRequiredMixin,View):
    login_url = '/user/login/'  # URL to redirect to if not logged in
    redirect_field_name= 'studenthome'
    def get(self,request):
        print("loginrequired")
        return render(request,'common/studentshome.html')

class UserLogin(View):
    template_name ="common/login.html"
    def get(self, request):
        print("hello")
        return render(request, self.template_name)

    def post(self, request):
        print("post")
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
                        "STUDENT": "/user/studentshome",
                        "INSTITUTE":"user:loadinstitute",
                        "TEACHER":"user:loadteacher",
                    }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        print("usename",username)
        print("authenticate",authenticated)
        try:
            user = UserProfile.objects.get(username=username)
            print("hel")
        except UserProfile.DoesNotExist:
            response_dict[
                            "reason"
                        ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
            print("response_dict[reason]",response_dict["reason"])
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            print("response_dict[reason]",response_dict["reason"])
            return redirect(request.GET.get("from") or "/user/login")

        else:
            print("hello")
            login(request, authenticated) 
            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                        user=user, defaults={"session_dict": json.dumps(session_dict)}
                        )

            user_type = authenticated.user_type




            print("hai")
            print(user)
            print(user_type)

            return redirect(landing_page_url[user_type])
        # return redirect(request.GET.get("from"))
        return render(request,'common/login.html')
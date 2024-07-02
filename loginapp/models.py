from django.db import models

# Create your models here.
class Employeedetails(models.Model):
    employeename=models.CharField(max_length=50,null=True,blank=True)
    employeeage=models.CharField(max_length=50,null=True,blank=True)
    designation=models.CharField(max_length=50,null=True,blank=True)


class tblSalesman(models.Model):
    user=models.OneToOneField('UserProfile',on_delete=models.CASCADE,null=True,blank=True)
    salesmanname = models.CharField(max_length=100,null=True,blank=True)
    salesmancode= models.CharField(max_length=50,null=True,blank=True)
    branch=models.CharField(max_length=50,null=True,blank=True)
    profileimg=models.FileField(upload_to='images',null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

class Studentsregistration(models.Model):
    user=models.OneToOneField('UserProfile',on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phoneno=models.CharField(max_length=100,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    dob=models.CharField(max_length=100,null=True,blank=True)
    profileimg=models.FileField(upload_to='images',null=True,blank=True)
    football=models.BooleanField(default=False)
    cricket=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

import random, string, re, json
from datetime import datetime

from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
USER_TYPE_CHOICES={
    ("STUDENT","STUDENT"),
    ("SALESMAN","SALESMAN"),
    ("ADMIN","admin"),
    ("CLIENT","client")
}
STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Deactive"),
}

class UserProfile(AbstractUser):
    # username
    # email
    # password
    # first_name
    # gender = models.CharField(max_length=10, null=False, default="MALE")
    user_type = models.CharField(
        max_length=30, null=False, blank=True, choices=USER_TYPE_CHOICES
    )
    # # mobile_no = models.CharField(
    #     max_length=30, verbose_name="Mobile number", null=True, blank=True
    # )

    status = models.CharField(max_length=50, null=False, blank=True, default="REJECT")
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Token(models.Model):
    key = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(
        UserProfile,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    dict_ready = False
    data_dict = None

    def _init_(self, *args, **kwargs):
        self.dict_ready = False
        self.data_dict = None
        super(Token, self)._init_(*args, **kwargs)

    def generate_key(self):
        return "".join(
            random.choice(
                string.ascii_lowercase + string.digits + string.ascii_uppercase
            )
            for i in range(40)
        )

    def save(self, *args, **kwargs):
        if not self.key:
            new_key = self.generate_key()
            while type(self).objects.filter(key=new_key).exists():
                new_key = self.generate_key()
            self.key = new_key
        return super(Token, self).save(*args, **kwargs)

    def read_session(self):
        if self.session_dict == "null":
            self.data_dict = {}
        else:
            self.data_dict = json.loads(self.session_dict)
        self.dict_ready = True

    def update_session(self, tdict, save=True, clear=False):
        if not clear and not self.dict_ready:
            self.read_session()
        if clear:
            self.data_dict = tdict
            self.dict_ready = True
        else:
            for key, value in tdict.items():
                self.data_dict[key] = value
        if save:
            self.write_back()

    def set(self, key, value, save=True):
        if not self.dict_ready:
            self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def write_back(self):
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        if not self.dict_ready:
            self.read_session()
        return self.data_dict.get(key, default)

    def _str_(self):
        return str(self.user) if self.user else str(self.id)


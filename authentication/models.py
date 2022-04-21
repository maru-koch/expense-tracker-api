from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password = None):
        if username is None:
            raise TypeError('Username cannot be empty')
        if email is None:
            raise TypeError('Email cannot be empty')
        user = self.model(username = username, email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise ValueError('password cannot be None')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique = True, db_index=True)
    email = models.EmailField(max_length= 200, unique = True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def token(self):
        return ''
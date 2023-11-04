from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractUser
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Email field must be set.")
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    firts_name = models.CharField(max_length=70,null=True, blank=True)
    middle_name = models.CharField(max_length=70, null=True, blank=True)
    last_name = models.CharField(max_length=70, null=True, blank=True)
    phone_number = models.CharField(max_length=70, null=True, blank=True)
    adress = models.CharField(max_length=90, null=True, blank=True)
    username = models.EmailField(unique=True)
    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        if self.first_name:
            return self.first_name
        return self.email


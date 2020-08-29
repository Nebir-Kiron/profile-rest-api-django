from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


# created model manager
class CustomUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('User must have an email')
        email = email.lower()
        first_name = first_name.title()
        last_name = last_name.title()

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,first_name,last_name,password=None):
        user = self.create_user(
           email = email,
           first_name = first_name,
           last_name = last_name,
           password = password

        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# created the models for user
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=254,unique=True,verbose_name='email')
    first_name = models.CharField(max_length=150,verbose_name='first_name')
    last_name = models.CharField(max_length=150,verbose_name='last_name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =('first_name','last_name')

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return self.is_admin
    
    class Meta:
        verbose_name_plural = 'Users'
    

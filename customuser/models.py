from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(make_password(password))
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField( verbose_name='email address',max_length=255,unique=True,)
    full_name=models.CharField(max_length=255,null=True)
    username=models.CharField(max_length=255,null=True,unique=True)
    address=models.CharField(null=True,blank=True,max_length=100)
    last_login=models.DateField(auto_now_add=True,null=True)
    phone = models.CharField(blank=True,max_length=20)
    facebook=models.URLField(blank=True,null=True,max_length=255)
    instagram=models.URLField(blank=True,null=True,max_length=255)
    twitter=models.URLField(blank=True,null=True,max_length=255)
    website=models.URLField(blank=True,null=True,max_length=255)
    images=models.ImageField(default='avatar.jpg',upload_to='profile_Images')
    description=models.TextField(max_length=2000,null=True)
    volunteer = models.BooleanField(default=True)
    organization = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    otp = models.IntegerField(null=True,blank=True)
    activation_key = models.CharField(max_length=150,blank=True,null=True)
    active=models.BooleanField(default=False)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.organization

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

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

        user.set_password(password)
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
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    full_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True, unique=True)
    province = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=100, null=True)
    municipality = models.CharField(max_length=255, null=True)
    ward = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    last_login = models.DateField(auto_now_add=True, null=True)
    phone = models.CharField(blank=True, max_length=20)
    facebook = models.URLField(blank=True, null=True, max_length=255)
    instagram = models.URLField(blank=True, null=True, max_length=255)
    twitter = models.URLField(blank=True, null=True, max_length=255)
    website = models.URLField(blank=True, null=True, max_length=255)
    images = models.ImageField(
        default='avatar.jpg', upload_to='profile_Images')
    description = models.TextField(max_length=2000, null=True)
    volunteer = models.BooleanField(default=True)
    organization = models.BooleanField(
        default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    otp = models.IntegerField(null=True, blank=True)
    activation_key = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    identity = models.FileField(
        default='avatar.jpg', upload_to='Identity')
    verify = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    skills = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.staff

    @property
    def is_admin(self):

        return self.admin

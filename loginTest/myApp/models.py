from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, full_name, **extra_fields):
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name):
        return self.create_user(email, password, full_name=full_name, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', blank=False, null=False, unique=True)
    full_name = models.CharField('full_name', max_length=150, blank=False, null=False)
    display_name = models.CharField('display_name', max_length=150, blank=True, null=True)
    is_staff = models.BooleanField('is_staff', default=False)

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting '
                  'accounts.',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()


class Item(models.Model):
    name = models.CharField('name', max_length=150, blank=False)

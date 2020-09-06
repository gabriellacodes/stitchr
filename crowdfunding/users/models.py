from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_artist = models.BooleanField('artist status', default=False, help_text=_('Designates whether the user has artist access to post projects, etc.'))
    is_active = models.BooleanField('active', default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(default=False, help_text=_('Designates if the user has full permissions to this site.'))
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    customuser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    given_name = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=5)
    profile_photo = models.ImageField(upload_to='uploads', blank=True)
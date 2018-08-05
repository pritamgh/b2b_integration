from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit import models as imagekitmodels
from imagekit.processors import ResizeToFill

from django_libs import utils

from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone should in the format:'+999999999'.Upto 15 digits allowed.")


def upload_user_media_to(instance, filename):
    """Upload media files to this folder.

    Returns:
        String. Generated path for image.

    """
    return '{name}/{id}/{filename}'.format(
        name=instance.__class__.__name__.lower(),
        id=instance.id,
        filename=utils.get_random_filename(filename)
    )


class CustomUserManager(UserManager):

    def create_superuser(self, email, password, username='', **extra_fields):
        return super().create_superuser(username, email, password,
                                        **extra_fields)

    def create_user(self, email, username='', password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.

        This method overrides parent method to suppress ValidationError on
        empty ``username`` parameter as soon as we use email as username field
        """
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        blank=True,
        error_messages={
            'unique': _("A user with this email already exists."),
        },
        help_text=_('Email is used as internal username'),
    )
    username = models.CharField(
        verbose_name=_('Username'),
        blank=True,
        null=True,
        help_text=_('Display username'),
        max_length=255,
    )
    avatar = imagekitmodels.ProcessedImageField(
        upload_to=upload_user_media_to,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 100},
        editable=False,
        null=True,
        blank=True
    )
    contact = models.CharField(
        validators=[phone_regex],
        max_length=17,
        null=True,
        blank=True,
        verbose_name=_('Contact')
    )
    user_role = models.CharField(
        max_length=100,
        verbose_name=_('Role of User'),
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=100,
        verbose_name=_('User Status'),
        help_text=_('Any User is Blocked/Unblocked by Buyer'),
        blank=True,
        null=True
    )
    warehouse_exchange_id = models.CharField(
        max_length=100,
        verbose_name=_('ID of Warehouse Exchange'),
        blank=True,
        null=True
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.first_name:
            return '{self.first_name} {self.last_name}'.format(
                self=self).strip()
        return self.email

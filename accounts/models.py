from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom user model to store user profiles.
    """
    username = models.CharField(
        _("username"),
        max_length=20,
        unique=True,
        null=True,
        blank=False,
        db_index=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("That username is not available"),
        },
    )

    email = models.EmailField(
        _("email address"),
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        error_messages={
            "unique": _("That email is not available"),
        },
    )
    
    first_name = models.CharField(
        _("first name"), max_length=100, null=False, blank=False
    )
    
    last_name = models.CharField(
        _("last name"), max_length=100, null=False, blank=False
    )

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="user_custom_set",  # Custom related name to avoid clashes
        related_query_name="user_custom",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="user_custom_set",  # Custom related name to avoid clashes
        related_query_name="user_custom",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "username",
        "first_name",
        "last_name",
    )
    
    def create_user(self, email, username=None, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

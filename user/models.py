from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    # Add any additional fields you want to the user model
    role_choices = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
        ('author', 'Author'),
    )
    role = models.CharField(max_length=10, choices=role_choices, default='member')
    email = models.EmailField(unique=True, verbose_name=_("email address"))
   
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
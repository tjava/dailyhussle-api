from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from api.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=11, default="09022218455"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    age = models.IntegerField(
        verbose_name=_("Your Age"), max_length=2, blank=True, null=True
    )
    state = models.CharField(
        verbose_name=_("State"),
        max_length=180,
        default="Niger",
        blank=False,
        null=False,
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Minna",
        blank=False,
        null=False,
    )
    is_employer = models.BooleanField(
        verbose_name=_("Employer"),
        default=False,
        help_text=_("Are you looking to employ someone?"),
    )
    is_employee = models.BooleanField(
        verbose_name=_("Employee"),
        default=False,
        help_text=_("Are you looking for work?"),
    )
    top_employer = models.BooleanField(verbose_name=_("Top Employer"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

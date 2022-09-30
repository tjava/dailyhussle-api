# Generated by Django 3.2.15 on 2022-09-30 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='09022218455', max_length=11, region=None, verbose_name='Phone Number')),
                ('about_me', models.TextField(default='say something about yourself', verbose_name='About me')),
                ('profile_photo', models.ImageField(default='/profile_default.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20, verbose_name='Gender')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Your Age')),
                ('state', models.CharField(default='Niger', max_length=180, verbose_name='State')),
                ('city', models.CharField(default='Minna', max_length=180, verbose_name='City')),
                ('is_employer', models.BooleanField(default=False, help_text='Are you looking to employ someone?', verbose_name='Employer')),
                ('is_employee', models.BooleanField(default=False, help_text='Are you looking for work?', verbose_name='Employee')),
                ('top_employer', models.BooleanField(default=False, verbose_name='Top Employer')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of Reviews')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

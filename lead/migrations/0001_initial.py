# Generated by Django 2.1.4 on 2018-12-12 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_edit', models.DateTimeField(auto_now=True, null=True, verbose_name='last edit')),
                ('date_birthday', models.DateField(blank=True, null=True)),
                ('address_label', models.CharField(blank=True, max_length=50, verbose_name='address label')),
                ('address_line_1', models.CharField(blank=True, max_length=50, verbose_name='address line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=50, verbose_name='address line 2')),
                ('address_zip', models.CharField(blank=True, max_length=50, verbose_name='zipcode')),
                ('address_city', models.CharField(blank=True, max_length=50, verbose_name='city')),
                ('address_country', models.CharField(blank=True, max_length=50, verbose_name='country')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='phone')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='title')),
                ('role', models.CharField(blank=True, max_length=50, verbose_name='role')),
                ('organization', models.CharField(blank=True, max_length=50, verbose_name='organization')),
                ('url', models.CharField(blank=True, max_length=50, verbose_name='url')),
                ('note', models.TextField(blank=True, verbose_name='note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

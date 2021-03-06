# Generated by Django 3.1.5 on 2021-01-30 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity', models.TextField(max_length=200)),
                ('Company', models.TextField(max_length=200)),
                ('Stage_of_completion', models.TextField(max_length=200)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

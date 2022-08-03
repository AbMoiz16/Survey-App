# Generated by Django 4.0.6 on 2022-07-20 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
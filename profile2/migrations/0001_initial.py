# Generated by Django 3.2.5 on 2021-10-27 14:16

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
            name='Profile2',
            fields=[
                ('nickname', models.CharField(max_length=64, verbose_name='닉네임')),
                ('phone_number', models.CharField(max_length=12, verbose_name='전화번호')),
                ('university', models.CharField(max_length=32, null=True, verbose_name='대학교')),
                ('profile_photo', models.ImageField(blank=True, upload_to='', verbose_name='프로필사진')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
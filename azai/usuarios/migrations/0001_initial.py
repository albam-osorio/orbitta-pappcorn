# Generated by Django 2.0.7 on 2018-07-22 16:39

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('numero_identificacion', models.CharField(max_length=10, unique=True, verbose_name='n�mero identificaci�n')),
                ('telefono', models.CharField(max_length=50, verbose_name='tel�fono')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('grupo', models.ForeignKey(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.Group', verbose_name='grupo')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', usuarios.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Ocupación',
                'verbose_name_plural': 'Ocupaciones',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='ocupacion',
            field=models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.Ocupacion'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

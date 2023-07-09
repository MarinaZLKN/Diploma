# Generated by Django 4.2.3 on 2023-07-09 13:33

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ControlledBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('guest', 'Гость'), ('client', 'Клиент'), ('service_company', 'Сервисная организация'), ('manager', 'Менеджер')], max_length=15)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_users', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DrivingBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_factory_number', models.CharField(max_length=4)),
                ('engine_factory_number', models.CharField(max_length=100)),
                ('transmission_factory_number', models.CharField(max_length=100)),
                ('driving_bridge_factory_number', models.CharField(max_length=100)),
                ('controlled_bridge_factory_number', models.CharField(max_length=100)),
                ('delivery_contract', models.CharField(max_length=100)),
                ('shipment_date', models.DateField()),
                ('consignee', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=100)),
                ('equipment', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
                ('controlled_bridge_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.controlledbridgemodel')),
                ('driving_bridge_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.drivingbridgemodel')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.enginemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('user', models.OneToOneField(default='ООО ФНС', on_delete=django.db.models.deletion.CASCADE, to='backend.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_maintenance', models.DateField()),
                ('operating_time', models.IntegerField()),
                ('order_number', models.CharField(max_length=100)),
                ('data_of_order', models.DateField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.organization')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany')),
                ('type_of_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.typeofmaintenance')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany'),
        ),
        migrations.AddField(
            model_name='machine',
            name='technical_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.technicalmodel'),
        ),
        migrations.AddField(
            model_name='machine',
            name='transmission_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.transmissionmodel'),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_failure', models.DateField()),
                ('operating_time', models.IntegerField()),
                ('spare_parts_used', models.TextField(blank=True, default=None, null=True)),
                ('date_of_recovery', models.DateField()),
                ('technical_downtime', models.IntegerField(default=None)),
                ('description_of_failure', models.CharField(max_length=100)),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.failurenode')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.machine')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.recoverymethod')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.servicecompany')),
            ],
        ),
    ]

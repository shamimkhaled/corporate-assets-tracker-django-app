# Generated by Django 4.2.5 on 2023-09-22 16:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('condition', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='AssetIMG/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_mail', models.EmailField(max_length=50)),
                ('contact_info', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suplier_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.company')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='AssetAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_time', models.DateField()),
                ('return_time', models.DateField()),
                ('condition_on_checkout', models.CharField(max_length=100)),
                ('condition_on_return', models.CharField(blank=True, max_length=100, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.employee')),
            ],
            options={
                'verbose_name_plural': 'Assets Allocation',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.categorytype'),
        ),
        migrations.AddField(
            model_name='asset',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.supplier'),
        ),
    ]

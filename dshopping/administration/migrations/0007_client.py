# Generated by Django 2.2.4 on 2019-10-23 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20191023_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=150, verbose_name='Title')),
                ('lastname', models.CharField(max_length=150, verbose_name='Title')),
                ('phone', models.IntegerField(verbose_name='Quantity')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=150, verbose_name='Title')),
                ('credit_card_number', models.IntegerField(verbose_name='Quantity')),
                ('status', models.BooleanField(default=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Country')),
                ('id_gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Gender')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
# Generated by Django 2.2.4 on 2019-10-23 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_auto_20191023_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shopping_date', models.DateTimeField(auto_now_add=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Client')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Product')),
            ],
            options={
                'verbose_name': 'Shopping',
                'verbose_name_plural': 'Shoppings',
            },
        ),
    ]
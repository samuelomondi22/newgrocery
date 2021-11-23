# Generated by Django 3.2.8 on 2021-10-27 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_comment', models.TextField(max_length=250)),
                ('item_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_mall', models.CharField(choices=[('WALMART', 'Walmart'), ('BROULIM', 'Broulim'), ('ALBERTSON', 'Albertson')], default='WALMART', max_length=20)),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.grocery')),
            ],
        ),
    ]
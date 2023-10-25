# Generated by Django 4.2.5 on 2023-10-25 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shuttle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['capacity', 'color'],
            },
        ),
        migrations.CreateModel(
            name='ShuttleSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schd_time', models.TimeField()),
                ('schd_date', models.DateField()),
                ('shuttle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ticketing.shuttle')),
            ],
            options={
                'ordering': ['schd_date', 'schd_time'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular ticket purchased', primary_key=True, serialize=False)),
                ('purchased_date', models.DateField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('shuttle_schd_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ticketing.shuttleschedule')),
            ],
            options={
                'ordering': ['purchased_date'],
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('payment_status', models.CharField(choices=[('PAID', 'Paid'), ('CANCELEED', 'Cancelled'), ('PENDING', 'Pending'), ('NO_STATUS', 'No_status')], default='NO_STATUS', max_length=50)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular transaction', primary_key=True, serialize=False)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketing.ticket')),
            ],
            options={
                'ordering': ['payment_status', 'payment_method', 'amount'],
            },
        ),
    ]

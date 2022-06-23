# Generated by Django 4.0.5 on 2022-06-23 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('', 'Choose'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('', 'Choose'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField()),
                ('message', models.TextField(max_length=300, null=True)),
                ('date_sent', models.DateField(auto_now_add=True, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.patient')),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]

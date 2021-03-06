# Generated by Django 2.2 on 2019-05-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0020_employeeaccess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=255)),
                ('date', models.DateField()),
                ('ctc', models.CharField(max_length=255)),
                ('ectc', models.CharField(max_length=255)),
                ('resume', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('IN PROGRESS', 'In Progress'), ('TAKEN', 'Taken'), ('REJECTED', 'Rejected')], default='SCHEDULED', max_length=255)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Designation')),
            ],
            options={
                'verbose_name': 'Interview',
                'verbose_name_plural': 'Interviews',
            },
        ),
    ]

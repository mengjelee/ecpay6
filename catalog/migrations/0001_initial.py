# Generated by Django 3.1.1 on 2021-03-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('class_serial', models.CharField(blank=True, max_length=10, null=True)),
                ('subject', models.CharField(blank=True, choices=[('mth', 'Math'), ('chn', 'Chinese'), ('eng', 'English'), ('geo', 'Geography'), ('his', 'History'), ('cvc', 'Civics'), ('scl', 'Social'), ('es', 'Earth Science'), ('phy', 'Physics'), ('chem', 'Chemistry'), ('bio', 'Biography'), ('pnc', 'PhyChem'), ('prg', 'Programming'), ('art', 'Art'), ('oth', 'Others')], default='oth', max_length=10)),
                ('pay_per_class', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('pay_or_not', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('trade_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('trade_amt', models.IntegerField(blank=True, null=True)),
                ('trade_status', models.CharField(max_length=100)),
                ('trade_time', models.CharField(default='no record', max_length=100)),
                ('CheckMacValue', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('account', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('bank_account', models.IntegerField(blank=True, null=True)),
                ('bank_no', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Tutor'), (2, 'Student')])),
            ],
        ),
        migrations.CreateModel(
            name='Class_details',
            fields=[
                ('class_detail_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('class_date', models.DateField(null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('finish_or_not', models.BooleanField(default=False)),
                ('fee', models.IntegerField(blank=True, null=True)),
                ('class_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.class')),
            ],
        ),
        migrations.CreateModel(
            name='Class_DayTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('class_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='catalog.user'),
        ),
        migrations.AddField(
            model_name='class',
            name='trade_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.payment'),
        ),
        migrations.AddField(
            model_name='class',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_class', to='catalog.user'),
        ),
    ]

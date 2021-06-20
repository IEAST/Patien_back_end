# Generated by Django 3.2 on 2021-04-13 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_alter_doctors_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('Did', models.IntegerField(verbose_name='医生编号')),
                ('Uid', models.IntegerField(verbose_name='患者编号')),
                ('Esummary', models.TextField(verbose_name='急救小结')),
                ('Etime', models.DateTimeField(auto_now_add=True, verbose_name='急救时间')),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('Did', models.IntegerField(verbose_name='医生编号')),
                ('Uid', models.IntegerField(verbose_name='患者编号')),
                ('EDid', models.IntegerField(verbose_name='检查医生编号')),
                ('Ename', models.CharField(max_length=100, verbose_name='项目名称')),
                ('Eresult', models.TextField(verbose_name='检查结果')),
                ('Etime', models.DateTimeField(auto_now_add=True, verbose_name='检查时间')),
            ],
        ),
        migrations.CreateModel(
            name='Physiological',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('Did', models.IntegerField(verbose_name='护士编号')),
                ('Uid', models.IntegerField(verbose_name='患者编号')),
                ('Pinformation', models.TextField(verbose_name='生理信息')),
                ('Ptime', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('Did', models.IntegerField(verbose_name='护士编号')),
                ('Uid', models.IntegerField(verbose_name='患者编号')),
                ('Tprograms', models.TextField(null=True, verbose_name='治疗建议')),
                ('Ttime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='电话')),
                ('allergy', models.TextField(verbose_name='过敏情况')),
                ('remarks', models.TextField(verbose_name='其他注意事项')),
            ],
        ),
        migrations.AlterField(
            model_name='doctors',
            name='department',
            field=models.IntegerField(verbose_name='科室'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='user',
            field=models.CharField(max_length=30, unique=True, verbose_name='用户名'),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, verbose_name='token')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Patient.doctors')),
            ],
            options={
                'verbose_name': 'token表',
                'verbose_name_plural': 'token表',
                'db_table': 'token',
            },
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-15 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appanswer', '0002_auto_20200415_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FirstPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SecondPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='images/')),
                ('content', models.CharField(max_length=255)),
                ('ofFirstPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appanswer.FirstPage')),
            ],
        ),
        migrations.CreateModel(
            name='ImageOfFirstPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('ofFirstPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appanswer.FirstPage')),
            ],
        ),
    ]

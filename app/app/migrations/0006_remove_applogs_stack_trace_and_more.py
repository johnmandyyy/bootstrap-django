# Generated by Django 4.2.2 on 2024-06-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_routeexclusion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applogs',
            name='stack_trace',
        ),
        migrations.AlterField(
            model_name='applogs',
            name='execution_time',
            field=models.TextField(blank=True, default=0.0, null=True),
        ),
        migrations.CreateModel(
            name='StackTrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('app_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.applogs')),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-04 09:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='check',
            managers=[
                ('check_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='printer',
            managers=[
                ('printer_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(blank=True, upload_to='pdfs/'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-02-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_customer_school_alter_school_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_firstname_remove_member_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='reviewvotes',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_reviewvotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='reviewvotes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

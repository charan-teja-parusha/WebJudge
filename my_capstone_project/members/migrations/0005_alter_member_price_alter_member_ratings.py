# Generated by Django 4.1.7 on 2023-03-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_reviewvotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ratings',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-01 08:30

from django.db import migrations, models
import ocw.models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='state',
            field=models.CharField(choices=[('UNK', 'unkown'), ('ACTIVE', 'active'), ('DELETING', 'deleting'), ('DELETED', 'deleted')], default=ocw.models.StateChoice('unkown'), max_length=8),
        ),
        migrations.AlterField(
            model_name='instance',
            name='provider',
            field=models.CharField(choices=[('GCE', 'Google'), ('EC2', 'EC2'), ('AZURE', 'Azure')], max_length=8),
        ),
    ]

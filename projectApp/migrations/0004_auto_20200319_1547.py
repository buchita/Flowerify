# Generated by Django 3.0.4 on 2020-03-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_auto_20200308_1949'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image_uploader',
        ),
        migrations.RenameField(
            model_name='flower',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='flower',
            old_name='flowerName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='caption',
        ),
        migrations.AddField(
            model_name='flower',
            name='description',
            field=models.CharField(default='please add description', max_length=2000),
        ),
        migrations.AlterField(
            model_name='flower',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='flower',
            table='flower',
        ),
    ]

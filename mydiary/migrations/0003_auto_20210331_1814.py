# Generated by Django 3.1.7 on 2021-03-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0002_content_my_feeling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='my_feeling',
            field=models.CharField(choices=[('good', '좋음'), ('best', '매우 좋음'), ('bad', '나쁨'), ('angry', '화남'), ('tired', '피곤함')], default='good', max_length=5),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-03 17:37

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('PGapp', '0010_alter_hotelemployees_photo_alter_hotelrooms_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelrooms',
            name='picture_thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='D:/A_PYTHONPROJECTS/Revashing/folder/PGsite/media/img/room_thumbnail_default.png', upload_to=''),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_tag_tag_name_tag_usage_num_alter_answer_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers_count',
            field=models.IntegerField(default=0),
        ),
    ]

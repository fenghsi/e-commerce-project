# Generated by Django 2.0.7 on 2019-04-22 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentUser',
            fields=[
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Customer')),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
    ]

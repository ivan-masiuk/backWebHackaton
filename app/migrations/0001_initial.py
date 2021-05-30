# Generated by Django 3.2.3 on 2021-05-29 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='group-name', max_length=20)),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='fist-name', max_length=200)),
                ('last_name', models.CharField(default='last-name', max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('link_zoom', models.URLField(default='')),
            ],
            options={
                'verbose_name': 'Викладач',
                'verbose_name_plural': 'Викладачі',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='week-name', max_length=100)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='app.group')),
            ],
            options={
                'verbose_name': 'Тиждень',
                'verbose_name_plural': 'Тиждні',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tutors', models.ManyToManyField(to='app.Tutor')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмети',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='day-name', max_length=50)),
                ('lesson_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson1', to='app.lesson')),
                ('lesson_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson2', to='app.lesson')),
                ('lesson_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson3', to='app.lesson')),
                ('lesson_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson4', to='app.lesson')),
                ('lesson_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson5', to='app.lesson')),
                ('tutor_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_1', to='app.tutor')),
                ('tutor_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_2', to='app.tutor')),
                ('tutor_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_3', to='app.tutor')),
                ('tutor_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_4', to='app.tutor')),
                ('tutor_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_5', to='app.tutor')),
                ('week', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='days', to='app.week')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дні',
            },
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-29 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='tutor_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_1', to='account.tutor'),
        ),
        migrations.AlterField(
            model_name='day',
            name='tutor_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_2', to='account.tutor'),
        ),
        migrations.AlterField(
            model_name='day',
            name='tutor_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_3', to='account.tutor'),
        ),
        migrations.AlterField(
            model_name='day',
            name='tutor_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_4', to='account.tutor'),
        ),
        migrations.AlterField(
            model_name='day',
            name='tutor_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_5', to='account.tutor'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tutors',
            field=models.ManyToManyField(to='account.Tutor'),
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]

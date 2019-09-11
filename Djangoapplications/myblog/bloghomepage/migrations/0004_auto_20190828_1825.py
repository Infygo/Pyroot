# Generated by Django 2.2.4 on 2019-08-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloghomepage', '0003_cities_citypics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='citypics',
            field=models.ImageField(default='media/images/black.jpg', upload_to='images/'),
        ),
        migrations.CreateModel(
            name='MoviesSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=100)),
                ('moviedescription', models.TextField(max_length=2000)),
                ('moviequote', models.CharField(max_length=100)),
                ('moviepic', models.ImageField(default='media/images/black.jpg', upload_to='images/')),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloghomepage.Content')),
            ],
        ),
    ]

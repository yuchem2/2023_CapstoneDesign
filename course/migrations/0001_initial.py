# Generated by Django 4.2.6 on 2023-10-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(db_column='bookID', primary_key=True, serialize=False)),
                ('bookname', models.CharField(blank=True, db_column='bookName', max_length=200, null=True)),
                ('author', models.CharField(max_length=100)),
                ('published', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('campus', models.CharField(max_length=15)),
                ('courseid', models.CharField(db_column='courseID', max_length=8)),
                ('subid', models.CharField(db_column='subID', max_length=4)),
                ('division', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=100)),
                ('coursename', models.CharField(db_column='courseName', max_length=200)),
                ('professor', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseBook',
            fields=[
                ('relationid', models.AutoField(db_column='relationID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'course_book',
                'managed': False,
            },
        ),
    ]
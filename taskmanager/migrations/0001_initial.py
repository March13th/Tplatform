# Generated by Django 2.1.4 on 2019-11-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casemodify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('version', models.CharField(blank=True, max_length=50, null=True)),
                ('reviser', models.CharField(blank=True, max_length=50, null=True)),
                ('modify', models.CharField(blank=True, max_length=255, null=True)),
                ('modifydate', models.DateField(blank=True, null=True)),
                ('modifytime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'casemodify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Caseversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'caseversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FcaseCipsFunction',
            fields=[
                ('name1', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=15)),
                ('relatecase', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.CharField(blank=True, max_length=600, null=True)),
                ('operation', models.CharField(blank=True, max_length=1200, null=True)),
                ('result', models.CharField(blank=True, max_length=600, null=True)),
                ('name2', models.CharField(max_length=30)),
                ('name3', models.CharField(max_length=30)),
                ('name4', models.CharField(max_length=30)),
                ('name5', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'fcase_cips_function',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FcaseCtcFunction',
            fields=[
                ('name1', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=15)),
                ('relatecase', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.CharField(blank=True, max_length=600, null=True)),
                ('operation', models.CharField(blank=True, max_length=1200, null=True)),
                ('result', models.CharField(blank=True, max_length=600, null=True)),
                ('name2', models.CharField(max_length=30)),
                ('name3', models.CharField(max_length=30)),
                ('name4', models.CharField(max_length=30)),
                ('name5', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'fcase_ctc_function',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('product', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('keycn', models.CharField(max_length=50)),
                ('keyen', models.CharField(max_length=50)),
                ('studyint', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeywordBlackname',
            fields=[
                ('product', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('keycn', models.CharField(max_length=50)),
                ('keyen', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'keyword_blackname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('product', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(blank=True, max_length=6100, null=True)),
                ('leixing', models.CharField(max_length=30)),
                ('author', models.CharField(blank=True, max_length=40, null=True)),
                ('keybody', models.CharField(blank=True, max_length=500, null=True)),
                ('keyint', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'knowledge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnowledgeModify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('reviser', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(max_length=200)),
                ('modify', models.CharField(blank=True, max_length=1000, null=True)),
                ('modifydate', models.DateField(blank=True, null=True)),
                ('modifytime', models.TimeField(blank=True, null=True)),
                ('leixing', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'knowledge_modify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loginrecord',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('logindate', models.DateField()),
                ('logintime', models.TimeField()),
                ('logouttime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'loginrecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ncr',
            fields=[
                ('rwh', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('dncr', models.IntegerField(blank=True, db_column='DNCR', null=True)),
                ('undncr', models.IntegerField(blank=True, db_column='UNDNCR', null=True)),
                ('testitem', models.IntegerField(blank=True, db_column='TestItem', null=True)),
                ('ncrmd', models.FloatField(blank=True, db_column='NCRMD', null=True)),
                ('endtime', models.CharField(blank=True, db_column='EndTime', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ncr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pictureandworld',
            fields=[
                ('product', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.TextField(blank=True, null=True)),
                ('world', models.TextField(blank=True, null=True)),
                ('picture_name', models.CharField(blank=True, max_length=50, null=True)),
                ('world_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pictureandworld',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productlist',
            fields=[
                ('prolist', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'productlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=20, null=True)),
                ('searchbody', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'search_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Son',
            fields=[
                ('taskid', models.CharField(db_column='TaskID', max_length=30, primary_key=True, serialize=False)),
                ('sonid', models.CharField(db_column='SonID', max_length=20)),
                ('p1', models.CharField(blank=True, max_length=30, null=True)),
                ('p2', models.CharField(blank=True, max_length=30, null=True)),
                ('p3', models.CharField(blank=True, max_length=30, null=True)),
                ('p4', models.CharField(blank=True, max_length=30, null=True)),
                ('p5', models.CharField(blank=True, max_length=30, null=True)),
                ('p6', models.CharField(blank=True, max_length=30, null=True)),
                ('p1task', models.CharField(blank=True, max_length=300, null=True)),
                ('p2task', models.CharField(blank=True, max_length=300, null=True)),
                ('p3task', models.CharField(blank=True, max_length=300, null=True)),
                ('p4task', models.CharField(blank=True, max_length=300, null=True)),
                ('p5task', models.CharField(blank=True, max_length=300, null=True)),
                ('p6task', models.CharField(blank=True, max_length=300, null=True)),
                ('p1time', models.CharField(blank=True, max_length=30, null=True)),
                ('p2time', models.CharField(blank=True, max_length=30, null=True)),
                ('p3time', models.CharField(blank=True, max_length=30, null=True)),
                ('p4time', models.CharField(blank=True, max_length=30, null=True)),
                ('p5time', models.CharField(blank=True, max_length=30, null=True)),
                ('p6time', models.CharField(blank=True, max_length=30, null=True)),
                ('p1ending', models.CharField(blank=True, max_length=30, null=True)),
                ('p2ending', models.CharField(blank=True, max_length=30, null=True)),
                ('p3ending', models.CharField(blank=True, max_length=30, null=True)),
                ('p4ending', models.CharField(blank=True, max_length=30, null=True)),
                ('p5ending', models.CharField(blank=True, max_length=30, null=True)),
                ('p6ending', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'son',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('mode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('plandital', models.CharField(blank=True, db_column='PlanDital', max_length=500, null=True)),
                ('taskdital', models.CharField(blank=True, max_length=300, null=True)),
                ('flag', models.CharField(blank=True, max_length=20, null=True)),
                ('endingtime', models.CharField(blank=True, db_column='EndingTime', max_length=40, null=True)),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('mail', models.CharField(blank=True, max_length=150, null=True)),
                ('product', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.CharField(max_length=255)),
                ('v2', models.CharField(db_column='V2', max_length=255)),
            ],
            options={
                'db_table': 'version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weektask',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('week', models.CharField(max_length=20)),
                ('term', models.CharField(blank=True, max_length=2000, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('applytime', models.DateField()),
            ],
            options={
                'db_table': 'weektask',
                'managed': False,
            },
        ),
    ]

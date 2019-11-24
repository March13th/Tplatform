# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Casemodify(models.Model):
    product = models.CharField(max_length=255)
    version = models.CharField(max_length=50, blank=True, null=True)
    reviser = models.CharField(max_length=50, blank=True, null=True)
    modify = models.CharField(max_length=255, blank=True, null=True)
    modifydate = models.DateField(blank=True, null=True)
    modifytime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casemodify'


class Caseversion(models.Model):
    version = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caseversion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FcaseCipsFunction(models.Model):
    name1 = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, max_length=50)
    level = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    relatecase = models.CharField(max_length=200, blank=True, null=True)
    condition = models.CharField(max_length=600, blank=True, null=True)
    operation = models.CharField(max_length=1200, blank=True, null=True)
    result = models.CharField(max_length=600, blank=True, null=True)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    name4 = models.CharField(max_length=30)
    name5 = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fcase_cips_function'


class FcaseCtcFunction(models.Model):
    name1 = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, max_length=50)
    level = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    relatecase = models.CharField(max_length=200, blank=True, null=True)
    condition = models.CharField(max_length=600, blank=True, null=True)
    operation = models.CharField(max_length=1200, blank=True, null=True)
    result = models.CharField(max_length=600, blank=True, null=True)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    name4 = models.CharField(max_length=30)
    name5 = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fcase_ctc_function'


class FortAccesslog(models.Model):
    log_type = models.CharField(max_length=32)
    content = models.TextField()
    c_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fort_accesslog'


class FortGroup(models.Model):
    group_name = models.CharField(unique=True, max_length=128)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fort_group'


class FortGroupRemoteUserBindHost(models.Model):
    group = models.ForeignKey(FortGroup, models.DO_NOTHING)
    remoteuserbindhost = models.ForeignKey('FortRemoteuserbindhost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fort_group_remote_user_bind_host'
        unique_together = (('group', 'remoteuserbindhost'),)


class FortHost(models.Model):
    host_name = models.CharField(unique=True, max_length=128)
    ip = models.CharField(max_length=39)
    port = models.SmallIntegerField()
    release = models.CharField(max_length=128)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fort_host'
        unique_together = (('ip', 'port'),)


class FortRemoteuser(models.Model):
    remote_user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'fort_remoteuser'
        unique_together = (('remote_user_name', 'password'),)


class FortRemoteuserbindhost(models.Model):
    enabled = models.IntegerField()
    host = models.ForeignKey(FortHost, models.DO_NOTHING)
    remote_user = models.ForeignKey(FortRemoteuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fort_remoteuserbindhost'
        unique_together = (('remote_user', 'host'),)


class FortUserprofile(models.Model):
    user_type = models.CharField(max_length=128)
    enabled = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'fort_userprofile'


class FortUserprofileGroups(models.Model):
    userprofile = models.ForeignKey(FortUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(FortGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fort_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class FortUserprofileRemoteUserBindHosts(models.Model):
    userprofile = models.ForeignKey(FortUserprofile, models.DO_NOTHING)
    remoteuserbindhost = models.ForeignKey(FortRemoteuserbindhost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fort_userprofile_remote_user_bind_hosts'
        unique_together = (('userprofile', 'remoteuserbindhost'),)


class Keyword(models.Model):
    product = models.CharField(primary_key=True, max_length=20)
    keycn = models.CharField(max_length=50)
    keyen = models.CharField(max_length=50)
    studyint = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'
        unique_together = (('product', 'keyen'),)


class KeywordBlackname(models.Model):
    product = models.CharField(primary_key=True, max_length=20)
    keycn = models.CharField(max_length=50)
    keyen = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'keyword_blackname'
        unique_together = (('product', 'keyen'),)


class Knowledge(models.Model):
    product = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=6100, blank=True, null=True)
    leixing = models.CharField(max_length=30)
    author = models.CharField(max_length=40, blank=True, null=True)
    keybody = models.CharField(max_length=500, blank=True, null=True)
    keyint = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge'
        unique_together = (('product', 'title'),)


class KnowledgeModify(models.Model):
    product = models.CharField(max_length=30)
    reviser = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=200)
    modify = models.CharField(max_length=1000, blank=True, null=True)
    modifydate = models.DateField(blank=True, null=True)
    modifytime = models.TimeField(blank=True, null=True)
    leixing = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'knowledge_modify'


class Loginrecord(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    logindate = models.DateField()
    logintime = models.TimeField()
    logouttime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginrecord'
        unique_together = (('name', 'logindate', 'logintime'),)


class Ncr(models.Model):
    rwh = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    dncr = models.IntegerField(db_column='DNCR', blank=True, null=True)  # Field name made lowercase.
    undncr = models.IntegerField(db_column='UNDNCR', blank=True, null=True)  # Field name made lowercase.
    testitem = models.IntegerField(db_column='TestItem', blank=True, null=True)  # Field name made lowercase.
    ncrmd = models.FloatField(db_column='NCRMD', blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ncr'


class Ncrmanager(models.Model):
    taskid = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)
    subtime = models.DateField(blank=True, null=True)
    closetime = models.DateField(blank=True, null=True)
    subperson = models.CharField(max_length=50, blank=True, null=True)
    disposeperson = models.CharField(max_length=50, blank=True, null=True)
    solution = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    sonid = models.IntegerField()
    version = models.CharField(max_length=255, blank=True, null=True)
    testperson = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50)
    product = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncrmanager'


class Pictureandworld(models.Model):
    product = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=200)
    picture = models.TextField(blank=True, null=True)
    world = models.TextField(blank=True, null=True)
    picture_name = models.CharField(max_length=50, blank=True, null=True)
    world_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pictureandworld'
        unique_together = (('product', 'title'),)


class Productlist(models.Model):
    prolist = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'productlist'


class SearchRecord(models.Model):
    product = models.CharField(max_length=20, blank=True, null=True)
    searchbody = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_record'


class Son(models.Model):
    taskid = models.CharField(db_column='TaskID', primary_key=True, max_length=30)  # Field name made lowercase.
    sonid = models.CharField(db_column='SonID', max_length=20)  # Field name made lowercase.
    p1 = models.CharField(max_length=30, blank=True, null=True)
    p2 = models.CharField(max_length=30, blank=True, null=True)
    p3 = models.CharField(max_length=30, blank=True, null=True)
    p4 = models.CharField(max_length=30, blank=True, null=True)
    p5 = models.CharField(max_length=30, blank=True, null=True)
    p6 = models.CharField(max_length=30, blank=True, null=True)
    p1task = models.CharField(max_length=300, blank=True, null=True)
    p2task = models.CharField(max_length=300, blank=True, null=True)
    p3task = models.CharField(max_length=300, blank=True, null=True)
    p4task = models.CharField(max_length=300, blank=True, null=True)
    p5task = models.CharField(max_length=300, blank=True, null=True)
    p6task = models.CharField(max_length=300, blank=True, null=True)
    p1time = models.CharField(max_length=30, blank=True, null=True)
    p2time = models.CharField(max_length=30, blank=True, null=True)
    p3time = models.CharField(max_length=30, blank=True, null=True)
    p4time = models.CharField(max_length=30, blank=True, null=True)
    p5time = models.CharField(max_length=30, blank=True, null=True)
    p6time = models.CharField(max_length=30, blank=True, null=True)
    p1ending = models.CharField(max_length=30, blank=True, null=True)
    p2ending = models.CharField(max_length=30, blank=True, null=True)
    p3ending = models.CharField(max_length=30, blank=True, null=True)
    p4ending = models.CharField(max_length=30, blank=True, null=True)
    p5ending = models.CharField(max_length=30, blank=True, null=True)
    p6ending = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'son'
        unique_together = (('taskid', 'sonid'),)


class Task(models.Model):
    mode = models.CharField(primary_key=True, max_length=20)
    product = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    id = models.CharField(max_length=20)
    name = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    plandital = models.CharField(db_column='PlanDital', max_length=500, blank=True, null=True)  # Field name made lowercase.
    taskdital = models.CharField(max_length=300, blank=True, null=True)
    flag = models.CharField(max_length=20, blank=True, null=True)
    endingtime = models.CharField(db_column='EndingTime', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'
        unique_together = (('mode', 'product', 'year', 'id'),)


class Taskdetail(models.Model):
    rwh = models.CharField(primary_key=True, max_length=50)
    wbs = models.CharField(max_length=50, blank=True, null=True)
    begantime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    no = models.IntegerField()
    canbegan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taskdetail'
        unique_together = (('rwh', 'no'),)


class Testlist(models.Model):
    testlist = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'testlist'


class User(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    mail = models.CharField(max_length=150, blank=True, null=True)
    product = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Version(models.Model):
    v1 = models.CharField(max_length=255)
    v2 = models.CharField(db_column='V2', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'version'


class Weektask(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    week = models.CharField(max_length=20)
    term = models.CharField(max_length=2000, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    applytime = models.DateField()

    class Meta:
        managed = False
        db_table = 'weektask'
        unique_together = (('name', 'week'),)


class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'year'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#
# class Apothecary(models.Model):
#     aid = models.CharField(db_column='aID', primary_key=True, max_length=10)  # Field name made lowercase.
#     aname = models.CharField(db_column='aName', max_length=10)  # Field name made lowercase.
#     apassword = models.CharField(db_column='aPassword', max_length=18)  # Field name made lowercase.
#     agender = models.CharField(db_column='aGender', max_length=8)  # Field name made lowercase.
#     atel = modelscd.CharField(db_column='aTel', max_length=11)  # Field name made lowercase.
#     afield = models.CharField(db_column='aField', max_length=200)  # Field name made lowercase.
#     atimetable = models.CharField(db_column='aTimetable', max_length=50)  # Field name made lowercase.
#     ahospital = models.CharField(db_column='aHospital', max_length=20)  # Field name made lowercase.
#     astate = models.CharField(db_column='aState', max_length=20)  # Field name made lowercase.
#     aintro = models.CharField(db_column='aIntro', max_length=1000)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Apothecary'
#
#
# class Appointment(models.Model):
#     aid = models.CharField(db_column='aID', primary_key=True, max_length=10)  # Field name made lowercase.
#     uid = models.CharField(db_column='uID', max_length=10)  # Field name made lowercase.
#     appresult = models.CharField(db_column='appResult', max_length=500)  # Field name made lowercase.
#     appdate = models.CharField(db_column='appDate', max_length=20)  # Field name made lowercase.
#     appperiod = models.CharField(db_column='appPeriod', max_length=20)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Appointment'
#         unique_together = (('aid', 'uid'),)
#
#
# class Device(models.Model):
#     name = models.CharField(primary_key=True, max_length=100)
#     price = models.CharField(max_length=10, blank=True, null=True)
#     device_usage = models.CharField(max_length=5000, blank=True, null=True)
#     picture = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Device'
#
#
# class Diagnose(models.Model):
#     aid = models.OneToOneField(Apothecary, models.DO_NOTHING, db_column='aID', primary_key=True)  # Field name made lowercase.
#     uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uID')  # Field name made lowercase.
#     dcontent = models.CharField(max_length=500)
#     dsymptom = models.CharField(db_column='dSymptom', max_length=500)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Diagnose'
#         unique_together = (('aid', 'uid'),)
#

class Drug(models.Model):
    id = models.BigAutoField(primary_key=True)
    dName = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dPrice = models.CharField(max_length=250)
    dEffect = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dUsage = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dType = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dSale = models.CharField(max_length=250)
    dNum = models.CharField(max_length=250)
    #dPicture = models.CharField(max_length = 250, default = 'NULL')
    dStatus = models.IntegerField()
    dCreate_at = models.DateTimeField()
    dUpdate_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'Drug'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=50)
    password_salt = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def toDict(self):
        return {'id': self.id, 'name': self.name, 'division': self.division,
                'password_hash': self.password_hash, 'password_salt': self.password_salt,
                'tel': self.tel, 'status': self.status,
                'create_at': str(self.create_at), 'update_at': str(self.update_at)}

    class Meta:
        managed = True
        abstract = False
        db_table = 'Employee'


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    uName = models.CharField(db_column='uName', max_length=50)  # Field name made lowercase.
    uPassword_hash = models.CharField(db_column='uPassword_hash', max_length=50)  # Field name made lowercase.
    uPassword_salt = models.CharField(db_column='uPassword_salt', max_length=50)  # Field name made lowercase.
    uTel = models.CharField(db_column='uTel', max_length=50)  # Field name made lowercase.
    uType = models.CharField(db_column='uType', max_length=50)
    # uStatus = models.IntegerField(db_column='uStatus')  # Field name made lowercase.
    uGender = models.CharField(db_column='uGender', max_length=1)  # Field name made lowercase.
    uBirth = models.DateTimeField(db_column='uBirth')  # Field name made lowercase.
    uAddress = models.CharField(db_column='uAddress', max_length=100)  # Field name made lowercase.
    uCreate_at = models.DateTimeField(default = 'NUll')  # Field name made lowercase.
    uUpdate_at = models.DateTimeField(default = 'NULL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Member'

class emp_Drug(models.Model):
    id = models.BigAutoField(primary_key=True)
    eName = models.ForeignKey(Employee, on_delete = models.CASCADE, default = 'Unknown')
    edName = models.ForeignKey(Drug, on_delete = models.CASCADE, default = 'Unknown')
    edCreate_at = models.DateTimeField(default='NUll')  # Field name made lowercase.
    edUpdate_at = models.DateTimeField(default='NULL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'emp_Drug'


# class user(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=25)
#     password = models.CharField(max_length=30)
#     type = models.CharField(max_length=25)
#
#     class Meta:
#         managed = True
#         db_table = 'user'

#
# class Saler(models.Model):
#     salid = models.CharField(db_column='salID', primary_key=True, max_length=10)  # Field name made lowercase.
#     salname = models.CharField(db_column='salName', max_length=10)  # Field name made lowercase.
#     salpassword = models.CharField(db_column='salPassword', max_length=10)  # Field name made lowercase.
#     saltel = models.CharField(db_column='salTel', max_length=11)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Saler'
#
#
# class Superiviser(models.Model):
#     supid = models.CharField(db_column='supID', max_length=10)  # Field name made lowercase.
#     supname = models.CharField(db_column='supName', max_length=10)  # Field name made lowercase.
#     suppassword = models.CharField(db_column='supPassword', max_length=10)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Superiviser'
#

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cName = models.CharField(db_column='cName', max_length=50)  # Field name made lowercase.
    cStatus = models.IntegerField(db_column='cStatus')  # Field name made lowercase.
    cCreate_at = models.DateTimeField(db_column='cCreate_at')  # Field name made lowercase.
    cUpdate_at = models.DateTimeField(db_column='cUpdate_at')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'category'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class DrugReview(models.Model):
#     uniqueid = models.IntegerField(db_column='uniqueID', primary_key=True)  # Field name made lowercase.
#     drugname = models.CharField(db_column='drugName', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     drug_condition = models.CharField(max_length=500, blank=True, null=True)
#     review = models.CharField(max_length=500, blank=True, null=True)
#     rating = models.IntegerField(blank=True, null=True)
#     use_date = models.CharField(max_length=100, blank=True, null=True)
#     usefulcount = models.IntegerField(db_column='usefulCount', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'drug_review'


class TotalDrug(models.Model):
    id = models.IntegerField(primary_key=True)
    dName = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dPrice = models.CharField(max_length=250)
    dEffect = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    dUsage = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    picture = models.CharField(max_length=250,default="null")
    number = models.IntegerField(default = 0)
    #
    # id = models.CharField(primary_key=True, max_length=250)
    # dName = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    # dPrice = models.CharField(max_length=250)
    # dEffect = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    # dUsage = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    # dType = models.CharField(max_length=250, db_collation='gbk_chinese_ci')
    # dSale = models.CharField(max_length=250)
    # dNum = models.CharField(max_length=250)
    # dStatus = models.IntegerField()
    # dCreate_at = models.DateTimeField()
    # dUpdate_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'total_drug'


# class UserReserve(models.Model):
#     time = models.CharField(max_length=20)
#     re_mon = models.CharField(max_length=10)
#     re_tus = models.CharField(max_length=10)
#     re_won = models.CharField(max_length=10)
#     re_thu = models.CharField(max_length=10)
#     re_fri = models.CharField(max_length=10)
#     re_sat = models.CharField(max_length=10)
#     re_sun = models.CharField(max_length=10)
#
#     class Meta:
#         managed = False
#         db_table = 'user_reserve'
# class django_content_type(models.model):
#     id = models.CharField
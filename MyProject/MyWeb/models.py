# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Drug(models.Model):
    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=1000, db_collation='gbk_chinese_ci')
    price = models.CharField(max_length=1000)
    effect = models.CharField(max_length=1000, db_collation='gbk_chinese_ci')
    drug_usage = models.CharField(max_length=1000, db_collation='gbk_chinese_ci')
    picture = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000, db_collation='gbk_chinese_ci')
    sale = models.CharField(max_length=1000)
    number = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'mywebDrug'

class Muser(models.Model):
    uId = models.BigAutoField(primary_key=True)
    uPassword = models.CharField(db_column='uPassword', max_length=10)  # Field name made lowercase.
    uName = models.CharField(db_column='uName', max_length=10)  # Field name made lowercase.
    uType = models.CharField(db_column='uType', max_length=10)
    uGender = models.CharField(db_column='uGender', max_length=6)  # Field name made lowercase.
    uBirth = models.CharField(db_column='uBirth', max_length=8)  # Field name made lowercase.
    uTel = models.CharField(db_column='uTel', max_length=11)  # Field name made lowercase.
    uAddress = models.CharField(db_column='uAddress', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mywebMuser'

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cName = models.CharField(db_column='cName', max_length=50)  # Field name made lowercase.
    cStatus = models.IntegerField(db_column='cStatus')  # Field name made lowercase.
    cCreate_at = models.DateTimeField(db_column='cCreate_at')  # Field name made lowercase.
    cUpdate_at = models.DateTimeField(db_column='cUpdate_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mcategory'

class Apothecary(models.Model):
    id = models.BigAutoField(primary_key=True)
    aid = models.CharField(db_column='aID', max_length=10)  # Field name made lowercase.
    aname = models.CharField(db_column='aName', max_length=10)  # Field name made lowercase.
    apassword = models.CharField(db_column='aPassword', max_length=18)  # Field name made lowercase.
    agender = models.CharField(db_column='aGender', max_length=8)  # Field name made lowercase.
    atel = models.CharField(db_column='aTel', max_length=11)  # Field name made lowercase.
    afield = models.CharField(db_column='aField', max_length=200)  # Field name made lowercase.
    atimetable = models.CharField(db_column='aTimetable', max_length=50)  # Field name made lowercase.
    ahospital = models.CharField(db_column='aHospital', max_length=20)  # Field name made lowercase.
    astate = models.CharField(db_column='aState', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Apothecary'

class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    aID = models.IntegerField(db_column='aID', max_length=10)  # Field name made lowercase.
    uID = models.IntegerField(db_column='uID', max_length=10)  # Field name made lowercase.
    addDate = models.DateField(db_column='addDate')  # Field name made lowercase.
    addTime = models.CharField(db_column='addTime', max_length=18)  # Field name made lowercase.
    addDepartment = models.CharField(db_column='addDepartment', max_length=11)  # Field name made lowercase.
    addResult = models.CharField(db_column='addResult', max_length=100)  # Field name made lowercase.
    createAt = models.DateTimeField(db_column='createAt')  # Field name made lowercase.
    updateAt = models.DateTimeField(db_column='updateAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppointmentRecord'
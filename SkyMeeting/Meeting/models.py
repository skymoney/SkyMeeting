from django.db import models
from MemManage.models import Role
# Create your models here.  
class Meeting(models.Model):
    meeting_id=models.AutoField(primary_key=True,db_column="meeting_id")
    meeting_title=models.CharField(max_length=50,db_column="meeting_title")
    meeting_type=models.IntegerField(default=1,db_column="meeting_type")
    start_time=models.DateTimeField(db_column="start_time")
    meeting_period=models.IntegerField(default=0,db_column="meeting_period")
    close_time=models.DateTimeField(db_column="close_time")
    meeting_place=models.CharField(max_length=100,db_column="meeting_place")
    contact_tel=models.CharField(max_length=100,db_column="contact_tel")
    contact_email=models.EmailField(db_column="contact_email")
    detail=models.TextField(db_column="meeting_detail")
    create_user=models.ForeignKey(Role,db_column="create_user")
    create_time=models.DateTimeField(db_column="create_time")
    meeting_status=models.IntegerField(default=0,db_column="meeting_status")
    role=models.ManyToManyField(Role,through="Meeting_Participant")
    class Meta:
        db_table="Meeting"

class File(models.Model):
    file_id=models.AutoField(primary_key=True,db_column="file_id")
    file_name=models.CharField(max_length=100,db_column="file_name")
    file_size=models.BigIntegerField(default=0,db_column="file_size")
    file_path=models.CharField(max_length=100,db_column="file_path")
    upload_user=models.ForeignKey(Role,db_column="upload_user")
    upload_time=models.DateTimeField(db_column="upload_time")
    file_status=models.IntegerField(default=0,db_column="file_status")
    
    class Meta:
        db_table="File"

class Meeting_Participant(models.Model):
    mp_id=models.AutoField(primary_key=True,db_column="mp_id")
    meeting_id=models.ForeignKey(Meeting,db_column='meeting_id')
    role_id=models.ForeignKey(Role,db_column="role_id")
    status=models.IntegerField(default=0,db_column="status")
    
    class Meta:
        db_table="Meeting_Participant"

class Meeting_File(models.Model):
    meeting_file_id=models.AutoField(primary_key=True,db_column="meeting_file_id")
    meeting_id=models.ForeignKey(Meeting,db_column="meeting_id")
    file_id=models.ForeignKey()
    
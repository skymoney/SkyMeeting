# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting_File_Visible'
        db.create_table('Meeting_File_Visible', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting_file_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Meeting.Meeting_File'], db_column='meeting_file_id')),
            ('role_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Role'], db_column='role_id')),
            ('visible_status', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='visible_status')),
        ))
        db.send_create_signal(u'Meeting', ['Meeting_File_Visible'])
        
        # Adding model 'Meeting_Participant'
        db.create_table('Meeting_Participant', (
            ('mp_id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='mp_id')),
            ('meeting_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Meeting.Meeting'], db_column='meeting_id')),
            ('role_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Role'], db_column='role_id')),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='status')),
        ))
        db.send_create_signal(u'Meeting', ['Meeting_Participant'])

        # Adding model 'File'
        db.create_table('File', (
            ('file_id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='file_id')),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='file_name')),
            ('file_size', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_column='file_size')),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='file_path')),
            ('upload_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Role'], db_column='upload_user')),
            ('upload_time', self.gf('django.db.models.fields.DateTimeField')(db_column='upload_time')),
            ('file_status', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='file_status')),
        ))
        db.send_create_signal(u'Meeting', ['File'])

        # Adding model 'Meeting_Comment'
        db.create_table('Meeting_Comment', (
            ('comment_id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='comment_id')),
            ('meeting_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Meeting.Meeting'], db_column='meeting_id')),
            ('create_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Role'], db_column='create_user')),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(db_column='create_time')),
            ('content', self.gf('django.db.models.fields.TextField')(db_column='content')),
            ('reply_to_user', self.gf('django.db.models.fields.IntegerField')(db_column='replay_to_user')),
        ))
        db.send_create_signal(u'Meeting', ['Meeting_Comment'])

        

        # Adding model 'Meeting_File'
        db.create_table('Meeting_File', (
            ('meeting_file_id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='meeting_file_id')),
            ('meeting_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Meeting.Meeting'], db_column='meeting_id')),
            ('file_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Meeting.File'], db_column='file_id')),
        ))
        db.send_create_signal(u'Meeting', ['Meeting_File'])

        # Adding model 'Meeting'
        db.create_table('Meeting', (
            ('meeting_id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='meeting_id')),
            ('meeting_title', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='meeting_title')),
            ('meeting_type', self.gf('django.db.models.fields.IntegerField')(default=1, db_column='meeting_type')),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(db_column='start_time')),
            ('meeting_period', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='meeting_period')),
            ('close_time', self.gf('django.db.models.fields.DateTimeField')(db_column='close_time')),
            ('meeting_place', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='meeting_place')),
            ('contact_tel', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='contact_tel')),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, db_column='contact_email')),
            ('detail', self.gf('django.db.models.fields.TextField')(db_column='meeting_detail')),
            ('create_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Role'], db_column='create_user')),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(db_column='create_time')),
            ('meeting_status', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='meeting_status')),
        ))
        db.send_create_signal(u'Meeting', ['Meeting'])


    def backwards(self, orm):
        # Deleting model 'Meeting_Participant'
        db.delete_table('Meeting_Participant')

        # Deleting model 'File'
        db.delete_table('File')

        # Deleting model 'Meeting_Comment'
        db.delete_table('Meeting_Comment')

        # Deleting model 'Meeting_File_Visible'
        db.delete_table('Meeting')

        # Deleting model 'Meeting_File'
        db.delete_table('Meeting_File')

        # Deleting model 'Meeting'
        db.delete_table('Meeting')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account'},
            'alastlogin': ('django.db.models.fields.DateTimeField', [], {}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'atime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Meeting.file': {
            'Meta': {'object_name': 'File', 'db_table': "'File'"},
            'file_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'file_id'"}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'file_name'"}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'file_path'"}),
            'file_size': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_column': "'file_size'"}),
            'file_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'file_status'"}),
            'meeting': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Meeting.Meeting']", 'through': u"orm['Meeting.Meeting_File']", 'symmetrical': 'False'}),
            'upload_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'upload_time'"}),
            'upload_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'upload_user'"})
        },
        u'Meeting.meeting': {
            'Meta': {'object_name': 'Meeting', 'db_table': "'Meeting'"},
            'close_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'close_time'"}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'db_column': "'contact_email'"}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'contact_tel'"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'create_time'"}),
            'create_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'create_user'"}),
            'detail': ('django.db.models.fields.TextField', [], {'db_column': "'meeting_detail'"}),
            'meeting_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'meeting_id'"}),
            'meeting_period': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'meeting_period'"}),
            'meeting_place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'meeting_place'"}),
            'meeting_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'meeting_status'"}),
            'meeting_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'meeting_title'"}),
            'meeting_type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_column': "'meeting_type'"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'start_time'"})
        },
        u'Meeting.meeting_comment': {
            'Meta': {'object_name': 'Meeting_Comment', 'db_table': "'Meeting_Comment'"},
            'comment_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'comment_id'"}),
            'content': ('django.db.models.fields.TextField', [], {'db_column': "'content'"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'create_time'"}),
            'create_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'create_user'"}),
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'reply_to_user': ('django.db.models.fields.IntegerField', [], {'db_column': "'replay_to_user'"})
        },
        u'Meeting.meeting_file': {
            'Meta': {'object_name': 'Meeting_File', 'db_table': "'Meeting_File'"},
            'file_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.File']", 'db_column': "'file_id'"}),
            'meeting_file_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'meeting_file_id'"}),
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Role']", 'through': u"orm['Meeting.Meeting_File_Visible']", 'symmetrical': 'False'})
        },
        u'Meeting.meeting_file_visible': {
            'Meta': {'object_name': 'Meeting_File_Visible', 'db_table': "'Meeting'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_file_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting_File']", 'db_column': "'meeting_file_id'"}),
            'role_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'role_id'"}),
            'visible_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'visible_status'"})
        },
        u'Meeting.meeting_participant': {
            'Meta': {'object_name': 'Meeting_Participant', 'db_table': "'Meeting_Participant'"},
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'mp_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'mp_id'"}),
            'role_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'role_id'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'status'"})
        },
        u'MemManage.company': {
            'Meta': {'object_name': 'Company'},
            'clocation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'MemManage.group': {
            'Meta': {'object_name': 'Group'},
            'cid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']"}),
            'gname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'MemManage.role': {
            'Meta': {'object_name': 'Role'},
            'aid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Login.Account']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Tag']", 'symmetrical': 'False'})
        },
        u'MemManage.tag': {
            'Meta': {'object_name': 'Tag'},
            'cid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Meeting']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):


        # Adding field 'Meeting_File.is_all_visiable'
        db.add_column('Meeting_File', 'is_all_visiable',
                      self.gf('django.db.models.fields.IntegerField')(default=1, db_column='is_all_visiable'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Meeting_Participant.status'
        db.add_column('Meeting_Participant', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_column='status'),
                      keep_default=False)

        # Deleting field 'Meeting_Participant.participant_status'
        db.delete_column('Meeting_Participant', 'participant_status')

        # Deleting field 'Meeting_Comment.comment_status'
        db.delete_column('Meeting_Comment', 'comment_status')

        # Adding field 'Meeting_File_Visible.visible_status'
        db.add_column('Meeting', 'visible_status',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_column='visible_status'),
                      keep_default=False)

        # Deleting field 'Meeting_File_Visible.visible_level'
        db.delete_column('Meeting', 'visible_level')

        # Deleting field 'Meeting_File.is_all_visiable'
        db.delete_column('Meeting_File', 'is_all_visiable')


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
            'comment_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'comment_status'"}),
            'content': ('django.db.models.fields.TextField', [], {'db_column': "'content'"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'db_column': "'create_time'"}),
            'create_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'create_user'"}),
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'reply_to_user': ('django.db.models.fields.IntegerField', [], {'db_column': "'replay_to_user'"})
        },
        u'Meeting.meeting_file': {
            'Meta': {'object_name': 'Meeting_File', 'db_table': "'Meeting_File'"},
            'file_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.File']", 'db_column': "'file_id'"}),
            'is_all_visiable': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_column': "'is_all_visiable'"}),
            'meeting_file_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'meeting_file_id'"}),
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Role']", 'through': u"orm['Meeting.Meeting_File_Visible']", 'symmetrical': 'False'})
        },
        u'Meeting.meeting_file_visible': {
            'Meta': {'object_name': 'Meeting_File_Visible', 'db_table': "'Meeting'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_file_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting_File']", 'db_column': "'meeting_file_id'"}),
            'role_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'role_id'"}),
            'visible_level': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'visible_level'"})
        },
        u'Meeting.meeting_participant': {
            'Meta': {'object_name': 'Meeting_Participant', 'db_table': "'Meeting_Participant'"},
            'meeting_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting']", 'db_column': "'meeting_id'"}),
            'mp_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'mp_id'"}),
            'participant_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'participant_status'"}),
            'role_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Role']", 'db_column': "'role_id'"})
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
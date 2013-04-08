# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Meeting_Comment.quote_from_comment_id'
        db.add_column('Meeting_Comment', 'quote_from_comment_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, db_column='quote_from_comment_id'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Meeting_Comment.quote_from_comment_id'
        db.delete_column('Meeting_Comment', 'quote_from_comment_id')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account', 'db_table': "'Account'"},
            'aid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'account_id'"}),
            'alastlogin': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_lastlogin'"}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_name'"}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_password'"}),
            'atime': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_createtime'"})
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
            'close_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 8, 0, 0)', 'null': 'True', 'db_column': "'close_time'", 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'default': "'null@null.com'", 'max_length': '75', 'null': 'True', 'db_column': "'contact_email'", 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'db_column': "'contact_tel'", 'blank': 'True'}),
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
            'quote_from_comment_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'quote_from_comment_id'"}),
            'reply_to_user': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'db_column': "'replay_to_user'"})
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
            'Meta': {'object_name': 'Meeting_File_Visible', 'db_table': "'Meeting_File_Visible'"},
            'meeting_file_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Meeting.Meeting_File']", 'db_column': "'meeting_file_id'"}),
            'mfv_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'mfv_id'"}),
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
            'Meta': {'object_name': 'Company', 'db_table': "'Company'"},
            'cid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'company_id'"}),
            'clocation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'company_location'"}),
            'cname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'company_name'"})
        },
        u'MemManage.group': {
            'Meta': {'object_name': 'Group', 'db_table': "'Group'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'group_company'"}),
            'gid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'group_id'"}),
            'gname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'group_name'"})
        },
        u'MemManage.role': {
            'Meta': {'object_name': 'Role', 'db_table': "'Role'"},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Login.Account']", 'db_column': "'role_account'"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'role_company'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'db_column': "'role_email'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Group']", 'symmetrical': 'False'}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'role_idcard'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'role_location'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'role_name'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_column': "'role_phone'"}),
            'rid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'role_id'"}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'db_column': "'role_sex'"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Tag']", 'symmetrical': 'False'})
        },
        u'MemManage.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "'Tag'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'tag_company'"}),
            'tid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'tag_id'"}),
            'tname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'tag_name'"})
        }
    }

    complete_apps = ['Meeting']
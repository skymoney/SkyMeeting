# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TempRole.permission'
        
        db.add_column('TempRole', 'permission',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_column='TempRolePermission'),
                      keep_default=False)

        # Adding field 'Role.permission'
        db.add_column('Role', 'permission',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_column='role_permission'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TempRole.permission'
        db.delete_column('TempRole', 'TempRolePermission')

        # Deleting field 'Role.permission'
        db.delete_column('Role', 'role_permission')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account', 'db_table': "'Account'"},
            'aid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'account_id'"}),
            'alevel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'account_level'"}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_name'"}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_password'"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_lastlogin'"}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_createtime'"})
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
        u'MemManage.headphoto': {
            'Meta': {'object_name': 'HeadPhoto', 'db_table': "'Head_Photo'"},
            'hid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'headphoto_id'"}),
            'hname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'headphoto_name'"}),
            'hpath': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'headphoto_path'"})
        },
        u'MemManage.role': {
            'Meta': {'object_name': 'Role', 'db_table': "'Role'"},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Login.Account']", 'db_column': "'role_account'"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'role_company'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'db_column': "'role_email'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Group']", 'symmetrical': 'False'}),
            'head_photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.HeadPhoto']", 'db_column': "'role_headphoto'"}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'role_idcard'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'role_location'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'role_name'"}),
            'permission': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'role_permission'"}),
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
        },
        u'MemManage.temprole': {
            'Meta': {'object_name': 'TempRole', 'db_table': "'TempRole'"},
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'db_column': "'TempCheckCode'"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'TempRoleCompany'"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TempRoleEmail'"}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'TempRoleIdCard'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TempRoleName'"}),
            'permission': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'TempRolePermission'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_column': "'TempRolePhone'"}),
            'trid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'TempRoleId'"}),
            'verifyAnswer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'db_column': "'VerifyAnswer'"}),
            'verifyByName': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'VerifyModeName'"}),
            'verifyByPhone': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'VerifyModePhone'"}),
            'verifyByQuest': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'VerifyModeQuest'"}),
            'verifyQuest': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'db_column': "'VerifyQuest'"})
        }
    }

    complete_apps = ['MemManage']
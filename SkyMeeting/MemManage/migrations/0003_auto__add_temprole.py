# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TempRole'
        db.create_table('TempRole', (
            ('trid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='TempRoleId')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TempRoleName')),
            ('idcard', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='TempRoleIdCard')),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, db_column='TempRolePhone')),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TempRoleEmail')),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='TempRoleCompany')),
            ('verifyByName', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModeName')),
            ('verifyByPhone', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModePhone')),
            ('verifyByQuest', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModeQuest')),
            ('verifyQuest', self.gf('django.db.models.fields.CharField')(default='', max_length=100, db_column='VerifyQuest')),
            ('verifyAnswer', self.gf('django.db.models.fields.CharField')(default='', max_length=100, db_column='VerifyAnswer')),
        ))
        db.send_create_signal(u'MemManage', ['TempRole'])


    def backwards(self, orm):
        # Deleting model 'TempRole'
        db.delete_table('TempRole')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account'},
            'alastlogin': ('django.db.models.fields.DateTimeField', [], {}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'atime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        },
        u'MemManage.temprole': {
            'Meta': {'object_name': 'TempRole', 'db_table': "'TempRole'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'TempRoleCompany'"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TempRoleEmail'"}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'TempRoleIdCard'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'TempRoleName'"}),
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
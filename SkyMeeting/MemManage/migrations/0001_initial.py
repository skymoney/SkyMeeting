# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('Company', (
            ('cid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='company_id')),
            ('cname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='company_name')),
            ('clocation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='company_location')),
        ))
        db.send_create_signal(u'MemManage', ['Company'])

        # Adding model 'HeadPhoto'
        db.create_table('Head_Photo', (
            ('hid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='headphoto_id')),
            ('hname', self.gf('django.db.models.fields.CharField')(max_length=150, db_column='headphoto_name')),
            ('hpath', self.gf('django.db.models.fields.CharField')(max_length=150, db_column='headphoto_path')),
        ))
        db.send_create_signal(u'MemManage', ['HeadPhoto'])

        # Adding model 'Group'
        db.create_table('Group', (
            ('gid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='group_id')),
            ('gname', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='group_name')),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='group_company')),
        ))
        db.send_create_signal(u'MemManage', ['Group'])

        # Adding model 'Tag'
        db.create_table('Tag', (
            ('tid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='tag_id')),
            ('tname', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='tag_name')),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='tag_company')),
        ))
        db.send_create_signal(u'MemManage', ['Tag'])

        # Adding model 'Role'
        db.create_table('Role', (
            ('rid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='role_id')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='role_name')),
            ('sex', self.gf('django.db.models.fields.IntegerField')(default=-1, db_column='role_sex')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='role_location')),
            ('idcard', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='role_idcard')),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, db_column='role_phone')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30, db_column='role_email')),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account'], db_column='role_account')),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='role_company')),
            ('head_photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.HeadPhoto'], db_column='role_headphoto')),
        ))
        db.send_create_signal(u'MemManage', ['Role'])

        # Adding M2M table for field groups on 'Role'
        db.create_table('Role_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'MemManage.role'], null=False)),
            ('group', models.ForeignKey(orm[u'MemManage.group'], null=False))
        ))
        db.create_unique('Role_groups', ['role_id', 'group_id'])

        # Adding M2M table for field tags on 'Role'
        db.create_table('Role_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'MemManage.role'], null=False)),
            ('tag', models.ForeignKey(orm[u'MemManage.tag'], null=False))
        ))
        db.create_unique('Role_tags', ['role_id', 'tag_id'])

        # Adding model 'TempRole'
        db.create_table('TempRole', (
            ('trid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='TempRoleId')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TempRoleName')),
            ('idcard', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='TempRoleIdCard')),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, db_column='TempRolePhone')),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='TempRoleEmail')),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='TempRoleCompany')),
            ('code', self.gf('django.db.models.fields.CharField')(default='', max_length=50, db_column='TempCheckCode')),
            ('verifyByName', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModeName')),
            ('verifyByPhone', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModePhone')),
            ('verifyByQuest', self.gf('django.db.models.fields.IntegerField')(default=0, db_column='VerifyModeQuest')),
            ('verifyQuest', self.gf('django.db.models.fields.CharField')(default='', max_length=100, db_column='VerifyQuest')),
            ('verifyAnswer', self.gf('django.db.models.fields.CharField')(default='', max_length=100, db_column='VerifyAnswer')),
        ))
        db.send_create_signal(u'MemManage', ['TempRole'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('Company')

        # Deleting model 'HeadPhoto'
        db.delete_table('Head_Photo')

        # Deleting model 'Group'
        db.delete_table('Group')

        # Deleting model 'Tag'
        db.delete_table('Tag')

        # Deleting model 'Role'
        db.delete_table('Role')

        # Removing M2M table for field groups on 'Role'
        db.delete_table('Role_groups')

        # Removing M2M table for field tags on 'Role'
        db.delete_table('Role_tags')

        # Deleting model 'TempRole'
        db.delete_table('TempRole')


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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TempAccountPwd'
        db.create_table('TempAccountPwd', (
            ('tapid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='tmp_accountpwd_id')),
            ('tapCode', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='tmp_accountpwd_code')),
            ('tapAid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account'], db_column='tmp_accountpwd_account')),
            ('tapDate', self.gf('django.db.models.fields.DateTimeField')(db_column='tmp_accountpwd_time')),
        ))
        db.send_create_signal(u'Login', ['TempAccountPwd'])
        '''
        # Deleting field 'Account.alastlogin'
        db.delete_column('Account', 'account_lastlogin')

        # Deleting field 'Account.atime'
        db.delete_column('Account', 'account_createtime')

        # Adding field 'Account.last_login'
        db.add_column('Account', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 22, 0, 0), db_column='account_createtime'),
                      keep_default=False)

        # Adding field 'Account.date_joined'
        db.add_column('Account', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 22, 0, 0), db_column='account_lastlogin'),
                      keep_default=False)

        # Adding field 'Account.alevel'
        db.add_column('Account', 'alevel',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=20, db_column='account_level'),
                      keep_default=False)

        '''
    def backwards(self, orm):
        # Deleting model 'TempAccountPwd'
        db.delete_table('TempAccountPwd')

        # Adding field 'Account.alastlogin'
        db.add_column('Account', 'alastlogin',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 22, 0, 0), db_column='account_lastlogin'),
                      keep_default=False)

        # Adding field 'Account.atime'
        db.add_column('Account', 'atime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 22, 0, 0), db_column='account_createtime'),
                      keep_default=False)

        # Deleting field 'Account.last_login'
        db.delete_column('Account', 'account_createtime')

        # Deleting field 'Account.date_joined'
        db.delete_column('Account', 'account_lastlogin')

        # Deleting field 'Account.alevel'
        db.delete_column('Account', 'account_level')


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
        u'Login.tempaccountpwd': {
            'Meta': {'object_name': 'TempAccountPwd', 'db_table': "'TempAccountPwd'"},
            'tapAid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Login.Account']", 'db_column': "'tmp_accountpwd_account'"}),
            'tapCode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'tmp_accountpwd_code'"}),
            'tapDate': ('django.db.models.fields.DateTimeField', [], {'db_column': "'tmp_accountpwd_time'"}),
            'tapid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'tmp_accountpwd_id'"})
        }
    }

    complete_apps = ['Login']
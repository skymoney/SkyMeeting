# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('Account', (
            ('aid', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='account_id')),
            ('aname', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='account_name')),
            ('apassword', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='account_password')),
            ('atime', self.gf('django.db.models.fields.DateTimeField')(db_column='account_createtime')),
            ('alastlogin', self.gf('django.db.models.fields.DateTimeField')(db_column='account_lastlogin')),
        ))
        db.send_create_signal(u'Login', ['Account'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('Account')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account', 'db_table': "'Account'"},
            'aid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'account_id'"}),
            'alastlogin': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_lastlogin'"}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_name'"}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'account_password'"}),
            'atime': ('django.db.models.fields.DateTimeField', [], {'db_column': "'account_createtime'"})
        }
    }

    complete_apps = ['Login']
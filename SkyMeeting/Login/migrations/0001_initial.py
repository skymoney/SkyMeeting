# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'Login_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apassword', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('atime', self.gf('django.db.models.fields.DateTimeField')()),
            ('alastlogin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Login', ['Account'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'Login_account')


    models = {
        u'Login.account': {
            'Meta': {'object_name': 'Account'},
            'alastlogin': ('django.db.models.fields.DateTimeField', [], {}),
            'aname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apassword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'atime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Login']
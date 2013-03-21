# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Role.sex'
        db.alter_column(u'MemManage_role', 'sex', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Role.sex'
        db.alter_column(u'MemManage_role', 'sex', self.gf('django.db.models.fields.CharField')(max_length=5))

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
            'sex': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Tag']", 'symmetrical': 'False'})
        },
        u'MemManage.tag': {
            'Meta': {'object_name': 'Tag'},
            'cid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['MemManage']
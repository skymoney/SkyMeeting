# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'MemManage_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clocation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'MemManage', ['Company'])

        # Adding model 'Group'
        db.create_table(u'MemManage_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'])),
        ))
        db.send_create_signal(u'MemManage', ['Group'])

        # Adding model 'Tag'
        db.create_table(u'MemManage_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'])),
        ))
        db.send_create_signal(u'MemManage', ['Tag'])

        # Adding model 'Role'
        db.create_table(u'MemManage_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('idcard', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('aid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'])),
        ))
        db.send_create_signal(u'MemManage', ['Role'])

        # Adding M2M table for field groups on 'Role'
        db.create_table(u'MemManage_role_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'MemManage.role'], null=False)),
            ('group', models.ForeignKey(orm[u'MemManage.group'], null=False))
        ))
        db.create_unique(u'MemManage_role_groups', ['role_id', 'group_id'])

        # Adding M2M table for field tags on 'Role'
        db.create_table(u'MemManage_role_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'MemManage.role'], null=False)),
            ('tag', models.ForeignKey(orm[u'MemManage.tag'], null=False))
        ))
        db.create_unique(u'MemManage_role_tags', ['role_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'MemManage_company')

        # Deleting model 'Group'
        db.delete_table(u'MemManage_group')

        # Deleting model 'Tag'
        db.delete_table(u'MemManage_tag')

        # Deleting model 'Role'
        db.delete_table(u'MemManage_role')

        # Removing M2M table for field groups on 'Role'
        db.delete_table('MemManage_role_groups')

        # Removing M2M table for field tags on 'Role'
        db.delete_table('MemManage_role_tags')


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
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
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
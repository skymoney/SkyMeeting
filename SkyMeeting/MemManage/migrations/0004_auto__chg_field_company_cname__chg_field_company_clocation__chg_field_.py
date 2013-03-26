# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Company.cname' to match new field type.
        db.rename_column('Company', 'cname', 'CompanyName')
        # Changing field 'Company.cname'
        db.alter_column('Company', 'CompanyName', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='CompanyName'))

        # Renaming column for 'Company.clocation' to match new field type.
        db.rename_column('Company', 'clocation', 'CompanyLocation')
        # Changing field 'Company.clocation'
        db.alter_column('Company', 'CompanyLocation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='CompanyLocation'))

        # Renaming column for 'Tag.tname' to match new field type.
        db.rename_column('Tag', 'tname', 'TagName')
        # Changing field 'Tag.tname'
        db.alter_column('Tag', 'TagName', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TagName'))

        # Renaming column for 'Tag.cid' to match new field type.
        db.rename_column('Tag', 'cid_id', 'TagCompany')
        # Changing field 'Tag.cid'
        db.alter_column('Tag', 'TagCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='TagCompany'))

        # Renaming column for 'Group.gname' to match new field type.
        db.rename_column('Group', 'gname', 'GroupName')
        # Changing field 'Group.gname'
        db.alter_column('Group', 'GroupName', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='GroupName'))

        # Renaming column for 'Group.cid' to match new field type.
        db.rename_column('Group', 'cid_id', 'GroupCompany')
        # Changing field 'Group.cid'
        db.alter_column('Group', 'GroupCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='GroupCompany'))
        # Adding field 'TempRole.code'
        db.add_column('TempRole', 'code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, db_column='TempCheckCode'),
                      keep_default=False)


        # Renaming column for 'Role.name' to match new field type.
        db.rename_column('Role', 'name', 'RoleName')
        # Changing field 'Role.name'
        db.alter_column('Role', 'RoleName', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='RoleName'))

        # Renaming column for 'Role.company' to match new field type.
        db.rename_column('Role', 'company_id', 'RoleCompany')
        # Changing field 'Role.company'
        db.alter_column('Role', 'RoleCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='RoleCompany'))

        # Renaming column for 'Role.idcard' to match new field type.
        db.rename_column('Role', 'idcard', 'RoleIdcard')
        # Changing field 'Role.idcard'
        db.alter_column('Role', 'RoleIdcard', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='RoleIdcard'))

        # Renaming column for 'Role.sex' to match new field type.
        db.rename_column('Role', 'sex', 'RoleSex')
        # Changing field 'Role.sex'
        db.alter_column('Role', 'RoleSex', self.gf('django.db.models.fields.IntegerField')(db_column='RoleSex'))

        # Renaming column for 'Role.phone' to match new field type.
        db.rename_column('Role', 'phone', 'RolePhone')
        # Changing field 'Role.phone'
        db.alter_column('Role', 'RolePhone', self.gf('django.db.models.fields.CharField')(max_length=15, db_column='RolePhone'))

        # Renaming column for 'Role.location' to match new field type.
        db.rename_column('Role', 'location', 'RoleLocation')
        # Changing field 'Role.location'
        db.alter_column('Role', 'RoleLocation', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='RoleLocation'))

        # Renaming column for 'Role.aid' to match new field type.
        db.rename_column('Role', 'aid_id', 'RoleAccount')
        # Changing field 'Role.aid'
        db.alter_column('Role', 'RoleAccount', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account'], db_column='RoleAccount'))

        # Renaming column for 'Role.email' to match new field type.
        db.rename_column('Role', 'email', 'RoleEmail')
        # Changing field 'Role.email'
        db.alter_column('Role', 'RoleEmail', self.gf('django.db.models.fields.EmailField')(max_length=30, db_column='RoleEmail'))

    def backwards(self, orm):

        # Renaming column for 'Company.cname' to match new field type.
        db.rename_column('Company', 'CompanyName', 'cname')
        # Changing field 'Company.cname'
        db.alter_column('Company', 'cname', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Company.clocation' to match new field type.
        db.rename_column('Company', 'CompanyLocation', 'clocation')
        # Changing field 'Company.clocation'
        db.alter_column('Company', 'clocation', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Tag.tname' to match new field type.
        db.rename_column('Tag', 'TagName', 'tname')
        # Changing field 'Tag.tname'
        db.alter_column('Tag', 'tname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Tag.cid' to match new field type.
        db.rename_column('Tag', 'TagCompany', 'cid_id')
        # Changing field 'Tag.cid'
        db.alter_column('Tag', 'cid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))

        # Renaming column for 'Group.gname' to match new field type.
        db.rename_column('Group', 'GroupName', 'gname')
        # Changing field 'Group.gname'
        db.alter_column('Group', 'gname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Group.cid' to match new field type.
        db.rename_column('Group', 'GroupCompany', 'cid_id')
        # Changing field 'Group.cid'
        db.alter_column('Group', 'cid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))
        # Deleting field 'TempRole.code'
        db.delete_column('TempRole', 'TempCheckCode')


        # Renaming column for 'Role.name' to match new field type.
        db.rename_column('Role', 'RoleName', 'name')
        # Changing field 'Role.name'
        db.alter_column('Role', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Renaming column for 'Role.company' to match new field type.
        db.rename_column('Role', 'RoleCompany', 'company_id')
        # Changing field 'Role.company'
        db.alter_column('Role', 'company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))

        # Renaming column for 'Role.idcard' to match new field type.
        db.rename_column('Role', 'RoleIdcard', 'idcard')
        # Changing field 'Role.idcard'
        db.alter_column('Role', 'idcard', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Renaming column for 'Role.sex' to match new field type.
        db.rename_column('Role', 'RoleSex', 'sex')
        # Changing field 'Role.sex'
        db.alter_column('Role', 'sex', self.gf('django.db.models.fields.IntegerField')())

        # Renaming column for 'Role.phone' to match new field type.
        db.rename_column('Role', 'RolePhone', 'phone')
        # Changing field 'Role.phone'
        db.alter_column('Role', 'phone', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Renaming column for 'Role.location' to match new field type.
        db.rename_column('Role', 'RoleLocation', 'location')
        # Changing field 'Role.location'
        db.alter_column('Role', 'location', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Role.aid' to match new field type.
        db.rename_column('Role', 'RoleAccount', 'aid_id')
        # Changing field 'Role.aid'
        db.alter_column('Role', 'aid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account']))

        # Renaming column for 'Role.email' to match new field type.
        db.rename_column('Role', 'RoleEmail', 'email')
        # Changing field 'Role.email'
        db.alter_column('Role', 'email', self.gf('django.db.models.fields.EmailField')(max_length=30))

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
            'Meta': {'object_name': 'Company', 'db_table': "'Company'"},
            'clocation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'CompanyLocation'"}),
            'cname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'CompanyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'MemManage.group': {
            'Meta': {'object_name': 'Group', 'db_table': "'Group'"},
            'cid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'GroupCompany'"}),
            'gname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'GroupName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'MemManage.role': {
            'Meta': {'object_name': 'Role', 'db_table': "'Role'"},
            'aid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Login.Account']", 'db_column': "'RoleAccount'"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'RoleCompany'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'db_column': "'RoleEmail'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'RoleIdcard'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'RoleLocation'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'RoleName'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_column': "'RolePhone'"}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'db_column': "'RoleSex'"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MemManage.Tag']", 'symmetrical': 'False'})
        },
        u'MemManage.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "'Tag'"},
            'cid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MemManage.Company']", 'db_column': "'TagCompany'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'TagName'"})
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
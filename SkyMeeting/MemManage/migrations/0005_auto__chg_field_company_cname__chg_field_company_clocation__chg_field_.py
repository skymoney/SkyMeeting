# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Company.cname' to match new field type.
        db.rename_column(u'MemManage_company', 'CompanyName', 'cname')
        # Changing field 'Company.cname'
        db.alter_column(u'MemManage_company', 'cname', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Company.clocation' to match new field type.
        db.rename_column(u'MemManage_company', 'CompanyLocation', 'clocation')
        # Changing field 'Company.clocation'
        db.alter_column(u'MemManage_company', 'clocation', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Tag.tname' to match new field type.
        db.rename_column(u'MemManage_tag', 'TagName', 'tname')
        # Changing field 'Tag.tname'
        db.alter_column(u'MemManage_tag', 'tname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Tag.cid' to match new field type.
        db.rename_column(u'MemManage_tag', 'TagCompany', 'cid_id')
        # Changing field 'Tag.cid'
        db.alter_column(u'MemManage_tag', 'cid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))

        # Renaming column for 'Group.gname' to match new field type.
        db.rename_column(u'MemManage_group', 'GroupName', 'gname')
        # Changing field 'Group.gname'
        db.alter_column(u'MemManage_group', 'gname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Group.cid' to match new field type.
        db.rename_column(u'MemManage_group', 'GroupCompany', 'cid_id')
        # Changing field 'Group.cid'
        db.alter_column(u'MemManage_group', 'cid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))

        # Renaming column for 'Role.name' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleName', 'name')
        # Changing field 'Role.name'
        db.alter_column(u'MemManage_role', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Renaming column for 'Role.company' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleCompany', 'company_id')
        # Changing field 'Role.company'
        db.alter_column(u'MemManage_role', 'company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company']))

        # Renaming column for 'Role.idcard' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleIdcard', 'idcard')
        # Changing field 'Role.idcard'
        db.alter_column(u'MemManage_role', 'idcard', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Renaming column for 'Role.sex' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleSex', 'sex')
        # Changing field 'Role.sex'
        db.alter_column(u'MemManage_role', 'sex', self.gf('django.db.models.fields.IntegerField')())

        # Renaming column for 'Role.phone' to match new field type.
        db.rename_column(u'MemManage_role', 'RolePhone', 'phone')
        # Changing field 'Role.phone'
        db.alter_column(u'MemManage_role', 'phone', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Renaming column for 'Role.location' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleLocation', 'location')
        # Changing field 'Role.location'
        db.alter_column(u'MemManage_role', 'location', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Role.aid' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleAccount', 'aid_id')
        # Changing field 'Role.aid'
        db.alter_column(u'MemManage_role', 'aid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account']))

        # Renaming column for 'Role.email' to match new field type.
        db.rename_column(u'MemManage_role', 'RoleEmail', 'email')
        # Changing field 'Role.email'
        db.alter_column(u'MemManage_role', 'email', self.gf('django.db.models.fields.EmailField')(max_length=30))

    def backwards(self, orm):

        # Renaming column for 'Company.cname' to match new field type.
        db.rename_column(u'MemManage_company', 'cname', 'CompanyName')
        # Changing field 'Company.cname'
        db.alter_column(u'MemManage_company', 'CompanyName', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='CompanyName'))

        # Renaming column for 'Company.clocation' to match new field type.
        db.rename_column(u'MemManage_company', 'clocation', 'CompanyLocation')
        # Changing field 'Company.clocation'
        db.alter_column(u'MemManage_company', 'CompanyLocation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column='CompanyLocation'))

        # Renaming column for 'Tag.tname' to match new field type.
        db.rename_column(u'MemManage_tag', 'tname', 'TagName')
        # Changing field 'Tag.tname'
        db.alter_column(u'MemManage_tag', 'TagName', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='TagName'))

        # Renaming column for 'Tag.cid' to match new field type.
        db.rename_column(u'MemManage_tag', 'cid_id', 'TagCompany')
        # Changing field 'Tag.cid'
        db.alter_column(u'MemManage_tag', 'TagCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='TagCompany'))

        # Renaming column for 'Group.gname' to match new field type.
        db.rename_column(u'MemManage_group', 'gname', 'GroupName')
        # Changing field 'Group.gname'
        db.alter_column(u'MemManage_group', 'GroupName', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='GroupName'))

        # Renaming column for 'Group.cid' to match new field type.
        db.rename_column(u'MemManage_group', 'cid_id', 'GroupCompany')
        # Changing field 'Group.cid'
        db.alter_column(u'MemManage_group', 'GroupCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='GroupCompany'))

        # Renaming column for 'Role.name' to match new field type.
        db.rename_column(u'MemManage_role', 'name', 'RoleName')
        # Changing field 'Role.name'
        db.alter_column(u'MemManage_role', 'RoleName', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='RoleName'))

        # Renaming column for 'Role.company' to match new field type.
        db.rename_column(u'MemManage_role', 'company_id', 'RoleCompany')
        # Changing field 'Role.company'
        db.alter_column(u'MemManage_role', 'RoleCompany', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MemManage.Company'], db_column='RoleCompany'))

        # Renaming column for 'Role.idcard' to match new field type.
        db.rename_column(u'MemManage_role', 'idcard', 'RoleIdcard')
        # Changing field 'Role.idcard'
        db.alter_column(u'MemManage_role', 'RoleIdcard', self.gf('django.db.models.fields.CharField')(max_length=20, db_column='RoleIdcard'))

        # Renaming column for 'Role.sex' to match new field type.
        db.rename_column(u'MemManage_role', 'sex', 'RoleSex')
        # Changing field 'Role.sex'
        db.alter_column(u'MemManage_role', 'RoleSex', self.gf('django.db.models.fields.IntegerField')(db_column='RoleSex'))

        # Renaming column for 'Role.phone' to match new field type.
        db.rename_column(u'MemManage_role', 'phone', 'RolePhone')
        # Changing field 'Role.phone'
        db.alter_column(u'MemManage_role', 'RolePhone', self.gf('django.db.models.fields.CharField')(max_length=15, db_column='RolePhone'))

        # Renaming column for 'Role.location' to match new field type.
        db.rename_column(u'MemManage_role', 'location', 'RoleLocation')
        # Changing field 'Role.location'
        db.alter_column(u'MemManage_role', 'RoleLocation', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='RoleLocation'))

        # Renaming column for 'Role.aid' to match new field type.
        db.rename_column(u'MemManage_role', 'aid_id', 'RoleAccount')
        # Changing field 'Role.aid'
        db.alter_column(u'MemManage_role', 'RoleAccount', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Login.Account'], db_column='RoleAccount'))

        # Renaming column for 'Role.email' to match new field type.
        db.rename_column(u'MemManage_role', 'email', 'RoleEmail')
        # Changing field 'Role.email'
        db.alter_column(u'MemManage_role', 'RoleEmail', self.gf('django.db.models.fields.EmailField')(max_length=30, db_column='RoleEmail'))

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
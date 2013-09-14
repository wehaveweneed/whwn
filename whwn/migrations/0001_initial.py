# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'whwn_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('sku', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.SKU'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('requested', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('possessor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'whwn', ['Item'])

        # Adding model 'SKU'
        db.create_table(u'whwn_sku', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('upc', self.gf('django.db.models.fields.CharField')(max_length=54, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'whwn', ['SKU'])

        # Adding model 'Category'
        db.create_table(u'whwn_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'whwn', ['Category'])

        # Adding model 'Message'
        db.create_table(u'whwn_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.User'])),
            ('contents', self.gf('django.db.models.fields.TextField')(default='')),
            ('flagged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'])),
        ))
        db.send_create_signal(u'whwn', ['Message'])

        # Adding model 'Team'
        db.create_table(u'whwn_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', null=True, to=orm['whwn.User'])),
        ))
        db.send_create_signal(u'whwn', ['Team'])

        # Adding model 'User'
        db.create_table(u'whwn_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('email_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Team'])),
        ))
        db.send_create_signal(u'whwn', ['User'])

        # Adding M2M table for field groups on 'User'
        db.create_table(u'whwn_user_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'whwn.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'whwn_user_groups', ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        db.create_table(u'whwn_user_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'whwn.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'whwn_user_user_permissions', ['user_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'whwn_item')

        # Deleting model 'SKU'
        db.delete_table(u'whwn_sku')

        # Deleting model 'Category'
        db.delete_table(u'whwn_category')

        # Deleting model 'Message'
        db.delete_table(u'whwn_message')

        # Deleting model 'Team'
        db.delete_table(u'whwn_team')

        # Deleting model 'User'
        db.delete_table(u'whwn_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table('whwn_user_groups')

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table('whwn_user_user_permissions')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'whwn.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'whwn.item': {
            'Meta': {'object_name': 'Item'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'possessor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.User']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'requested': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.SKU']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'whwn.message': {
            'Meta': {'object_name': 'Message'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.User']"}),
            'contents': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'whwn.sku': {
            'Meta': {'object_name': 'SKU'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.Team']"}),
            'upc': ('django.db.models.fields.CharField', [], {'max_length': '54', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'whwn.team': {
            'Meta': {'object_name': 'Team'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'null': 'True', 'to': u"orm['whwn.User']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'whwn.user': {
            'Meta': {'object_name': 'User'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['whwn']
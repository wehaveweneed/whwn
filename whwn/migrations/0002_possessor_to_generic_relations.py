# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Item.possessor'
        db.delete_column(u'whwn_item', 'possessor_id')

        # Adding field 'Item.content_type'
        db.add_column(u'whwn_item', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.object_id'
        db.add_column(u'whwn_item', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'SKU.category'
        db.add_column(u'whwn_sku', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.Category'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Item.possessor'
        db.add_column(u'whwn_item', 'possessor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whwn.User'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Item.content_type'
        db.delete_column(u'whwn_item', 'content_type_id')

        # Deleting field 'Item.object_id'
        db.delete_column(u'whwn_item', 'object_id')

        # Deleting field 'SKU.category'
        db.delete_column(u'whwn_sku', 'category_id')


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
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whwn.Category']", 'null': 'True', 'blank': 'True'}),
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
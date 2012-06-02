# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shape'
        db.create_table(u'stgd', (
            ('gid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('address_po', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address_fu', self.gf('django.db.models.fields.CharField')(max_length=131, blank=True)),
            ('objectid', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('struct_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('common_nam', self.gf('django.db.models.fields.CharField')(max_length=254, blank=True)),
            ('botanical', self.gf('django.db.models.fields.CharField')(max_length=254, blank=True)),
            ('diameter_b', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('tree_posit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=0, null=True, blank=True)),
        ))
        db.send_create_signal('arbor', ['Shape'])


    def backwards(self, orm):
        # Deleting model 'Shape'
        db.delete_table(u'stgd')


    models = {
        'arbor.shape': {
            'Meta': {'object_name': 'Shape', 'db_table': "u'stgd'"},
            'address_fu': ('django.db.models.fields.CharField', [], {'max_length': '131', 'blank': 'True'}),
            'address_po': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'botanical': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'common_nam': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'diameter_b': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '0', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'objectid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'struct_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'tree_posit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['arbor']
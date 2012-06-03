# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('arbor_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('small_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('big_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('arbor', ['Image'])

        # Adding M2M table for field botanical on 'Image'
        db.create_table('arbor_image_botanical', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm['arbor.image'], null=False)),
            ('shape', models.ForeignKey(orm['arbor.shape'], null=False))
        ))
        db.create_unique('arbor_image_botanical', ['image_id', 'shape_id'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('arbor_image')

        # Removing M2M table for field botanical on 'Image'
        db.delete_table('arbor_image_botanical')


    models = {
        'arbor.image': {
            'Meta': {'object_name': 'Image'},
            'big_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'botanical': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['arbor.Shape']", 'symmetrical': 'False'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'small_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'arbor.shape': {
            'Meta': {'object_name': 'Shape', 'db_table': "u'stgd'"},
            'address_fu': ('django.db.models.fields.CharField', [], {'max_length': '131', 'blank': 'True'}),
            'address_po': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'botanical': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_column': "'botanical_'", 'blank': 'True'}),
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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tutor.availability'
        db.add_column(u'tutorboard_tutor', 'availability',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.picture'
        db.add_column(u'tutorboard_tutor', 'picture',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Tutor.neighborhood'
        db.alter_column(u'tutorboard_tutor', 'neighborhood', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.bioline2'
        db.alter_column(u'tutorboard_tutor', 'bioline2', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.zip'
        db.alter_column(u'tutorboard_tutor', 'zip', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.address1'
        db.alter_column(u'tutorboard_tutor', 'address1', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.address2'
        db.alter_column(u'tutorboard_tutor', 'address2', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.lname'
        db.alter_column(u'tutorboard_tutor', 'lname', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.bioline5'
        db.alter_column(u'tutorboard_tutor', 'bioline5', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.state'
        db.alter_column(u'tutorboard_tutor', 'state', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.city'
        db.alter_column(u'tutorboard_tutor', 'city', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.bioline1'
        db.alter_column(u'tutorboard_tutor', 'bioline1', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.fname'
        db.alter_column(u'tutorboard_tutor', 'fname', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.bioline3'
        db.alter_column(u'tutorboard_tutor', 'bioline3', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.bioline4'
        db.alter_column(u'tutorboard_tutor', 'bioline4', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.altemail'
        db.alter_column(u'tutorboard_tutor', 'altemail', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.email'
        db.alter_column(u'tutorboard_tutor', 'email', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.gotofor'
        db.alter_column(u'tutorboard_tutor', 'gotofor', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Subject.name'
        db.alter_column(u'tutorboard_subject', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'Tutor.availability'
        db.delete_column(u'tutorboard_tutor', 'availability')

        # Deleting field 'Tutor.picture'
        db.delete_column(u'tutorboard_tutor', 'picture')


        # Changing field 'Tutor.neighborhood'
        db.alter_column(u'tutorboard_tutor', 'neighborhood', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.bioline2'
        db.alter_column(u'tutorboard_tutor', 'bioline2', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.zip'
        db.alter_column(u'tutorboard_tutor', 'zip', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Tutor.address1'
        db.alter_column(u'tutorboard_tutor', 'address1', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Tutor.address2'
        db.alter_column(u'tutorboard_tutor', 'address2', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.lname'
        db.alter_column(u'tutorboard_tutor', 'lname', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Tutor.bioline5'
        db.alter_column(u'tutorboard_tutor', 'bioline5', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.state'
        db.alter_column(u'tutorboard_tutor', 'state', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Tutor.city'
        db.alter_column(u'tutorboard_tutor', 'city', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.bioline1'
        db.alter_column(u'tutorboard_tutor', 'bioline1', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Tutor.fname'
        db.alter_column(u'tutorboard_tutor', 'fname', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Tutor.bioline3'
        db.alter_column(u'tutorboard_tutor', 'bioline3', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.bioline4'
        db.alter_column(u'tutorboard_tutor', 'bioline4', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.altemail'
        db.alter_column(u'tutorboard_tutor', 'altemail', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.email'
        db.alter_column(u'tutorboard_tutor', 'email', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Tutor.gotofor'
        db.alter_column(u'tutorboard_tutor', 'gotofor', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Subject.name'
        db.alter_column(u'tutorboard_subject', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'tutorboard.capability': {
            'Meta': {'object_name': 'Capability'},
            'ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Subject']"}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Tutor']"})
        },
        u'tutorboard.subject': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tutorboard.tutor': {
            'Meta': {'ordering': "('lname',)", 'object_name': 'Tutor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altemail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '1', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'bioline1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
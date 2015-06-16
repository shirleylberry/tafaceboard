# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tutor.hidden'
        db.alter_column(u'tutorboard_tutor', 'hidden', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Tutor.hidden'
        db.alter_column(u'tutorboard_tutor', 'hidden', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    models = {
        u'tutorboard.archetype': {
            'Meta': {'object_name': 'Archetype'},
            'archetype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tutorboard.capability': {
            'Meta': {'object_name': 'Capability'},
            'ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'level_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modifier1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Subject']"}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Tutor']"})
        },
        u'tutorboard.energy': {
            'Meta': {'object_name': 'Energy'},
            'energy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tutorboard.levelpreference': {
            'Meta': {'object_name': 'LevelPreference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'levelPref': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.presence': {
            'Meta': {'object_name': 'Presence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.studentengagement': {
            'Meta': {'object_name': 'StudentEngagement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'studentName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.style': {
            'Meta': {'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.subject': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageAP': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modifier1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modifier2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modifier3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modifier4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.subjectupdate': {
            'Meta': {'object_name': 'SubjectUpdate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tutorboard.tutor': {
            'Meta': {'ordering': "('fname',)", 'object_name': 'Tutor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altemail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'archetype': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Archetype']", 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '255', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'availability_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'availability_vacation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bioline1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Energy']", 'null': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'highestLevel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'highestLevelManual': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levelPreferences': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.LevelPreference']", 'null': 'True', 'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Location']", 'null': 'True', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Presence']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '255', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Skill']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'studentEngagements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.StudentEngagement']", 'null': 'True', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Style']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
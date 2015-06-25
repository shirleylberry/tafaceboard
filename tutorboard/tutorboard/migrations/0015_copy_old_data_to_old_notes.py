# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        tutors = orm.Tutor.objects.all()

        for tutor in tutors:
            if tutor.availability_note:
                notes_text = tutor.availability_note
                parts = notes_text.split('###')
                real_note = parts[0]
                tutor.availability_note = real_note
                if len(parts) > 1:
                    old_data = parts[1]
                    tutor.old_notes = old_data
                tutor.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'tutorboard.capability': {
            'Meta': {'object_name': 'Capability'},
            'area': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '255'}),
            'level_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Subject']"}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Tutor']"})
        },
        u'tutorboard.subject': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageAP': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'area': ('django.db.models.fields.CharField', [], {'default': "'verbal'", 'max_length': '255', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'availability_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'availability_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'availability_vacation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bioline1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'highestLevel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'highestLevelManual': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'old_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tutorboard.Subject']", 'through': u"orm['tutorboard.Capability']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
    symmetrical = True

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skill'
        db.create_table(u'tutorboard_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Skill'])

        # Adding field 'Style.image'
        db.add_column(u'tutorboard_style', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier1'
        db.add_column(u'tutorboard_subject', 'modifier1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod1'
        db.add_column(u'tutorboard_subject', 'imageMod1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier2'
        db.add_column(u'tutorboard_subject', 'modifier2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod2'
        db.add_column(u'tutorboard_subject', 'imageMod2',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier3'
        db.add_column(u'tutorboard_subject', 'modifier3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod3'
        db.add_column(u'tutorboard_subject', 'imageMod3',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier4'
        db.add_column(u'tutorboard_subject', 'modifier4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod4'
        db.add_column(u'tutorboard_subject', 'imageMod4',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageAP'
        db.add_column(u'tutorboard_subject', 'imageAP',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'LevelPreference.image'
        db.add_column(u'tutorboard_levelpreference', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.highestLevel'
        db.add_column(u'tutorboard_tutor', 'highestLevel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding M2M table for field skills on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('skill', models.ForeignKey(orm[u'tutorboard.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'skill_id'])


        # Changing field 'Tutor.cell'
        db.alter_column(u'tutorboard_tutor', 'cell', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.sex'
        db.alter_column(u'tutorboard_tutor', 'sex', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.zip'
        db.alter_column(u'tutorboard_tutor', 'zip', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.area'
        db.alter_column(u'tutorboard_tutor', 'area', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Tutor.altphone'
        db.alter_column(u'tutorboard_tutor', 'altphone', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Adding field 'Capability.modifier1'
        db.add_column(u'tutorboard_capability', 'modifier1',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Capability.modifier2'
        db.add_column(u'tutorboard_capability', 'modifier2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Capability.modifier3'
        db.add_column(u'tutorboard_capability', 'modifier3',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Capability.modifier4'
        db.add_column(u'tutorboard_capability', 'modifier4',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Capability.level'
        db.alter_column(u'tutorboard_capability', 'level', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting model 'Skill'
        db.delete_table(u'tutorboard_skill')

        # Deleting field 'Style.image'
        db.delete_column(u'tutorboard_style', 'image')

        # Deleting field 'Subject.modifier1'
        db.delete_column(u'tutorboard_subject', 'modifier1')

        # Deleting field 'Subject.imageMod1'
        db.delete_column(u'tutorboard_subject', 'imageMod1')

        # Deleting field 'Subject.modifier2'
        db.delete_column(u'tutorboard_subject', 'modifier2')

        # Deleting field 'Subject.imageMod2'
        db.delete_column(u'tutorboard_subject', 'imageMod2')

        # Deleting field 'Subject.modifier3'
        db.delete_column(u'tutorboard_subject', 'modifier3')

        # Deleting field 'Subject.imageMod3'
        db.delete_column(u'tutorboard_subject', 'imageMod3')

        # Deleting field 'Subject.modifier4'
        db.delete_column(u'tutorboard_subject', 'modifier4')

        # Deleting field 'Subject.imageMod4'
        db.delete_column(u'tutorboard_subject', 'imageMod4')

        # Deleting field 'Subject.imageAP'
        db.delete_column(u'tutorboard_subject', 'imageAP')

        # Deleting field 'LevelPreference.image'
        db.delete_column(u'tutorboard_levelpreference', 'image')

        # Deleting field 'Tutor.highestLevel'
        db.delete_column(u'tutorboard_tutor', 'highestLevel')

        # Removing M2M table for field skills on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_skills'))


        # Changing field 'Tutor.cell'
        db.alter_column(u'tutorboard_tutor', 'cell', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.sex'
        db.alter_column(u'tutorboard_tutor', 'sex', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Tutor.zip'
        db.alter_column(u'tutorboard_tutor', 'zip', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Tutor.area'
        db.alter_column(u'tutorboard_tutor', 'area', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Tutor.altphone'
        db.alter_column(u'tutorboard_tutor', 'altphone', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Deleting field 'Capability.modifier1'
        db.delete_column(u'tutorboard_capability', 'modifier1')

        # Deleting field 'Capability.modifier2'
        db.delete_column(u'tutorboard_capability', 'modifier2')

        # Deleting field 'Capability.modifier3'
        db.delete_column(u'tutorboard_capability', 'modifier3')

        # Deleting field 'Capability.modifier4'
        db.delete_column(u'tutorboard_capability', 'modifier4')


        # Changing field 'Capability.level'
        db.alter_column(u'tutorboard_capability', 'level', self.gf('django.db.models.fields.CharField')(max_length=2))

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
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modifier1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modifier4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'tutorboard.tutor': {
            'Meta': {'ordering': "('fname',)", 'object_name': 'Tutor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altemail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'archetype': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Archetype']", 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '255', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
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
            'highestLevel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
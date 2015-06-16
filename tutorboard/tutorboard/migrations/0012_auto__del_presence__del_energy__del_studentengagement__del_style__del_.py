# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Presence'
        db.delete_table(u'tutorboard_presence')

        # Deleting model 'Energy'
        db.delete_table(u'tutorboard_energy')

        # Deleting model 'StudentEngagement'
        db.delete_table(u'tutorboard_studentengagement')

        # Deleting model 'Style'
        db.delete_table(u'tutorboard_style')

        # Deleting model 'LevelPreference'
        db.delete_table(u'tutorboard_levelpreference')

        # Deleting model 'Skill'
        db.delete_table(u'tutorboard_skill')

        # Deleting model 'Archetype'
        db.delete_table(u'tutorboard_archetype')

        # Deleting model 'Location'
        db.delete_table(u'tutorboard_location')

        # Deleting field 'Subject.modifier1'
        db.delete_column(u'tutorboard_subject', 'modifier1')

        # Deleting field 'Subject.modifier3'
        db.delete_column(u'tutorboard_subject', 'modifier3')

        # Deleting field 'Subject.imageMod2'
        db.delete_column(u'tutorboard_subject', 'imageMod2')

        # Deleting field 'Subject.imageMod3'
        db.delete_column(u'tutorboard_subject', 'imageMod3')

        # Deleting field 'Subject.modifier2'
        db.delete_column(u'tutorboard_subject', 'modifier2')

        # Deleting field 'Subject.imageMod1'
        db.delete_column(u'tutorboard_subject', 'imageMod1')

        # Deleting field 'Subject.modifier4'
        db.delete_column(u'tutorboard_subject', 'modifier4')

        # Deleting field 'Subject.imageMod4'
        db.delete_column(u'tutorboard_subject', 'imageMod4')

        # Adding field 'Subject.is_ap'
        db.add_column(u'tutorboard_subject', 'is_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Capability.ap'
        db.delete_column(u'tutorboard_capability', 'ap')

        # Deleting field 'Capability.modifier1'
        db.delete_column(u'tutorboard_capability', 'modifier1')

        # Deleting field 'Capability.modifier2'
        db.delete_column(u'tutorboard_capability', 'modifier2')

        # Deleting field 'Capability.modifier3'
        db.delete_column(u'tutorboard_capability', 'modifier3')

        # Deleting field 'Capability.modifier4'
        db.delete_column(u'tutorboard_capability', 'modifier4')

        # Deleting field 'Capability.modifier'
        db.delete_column(u'tutorboard_capability', 'modifier')

        # Adding field 'Capability.area'
        db.add_column(u'tutorboard_capability', 'area',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Tutor.sex'
        db.delete_column(u'tutorboard_tutor', 'sex')

        # Removing M2M table for field styles on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_styles'))

        # Removing M2M table for field levelPreferences on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_levelPreferences'))

        # Removing M2M table for field energy on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_energy'))

        # Removing M2M table for field archetype on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_archetype'))

        # Removing M2M table for field studentEngagements on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_studentEngagements'))

        # Removing M2M table for field presence on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_presence'))

        # Removing M2M table for field skills on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_skills'))

        # Removing M2M table for field location on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_location'))


    def backwards(self, orm):
        # Adding model 'Presence'
        db.create_table(u'tutorboard_presence', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presence', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Presence'])

        # Adding model 'Energy'
        db.create_table(u'tutorboard_energy', (
            ('energy', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Energy'])

        # Adding model 'StudentEngagement'
        db.create_table(u'tutorboard_studentengagement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('studentName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['StudentEngagement'])

        # Adding model 'Style'
        db.create_table(u'tutorboard_style', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Style'])

        # Adding model 'LevelPreference'
        db.create_table(u'tutorboard_levelpreference', (
            ('levelPref', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tutorboard', ['LevelPreference'])

        # Adding model 'Skill'
        db.create_table(u'tutorboard_skill', (
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Skill'])

        # Adding model 'Archetype'
        db.create_table(u'tutorboard_archetype', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('archetype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Archetype'])

        # Adding model 'Location'
        db.create_table(u'tutorboard_location', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Location'])

        # Adding field 'Subject.modifier1'
        db.add_column(u'tutorboard_subject', 'modifier1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier3'
        db.add_column(u'tutorboard_subject', 'modifier3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod2'
        db.add_column(u'tutorboard_subject', 'imageMod2',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod3'
        db.add_column(u'tutorboard_subject', 'imageMod3',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.modifier2'
        db.add_column(u'tutorboard_subject', 'modifier2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Subject.imageMod1'
        db.add_column(u'tutorboard_subject', 'imageMod1',
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

        # Deleting field 'Subject.is_ap'
        db.delete_column(u'tutorboard_subject', 'is_ap')

        # Adding field 'Capability.ap'
        db.add_column(u'tutorboard_capability', 'ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

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

        # Adding field 'Capability.modifier'
        db.add_column(u'tutorboard_capability', 'modifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Capability.area'
        db.delete_column(u'tutorboard_capability', 'area')

        # Adding field 'Tutor.sex'
        db.add_column(u'tutorboard_tutor', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='F', max_length=255, blank=True),
                      keep_default=False)

        # Adding M2M table for field styles on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_styles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('style', models.ForeignKey(orm[u'tutorboard.style'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'style_id'])

        # Adding M2M table for field levelPreferences on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_levelPreferences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('levelpreference', models.ForeignKey(orm[u'tutorboard.levelpreference'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'levelpreference_id'])

        # Adding M2M table for field energy on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_energy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('energy', models.ForeignKey(orm[u'tutorboard.energy'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'energy_id'])

        # Adding M2M table for field archetype on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_archetype')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('archetype', models.ForeignKey(orm[u'tutorboard.archetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'archetype_id'])

        # Adding M2M table for field studentEngagements on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_studentEngagements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('studentengagement', models.ForeignKey(orm[u'tutorboard.studentengagement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'studentengagement_id'])

        # Adding M2M table for field presence on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_presence')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('presence', models.ForeignKey(orm[u'tutorboard.presence'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'presence_id'])

        # Adding M2M table for field skills on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('skill', models.ForeignKey(orm[u'tutorboard.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'skill_id'])

        # Adding M2M table for field location on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_location')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('location', models.ForeignKey(orm[u'tutorboard.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'location_id'])


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
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
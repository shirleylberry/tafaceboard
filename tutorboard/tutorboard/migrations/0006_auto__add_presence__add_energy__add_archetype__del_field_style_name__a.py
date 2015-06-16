# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presence'
        db.create_table(u'tutorboard_presence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presence', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Presence'])

        # Adding model 'Energy'
        db.create_table(u'tutorboard_energy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('energy', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Energy'])

        # Adding model 'Archetype'
        db.create_table(u'tutorboard_archetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archetype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Archetype'])

        # Deleting field 'Style.name'
        db.delete_column(u'tutorboard_style', 'name')

        # Adding field 'Style.style'
        db.add_column(u'tutorboard_style', 'style',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Tutor.energy'
        db.delete_column(u'tutorboard_tutor', 'energy')

        # Deleting field 'Tutor.presence'
        db.delete_column(u'tutorboard_tutor', 'presence')

        # Deleting field 'Tutor.archetype'
        db.delete_column(u'tutorboard_tutor', 'archetype')

        # Deleting field 'Tutor.location'
        db.delete_column(u'tutorboard_tutor', 'location_id')

        # Adding M2M table for field energy on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_energy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('energy', models.ForeignKey(orm[u'tutorboard.energy'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'energy_id'])

        # Adding M2M table for field presence on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_presence')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('presence', models.ForeignKey(orm[u'tutorboard.presence'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'presence_id'])

        # Adding M2M table for field archetype on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_archetype')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('archetype', models.ForeignKey(orm[u'tutorboard.archetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'archetype_id'])

        # Adding M2M table for field location on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_location')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('location', models.ForeignKey(orm[u'tutorboard.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'location_id'])

        # Deleting field 'LevelPreference.level'
        db.delete_column(u'tutorboard_levelpreference', 'level')

        # Adding field 'LevelPreference.levelPref'
        db.add_column(u'tutorboard_levelpreference', 'levelPref',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Location.image'
        db.add_column(u'tutorboard_location', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.image'
        db.add_column(u'tutorboard_subject', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Presence'
        db.delete_table(u'tutorboard_presence')

        # Deleting model 'Energy'
        db.delete_table(u'tutorboard_energy')

        # Deleting model 'Archetype'
        db.delete_table(u'tutorboard_archetype')

        # Adding field 'Style.name'
        db.add_column(u'tutorboard_style', 'name',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=255),
                      keep_default=False)

        # Deleting field 'Style.style'
        db.delete_column(u'tutorboard_style', 'style')

        # Adding field 'Tutor.energy'
        db.add_column(u'tutorboard_tutor', 'energy',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.presence'
        db.add_column(u'tutorboard_tutor', 'presence',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.archetype'
        db.add_column(u'tutorboard_tutor', 'archetype',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.location'
        db.add_column(u'tutorboard_tutor', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutorboard.Location'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field energy on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_energy'))

        # Removing M2M table for field presence on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_presence'))

        # Removing M2M table for field archetype on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_archetype'))

        # Removing M2M table for field location on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_location'))

        # Adding field 'LevelPreference.level'
        db.add_column(u'tutorboard_levelpreference', 'level',
                      self.gf('django.db.models.fields.CharField')(default='level', max_length=255),
                      keep_default=False)

        # Deleting field 'LevelPreference.levelPref'
        db.delete_column(u'tutorboard_levelpreference', 'levelPref')

        # Deleting field 'Location.image'
        db.delete_column(u'tutorboard_location', 'image')

        # Deleting field 'Subject.image'
        db.delete_column(u'tutorboard_subject', 'image')


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
            'level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'modifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
        u'tutorboard.studentengagement': {
            'Meta': {'object_name': 'StudentEngagement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'studentName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.style': {
            'Meta': {'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.subject': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.tutor': {
            'Meta': {'ordering': "('fname',)", 'object_name': 'Tutor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altemail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'archetype': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Archetype']", 'null': 'True', 'blank': 'True'}),
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
            'energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Energy']", 'null': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levelPreferences': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.LevelPreference']", 'null': 'True', 'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Location']", 'null': 'True', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Presence']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'studentEngagements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.StudentEngagement']", 'null': 'True', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Style']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
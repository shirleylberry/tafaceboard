# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Style'
        db.create_table(u'tutorboard_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tutorboard', ['Style'])

        # Adding model 'StudentEngagement'
        db.create_table(u'tutorboard_studentengagement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('studentName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tutorboard', ['StudentEngagement'])

        # Adding model 'LevelPreference'
        db.create_table(u'tutorboard_levelpreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tutorboard', ['LevelPreference'])

        # Adding model 'Location'
        db.create_table(u'tutorboard_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tutorboard', ['Location'])

        # Adding field 'Capability.modifier'
        db.add_column(u'tutorboard_capability', 'modifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Tutor.gender'
        db.add_column(u'tutorboard_tutor', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

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

        # Adding M2M table for field studentEngagements on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_studentEngagements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('studentengagement', models.ForeignKey(orm[u'tutorboard.studentengagement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'studentengagement_id'])


    def backwards(self, orm):
        # Deleting model 'Style'
        db.delete_table(u'tutorboard_style')

        # Deleting model 'StudentEngagement'
        db.delete_table(u'tutorboard_studentengagement')

        # Deleting model 'LevelPreference'
        db.delete_table(u'tutorboard_levelpreference')

        # Deleting model 'Location'
        db.delete_table(u'tutorboard_location')

        # Deleting field 'Capability.modifier'
        db.delete_column(u'tutorboard_capability', 'modifier')

        # Deleting field 'Tutor.gender'
        db.delete_column(u'tutorboard_tutor', 'gender')

        # Deleting field 'Tutor.energy'
        db.delete_column(u'tutorboard_tutor', 'energy')

        # Deleting field 'Tutor.presence'
        db.delete_column(u'tutorboard_tutor', 'presence')

        # Deleting field 'Tutor.archetype'
        db.delete_column(u'tutorboard_tutor', 'archetype')

        # Deleting field 'Tutor.location'
        db.delete_column(u'tutorboard_tutor', 'location_id')

        # Removing M2M table for field styles on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_styles'))

        # Removing M2M table for field levelPreferences on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_levelPreferences'))

        # Removing M2M table for field studentEngagements on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_studentEngagements'))


    models = {
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
        u'tutorboard.levelpreference': {
            'Meta': {'object_name': 'LevelPreference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tutorboard.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tutorboard.studentengagement': {
            'Meta': {'object_name': 'StudentEngagement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'studentName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tutorboard.style': {
            'Meta': {'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'archetype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
            'energy': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levelPreferences': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.LevelPreference']", 'null': 'True', 'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutorboard.Location']", 'null': 'True', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'studentEngagements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.StudentEngagement']", 'null': 'True', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tutorboard.Style']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
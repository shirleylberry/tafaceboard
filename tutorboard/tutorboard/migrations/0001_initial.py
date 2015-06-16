# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'tutorboard_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('level', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('ap', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'tutorboard', ['Subject'])

        # Adding model 'Tutor'
        db.create_table(u'tutorboard_tutor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('altphone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('altemail', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gotofor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bioline1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bioline2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bioline3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bioline4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bioline5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
            ('area', self.gf('django.db.models.fields.CharField')(default='V', max_length=1)),
        ))
        db.send_create_signal(u'tutorboard', ['Tutor'])

        # Adding M2M table for field subjects on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('subject', models.ForeignKey(orm[u'tutorboard.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'subject_id'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'tutorboard_subject')

        # Deleting model 'Tutor'
        db.delete_table(u'tutorboard_tutor')

        # Removing M2M table for field subjects on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_subjects'))


    models = {
        u'tutorboard.subject': {
            'Meta': {'object_name': 'Subject'},
            'ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'tutorboard.tutor': {
            'Meta': {'ordering': "('lname',)", 'object_name': 'Tutor'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'altemail': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'area': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '1'}),
            'bioline1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bioline2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bioline3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bioline4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bioline5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tutorboard.Subject']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['tutorboard']
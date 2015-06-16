# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'tutorboard_subject')

        # Adding field 'Tutor.cornerstone_math_level'
        db.add_column(u'tutorboard_tutor', 'cornerstone_math_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.cornerstone_math_ap'
        db.add_column(u'tutorboard_tutor', 'cornerstone_math_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.cornerstone_math_score'
        db.add_column(u'tutorboard_tutor', 'cornerstone_math_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.cornerstone_verbal_level'
        db.add_column(u'tutorboard_tutor', 'cornerstone_verbal_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.cornerstone_verbal_ap'
        db.add_column(u'tutorboard_tutor', 'cornerstone_verbal_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.cornerstone_verbal_score'
        db.add_column(u'tutorboard_tutor', 'cornerstone_verbal_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.math_lower_level'
        db.add_column(u'tutorboard_tutor', 'math_lower_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.math_lower_ap'
        db.add_column(u'tutorboard_tutor', 'math_lower_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.math_lower_score'
        db.add_column(u'tutorboard_tutor', 'math_lower_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.math_upper_level'
        db.add_column(u'tutorboard_tutor', 'math_upper_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.math_upper_ap'
        db.add_column(u'tutorboard_tutor', 'math_upper_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.math_upper_score'
        db.add_column(u'tutorboard_tutor', 'math_upper_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.biology_level'
        db.add_column(u'tutorboard_tutor', 'biology_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.biology_ap'
        db.add_column(u'tutorboard_tutor', 'biology_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.biology_score'
        db.add_column(u'tutorboard_tutor', 'biology_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.chemistry_level'
        db.add_column(u'tutorboard_tutor', 'chemistry_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.chemistry_ap'
        db.add_column(u'tutorboard_tutor', 'chemistry_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.chemistry_score'
        db.add_column(u'tutorboard_tutor', 'chemistry_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.physics_level'
        db.add_column(u'tutorboard_tutor', 'physics_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.physics_ap'
        db.add_column(u'tutorboard_tutor', 'physics_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.physics_score'
        db.add_column(u'tutorboard_tutor', 'physics_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.english_level'
        db.add_column(u'tutorboard_tutor', 'english_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.english_ap'
        db.add_column(u'tutorboard_tutor', 'english_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.english_score'
        db.add_column(u'tutorboard_tutor', 'english_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.english_grammer_level'
        db.add_column(u'tutorboard_tutor', 'english_grammer_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.english_grammer_ap'
        db.add_column(u'tutorboard_tutor', 'english_grammer_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.english_grammer_score'
        db.add_column(u'tutorboard_tutor', 'english_grammer_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.history_us_level'
        db.add_column(u'tutorboard_tutor', 'history_us_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.history_us_ap'
        db.add_column(u'tutorboard_tutor', 'history_us_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.history_us_score'
        db.add_column(u'tutorboard_tutor', 'history_us_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.history_world_level'
        db.add_column(u'tutorboard_tutor', 'history_world_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.history_world_ap'
        db.add_column(u'tutorboard_tutor', 'history_world_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.history_world_score'
        db.add_column(u'tutorboard_tutor', 'history_world_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.spanish_level'
        db.add_column(u'tutorboard_tutor', 'spanish_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.spanish_ap'
        db.add_column(u'tutorboard_tutor', 'spanish_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.spanish_score'
        db.add_column(u'tutorboard_tutor', 'spanish_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.french_level'
        db.add_column(u'tutorboard_tutor', 'french_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.french_ap'
        db.add_column(u'tutorboard_tutor', 'french_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.french_score'
        db.add_column(u'tutorboard_tutor', 'french_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.latin_level'
        db.add_column(u'tutorboard_tutor', 'latin_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.latin_ap'
        db.add_column(u'tutorboard_tutor', 'latin_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.latin_score'
        db.add_column(u'tutorboard_tutor', 'latin_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.echelon_math_level'
        db.add_column(u'tutorboard_tutor', 'echelon_math_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.echelon_math_ap'
        db.add_column(u'tutorboard_tutor', 'echelon_math_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.echelon_math_score'
        db.add_column(u'tutorboard_tutor', 'echelon_math_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level1_level'
        db.add_column(u'tutorboard_tutor', 'sat_math_level1_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level1_ap'
        db.add_column(u'tutorboard_tutor', 'sat_math_level1_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level1_score'
        db.add_column(u'tutorboard_tutor', 'sat_math_level1_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level2_level'
        db.add_column(u'tutorboard_tutor', 'sat_math_level2_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level2_ap'
        db.add_column(u'tutorboard_tutor', 'sat_math_level2_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_math_level2_score'
        db.add_column(u'tutorboard_tutor', 'sat_math_level2_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.echelon_verbal_level'
        db.add_column(u'tutorboard_tutor', 'echelon_verbal_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.echelon_verbal_ap'
        db.add_column(u'tutorboard_tutor', 'echelon_verbal_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.echelon_verbal_score'
        db.add_column(u'tutorboard_tutor', 'echelon_verbal_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_lit_level'
        db.add_column(u'tutorboard_tutor', 'sat_lit_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_lit_ap'
        db.add_column(u'tutorboard_tutor', 'sat_lit_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_lit_score'
        db.add_column(u'tutorboard_tutor', 'sat_lit_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_bio_level'
        db.add_column(u'tutorboard_tutor', 'sat_bio_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_bio_ap'
        db.add_column(u'tutorboard_tutor', 'sat_bio_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_bio_score'
        db.add_column(u'tutorboard_tutor', 'sat_bio_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_chem_level'
        db.add_column(u'tutorboard_tutor', 'sat_chem_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_chem_ap'
        db.add_column(u'tutorboard_tutor', 'sat_chem_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_chem_score'
        db.add_column(u'tutorboard_tutor', 'sat_chem_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_physics_level'
        db.add_column(u'tutorboard_tutor', 'sat_physics_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_physics_ap'
        db.add_column(u'tutorboard_tutor', 'sat_physics_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_physics_score'
        db.add_column(u'tutorboard_tutor', 'sat_physics_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_us_hist_level'
        db.add_column(u'tutorboard_tutor', 'sat_us_hist_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_us_hist_ap'
        db.add_column(u'tutorboard_tutor', 'sat_us_hist_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_us_hist_score'
        db.add_column(u'tutorboard_tutor', 'sat_us_hist_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_world_hist_level'
        db.add_column(u'tutorboard_tutor', 'sat_world_hist_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_world_hist_ap'
        db.add_column(u'tutorboard_tutor', 'sat_world_hist_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_world_hist_score'
        db.add_column(u'tutorboard_tutor', 'sat_world_hist_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_spanish_level'
        db.add_column(u'tutorboard_tutor', 'sat_spanish_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_spanish_ap'
        db.add_column(u'tutorboard_tutor', 'sat_spanish_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_spanish_score'
        db.add_column(u'tutorboard_tutor', 'sat_spanish_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_french_level'
        db.add_column(u'tutorboard_tutor', 'sat_french_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_french_ap'
        db.add_column(u'tutorboard_tutor', 'sat_french_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_french_score'
        db.add_column(u'tutorboard_tutor', 'sat_french_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Tutor.sat_latin_level'
        db.add_column(u'tutorboard_tutor', 'sat_latin_level',
                      self.gf('django.db.models.fields.CharField')(default='NO', max_length=2),
                      keep_default=False)

        # Adding field 'Tutor.sat_latin_ap'
        db.add_column(u'tutorboard_tutor', 'sat_latin_ap',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tutor.sat_latin_score'
        db.add_column(u'tutorboard_tutor', 'sat_latin_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Removing M2M table for field subjects on 'Tutor'
        db.delete_table(db.shorten_name(u'tutorboard_tutor_subjects'))


    def backwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'tutorboard_subject', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('level', self.gf('django.db.models.fields.CharField')(default='NO', max_length=2)),
            ('ap', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tutorboard', ['Subject'])

        # Deleting field 'Tutor.cornerstone_math_level'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_math_level')

        # Deleting field 'Tutor.cornerstone_math_ap'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_math_ap')

        # Deleting field 'Tutor.cornerstone_math_score'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_math_score')

        # Deleting field 'Tutor.cornerstone_verbal_level'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_verbal_level')

        # Deleting field 'Tutor.cornerstone_verbal_ap'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_verbal_ap')

        # Deleting field 'Tutor.cornerstone_verbal_score'
        db.delete_column(u'tutorboard_tutor', 'cornerstone_verbal_score')

        # Deleting field 'Tutor.math_lower_level'
        db.delete_column(u'tutorboard_tutor', 'math_lower_level')

        # Deleting field 'Tutor.math_lower_ap'
        db.delete_column(u'tutorboard_tutor', 'math_lower_ap')

        # Deleting field 'Tutor.math_lower_score'
        db.delete_column(u'tutorboard_tutor', 'math_lower_score')

        # Deleting field 'Tutor.math_upper_level'
        db.delete_column(u'tutorboard_tutor', 'math_upper_level')

        # Deleting field 'Tutor.math_upper_ap'
        db.delete_column(u'tutorboard_tutor', 'math_upper_ap')

        # Deleting field 'Tutor.math_upper_score'
        db.delete_column(u'tutorboard_tutor', 'math_upper_score')

        # Deleting field 'Tutor.biology_level'
        db.delete_column(u'tutorboard_tutor', 'biology_level')

        # Deleting field 'Tutor.biology_ap'
        db.delete_column(u'tutorboard_tutor', 'biology_ap')

        # Deleting field 'Tutor.biology_score'
        db.delete_column(u'tutorboard_tutor', 'biology_score')

        # Deleting field 'Tutor.chemistry_level'
        db.delete_column(u'tutorboard_tutor', 'chemistry_level')

        # Deleting field 'Tutor.chemistry_ap'
        db.delete_column(u'tutorboard_tutor', 'chemistry_ap')

        # Deleting field 'Tutor.chemistry_score'
        db.delete_column(u'tutorboard_tutor', 'chemistry_score')

        # Deleting field 'Tutor.physics_level'
        db.delete_column(u'tutorboard_tutor', 'physics_level')

        # Deleting field 'Tutor.physics_ap'
        db.delete_column(u'tutorboard_tutor', 'physics_ap')

        # Deleting field 'Tutor.physics_score'
        db.delete_column(u'tutorboard_tutor', 'physics_score')

        # Deleting field 'Tutor.english_level'
        db.delete_column(u'tutorboard_tutor', 'english_level')

        # Deleting field 'Tutor.english_ap'
        db.delete_column(u'tutorboard_tutor', 'english_ap')

        # Deleting field 'Tutor.english_score'
        db.delete_column(u'tutorboard_tutor', 'english_score')

        # Deleting field 'Tutor.english_grammer_level'
        db.delete_column(u'tutorboard_tutor', 'english_grammer_level')

        # Deleting field 'Tutor.english_grammer_ap'
        db.delete_column(u'tutorboard_tutor', 'english_grammer_ap')

        # Deleting field 'Tutor.english_grammer_score'
        db.delete_column(u'tutorboard_tutor', 'english_grammer_score')

        # Deleting field 'Tutor.history_us_level'
        db.delete_column(u'tutorboard_tutor', 'history_us_level')

        # Deleting field 'Tutor.history_us_ap'
        db.delete_column(u'tutorboard_tutor', 'history_us_ap')

        # Deleting field 'Tutor.history_us_score'
        db.delete_column(u'tutorboard_tutor', 'history_us_score')

        # Deleting field 'Tutor.history_world_level'
        db.delete_column(u'tutorboard_tutor', 'history_world_level')

        # Deleting field 'Tutor.history_world_ap'
        db.delete_column(u'tutorboard_tutor', 'history_world_ap')

        # Deleting field 'Tutor.history_world_score'
        db.delete_column(u'tutorboard_tutor', 'history_world_score')

        # Deleting field 'Tutor.spanish_level'
        db.delete_column(u'tutorboard_tutor', 'spanish_level')

        # Deleting field 'Tutor.spanish_ap'
        db.delete_column(u'tutorboard_tutor', 'spanish_ap')

        # Deleting field 'Tutor.spanish_score'
        db.delete_column(u'tutorboard_tutor', 'spanish_score')

        # Deleting field 'Tutor.french_level'
        db.delete_column(u'tutorboard_tutor', 'french_level')

        # Deleting field 'Tutor.french_ap'
        db.delete_column(u'tutorboard_tutor', 'french_ap')

        # Deleting field 'Tutor.french_score'
        db.delete_column(u'tutorboard_tutor', 'french_score')

        # Deleting field 'Tutor.latin_level'
        db.delete_column(u'tutorboard_tutor', 'latin_level')

        # Deleting field 'Tutor.latin_ap'
        db.delete_column(u'tutorboard_tutor', 'latin_ap')

        # Deleting field 'Tutor.latin_score'
        db.delete_column(u'tutorboard_tutor', 'latin_score')

        # Deleting field 'Tutor.echelon_math_level'
        db.delete_column(u'tutorboard_tutor', 'echelon_math_level')

        # Deleting field 'Tutor.echelon_math_ap'
        db.delete_column(u'tutorboard_tutor', 'echelon_math_ap')

        # Deleting field 'Tutor.echelon_math_score'
        db.delete_column(u'tutorboard_tutor', 'echelon_math_score')

        # Deleting field 'Tutor.sat_math_level1_level'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level1_level')

        # Deleting field 'Tutor.sat_math_level1_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level1_ap')

        # Deleting field 'Tutor.sat_math_level1_score'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level1_score')

        # Deleting field 'Tutor.sat_math_level2_level'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level2_level')

        # Deleting field 'Tutor.sat_math_level2_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level2_ap')

        # Deleting field 'Tutor.sat_math_level2_score'
        db.delete_column(u'tutorboard_tutor', 'sat_math_level2_score')

        # Deleting field 'Tutor.echelon_verbal_level'
        db.delete_column(u'tutorboard_tutor', 'echelon_verbal_level')

        # Deleting field 'Tutor.echelon_verbal_ap'
        db.delete_column(u'tutorboard_tutor', 'echelon_verbal_ap')

        # Deleting field 'Tutor.echelon_verbal_score'
        db.delete_column(u'tutorboard_tutor', 'echelon_verbal_score')

        # Deleting field 'Tutor.sat_lit_level'
        db.delete_column(u'tutorboard_tutor', 'sat_lit_level')

        # Deleting field 'Tutor.sat_lit_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_lit_ap')

        # Deleting field 'Tutor.sat_lit_score'
        db.delete_column(u'tutorboard_tutor', 'sat_lit_score')

        # Deleting field 'Tutor.sat_bio_level'
        db.delete_column(u'tutorboard_tutor', 'sat_bio_level')

        # Deleting field 'Tutor.sat_bio_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_bio_ap')

        # Deleting field 'Tutor.sat_bio_score'
        db.delete_column(u'tutorboard_tutor', 'sat_bio_score')

        # Deleting field 'Tutor.sat_chem_level'
        db.delete_column(u'tutorboard_tutor', 'sat_chem_level')

        # Deleting field 'Tutor.sat_chem_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_chem_ap')

        # Deleting field 'Tutor.sat_chem_score'
        db.delete_column(u'tutorboard_tutor', 'sat_chem_score')

        # Deleting field 'Tutor.sat_physics_level'
        db.delete_column(u'tutorboard_tutor', 'sat_physics_level')

        # Deleting field 'Tutor.sat_physics_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_physics_ap')

        # Deleting field 'Tutor.sat_physics_score'
        db.delete_column(u'tutorboard_tutor', 'sat_physics_score')

        # Deleting field 'Tutor.sat_us_hist_level'
        db.delete_column(u'tutorboard_tutor', 'sat_us_hist_level')

        # Deleting field 'Tutor.sat_us_hist_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_us_hist_ap')

        # Deleting field 'Tutor.sat_us_hist_score'
        db.delete_column(u'tutorboard_tutor', 'sat_us_hist_score')

        # Deleting field 'Tutor.sat_world_hist_level'
        db.delete_column(u'tutorboard_tutor', 'sat_world_hist_level')

        # Deleting field 'Tutor.sat_world_hist_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_world_hist_ap')

        # Deleting field 'Tutor.sat_world_hist_score'
        db.delete_column(u'tutorboard_tutor', 'sat_world_hist_score')

        # Deleting field 'Tutor.sat_spanish_level'
        db.delete_column(u'tutorboard_tutor', 'sat_spanish_level')

        # Deleting field 'Tutor.sat_spanish_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_spanish_ap')

        # Deleting field 'Tutor.sat_spanish_score'
        db.delete_column(u'tutorboard_tutor', 'sat_spanish_score')

        # Deleting field 'Tutor.sat_french_level'
        db.delete_column(u'tutorboard_tutor', 'sat_french_level')

        # Deleting field 'Tutor.sat_french_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_french_ap')

        # Deleting field 'Tutor.sat_french_score'
        db.delete_column(u'tutorboard_tutor', 'sat_french_score')

        # Deleting field 'Tutor.sat_latin_level'
        db.delete_column(u'tutorboard_tutor', 'sat_latin_level')

        # Deleting field 'Tutor.sat_latin_ap'
        db.delete_column(u'tutorboard_tutor', 'sat_latin_ap')

        # Deleting field 'Tutor.sat_latin_score'
        db.delete_column(u'tutorboard_tutor', 'sat_latin_score')

        # Adding M2M table for field subjects on 'Tutor'
        m2m_table_name = db.shorten_name(u'tutorboard_tutor_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutor', models.ForeignKey(orm[u'tutorboard.tutor'], null=False)),
            ('subject', models.ForeignKey(orm[u'tutorboard.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tutor_id', 'subject_id'])


    models = {
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
            'biology_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'biology_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'biology_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'chemistry_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chemistry_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'chemistry_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'cornerstone_math_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cornerstone_math_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'cornerstone_math_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cornerstone_verbal_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cornerstone_verbal_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'cornerstone_verbal_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'echelon_math_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'echelon_math_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'echelon_math_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'echelon_verbal_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'echelon_verbal_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'echelon_verbal_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'english_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'english_grammer_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'english_grammer_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'english_grammer_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'english_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'english_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'french_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'french_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'french_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'history_us_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'history_us_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'history_us_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'history_world_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'history_world_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'history_world_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latin_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latin_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'latin_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'math_lower_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'math_lower_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'math_lower_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'math_upper_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'math_upper_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'math_upper_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'physics_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physics_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'physics_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_bio_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_bio_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_bio_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_chem_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_chem_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_chem_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_french_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_french_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_french_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_latin_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_latin_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_latin_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_lit_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_lit_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_lit_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_math_level1_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_math_level1_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_math_level1_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_math_level2_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_math_level2_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_math_level2_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_physics_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_physics_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_physics_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_spanish_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_spanish_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_spanish_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_us_hist_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_us_hist_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_us_hist_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sat_world_hist_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_world_hist_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sat_world_hist_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'spanish_ap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spanish_level': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'spanish_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['tutorboard']
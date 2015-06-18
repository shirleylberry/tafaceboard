# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Migration(DataMigration):
    def forwards(self, orm):

        #old_subs = list(orm.Subject.objects.all())

        sub1, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SSAT Math')
        sub2, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='ISEE Math')
        sub3, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SHSAT Math')
        sub4, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Math')
        sub5, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='ACT Math & Science')
        sub6, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Level I Math')
        sub7, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Level II Math')
        sub8, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Algebra / Trigonometry')
        sub9, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Geometry')
        sub10, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Pre-calculus')
        sub11, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Calculus')
        sub12, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Calculus AB')
        sub13, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Calculus BC')
        sub14, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Statistics')
        sub16, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Biology')
        sub17, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Biology')
        sub19, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Chemistry')
        sub20, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Chemistry')
        sub22, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Physics')
        sub23, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Physics')
        sub25, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SSAT Verbal')
        sub26, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='ISEE Verbal')
        sub27, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SHSAT Verbal')
        sub28, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Verbal')
        sub29, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='ACT Verbal')
        sub33, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Writing & Grammar')
        sub34, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Reading Skills')
        sub36, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic US History')
        sub37, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic World History')
        sub38, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic European History')
        sub39, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Literature & Composition')
        sub40, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Language & Composition')
        sub41, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP US History')
        sub42, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP World History')
        sub43, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP European History')
        sub47, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic French')
        sub48, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP French')
        sub49, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Spanish')
        sub50, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Spanish')
        sub51, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Academic Latin')
        sub52, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='AP Latin')

        # Unused
        sub35, is_created = orm['tutorboard.Subject'].objects.get_or_create(
            name='St. Bernard’s & Buckley Grammar')  # unused
        sub15, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Economics')  # unused
        sub53, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Application Essays')
        sub57, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='TOEFL')

        # From Skills
        sub54, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='International')
        sub55, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Skype')
        sub56, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='Schoology')
        sub58, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='LD')

        # SAT subject tests
        sub44, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT French')
        sub45, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Spanish')
        sub46, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Latin')
        sub30, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Literature')
        sub31, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT US History')
        sub32, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT World History')
        sub24, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Physics')
        sub21, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Chemistry')
        sub18, is_created = orm['tutorboard.Subject'].objects.get_or_create(name='SAT Biology')

        new_subs = []

        new_subs.append(sub1)
        new_subs.append(sub2)
        new_subs.append(sub3)
        new_subs.append(sub4)
        new_subs.append(sub5)
        new_subs.append(sub6)
        new_subs.append(sub7)
        new_subs.append(sub8)
        new_subs.append(sub9)
        new_subs.append(sub10)
        new_subs.append(sub11)
        new_subs.append(sub12)
        new_subs.append(sub13)
        new_subs.append(sub14)
        new_subs.append(sub16)
        new_subs.append(sub17)
        new_subs.append(sub19)
        new_subs.append(sub20)
        new_subs.append(sub22)
        new_subs.append(sub23)
        new_subs.append(sub25)
        new_subs.append(sub26)
        new_subs.append(sub27)
        new_subs.append(sub28)
        new_subs.append(sub29)
        new_subs.append(sub33)
        new_subs.append(sub34)
        new_subs.append(sub36)
        new_subs.append(sub37)
        new_subs.append(sub38)
        new_subs.append(sub39)
        new_subs.append(sub40)
        new_subs.append(sub41)
        new_subs.append(sub42)
        new_subs.append(sub43)
        new_subs.append(sub47)
        new_subs.append(sub48)
        new_subs.append(sub49)
        new_subs.append(sub50)
        new_subs.append(sub51)
        new_subs.append(sub52)

        # Unused
        new_subs.append(sub35)
        new_subs.append(sub15)

        # From Skills
        new_subs.append(sub53)
        new_subs.append(sub54)
        new_subs.append(sub55)
        new_subs.append(sub56)
        new_subs.append(sub57)
        new_subs.append(sub58)

        # SAT new_subs.append(subject tests
        new_subs.append(sub44)
        new_subs.append(sub45)
        new_subs.append(sub46)
        new_subs.append(sub30)
        new_subs.append(sub31)
        new_subs.append(sub32)
        new_subs.append(sub24)
        new_subs.append(sub21)
        new_subs.append(sub18)

        for s in new_subs:
            s.save()

        tutors = orm.Tutor.objects.all()

        for tutor in tutors:

            energy_text = ''
            energy = tutor.energy.all()
            for e in energy:
                if energy_text:
                    energy_text += ', '
                energy_text += e.energy

            presence_text = ''
            presence = tutor.presence.all()
            for p in presence:
                if presence_text:
                    presence_text += ', '
                presence_text += p.presence

            archetype_text = ''
            archetype = tutor.archetype.all()
            for a in archetype:
                if archetype_text:
                    archetype_text += ', '
                archetype_text += a.archetype

            location_text = ''
            location = tutor.location.all()
            for l in location:
                if location_text:
                    location_text += ', '
                location_text += l.name

            styles_text = ''
            styles = tutor.styles.all()
            for s in styles:
                if styles_text:
                    styles_text += ', '
                styles_text += s.style

            level_preferences_text = ''
            level_preferences = tutor.levelPreferences.all()
            for l in level_preferences:
                if level_preferences_text:
                    level_preferences_text += ', '
                level_preferences_text += l.levelPref

            student_engagements_text = ''
            student_engagements = tutor.studentEngagements.all()
            for s in student_engagements:
                if student_engagements_text:
                    student_engagements_text += ', '
                student_engagements_text += s.studentName

            skills_text = ''
            skills = tutor.skills.all()
            for s in skills:
                if skills_text:
                    skills_text += ', '
                skills_text += s.skill

            notes_text = '\n###\n{"notes":{'

            notes_text += '"energy":"' + energy_text + '",'
            notes_text += '"skill":"' + skills_text + '",'
            notes_text += '"presence":"' + presence_text + '",'
            notes_text += '"archetype":"' + archetype_text + '",'
            notes_text += '"location":"' + location_text + '",'
            notes_text += '"style":"' + styles_text + '",'
            notes_text += '"levelPreference":"' + level_preferences_text + '",'
            notes_text += '"studentEngagement":"' + student_engagements_text + '"'

            notes_text += '}}'

            tutor.availability_note += notes_text

            # Save skills as subjects
            # sub54 = orm.Subject.objects.create(name='International')
            # sub55 = orm.Subject.objects.create(name='Skype')
            # sub56 = orm.Subject.objects.create(name='Schoology')
            # sub58 = orm.Subject.objects.create(name='LD')
            for skill in tutor.skills.all():
                skill_cap_subject = None
                if skill.skill == 'Skype':
                    skill_cap_subject = sub55
                elif skill.skill == 'International':
                    skill_cap_subject = sub54
                elif skill.skill == 'LD':
                    skill_cap_subject = sub58
                elif skill.skill == 'Schoology':
                    skill_cap_subject = sub56
                if skill_cap_subject is not None:
                    skill_cap = orm.Capability.objects.create(subject=skill_cap_subject, tutor=tutor)
                    skill_cap.save()

            # Map subjects

            caps = tutor.capability_set.all()
            for cap in caps:

                if 'subject' in cap.notes.lower():
                    sub_test = True
                else:
                    sub_test = False

                sub = None
                try:
                    sub = cap.subject
                except ObjectDoesNotExist:
                    print('Subject does not exist for cap: ' + str(cap.pk))
                    break

                new_subs_for_tutor = []

                # what sub is it?
                if sub.name == 'Cornerstone Math':
                    new_subs_for_tutor.append(sub1)
                    new_subs_for_tutor.append(sub2)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub3)

                elif sub.name == 'Cornerstone Verbal':
                    new_subs_for_tutor.append(sub25)
                    new_subs_for_tutor.append(sub26)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub27)

                elif sub.name == 'Academic Math Lower':
                    new_subs_for_tutor.append(sub8)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub9)

                elif sub.name == 'Academic Math Upper':
                    new_subs_for_tutor.append(sub10)
                    new_subs_for_tutor.append(sub11)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub12)
                    if cap.modifier2:
                        new_subs_for_tutor.append(sub13)

                elif sub.name == 'Academic Biology':
                    new_subs_for_tutor.append(sub16)
                    if cap.ap:
                        new_subs_for_tutor.append(sub17)
                    if sub_test:
                        new_subs_for_tutor.append(sub18)

                elif sub.name == 'Academic Chemistry':
                    new_subs_for_tutor.append(sub19)
                    if cap.ap:
                        new_subs_for_tutor.append(sub20)
                    if sub_test:
                        new_subs_for_tutor.append(sub21)

                elif sub.name == 'Academic Physics':
                    new_subs_for_tutor.append(sub22)
                    if cap.ap:
                        new_subs_for_tutor.append(sub23)
                    if sub_test:
                        new_subs_for_tutor.append(sub24)

                elif sub.name == 'Academic English':
                    new_subs_for_tutor.append(sub34)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub33)
                    if cap.ap:
                        new_subs_for_tutor.append(sub39)
                        new_subs_for_tutor.append(sub40)

                elif sub.name == 'Academic History US':
                    new_subs_for_tutor.append(sub36)
                    if cap.ap:
                        new_subs_for_tutor.append(sub41)
                    if sub_test:
                        new_subs_for_tutor.append(sub31)

                elif sub.name == 'Academic History Euro/World':
                    new_subs_for_tutor.append(sub37)
                    new_subs_for_tutor.append(sub38)
                    if cap.ap:
                        new_subs_for_tutor.append(sub42)
                        new_subs_for_tutor.append(sub43)
                    if sub_test:
                        new_subs_for_tutor.append(sub32)

                elif sub.name == 'Academic Spanish':
                    new_subs_for_tutor.append(sub49)
                    if cap.ap:
                        new_subs_for_tutor.append(sub50)
                    if sub_test:
                        new_subs_for_tutor.append(sub45)

                elif sub.name == 'Academic French':
                    new_subs_for_tutor.append(sub47)
                    if cap.ap:
                        new_subs_for_tutor.append(sub48)
                    if sub_test:
                        new_subs_for_tutor.append(sub44)

                elif sub.name == 'Academic Latin':
                    new_subs_for_tutor.append(sub51)
                    if cap.ap:
                        new_subs_for_tutor.append(sub52)
                    if sub_test:
                        new_subs_for_tutor.append(sub46)

                elif sub.name == 'Echelon Math':
                    new_subs_for_tutor.append(sub4)
                    new_subs_for_tutor.append(sub5)
                    if cap.modifier1:
                        new_subs_for_tutor.append(sub6)
                    if cap.modifier2:
                        new_subs_for_tutor.append(sub7)

                elif sub.name == 'Echelon Verbal':
                    new_subs_for_tutor.append(sub28)
                    new_subs_for_tutor.append(sub29)
                    if cap.modifier1 or sub_test:
                        new_subs_for_tutor.append(sub30)

                elif sub.name == 'Statistics':
                    new_subs_for_tutor.append(sub14)

                for sub in new_subs_for_tutor:
                    new_cap = cap  # copy the capability object
                    new_cap.pk = None  # this make a new pk on save
                    new_cap.tutor = tutor
                    new_cap.subject = sub
                    new_cap.save()

                    # end of capability, subject loop

                    # end of tutor loop

                    # delete all old subjects and capabilities
                    # for sub in old_subs:
                    #     caps = sub.capability_set.all()
                    #     for cap in caps:
                    #         cap.delete()
                    #     sub.delete()

    # end of forwards





    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'tutorboard.archetype': {
            'Meta': {'object_name': 'Archetype'},
            'archetype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tutorboard.levelpreference': {
            'Meta': {'object_name': 'LevelPreference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'levelPref': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.presence': {
            'Meta': {'object_name': 'Presence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tutorboard.subject': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageAP': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod1': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod2': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod3': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imageMod4': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'archetype': ('django.db.models.fields.related.ManyToManyField', [],
                          {'symmetrical': 'False', 'to': u"orm['tutorboard.Archetype']", 'null': 'True',
                           'blank': 'True'}),
            'area': (
            'django.db.models.fields.CharField', [], {'default': "'verbal'", 'max_length': '255', 'blank': 'True'}),
            'availability': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'availability_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'availability_updated': (
            'django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'availability_vacation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bioline1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bioline5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'energy': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': u"orm['tutorboard.Energy']", 'null': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gotofor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'highestLevel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'highestLevelManual': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levelPreferences': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'to': u"orm['tutorboard.LevelPreference']", 'null': 'True',
                                  'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': u"orm['tutorboard.Location']", 'null': 'True',
                          'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'picture': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presence': ('django.db.models.fields.related.ManyToManyField', [],
                         {'symmetrical': 'False', 'to': u"orm['tutorboard.Presence']", 'null': 'True',
                          'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '255', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': u"orm['tutorboard.Skill']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'studentEngagements': ('django.db.models.fields.related.ManyToManyField', [],
                                   {'symmetrical': 'False', 'to': u"orm['tutorboard.StudentEngagement']",
                                    'null': 'True', 'blank': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'to': u"orm['tutorboard.Style']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['tutorboard']
    symmetrical = True

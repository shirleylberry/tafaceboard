import sys, os
# 
# Python has no prepend function, so we must do an insert. We insert the key directories
# BEFORE ANYTHING, so the python installation sees them before the system-wide libraries.

virtualenv_root = '/home/takristin/shandy.tutorassociates.com/tutorboard'

INTERP = os.path.join(virtualenv_root, 'bin', 'python')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)


sys.path.insert(0,'/home/takristin/shandy.tutorassociates.com/tutorboard')
sys.path.insert(0,'/home/takristin/shandy.tutorassociates.com/tutorboard/bin')
sys.path.insert(0,'/home/takristin/shandy.tutorassociates.com/tutorboard/lib/python2.6/site-packages')
sys.path.insert(0,'/home/takristin/shandy.tutorassociates.com/tutorboard/lib/python2.6')
 
os.environ['DJANGO_SETTINGS_MODULE'] = "django_roster.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

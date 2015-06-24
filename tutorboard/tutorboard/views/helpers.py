from tutorboard.models import Capability

def findNextTutor(tutor_id, tutor_list):
    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list):  # we just want to find the index of the tutor
        # find the current tutor in the list, make sure its not the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index + 1 < len(tutor_list):
            return tutor_list[index + 1:index + 2][0]  # returns the tutor object
    return None

def findPrevTutor(tutor_id, tutor_list):
    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list):  # we just want to find the index of the tutor

        # find the current tutor in the list, make sure its no the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index + 1 > 1:
            return tutor_list[index - 1:index][0]
    return None

def getHighestLevel(tutor_id):
    all_caps = Capability.objects.all().filter(tutor__id=tutor_id)
    highestlevel = "Professional"
    for cap in all_caps:
        if cap.level == "director":
            return "Director"
        elif cap.level == "expert":
            highestlevel = "Expert"
    return highestlevel

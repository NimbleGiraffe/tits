from django.contrib.auth.models import User
from nips.models import *
import csv
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
reader = csv.reader(open("dayfour.csv"))
reader = csv.reader(open("dayfour.csv"), delimiter=",")
default = File(open("/home/wbstueck/huge_tits.jpg"))
for row in reader:
    nip = None
    for i in Nipple.objects.all():
        if i.first_name.lower() == row[0] and i.last_name.lower() == row[1]:
            nip = i
            break
    if nip != None:
        df = DayFour(nipple=nip)
        df.save()
    else:
        nip = Nipple(first_name=row[0], last_name=row[1], image=default, interests="", hometown="", high_school="")
        nip.save()
        df = DayFour(nipple=nip)
        df.save()

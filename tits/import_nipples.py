import csv
from nips.models import Nipple
from django.core.files import File


nipReader = csv.reader(open('freshmen_csv.csv', 'rb'), delimiter=',')

for i in nipReader:
    file_name = i[0]
    first = i[1]
    last = i[2]
    hometown = i[3]
    interests = i[4]
    high_school = i[5]
    file = File(open('/home/wbstueck/freshman/'+file_name))
    
    nipple = Nipple(first_name=first, last_name=last, interests=interests, hometown=hometown, high_school=high_school, image=file)
    
    nipple.save()
    print first+" "+last
    

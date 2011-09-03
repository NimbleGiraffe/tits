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
    
    if file_name[(len(file_name)-3):] != "jpg":
        file_name = file_name + ".jpg"
    file = File(open('/home/wbstueck/freshmen/'+file_name))
    
    nipple = Nipple(first_name=first, last_name=last, interests=interests, hometown=hometown, high_school=high_school, image=file)
    
    nipple.save()
    print first+" "+last
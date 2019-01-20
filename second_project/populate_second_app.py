import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')
import django
django.setup()
import random
from second_app.models import AccessRecord,Topic,Webpage
from faker import Faker
fakegen = Faker()
topics = ['social','search','eshopping','news','games']

def addTopic():
    top = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    top.save()
    return top

def populate(n=5):
    for i in range(n):
        top = addTopic()
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        arecord = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        webpg.save()
        arecord.save()

if __name__ == "__main__":
    print("populating script")
    populate(20)
    print("populating done")

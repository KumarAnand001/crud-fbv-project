import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbvProject.settings')
import django
django.setup()

from testApp.models import Employee
from faker import Faker
from random import randint

fake = Faker()

def populate(n):
    
    for i in range(n):
        feno = randint(1001, 9999)
        fename = fake.name()
        fesal = randint(10000, 20000)
        feadd = fake.city()
        emp_record = Employee.objects.get_or_create(eno = feno, ename = fename, esal = fesal, eadd = feadd)

# Call the populate function with the desired number of entries
populate(20)



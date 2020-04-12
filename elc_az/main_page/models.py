from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.core.validators import RegexValidator
from phone_field import PhoneField
from django.core.exceptions import ValidationError
import re
from django.core import validators
from django import forms
# COURSE_CHOICES = (
#     ('EN', 'English Level 1'),
#     ('RU', 'Rus dili 1'),
#     ('FR', 'Fransız Dili'),
# )

def check_name(value):
  if len(value) < 3:
    raise forms.ValidationError("Ad minimum 3 simvol olmalıdır")

# Below function not Working yet
def validate_hash(value):
    reg = re.compile('^[0-9]{7,7}$')
    if not reg.match(value) :
        raise ValidationError(u'%s must be 7 ' % value)

# Create your models here.
class course(models.Model):
    """docstring for course Model"""

    c_id = models.CharField("Course_ID", max_length=4, primary_key=True)
    c_name = models.CharField("course_name", max_length=20)
    c_description = models.TextField()
    c_photo_uri = models.CharField("course_photo_url", max_length=200)

    def __str__(self):
        return self.c_name

class user(models.Model):
    """docstring for User model"""

    # Creating a tuble of Courses with PK (first three letters of a Course) from DB
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    course_l = []
    course_list = course.objects.all()
    count = course_list.count()
    print("Count of Courses",count)

    for i in range(count):
        print("NAME of {}. course: ".format(i),course_list[i].c_name[:3])
        print("TYPE of {}. course: ".format(i),type(course_list[i]),type(course_list[i].c_name))
        print("PK of {}. course: ".format(i),course_list[i].pk)

        course_l.append((course_list[i].c_id,course_list[i].c_name))

    print(tuple(course_l))
    COURSE_CHOICES = tuple(course_l)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    PHONE_PREFIXES = (
        ('Aze1','050'),
        ('Aze2','051'),
        ('Bak1','055'),
        ('Bak2','099'),
        ('Nar1','070'),
        ('Nar2','077')
    )

    u_shx_pin = models.CharField("User's ID card pin",max_length=7, primary_key=True)
    name = models.CharField("User's name", max_length=20,validators=[check_name,])
    u_sname = models.CharField("User's surname", max_length=20)

    # u_phonenumber = models.CharField("user_mobile_phone_number", max_length=7,validators=[validate_hash])
    phone_regex = RegexValidator(regex=r'^\d{7}$', message="Mobil nömrə 7 rəqəmli olmalıdır. Məs: 1234567")
    u_phonenumber = models.CharField(validators=[phone_regex], max_length=7, blank=True)

    u_phoneprefix = models.CharField("Phone prefix ",max_length=5,choices=PHONE_PREFIXES,default='Nar1')
    # u_phonenumber = PhoneField(blank=True, help_text='Contact phone number',max_length=13)
    u_birthdate = models.DateField("User's birthdate", auto_now=False)
    u_regis_date = models.DateTimeField("User's registration date", default=timezone.now)
    u_course = models.CharField("User's course(s)", max_length=20,choices=COURSE_CHOICES,default='Rus')

    def __str__(self):
        full_name = self.name + " " + self.u_sname
        return full_name

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     if name:
    #         if len(data) < 3:
    #             raise ValidationError("Ad minimum 3 simvol olmalıdır")

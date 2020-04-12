from django import forms
from .models import user
from .models import course
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re
import datetime


this_year = datetime.date.today().year
YEARS = [x for x in range(1940, this_year+1)] #automaticaly takes from 1940 to current year

# Validator for phonenumber
phone_validator = RegexValidator(r"^[0-9]{7,7}$", message="Mobil nömrə 7 rəqəmdən ibarət olmalıdır")


def check_name(value):
    if len(value) < 3:
        raise forms.ValidationError("Ad minimum 3 hərfdən ibarət ola bilər")
    if not value.isalpha():
        raise forms.ValidationError("Ad ancaq böyük və kiçik hərflərdən ibarət ola bilər")

def check_surname(value):
    if len(value) < 3:
        raise forms.ValidationError("Soyad minimum 3 hərfdən ibarət ola bilər")
    if not value.isalpha():
        raise forms.ValidationError("Soyad ancaq böyük və kiçik hərflərdən ibarət ola bilər")

def check_fincode(value):
    pattern = re.compile("[A-Za-z0-9]+")
    if not pattern.fullmatch(value):
        raise forms.ValidationError("FİN kod ancaq hərf və rəqəmdən ibarət ola bilər")
    elif len(value) < 5 or len(value) == 6 or len(value) > 7:
        raise forms.ValidationError("FİN kodun uzunluğu 5 və ya 7 simvol ola bilər")

class RegisterForm(forms.ModelForm):
    """docstring - registeration from for users - new coning students"""
    error_css_class = 'error'
    required_css_class = 'required'

    u_shx_pin = forms.CharField(required=True, max_length=7, validators=[check_fincode,],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-lg col-md-5',
                'placeholder': 'Şəxsiyyət Vəsiqəsinin FİN kodu'
            }
            )
            )

    name = forms.CharField(required=True,validators=[check_name,],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-lg col-md-5',
                'placeholder': 'Adınız',
            }
            )
            )

    u_sname = forms.CharField(required=True, validators=[check_surname,],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-lg col-md-5',
                'placeholder': 'Soyadınız'
            }
            )
            )

    u_phoneprefix = forms.ChoiceField(choices=user.PHONE_PREFIXES, required=True,
        widget=forms.Select(attrs={'class':'form-control-lg col-md-1'})
            )

    u_phonenumber = forms.CharField(
        label="Test field",
        required=True,  # Note: validators are not run against empty fields
        validators=[phone_validator],
        max_length=7,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-lg col-md-4',
                'placeholder': 'Mobil nömrə (e.g 1234567) '
            }
        )
    )
    u_birthdate = forms.DateField(required=True,
        widget=forms.SelectDateWidget(years=YEARS, attrs={
                                              'class': 'form-control-lg col-md-1.5',
                                              }
                  )
                  )

    u_course = forms.ChoiceField(choices=user.COURSE_CHOICES, required=True,
                                    # , widget=forms.Select(choices=COURSE_CHOICES)
                                      widget=forms.Select(attrs={
                                                                  'class': 'form-control-lg col-md-5',
                                                                'placeholder': 'Kurs seçimi'
                                                                })
                                      )

    class Meta(object):
        """docstring for Meta"""
        model = user
        fields = ['u_shx_pin', 'name', 'u_sname','u_phoneprefix', 'u_phonenumber', 'u_birthdate', 'u_course']

from django import forms
from django.forms.widgets import NumberInput
import datetime
from first_app.models import PracticeModelForm

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

# class practiceForm(forms.Form):
#     # name = forms.CharField()
#     # comment = forms.CharField(widget=forms.Textarea(attrs={'row': 3}))
#     # email = forms.EmailField()
#     # agree = forms.BooleanField()
#     # Date = forms.DateField()
#     # birth_date = forms.DateField(widget=NumberInput(attrs = {'type': 'date'}))
#     # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     # email_address = forms.EmailField(label='Please Enter Your Email Address', max_length=30)
#     # first_name = forms.CharField(initial='Enter Your Name')
#     # day = forms.DateField(initial=datetime.date.today)
#     # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
#     # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
#     # favorite_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
#     # favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)


class PracticeModel(forms.ModelForm):
    class Meta:
        model = PracticeModelForm
        fields = '__all__'
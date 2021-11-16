from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from ..models.models import T_user
from bootstrap3_datetime.widgets import DateTimePicker
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
ACTIF = (
    ('', 'Selectionner...'),
    ('1', 'Actif'),
    ('2', 'Desactive'),
)

class Tuserform(forms.ModelForm):
    ftpUsername = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    ftpPAssword = forms.CharField(widget=forms.PasswordInput())
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Entrez le nom'})
    )
    societe = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nom Societe'})
    )
    contact_internne = forms.CharField(
        label='Contact Interne',
        widget=forms.TextInput(attrs={'placeholder': 'Le contact interne'})
    )
    actif = forms.ChoiceField(choices=ACTIF)
    telephone = forms.CharField(label='Telephone')
    dateExpiration = forms.DateTimeField(widget=DateTimePickerInput(options={
                    "format": "MM/DD/YYYY",  # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,


                }
    )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('ftpUsername', css_class='form-group col-md-2 mb-0'),
                Column('ftpPassword', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('nom', css_class='form-group col-md-4 mb-0'),
                Column('societe', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('telephone', css_class='form-group col-md-4 mb-0'),
                Column('ftpHomeDir', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('actif', css_class='form-group col-md-4 mb-0'),
                Column('dateExpiration', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Enregistrer')
        )

    class Meta:
        model = T_user
        fields = (
            'ftpUsername', 'ftpPassword', 'actif', 'ftpHomeDir', 'nom', 'societe', 'telephone', 'contact_interne',
            'dateExpiration')
        # fields = '__all__'
        widgets = {
            'dateExpiration': DateTimePickerInput(format='%m/%d/%Y'),
        }


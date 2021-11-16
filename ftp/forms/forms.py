from ..models.models import T_user
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.bootstrap import StrictButton

ACTIF = (
        ('', 'Selectionner...'),
        ('1', 'Actif'),
        ('0', 'Desactive'),
    )
class TuserForms(forms.ModelForm):
    ftpUsername = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'utilisateur'}))
    ftpPassword = forms.CharField(widget=forms.PasswordInput())
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Entrez le nom'})
    )
    societe = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nom Societe'})
    )
    contact_interne = forms.CharField(
        label='Contact Interne',
        widget=forms.TextInput(attrs={'placeholder': 'Le contact interne'})
    )
    actif = forms.ChoiceField(choices=ACTIF)
    telephone = forms.CharField(label='Telephone')
    dateExpiration = forms.DateTimeField(widget=DatePickerInput(options={
                    "format": "YYYY-MM-DD",  # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,


                }
    )
    )

    def __init__(self, *args, **kwargs):
        super(TuserForms, self).__init__(*args, **kwargs)


        self.fields['ftpUsername'].label = "nom utilisateur"
        self.fields['ftpPassword'].label = "mot de passe"
        self.fields['nom'].label = "nom client"
        self.fields['societe'].label = "Compagny name"
        self.fields['telephone'].label = "telephone"
        self.fields['contact_interne'].label = "contact interne"
        self.fields['actif'].label = "actif/inactif"
        self.fields['ftpHomeDir'].label = "repertoire ftp"
        self.fields['dateExpiration'].label = "%s (AAAA-MM-JJ)" % "Jour Expiration"


        # customiser ton formulaire
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper._form_action = ''
        # id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        # Taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-8'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(

            Row(
                Column('ftpUsername', css_class='form-group col-md-6 mb-0'),
                Column('ftpPassword', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('nom', css_class='form-group col-md-4 mb-0'),
                Column('societe', css_class='form-group col-md-4 mb-0'),
                Column('contact_interne',css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('telephone', css_class='form-group col-md-4 mb-0'),
                Column('ftpHomeDir', css_class='form-group col-md-8 mb-0'),
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
        fields = ('ftpUsername', 'ftpPassword', 'actif', 'ftpHomeDir', 'nom', 'societe', 'telephone', 'contact_interne', 'dateExpiration')

        # fields = '__all__'
        widgets = {
            #'dateExpiration': DatePickerInput(format='%Y/%m/%d HH:mm'),
            'dateExpiration': DatePickerInput(),

        }

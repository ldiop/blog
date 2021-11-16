from django.db import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder

class EmailForm(forms.Form):
    TRUE_FALSE_CHOICES = (
        (True, 'Oui'),
        (False, 'Non')
    )
    ACTIF = (
        ('', 'Selectionner...'),
        (True, 'Actif'),
        (False, 'Desactive'),
    )
    cn = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    sn = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Prenom'}))
    mail = forms.EmailField(label="Email", max_length=100)
    userPassword = forms.CharField(widget=forms.PasswordInput())
    telephoneNumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$',error_messages={'required': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."}, label="Telephone")
    vacationInfo = forms.CharField(label="Reponse Automatique", widget=forms.Textarea(attrs={'placeholder': 'Tapez ici votre reponse automatique'}))
    vacationActive = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Activer Réponse Auto",
                                  initial='', widget=forms.Select(), required=True)
    #vacationActive = forms.BooleanField(initial=True)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        self.fields['cn'].label = "Nom"
        self.fields['sn'].label = "Prenom"
        self.fields['mail'].label = "Adresse mail"
        self.fields['telephoneNumber'].label = "Numero Telephone"
        self.fields['userPassword'].label = "Mot de passe"
        self.fields['vacationInfo'].label = "Reponse Auto"
        self.fields['vacationActive'].label = "Activer Reponse Auto"

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
                Column('cn', css_class='form-group col-md-6 mb-0'),
                Column('sn', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mail', css_class='form-group col-md-4 mb-0'),
                Column('telephoneNumber', css_class='form-group col-md-4 mb-0'),
                Column('userPassword', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('vacationInfo', css_class='form-group col-md-6 mb-0'),
                Column('vacationActive', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Enregistrer')

        )




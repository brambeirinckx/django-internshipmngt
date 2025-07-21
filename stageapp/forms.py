from django import forms
from django.forms.widgets import SelectDateWidget, CheckboxInput, DateTimeInput, SplitDateTimeWidget
from django.forms.models import inlineformset_factory
from django.conf import settings

from .models import StageOpdrachten, Opleidingen, Scholen, BedrijvenGroep,  StageOpdrachtEvaluaties, StageOpdrachtEvaluatieDetails, Bedrijfsvestingen, Afdelingen, Contactpersonen, StageOpdrachtCalevents, Taken, ScholenGroep, Schooljaren, Klassen, Studenten, Leerkrachten

#Test with crispy forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Row, Column, Field, HTML

class Row(Div):
    css_class = 'row'

class Column(Div):
    css_class = 'column'


class ScholenGroepForm(forms.ModelForm):
    class Meta:
        model = ScholenGroep
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

        widgets = {
            'website': forms.TextInput,
        }
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ScholenGroepForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('scholen_groep_naam', wrapper_class='form-group col-md-4 mb-0'),
            Div(
                Row(
                    Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                    Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div(
                Row(
                    Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                    Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div(
                Row(
                    Field('email', wrapper_class='form-group col-md-6 mb-0'),
                    Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Row(
                Field('website', wrapper_class='form-group col-md-4 mb-0'),
            ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'

class SchooljaarForm(forms.ModelForm):
    class Meta:
        model = Schooljaren
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

    def __init__(self, *args, **kwargs):
        super(SchooljaarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('schooljaar', wrapper_class='form-group col-md-4 mb-0'),
               Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'


class KlasForm(forms.ModelForm):
    class Meta:
        model = Klassen
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

    def __init__(self, *args, **kwargs):
        super(KlasForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                    Field('klas', wrapper_class='form-group col-md-6 mb-0'),
                    Field('opleidingen', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Field('klas_omschrijving', wrapper_class='form-group col-md-12 mb-0'),
            Div(
                Row(
                    Field('schooljaren', wrapper_class='form-group col-md-4 mb-0'),
                    Field('opleidingsjaar', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
               Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'

class ScholenForm(forms.ModelForm):
    class Meta:
        model = Scholen
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

        widgets = {
            'website': forms.TextInput,
        }
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(ScholenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                        Field('school_naam', wrapper_class='form-group col-md-6 mb-0'),
                    Field('scholengroep', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div(
                Row(
                    Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                    Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div(
                Row(
                    Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                    Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div(
                Row(
                    Field('email', wrapper_class='form-group col-md-6 mb-0'),
                    Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Row(
                Field('website', wrapper_class='form-group col-md-4 mb-0'),
            ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Studenten
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

        widgets = {
            'actief': forms.CheckboxInput(),
            'ingeschreven_sinds': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }),
        }
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                    Row(
                        Field('voornaam', wrapper_class='form-group col-md-3 mb-0'),
                        Field('naam', wrapper_class='form-group col-md-4 mb-0'),
                        Field('scholen', wrapper_class='form-group col-md-2 mb-0'),
                        Field('klassen', wrapper_class='form-group col-md-3 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                        Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                        Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('email', wrapper_class='form-group col-md-5 mb-0'),
                        Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                        Field('rijksregisternr', wrapper_class='form-group col-md-3 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('actief', wrapper_class='form-group col-md-4 mb-0'),
                        Field('ingeschreven_sinds', wrapper_class='form-group col-md-4 mb-0'),
                    ),
                ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'

class LeerkrachtForm(forms.ModelForm):
    class Meta:
        model = Leerkrachten
        exclude = ['created_by', 'created_at', 'last_updated_by', 'last_updated_at', ]

        widgets = {
            'actief': forms.CheckboxInput(),
            'werkzaam_sinds': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }),
        }
        # fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(LeerkrachtForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                    Row(
                        Field('voornaam', wrapper_class='form-group col-md-3 mb-0'),
                        Field('naam', wrapper_class='form-group col-md-4 mb-0'),
                        Field('scholen', wrapper_class='form-group col-md-2 mb-0'),
                        Field('klassen', wrapper_class='form-group col-md-3 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                        Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                        Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('email', wrapper_class='form-group col-md-5 mb-0'),
                        Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                        Field('rijksregisternr', wrapper_class='form-group col-md-3 mb-0'),
                    ),
                ),
                Div(
                    Row(
                        Field('actief', wrapper_class='form-group col-md-4 mb-0'),
                        Field('werkzaam_sinds', wrapper_class='form-group col-md-4 mb-0'),
                    ),
                ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method = 'post'
class StageOpdrachtenForm(forms.ModelForm):
    """ Form built via FormHelper so that fields can be organised in multiple columns to make better use of screen space """
    class Meta:
        model = StageOpdrachten
        fields = ['stage_opdracht', 'stage_opportuniteit', 'bedrijfsvestingen', 'afdelingen', 'contactpersonen', 'leerkrachten','studenten','actief','stage_opdracht_van','stage_opdracht_tot','stage_omschrijving','afspraken','doelstellingen','verwachtte_attitudes','stage_opdracht_afgesloten', 'datum_stage_opdracht_afgesloten']
        widgets = {
            'stage_opdracht': forms.TextInput(
                attrs={'cols': 80, 'placeholder': 'Korte naam stageopdracht'}),
            'actief': forms.CheckboxInput(),
            'stage_opdracht_van': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }
            ),
            'stage_opdracht_tot': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # False = block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }
            ),
            'stage_omschrijving': forms.Textarea(attrs={'cols': 120, 'rows': 5, 'style': 'font-size: 12px' }),
            'afspraken': forms.Textarea(attrs={'cols': 38, 'rows': 5, 'style': 'font-size: 12px'}),
            'doelstellingen': forms.Textarea(attrs={'cols': 38, 'rows': 5, 'style': 'font-size: 12px'}),
            'verwachtte_attitudes': forms.Textarea(attrs={'cols': 38, 'rows': 5, 'style': 'font-size: 12px'}),
            'stage_opdracht_afgesloten': forms.CheckboxInput(),
            'datum_stage_opdracht_afgesloten': forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }
            ),
        }

        # labels = {StageOpdrachten' : ''}  #The '' specifies that no labels are generated

    def __init__(self, *args, **kwargs):
        super(StageOpdrachtenForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div (
                Row(
                Field('stage_opdracht', wrapper_class='form-group col-md-6 mb-0'),
                Field('stage_opportuniteit', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div (
                Row(
                Field('bedrijfsvestingen', wrapper_class='form-group col-md-4 mb-0'),
                   Field('afdelingen', wrapper_class='form-group col-md-4 mb-0'),
                    Field('contactpersonen', wrapper_class='form-group col-md-4 mb-0'),
                    ),
                ),
            Div (
                Row(
                    Field('leerkrachten', wrapper_class='form-group col-md-6 mb-0'),
                    Field('studenten', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),
            Div (
            Row(
                        Field('stage_omschrijving'),
                    ),
                    Row(
                        Field('stage_opdracht_van', wrapper_class='form-group col-md-6 mb-0'),
                        Field('stage_opdracht_tot', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                    Row(
                        Field('afspraken', wrapper_class='form-group col-md-4 mb-0'),
                        Field('doelstellingen', wrapper_class='form-group col-md-4 mb-0'),
                        Field('verwachtte_attitudes', wrapper_class='form-group col-md-4 mb-0'),
                    ),
                ),
            Field('actief', wrapper_class='form-group col-md-6 mb-0'),
            Div(
                Row(
                    Field('stage_opdracht_afgesloten', wrapper_class='form-group col-md-3 mb-0', display = 'flex'),
                    Field('datum_stage_opdracht_afgesloten', wrapper_class='form-group col-md-3 mb-0', disabled=True),
                    css_class='checkbox_inline',
                    ),
                ),
            Div(
            Submit('save', 'Save changes', style='max-width: 20em'),
                css_class='btn-right',
            ),
        )
        self.helper.form_method =  'post'


class OpleidingenForm(forms.ModelForm):
    """ Overzicht opleidingen Crispy Helper form """
    class Meta:
        model = Opleidingen
        fields = ['scholen', 'opleiding', 'graad']
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OpleidingenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
         Field('scholen', wrapper_class='form-group col-md-4 mb-0'),
                Field('opleiding', wrapper_class='form-group col-md-4 mb-0', placeholder = 'Korte omschrijving van de opleiding'),
                Field('graad', wrapper_class='form-group col-md-4 mb-0', placeholder ='Xste graad'),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
         )
        self.helper.form_method = 'post'



class AfdelingForm(forms.ModelForm):
    """ Overzicht afdeling Crispy Helper form """
    class Meta:
        model = Afdelingen
        fields = ['afdeling', 'afdeling_omschrijving']
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AfdelingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
         Field('afdeling', wrapper_class='form-group col-md-4 mb-0'),
                Field('afdeling_omschrijving', wrapper_class='form-group col-md-4 mb-0', placeholder = 'Korte omschrijving van de afdeling'),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
         )
        self.helper.form_method = 'post'

class VestingForm(forms.ModelForm):
    """ Overzicht Vesting Crispy Helper form """
    class Meta:
        model = Bedrijfsvestingen
        fields =  ['bedrijfsnaam', 'adres', 'nummer', 'postcode', 'plaats', 'email', 'tel','website']
        widgets = {
            'website': forms.TextInput,
        }
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VestingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
         Field('bedrijfsnaam', wrapper_class='form-group col-md-4 mb-0'),
            Div(
                Row(
                    Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                    Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                    Field('email', wrapper_class='form-group col-md-6 mb-0'),
                    Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Row(
                Field('website', wrapper_class='form-group col-md-4 mb-0'),
                ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
         )
        self.helper.form_method = 'post'

class ContactPersoonForm(forms.ModelForm):
    """ Overzicht Contactpersoon Crispy Helper form """
    class Meta:
        model = Contactpersonen
        fields =  ['voornaam', 'naam', 'adres', 'nummer', 'postcode', 'plaats', 'email', 'tel','actief']
        widgets = {
            'actief': forms.CheckboxInput,
        }
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactPersoonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
         Div(
                Row(
                    Field('voornaam', wrapper_class='form-group col-md-6 mb-0'),
                    Field('naam', wrapper_class='form-group col-md-6 mb-0'),
                ),
            ),

            Div(
                Row(
                    Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                    Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                    Field('email', wrapper_class='form-group col-md-6 mb-0'),
                    Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Row(
                Field('actief', wrapper_class='form-group col-md-4 mb-0'),
                ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
         )
        self.helper.form_method = 'post'

class BedrijvenGroepForm(forms.ModelForm):
    """ Overzicht Bedrijvengroepen Crispy Helper form """
    class Meta:
        model = BedrijvenGroep
        fields =  ['bedrijfsgroep_naam', 'adres', 'nummer', 'postcode', 'plaats', 'email', 'tel','website']
        widgets = {
            'website': forms.TextInput,
        }
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BedrijvenGroepForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
         Field('bedrijfsgroep_naam', wrapper_class='form-group col-md-4 mb-0'),
            Div(
                Row(
                    Field('adres', wrapper_class='form-group col-md-6 mb-0'),
                    Field('nummer', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                Field('postcode', wrapper_class='form-group col-md-6 mb-0'),
                Field('plaats', wrapper_class='form-group col-md-6 mb-0'),
                    ),
                ),
            Div(
                Row(
                    Field('email', wrapper_class='form-group col-md-6 mb-0'),
                    Field('tel', wrapper_class='form-group col-md-4 mb-0'),
                ),
            ),
            Row(
                Field('website', wrapper_class='form-group col-md-4 mb-0'),
                ),
            Div(
                Submit('save', 'Save', style='max-width: 20em'),
                css_class='btn-right',
            ),
         )
        self.helper.form_method = 'post'

class OpdrachtEvaluatieForm(forms.ModelForm):
    """Opdracht evaluatie formulier """
    class Meta:
        model = StageOpdrachtEvaluaties
        exclude = ['created_by', 'created_at' , 'last_updated_by', 'last_updated_at',]
        widgets = {
            'vrijgegeven': forms.CheckboxInput(),
            'ontvangst_studentverantwoordelijke': forms.CheckboxInput(),
            'notities_studentverantwoordelijke': forms.Textarea(attrs={'cols': 350, 'rows': 5, 'style': 'font-size: 10px'}),
        }

    def __init__(self, *args, **kwargs):
        super(OpdrachtEvaluatieForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                    Field('stageopdrachten', wrapper_class='form-group col-md-6 mb-0', display='flex', locked=True ),
                    Field('evaluatietemplates', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                ),
            ),
            Div(
                Row(
                    Field('vrijgegeven',wrapper_class='col-md-6 mb-0', display='inline'),
                    Field('ontvangst_studentverantwoordelijke',wrapper_class='col-md-6 mb-0', display='inline'),
                    css_class='col-md-6 mb-0',
                    ),
                css_class='form-check form-check-inline',
            ),
            Div(
                Row(

                    Field('datum_vrijgegeven', wrapper_class='form-group col-md-3 mb-0', disabled=True),
                    Field('datum_ontvangst_studentverantwoordelijke', wrapper_class='form-group col-md-3 mb-0', disabled=True),
                    css_class='checkbox_inline',
                ),
            ),
            Field('notities_studentverantwoordelijke', wrapper_class='form-group col-md-6 mb-0',
                          display='flex'),
            Field('datum_last_update_notities_studentverantwoordelijke', wrapper_class='form-group col-md-3 mb-0',
                          disabled=True),
            Div(
                Submit('save', 'Save changes', style='max-width: 20em'),
                css_class='btn-right',
            )
        )
        self.helper.form_method = 'post'

class OpdrachtEvaluatieDetailForm(forms.ModelForm):
    """Opdracht evaluatie detail formulier """
    class Meta:
        model = StageOpdrachtEvaluatieDetails
        exclude = ['created_by', 'created_at' , 'last_updated_by', 'last_updated_at',]
        widgets = {
            'score_nvt': forms.CheckboxInput(),
            'score_argumentatie': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'style': 'font-size: 10px'}),
            'score_opmerking': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'style': 'font-size: 10px'}),
            'datum_vrijgegeven': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                    'class': 'form-control',
                }),
            'datum_ontvangst_studentverantwoordelijke': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }),
            'datum_last_update_notities_studentverantwoordelijke': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(OpdrachtEvaluatieDetailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                        Field('stageopdrachtevaluaties', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                    Field('EvaluatieTemplateHoofddeel', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('EvaluatieTemplateSubdeel', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                ),
                Div(
                    Row(
                    Field('EvaluatieCriteria', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                        Field('EvaluatieScoreRange', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                    )
                ),
                Div(
                    Row(
                        Field('score', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('score_nvt', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('score_argumentatie', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                        Field('score_opmerking', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                    )
                ),
            ),
        Div(
                Submit('save', 'Save changes', style='max-width: 20em'),
                css_class='btn-right',
            )
        )
        self.helper.form_method = 'post'

""" Nog niet ok"""
class OpdrachtCalEventForm(forms.ModelForm):
    """Opdracht Cal Events  detail formulier """
    class Meta:
        model = StageOpdrachtCalevents
        exclude = ['created_by', 'created_at' , 'last_updated_by', 'last_updated_at',]
        widgets = {
            'omschrijving': forms.Textarea(attrs={'cols': 250, 'rows': 4, 'style': 'font-size: 10px', 'placeholder': 'Omschrijving van event (herrinering, taak, afspraak)'}),
            'afspraak_invitees': forms.TextInput(attrs={'placeholder': 'lijst van email adressen naarwaar de taak verstuurd moet worden', 'style': 'font-size: 10px'}),
            'taak_omschrijving': forms.Textarea(attrs={'cols': 250, 'rows': 4, 'style': 'font-size: 10px'}),
            'taak_zelfevaluatie': forms.Textarea(attrs={'cols': 250, 'rows': 4, 'style': 'font-size: 10px'}),
            'taak_feedback': forms.Textarea(attrs={'cols': 250, 'rows': 4, 'style': 'font-size: 10px'}),
            'estimate_effort_hrs': forms.TextInput(attrs={'placeholder': 'ingeschatte effort in uren','style': 'font-size: 10px'}),
            'actual_effort_hrs': forms.TextInput(attrs={'placeholder': 'effectieve effort in uren', 'style': 'font-size: 10px'}),
            'wip': forms.TextInput(attrs={'placeholder': 'progressie effort in uren', 'style': 'font-size: 10px'}),
            'event_van': forms.DateTimeInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'datetime-local',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                    'class': 'form-control',
                }),
            'event_tot': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                    'class': 'form-control',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(OpdrachtCalEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                        Field('event_type', wrapper_class='form-group col-md-2 mb-0', display='flex'),
                    Field('event', wrapper_class='form-group col-md-7 mb-0', display='flex'),
                    Field('stageopdrachten', wrapper_class='form-group col-md-3 mb-0', display='flex'       ),
                ),
                Div(
                    Row(
                    Field('event_van', wrapper_class='form-group col-md-2 mb-0', display='flex'),
                        Field('event_tot', wrapper_class='form-group col-md-2 mb-0', display='flex'),
                        Field('afspraak_invitees', wrapper_class='form-group col-md-8 mb-0', display='flex'),
                    )
                ),
                Div(
                    Row(
                        Field('omschrijving', wrapper_class='form-group col-md-12 mb-0', display='flex'),
                    )
                ),
                Div(
                  Row(
                      Field('taak', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                      Field('taaktype', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                      Field('taak_omschrijving', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                  ),
                    Row(
                        Field('estimate_effort_hrs', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('actual_effort_hrs', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('wip', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                    ),
                    Row(
                        Field('taak_bijlage', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                    )
                ),
                Div(
                    Row(
                        Field('taak_ingediend', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                        Field('datum_ingediend', wrapper_class='form-group col-md-2 mb-0', display='flex', disabled=True),
                        Field('taak_zelfevaluatie', wrapper_class='form-group col-md-7 mb-0', display='flex'),
                    ),
                ),
                Div(
                    Row(
                        Field('taak_nagekeken', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                        Field('datum_nagekeken', wrapper_class='form-group col-md-2 mb-0', display='flex', disabled=True),
                        Field('feedback_door', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                        Field('taak_score', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                    ),
                    Row(
                        Field('taak_feedback', wrapper_class='form-group col-md-12 mb-0', display='flex'),
                    ),
                ),
            ),
        Div(
                Submit('save', 'Save changes', style='max-width: 20em'),
                css_class='btn-right',
            )
        )
        self.helper.form_method = 'post'

class Taken(forms.ModelForm):
    """Taken detail formulier """
    class Meta:
        model = Taken
        exclude = ['created_by', 'created_at' , 'last_updated_by', 'last_updated_at',]
        widgets = {
            'taak_omschrijving': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'style': 'font-size: 10px'}),
            'taak_zelfevaluatie': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'style': 'font-size: 10px'}),
            'taak_feedback': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'style': 'font-size: 10px'}),
            'datum_ingediend': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                    'class': 'form-control',
                }),
            'datum_nagekeken': forms.DateInput(
                attrs={
                    'style': 'font-size: 10px; cursor:pointer',
                    'type': 'date',
                    'onkeydown': 'return true',  # block typing insite the input
                    'min': '1950-01-01',
                    'max': '2030-12-31',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(TakenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                        Field('event_type', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                    Field('event', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                    Field('stageopdrachten', wrapper_class='form-group col-md-3 mb-0', display='flex'),
                ),
                Div(
                    Row(
                    Field('event_van', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                        Field('event_tot', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                    )
                ),
                Div(
                    Row(
                        Field('omschrijving', wrapper_class='form-group col-md-4 mb-0', display='flex'),
                    )
                ),
                Div(
                    Row(
                        Field('afspraak_invitees', wrapper_class='form-group col-md-6 mb-0', display='flex'),
                    )
                ),
            ),
        Div(
                Submit('save', 'Save changes', style='max-width: 20em'),
                css_class='btn-right',
            )
        )
        self.helper.form_method = 'post'


"""NIET MEER IN GEBRUIK"""
"""Inline formset om evalutietemplate & details te onderhouden"""
EvaluatieFormset = inlineformset_factory(StageOpdrachtEvaluaties, StageOpdrachtEvaluatieDetails, exclude=('created_by', 'created_at','last_updated_by','last_updated_at'))

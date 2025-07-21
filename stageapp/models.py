import datetime

from django.db import models
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User #To restrict access to the user who created the entry
from django.conf import settings
#from django_extension.db.models import TimeStampedModel
import datetime as dt

# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)

    class Meta:
        abstract = True

class BedrijvenGroep(models.Model):
    bedrijfsgroep_naam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255)
    website = models.TextField(validators=[URLValidator()],max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'bedrijven_groep'
        verbose_name = 'BedrijvenGroep'
        verbose_name_plural = 'BedrijvenGroep'

    def __str__(self):
        return self.bedrijfsgroep_naam

class Bedrijfsvestingen(models.Model):
    bedrijvengroep = models.ForeignKey('BedrijvenGroep', on_delete=models.CASCADE, related_name='bedrijfsvestingen')
    bedrijfsnaam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    website = models.TextField(validators=[URLValidator()],max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'bedrijfsvestingen'
        verbose_name = 'Bedrijfsvestingen'
        verbose_name_plural = 'Bedrijfsvestingen'

    def get_absolute_url(self):
        return reverse('stageapp:bedrijfsnaam_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.bedrijfsnaam

class Afdelingen(models.Model):
    bedrijvengroep = models.ForeignKey('BedrijvenGroep', on_delete=models.CASCADE, related_name='afdelingen')
    afdeling = models.CharField(max_length=255)
    afdeling_omschrijving = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'afdelingen'
        verbose_name = 'afdelingen'
        verbose_name_plural = 'afdelingen'

    def __str__(self):
        return self.afdeling
class Contactpersonen(models.Model):
    bedrijfsvestingen = models.ForeignKey('Bedrijfsvestingen', on_delete=models.CASCADE, related_name='contactpersonen')
    voornaam = models.CharField(max_length=255)
    naam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    actief = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'contactpersonen'
        verbose_name = 'Contactpersonen'
        verbose_name_plural = 'Contactpersonen'

    def __str__(self):
        return self.voornaam + ' ' + self.naam

class ScholenGroep(models.Model):
    scholen_groep_naam = models.CharField(db_column='Scholen_groep_naam', max_length=255)  # Field name made lowercase.
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    website = models.TextField(validators=[URLValidator()],max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'scholen_groep'
        verbose_name = 'scholen_groep'
        verbose_name_plural = 'scholen_groep'

    def __str__(self):
        return self.scholen_groep_naam
class Scholen(models.Model):
    scholengroep = models.ForeignKey('ScholenGroep', on_delete=models.CASCADE, related_name='scholen')
    school_naam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    website = models.TextField(validators=[URLValidator()],max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'scholen'
        verbose_name = 'scholen'
        verbose_name_plural = 'scholen'

    def __str__(self):
        return self.school_naam

class Opleidingen(models.Model):
    scholen = models.ForeignKey('Scholen', on_delete=models.CASCADE, related_name='opleidingen')
    opleiding = models.CharField(max_length=255)
    graad = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'opleidingen'
        verbose_name = 'opleidingen'
        verbose_name_plural = 'opleidingen'

    def __str__(self):
        return self.opleiding
class Schooljaren(models.Model):
    schooljaar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'schooljaren'
        verbose_name = 'schooljaren'
        verbose_name_plural = 'schooljaren'

    def __str__(self):
        return self.schooljaar

class Klassen(models.Model):
    klas = models.CharField(max_length=255)
    klas_omschrijving = models.CharField(max_length=255)
    opleidingen = models.ForeignKey('Opleidingen', on_delete=models.CASCADE, related_name='klassen')
    schooljaren = models.ForeignKey('Schooljaren', on_delete=models.CASCADE, related_name='klassen')
    opleidingsjaar = models.CharField(max_length=255, verbose_name='Eerste jaar, tweede jaar, ...', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'klassen'
        verbose_name = 'klassen'
        verbose_name_plural = 'klassen'

    def __str__(self):
        return self.klas
class Studenten(models.Model):
    scholen = models.ForeignKey('Scholen', on_delete=models.CASCADE, related_name='studenten')
    klassen = models.ManyToManyField('Klassen', related_name='klassen')
    voornaam = models.CharField(max_length=255)
    naam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    rijksregisternr = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    actief = models.BooleanField(default=True)
    ingeschreven_sinds = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'studenten'
        verbose_name = 'studenten'
        verbose_name_plural = 'studenten'

    def __str__(self):
        return self.voornaam + ' ' + self.naam

class Leerkrachten(models.Model):
    scholen = models.ForeignKey('Scholen', on_delete=models.CASCADE, related_name='scholen')
    klassen = models.ManyToManyField('Klassen', related_name='leerkrachten')
    voornaam = models.CharField(max_length=255)
    naam = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    nummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    plaats = models.CharField(max_length=255)
    rijksregisternr = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    actief = models.BooleanField(default=True)
    werkzaam_sinds = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'leerkrachten'
        verbose_name = 'leerkrachten'
        verbose_name_plural = 'leerkrachten'

    def __str__(self):
        return self.voornaam + ' ' + self.naam


#class KlasLeerkrachten((models.Model)):
#This model is not required because of manytomany relationship between leerkrachten en klassen
#    klassen = models.ForeignKey('Klassen', on_delete=models.CASCADE, related_name='klasleerkrachten')
#    leerkrachten = models.ForeignKey('Leerkrachten', on_delete=models.CASCADE, related_name='klasleerkrachten')
#    created_at = models.DateTimeField(auto_now_add=True)
#    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
 #   last_updated_at = models.DateTimeField(auto_now=True)
 #   last_updated_by = models.CharField(max_length=255, blank=True,null=True)

 #   class Meta:
 #       db_table = 'klas_leerkrachten'
 #       verbose_name = 'klas_leerkrachten'
 #       verbose_name_plural = 'klas_leerkrachten'

#class KlasStudenten((models.Model)):
#not required because of manytomanyrelationship between studenten en klassen
#    klassen = models.ForeignKey('Klassen', on_delete=models.CASCADE, related_name='klasstudenten')
#    studenten = models.ForeignKey('Studenten', on_delete=models.CASCADE, related_name='klasstudenten')
#    created_at = models.DateTimeField(auto_now_add=True)
#    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
#    last_updated_at = models.DateTimeField(auto_now=True)
    #last_updated_by = models.CharField(max_length=255)

    #class Meta:
     #   db_table = 'klas_studenten'
      #  verbose_name = 'klas_studenten'
       # verbose_name_plural = 'klas_studenten'

class StageOpportuniteiten(models.Model):
    bedrijfsvestingen = models.ForeignKey('Bedrijfsvestingen', on_delete=models.CASCADE, related_name='stageopportuniteiten')
    afdelingen = models.ForeignKey('Afdelingen', on_delete=models.CASCADE, related_name='stageopportuniteiten')
    contactpersonen = models.ForeignKey('Contactpersonen', on_delete=models.CASCADE, related_name='stageopportuniteiten')
    stage = models.CharField(max_length=255)
    ingevuld = models.BooleanField(verbose_name='Aangvinkt = student gevonden om stage in te vullen.', default=False)
    opmerking_invulling = models.TextField(max_length=255,
                                           verbose_name='Achtergrond informatie over het al dan niet ingevuld zijn van de opdracht')
    actief = models.BooleanField(verbose_name='Aangevinkt = Staat nog open voor studenten.', default=False)
    stage_opdracht_van = models.DateField()
    stage_opdracht_tot = models.DateField()
    stage_omschrijving = models.TextField()
    werkuren = models.CharField(max_length=255)
    gewenste_profielen = models.TextField()
    applicaties_tot = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'stage_opportuniteiten'
        verbose_name = 'stage_opportuniteiten'
        verbose_name_plural = 'stage_opportuniteiten'

    def __str__(self):
        return self.stage
class StageOppKandidaten(models.Model):
    stageopportuniteiten = models.ForeignKey('StageOpportuniteiten',on_delete=models.CASCADE,related_name='stageoppkandidaten')
    studenten = models.ForeignKey('Studenten', on_delete=models.CASCADE,related_name='stageoppkandidaten')
    motivatie = models.TextField()
    cv = models.FileField(upload_to='cv/')
    zichtbaar = models.BooleanField(verbose_name='applicatie door student is zichtbaar voor het bedrijf', default=False)
    datum_doorgestuurd = models.DateTimeField(
        verbose_name='Datum/uur waarop applicatie zichtbaar is gekomen en doorgestuurd/zichtbaar is naar/voor het bedrijf')
    match_gevonden = models.BooleanField(verbose_name='Aangevinkt = student is weerhoude voor de stageopdracht', default=False)
    match_motivatie = models.TextField(verbose_name='achtergrond bij weerhouden student voor de stage')
    motivatie_door = models.CharField(max_length=255,
                                      verbose_name='user id van de persoon die de motivatie ingevuld heeft')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'stage_opp_kandidaten'
        verbose_name = 'stage_opp_kandidaten'
        verbose_name_plural = 'stage_opp_kandidaten'

class ScoreType(models.Model):
    score_type = models.CharField(max_length=255, verbose_name='Quantitative or Qualitative')
    score_type_omschrijving = models.TextField(verbose_name='quantitative = with range, qualitative = text feedback', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'score_type'
        verbose_name = 'score_type'
        verbose_name_plural = 'score_type'

    def __str__(self):
        return self.score_type
class EvaluatieCriteria(models.Model):
    criteria = models.CharField(max_length=255)
    criteria_omschrijving = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_criteria'
        verbose_name = 'evaluatie_criteria'
        verbose_name_plural = 'evaluatie_criteria'

    def __str__(self):
        return self.criteria
class EvaluatieScoreRange(models.Model):
    scoretype = models.ForeignKey('ScoreType', on_delete=models.CASCADE, related_name='evaluatiescorerange') #Quantitative
    score_range = models.CharField(max_length=255, blank=True, null=True)
    score_van = models.IntegerField(verbose_name='Score van: When type = 1; eg 1', blank=True, null=True)
    score_tot = models.IntegerField(verbose_name='Score tot: When type = 1; eg 10', blank=True, null=True)
    toelichting_score_range = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_score_range'
        verbose_name = 'evaluatie_score_range'
        verbose_name_plural = 'evaluatie_score_range'

    def __str__(self):
        return self.score_range
class EvaluatieTemplateHoofddeel(models.Model):
    hoofddeel = models.CharField(max_length=255)
    hoofddeel_omschrijving = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_template_hoofddeel'
        verbose_name = 'evaluatie_template_hoofddeel'
        verbose_name_plural = 'evaluatie_template_hoofddeel'

    def __str__(self):
        return self.hoofddeel
class EvaluatieTemplateSubdeel(models.Model):
    subdeel = models.CharField(max_length=255)
    subdeel_omschrijving = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_template_subdeel'
        verbose_name = 'evaluatie_template_subdeel'
        verbose_name_plural = 'evaluatie_template_subdeel'

    def __str__(self):
        return self.subdeel
class EvaluatieTemplates(models.Model):
    scholengroep = models.ForeignKey('ScholenGroep', on_delete=models.CASCADE, related_name='scholengroep')
    template_naam = models.CharField(max_length=255)
    template_omschrijving = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_templates'
        verbose_name = 'evaluatie_templates'
        verbose_name_plural = 'evaluatie_templates'

    def __str__(self):
        return self.template_naam
class EvaluatieTemplateDetails(models.Model):
    evaluatietemplates = models.ForeignKey('EvaluatieTemplates', on_delete=models.CASCADE, related_name='evaluatietemplatedetails')
    hoofddeel = models.ForeignKey('EvaluatieTemplateHoofddeel', on_delete=models.CASCADE, related_name='evaluatietemplatedetails')
    subdeel = models.ForeignKey('EvaluatieTemplateSubdeel', on_delete=models.CASCADE, blank=True, null=True, related_name='evaluatietemplatedetails')
    criteria = models.ForeignKey('EvaluatieCriteria', on_delete=models.CASCADE, related_name='evaluatietemplatedetails')
    score_range = models.ForeignKey('EvaluatieScoreRange', on_delete=models.CASCADE, related_name='evaluatietemplatedetails')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'evaluatie_template_details'
        verbose_name ='evaluatie_template_details'
        verbose_name_plural = 'evaluatie_template_details'

    def __str__(self):
        return str(self.evaluatietemplates) + ' - ' + str(self.hoofddeel) + ' - ' + str(self.subdeel) + ' - ' + str(self.criteria) + ' - ' + str(self.score_range)

class StageOpdrachten(models.Model):
    stage_opdracht = models.CharField(max_length=255)
    stage_opportuniteit = models.ForeignKey('StageOpportuniteiten',verbose_name='Referentie naar een stageopportuniteit indien van toepassing', related_name='stageopdrachten',null=True,on_delete=models.CASCADE, db_constraint=False, blank=True)
    bedrijfsvestingen = models.ForeignKey('Bedrijfsvestingen', on_delete=models.CASCADE, related_name='stageopdrachten')
    afdelingen = models.ForeignKey('Afdelingen', on_delete=models.CASCADE, related_name='stageopdrachten')
    contactpersonen = models.ForeignKey('Contactpersonen', on_delete=models.CASCADE, verbose_name='Stagebegeleider firma', related_name='stageopdrachten')
    #school = models.ForeignKey('Scholen', on_delete=models.CASCADE, related_name='stageopdrachten')
    #opleiding = models.ForeignKey('Opleidingen', on_delete=models.CASCADE, related_name='stageopdrachten')
    #klas = models.ForeignKey('Klassen', on_delete=models.CASCADE, related_name='stageopdrachten')
    leerkrachten = models.ForeignKey('Leerkrachten', on_delete=models.CASCADE, verbose_name='student begeleider van de school', related_name='stageopdrachten')
    studenten = models.ForeignKey('Studenten', on_delete=models.CASCADE, verbose_name='student die stage opdracht gaat uitvoeren', related_name='stageopdrachten')
    actief = models.BooleanField(default=False, help_text='Aangevinkt indien opdracht actief is.')
    stage_opdracht_van = models.DateField()
    stage_opdracht_tot = models.DateField()
    stage_omschrijving = models.TextField()
    afspraken = models.TextField(blank=True, null=True)
    doelstellingen = models.TextField()
    verwachtte_attitudes = models.TextField(blank=True, null=True)
    stage_opdracht_afgesloten = models.BooleanField(default=False)
    datum_stage_opdracht_afgesloten = models.DateTimeField(blank=True, null=True, verbose_name='Datum afgesloten')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True, default='Admin')

    class Meta:
        db_table = 'stage_opdrachten'
        verbose_name = 'stage_opdrachten'
        verbose_name_plural = 'stage_opdrachten'

    def __str__(self):
        return self.stage_opdracht

    def _validate_van_tot(self):
        if self.stage_opdracht_tot < self.stage_opdracht_van:
            raise ValidationError('Eind datum opdracht kan niet voor de start datum vallen.')

    def save(self, *args, **kwargs):
        self._validate_van_tot()
        self._set_dat_closed()
        return super().save(*args,**kwargs)

    def _set_dat_closed(self):
        dat = dt.datetime.now()
        if self.stage_opdracht_afgesloten == True and self.datum_stage_opdracht_afgesloten == None:
            self.datum_stage_opdracht_afgesloten = dat

class TaakType(models.Model):
    taak_type = models.CharField(max_length=255)
    taak_type_omschrijving = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'taak_type'
        verbose_name = 'taak_type'
        verbose_name_plural = 'taak_type'

    def __str__(self):
        return self.taak_type

class StageOpdrachtCalevents(models.Model):
    Type_Herinnering = 'Herinnering'
    Type_Afspraak = 'Afspraak'
    Type_Taak = 'Taak'

    Event_Type_Choices = [
        (Type_Herinnering, 'Herinnering'),
        (Type_Afspraak, 'Afspraak'),
        (Type_Taak, 'Taak'),
    ]

    stageopdrachten = models.ForeignKey('StageOpdrachten', on_delete=models.CASCADE, related_name='stageopdrachtcalevents')
    event_type = models.CharField(choices=Event_Type_Choices, default=Type_Taak, max_length=40)
    event = models.CharField(max_length=40)
    event_van = models.DateTimeField()
    event_tot = models.DateTimeField(blank=True, null=True)
    omschrijving = models.TextField(blank=True, null=True)
    afspraak_invitees = models.CharField(max_length=255, blank=True, null=True)
    taaktype = models.ForeignKey('TaakType', on_delete=models.CASCADE, related_name='taaktype', blank=True, null=True, db_constraint=False)
    taak = models.CharField(max_length=255, blank=True, null=True)
    taak_omschrijving = models.TextField(blank=True, null=True)
    taak_bijlage = models.FileField(upload_to='taken/', blank=True, null=True)
    estimate_effort_hrs = models.FloatField(blank=True, null=True)
    actual_effort_hrs = models.FloatField(blank=True, null=True)
    wip = models.IntegerField(blank=True, null=True)
    taak_zelfevaluatie = models.TextField(blank=True, null=True)
    taak_ingediend = models.BooleanField(default=False, blank=True, null=True)
    datum_ingediend = models.DateTimeField(blank=True, null=True)
    taak_nagekeken = models.BooleanField(default=False, blank=True, null=True)
    datum_nagekeken = models.DateTimeField(blank=True, null=True)
    taak_feedback = models.TextField(blank=True, null=True)
    taak_score = models.CharField(max_length=255, blank=True, null=True)
    feedback_door = models.CharField(max_length=255,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'stage_opdracht_calevents'
        verbose_name = 'stage_opdracht_calevents'
        verbose_name_plural = 'stage_opdracht_calevents'

    def __str__(self):
        return self.event

    def _validate_van_tot(self):
        if self.event_tot < self.event_van:
            raise ValidationError('Eind datum event kan niet voor de start datum vallen.')

    def save(self, *args, **kwargs):
        self._set_taak_ingediend()
        self._set_taak_nagekeken()
        return super().save(*args,**kwargs)

    def _set_taak_ingediend(self):
        dat = dt.datetime.now()
        if self.taak_ingediend == True and self.datum_ingediend == None:
            self.datum_ingediend = dat

    def _set_taak_nagekeken(self):
        dat = dt.datetime.now()
        if self.taak_nagekeken == True and self.datum_nagekeken == None:
            self.datum_nagekeken = dat

class Taken(models.Model):
    stageopdrachtcalevents = models.OneToOneField('StageOpdrachtCalevents', on_delete=models.CASCADE, related_name='taken')
    taaktype = models.ForeignKey('TaakType',on_delete=models.CASCADE, related_name='taken')
    taak = models.CharField(max_length=255)
    taak_omschrijving = models.TextField(blank=True, null=True)
    taak_bijlage = models.FileField(upload_to='taken/', blank=True,null=True)
    ingeschatte_effort_hrs = models.FloatField(verbose_name='Ingeschatte effort in uren', blank=True,null=True)
    werkelijke_effort_hrs = models.FloatField(
        verbose_name='Werkelijk benodigd aantal uren om taak af te werken/uit te voeren.', blank=True,null=True)
    progressie = models.IntegerField(verbose_name='Ingeschatte progressie in %', blank=True,null=True)
    taak_zelfevalutie = models.TextField(blank=True,null=True)
    taak_ingediend = models.BooleanField(verbose_name='Aangevinkt = student heeft taak afgewerkt en ingediend', default=False, blank=True,null=True)
    datum_ingediend = models.DateTimeField(blank=True,null=True)
    nagekeken = models.BooleanField(
        verbose_name='stagebegeleider kan aangeven of taak nagekeken is.  Feedback daarna ook zichtbaar voor student.', default=False, blank=True,null=True)
    datum_nagekeken = models.DateTimeField(blank=True,null=True)
    taak_feedback = models.TextField(verbose_name='feedback stagebegeleider op ingediende/afgewerkte taak', default=False, blank=True,null=True)
    taak_score = models.CharField(max_length=255, blank=True,null=True)
    feedback_door = models.CharField(max_length=255,
                                     verbose_name='user id van de persoon die de taak heeft nagekeken en feedback ingevuld.', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'taken'
        verbose_name = 'taken'
        verbose_name_plural = 'taken'

    def __str__(self):
        return self.taak

    def save(self, *args, **kwargs):
        self._set_taak_ingediend()
        self._set_taak_nagekeken()
        return super().save(*args,**kwargs)

    def _set_taak_ingediend(self):
        dat = dt.datetime.now()
        if self.taak_ingediend == True and self.datum_ingediend == None:
            self.datum_ingediend = dat

    def _set_taak_nagekeken(self):
        dat = dt.datetime.now()
        if self.nagekeken == True and self.datum_nagekeken == None:
            self.datum_nagekeken = dat

class StageOpdrachtEvaluaties(models.Model):
    stageopdrachten = models.OneToOneField('StageOpdrachten', on_delete=models.CASCADE, related_name='stageopdrachtevaluaties')
    evaluatietemplates = models.ForeignKey('EvaluatieTemplates', on_delete=models.CASCADE, related_name='stageopdrachtevaluaties')
    vrijgegeven = models.BooleanField(verbose_name='Aangevinkt = Eindverslag ingevuld en zichtbaar.', default=False)
    datum_vrijgegeven = models.DateTimeField(blank=True, null=True)
    ontvangst_studentverantwoordelijke = models.BooleanField(verbose_name='verantwoordelijke van de student heeft eindbeoordeling gezien.', default=False)
    datum_ontvangst_studentverantwoordelijke = models.DateTimeField(blank=True, null=True)
    notities_studentverantwoordelijke = models.TextField(blank=True, null=True)
    datum_last_update_notities_studentverantwoordelijke = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'stage_opdracht_evaluaties'
        verbose_name = 'stage_opdracht_evaluaties'
        verbose_name_plural = 'stage_opdracht_evaluaties'

    def save(self, *args, **kwargs):
        self._set_dat_vrijgegeven()
        self._set_dat_ontvangststudentverantwoordelijke()
        return super().save(*args,**kwargs)

    def _set_dat_vrijgegeven(self):
        dat = dt.datetime.now()
        if self.vrijgegeven == True and self.datum_vrijgegeven == None:
            self.datum_vrijgegeven = dat

    def _set_dat_ontvangststudentverantwoordelijke(self):
        dat = dt.datetime.now()
        if self.ontvangst_studentverantwoordelijke == True and self.datum_ontvangst_studentverantwoordelijke == None:
            self.datum_ontvangst_studentverantwoordelijke = dat


class StageOpdrachtEvaluatieDetails(models.Model):
    stageopdrachtevaluaties = models.ForeignKey('StageOpdrachtEvaluaties', on_delete=models.CASCADE, related_name='stageopdrachtevaluatiedetails')
    EvaluatieTemplateHoofddeel = models.ForeignKey('EvaluatieTemplateHoofddeel', on_delete=models.CASCADE, related_name='stageopdrachtevaluatiedetails', blank=True, null=True, db_constraint=False)
    EvaluatieTemplateSubdeel = models.ForeignKey('EvaluatieTemplateSubdeel', on_delete=models.CASCADE, related_name='stageopdrachtevaluatiedetails', blank=True, null=True, db_constraint=False)
    EvaluatieCriteria = models.ForeignKey('EvaluatieCriteria', on_delete=models.CASCADE, related_name='stageopdrachtevaluatiedetails')
    EvaluatieScoreRange = models.ForeignKey('EvaluatieScoreRange', on_delete=models.CASCADE, related_name='stageopdrachtevaluatiedetails')
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],  blank=True, null=True)
    score_nvt = models.BooleanField(default=False,
        verbose_name='NVT: Als score niet gegeven kan worden.', blank=True, null=True)
    score_argumentatie = models.TextField(blank=True, null=True,verbose_name='bijkomende argumentatie bij quantitatieve score')
    score_opmerking = models.TextField(blank=True, null=True,
        verbose_name='Vrije feedback voor qualitatieve assessment.')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, max_length=255)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, default='Admin')

    class Meta:
        db_table = 'stage_opdracht_evaluatie_details'
        verbose_name = 'stage_opdracht_evaluatie_details'
        verbose_name_plural = 'stage_opdracht_evaluatie_details'



"""Niet nodig"""
class Afspraken(models.Model):
    stageopdrachtcalevents = models.ForeignKey('StageOpdrachtCalevents', on_delete=models.CASCADE, related_name='afspraken')
    afspraak = models.CharField(max_length=255)
    afspraak_omschrijving = models.TextField()
    afspraak_invitees = models.CharField(max_length=255, verbose_name='afspraak sturen naar x emails')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, default=User)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=255, blank=True,null=True, default='Admin')

    class Meta:
        db_table = 'afspraken'
        verbose_name = 'afspraken'
        verbose_name_plural = 'afspraken'

    def __str__(self):
        return self.afspraak


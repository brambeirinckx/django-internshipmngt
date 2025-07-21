from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect

from django import forms

from .models import StageOpdrachten, Opleidingen, BedrijvenGroep, Bedrijfsvestingen, Afdelingen,  StageOpdrachtEvaluaties, StageOpdrachtEvaluatieDetails, Contactpersonen, EvaluatieTemplates, EvaluatieTemplateDetails, Klassen, Opleidingen, Scholen, ScholenGroep, Studenten, StageOpdrachtCalevents, Taken, Schooljaren, Leerkrachten
from .forms import StageOpdrachtenForm, OpleidingenForm, OpdrachtEvaluatieForm, OpdrachtEvaluatieDetailForm, EvaluatieFormset, BedrijvenGroepForm, VestingForm, AfdelingForm, ContactPersoonForm, OpdrachtCalEventForm, ScholenGroepForm, ScholenForm, SchooljaarForm, KlasForm, StudentForm, LeerkrachtForm

from django.contrib.auth.models import User

from django.views.generic import (FormView, ListView,DetailView, CreateView)
from django.views.generic.detail import SingleObjectMixin

from django.utils.decorators import method_decorator

from django.contrib import messages
from django.db.models import Prefetch

# Create your views here.
#Homepage
@login_required
def index(request):
    """Homepage of the Stagebegeleidings App """
    return render(request, 'stageapp/index.html')

@login_required
def test(request):
    return render(request,'stageapp/test.html')


def general_admin(request):
    """Return the page with links for general maintenance"""
    return render(request,'stageapp/general_admin.html')
@login_required
def view_opleidingen(request, id):
    """ Toon alle opleidingen van de geselecteerde school """
    """ ID = scholen id"""
    o_en = Opleidingen.objects.filter(scholen_id = id)
    s = Scholen.objects.get(id = id)
    sg = ScholenGroep.objects.get(id = s.scholengroep_id)
    context ={'o_en': o_en, 's': s, 'sg': sg}
    return render(request,'stageapp/opleidingen.html', context)


@login_required
def create_opleiding(request, id):
    """ Aanmaken nieuwe opleiding voor de geselecteerde school via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    """id = scholen_id """
    s = Scholen.objects.get(id = id)
    if request.method != 'POST':
        #no data submitted
        form = OpleidingenForm()
        form.fields['scholen'].initial = id
    else:
        #POST submitted
        form = OpleidingenForm(data=request.POST)
        if form.is_valid():
            nieuwe_opleiding = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_opleiding.created_by = request.user
            nieuwe_opleiding.save()
        return redirect('stageapp:view_opleidingen', id = s.id)
    #blank form
    context = {'form': form, 's': s}
    return render(request, 'stageapp/nieuwe_opleiding.html', context)

@login_required
def edit_opleiding(request, id):
    """ Update/edit bestaande opleiding """
    """ ID = opleidingen ID"""
    o = Opleidingen.objects.get(id=id)
    s = Scholen.objects.get(id = o.scholen_id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = OpleidingenForm(instance = o)
    else:
        # POST submitted, process data
        form = OpleidingenForm(instance = o, data=request.POST)
        if form.is_valid():
            updated_instance = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_instance.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_instance.save()
            return redirect('stageapp:view_opleidingen', id = s.id) #Return to the view from which the request was launched

    context = {'o': o, 'form': form, 's': s}
    return render(request, 'stageapp/edit_opleiding.html', context)

@login_required
def delete_opleiding(request, id):
    """ Delete selected opleiding """
    o = Opleidingen.objects.get(id=id)
    s = Scholen.objects.get(id=o.scholen_id)

    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_opleidingen', id = s.id )
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

"""Voor studenten """
@login_required
def view_studenten(request, id):
    """ Toon alle studenten van de geselecteerde school """
    """ ID = scholen id"""
    studenten = Studenten.objects.filter(scholen_id = id)
    s = Scholen.objects.get(id = id)
    sg = ScholenGroep.objects.get(id = s.scholengroep_id)
    context ={'studenten': studenten, 's': s, 'sg': sg}
    return render(request,'stageapp/view_studenten.html', context)


@login_required
def create_opleiding(request, id):
    """ Aanmaken nieuwe opleiding voor de geselecteerde school via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    """id = scholen_id """
    s = Scholen.objects.get(id = id)
    if request.method != 'POST':
        #no data submitted
        form = OpleidingenForm()
        form.fields['scholen'].initial = id
    else:
        #POST submitted
        form = OpleidingenForm(data=request.POST)
        if form.is_valid():
            nieuwe_opleiding = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_opleiding.created_by = request.user
            nieuwe_opleiding.save()
        return redirect('stageapp:view_opleidingen', id = s.id)
    #blank form
    context = {'form': form, 's': s}
    return render(request, 'stageapp/nieuwe_opleiding.html', context)

@login_required
def edit_opleiding(request, id):
    """ Update/edit bestaande opleiding """
    """ ID = opleidingen ID"""
    o = Opleidingen.objects.get(id=id)
    s = Scholen.objects.get(id = o.scholen_id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = OpleidingenForm(instance = o)
    else:
        # POST submitted, process data
        form = OpleidingenForm(instance = o, data=request.POST)
        if form.is_valid():
            updated_instance = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_instance.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_instance.save()
            return redirect('stageapp:view_opleidingen', id = s.id) #Return to the view from which the request was launched

    context = {'o': o, 'form': form, 's': s}
    return render(request, 'stageapp/edit_opleiding.html', context)

@login_required
def delete_opleiding(request, id):
    """ Delete selected opleiding """
    o = Opleidingen.objects.get(id=id)
    s = Scholen.objects.get(id=o.scholen_id)

    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_opleidingen', id = s.id )
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)



#StageOpdrachten
@login_required
def stageopdrachten_lijst(request, id):
    """ Genereer een form met de stageopdrachten voor  geselecteerd bedrijfsvesting"""
    so_en =StageOpdrachten.objects.filter(bedrijfsvestingen_id=id)
    bv = Bedrijfsvestingen.objects.get(id = id)
    context = {'so_en': so_en, 'bv': bv}
    return render(request, 'stageapp/stageopdrachten_lijst.html', context)

@login_required
def nieuwe_opdracht(request, id):
    """ Aanmaken nieuwe stageopdracht voor de geselecteerde bedrijfsvesting """
    bv = Bedrijfsvestingen.objects.get(id=id)
    if request.method != 'POST':
        #no data submitted
        form = StageOpdrachtenForm()
        form.fields['bedrijfsvestingen'].initial = bv

    else:
        #POST submitted
        form = StageOpdrachtenForm(data=request.POST)
        if form.is_valid():
            nieuwe_opdracht = form.save(commit=False)
            #Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            #nieuwe_opdracht.bedrijfsvestingen_id = id  #We gaan dat hier niet overrulen want veld kan ingevuld worden via form.  Het wordt hierboven wel gedefault naar de bedrijfsvesting.
            nieuwe_opdracht.created_by = request.user
            nieuwe_opdracht.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Nieuwe stageopdracht is aangemaakt.')
        return redirect('stageapp:lijst_stageopdrachten', id = id)
    #blank form
    bv = Bedrijfsvestingen.objects.get(id=id)
    context = {'form': form, 'bv': bv}
    return render(request, 'stageapp/nieuwe_opdracht.html', context)

@login_required
def edit_so(request, so_id):
    """ Update/edit bestaande stageopdracht """
    so = StageOpdrachten.objects.get(id=so_id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = StageOpdrachtenForm(instance = so)
    else:
        # POST submitted, process data
        form = StageOpdrachtenForm(instance = so, data=request.POST)
        if form.is_valid():
            updated_opdracht = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_opdracht.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_opdracht.save()
            return redirect('stageapp:lijst_stageopdrachten', id = so.bedrijfsvestingen_id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'so': so, 'form': form}
    return render(request, 'stageapp/edit_so.html', context)

@login_required
def delete_so(request, so_id):
    """ Delete selected stageopdracht """
    so = StageOpdrachten.objects.get(id=so_id)
    if request.method == 'POST':
        so.delete()
        return redirect('stageapp:stageopdrachten')
    context = {'obj': so} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@method_decorator(login_required, name = 'dispatch' )
class BedrijvenGroepLijst(ListView):
    model = BedrijvenGroep
    template_name = 'stageapp/bedrijvengroep_lijst.html'

@login_required
def BedrijvenGroepCreate(request):
    """ Aanmaken nieuwe bedrijvengroep via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = BedrijvenGroepForm()
    else:
        #POST submitted
        form = BedrijvenGroepForm(data=request.POST)
        if form.is_valid():
            nieuwe_bg = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_bg.created_by = request.user
            nieuwe_bg.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Bedrijvengroep is aangemaakt.')
        return redirect('stageapp:lijst_bedrijfsgroepen')
    #blank form
    context = {'form': form}
    return render(request, 'stageapp/bedrijvengroep_create.html', context)

@login_required
def delete_bedrijvengroep(request, id):
    """ Delete selected bedrijvengroep """
    bg = BedrijvenGroep.objects.get(id=id)
    if request.method == 'POST':
        bg.delete()
        return redirect('stageapp:lijst_bedrijfsgroepen')
    context = {'obj': bg} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_bedrijvengroep(request, id):
    """ Update/edit bestaande bedrijfsgroep """
    bg = BedrijvenGroep.objects.get(id=id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = BedrijvenGroepForm(instance = bg)
    else:
        # POST submitted, process data
        form = BedrijvenGroepForm(instance = bg, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:lijst_bedrijfsgroepen') #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'bg': bg, 'form': form}
    return render(request, 'stageapp/bedrijvengroep_detail.html', context)


@login_required
def bedrijvengroep_alldata(request, id):
    """ Ophalen van bedrijfsvestingen en afdelingen voor een geselecteerde bedrijfsgroep """

    bedrijven1 = BedrijvenGroep.objects.prefetch_related('bedrijfsvestingen').get(pk=id)
    bedrijven2 = BedrijvenGroep.objects.prefetch_related('afdelingen').get(pk=id)
    vestingen = bedrijven1.bedrijfsvestingen.all()
    afd = bedrijven2.afdelingen.all()

    context = {'vestingen': vestingen, 'afd': afd, 'bg': bedrijven1}
    return render(request, 'stageapp/bedrijvengroep_alldata.html', context)

@login_required
def vestingCreate(request, id):
    """ Aanmaken nieuwe vesting via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    """ Een bedrijfsvesting is gelinkt aan Bedrijvengroep (id) """
    if request.method != 'POST':
        #no data submitted
        form = VestingForm()
    else:
        #POST submitted
        form = VestingForm(data=request.POST)
        if form.is_valid():
            nieuwe_record = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_record.bedrijvengroep_id = id
            nieuwe_record.created_by = request.user
            nieuwe_record.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Nieuwe vesting is aangemaakt.')
        return redirect('stageapp:bedrijvengroep_alldata', id = id)
    #blank form
    context = {'form': form}
    return render(request, 'stageapp/vesting_create.html', context)

@login_required
def delete_vesting(request, id):
    """ Delete selected vesting """
    r = Bedrijfsvestingen.objects.get(id=id)
    if request.method == 'POST':
        r.delete()
        return redirect('stageapp:bedrijvengroep_alldata', id = r.bedrijvengroep_id)
    context = {'obj': r} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_vesting(request, id):
    """ Update/edit bestaande vesting """
    bv = Bedrijfsvestingen.objects.get(id=id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = VestingForm(instance = bv)
    else:
        # POST submitted, process data
        form = VestingForm(instance = bv, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:bedrijvengroep_alldata', id= bv.bedrijvengroep_id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'vesting': bv, 'form': form}
    return render(request, 'stageapp/vesting_detail.html', context)


@login_required
def afdelingCreate(request, id):
    """ Aanmaken nieuwe afdeling via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    """ Nieuwe afdeling moet gelinkt worden met Bedrijvengroep """
    """ Id is ID van bedrijvengroep """
    if request.method != 'POST':
        #no data submitted
        form = AfdelingForm()
    else:
        #POST submitted
        form = AfdelingForm(data=request.POST)
        if form.is_valid():
            nieuwe_record = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_record.bedrijvengroep_id = id
            nieuwe_record.created_by = request.user
            nieuwe_record.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Nieuwe afdeling is aangemaakt.')
        return redirect('stageapp:bedrijvengroep_alldata', id= id)
    #blank form
    context = {'form': form}
    return render(request, 'stageapp/afdeling_create.html', context)

@login_required
def delete_afdeling(request, id):
    """ Delete selected afdeling """
    r = Afdelingen.objects.get(id=id)
    if request.method == 'POST':
        r.delete()
        return redirect('stageapp:bedrijvengroep_alldata', id = r.bedrijvengroep_id)
    context = {'obj': r} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_afdeling(request, id):
    """ Update/edit bestaande afdeling """
    r = Afdelingen.objects.get(id=id)
    print(r)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = AfdelingForm(instance = r)
    else:
        # POST submitted, process data
        form = AfdelingForm(instance = r, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:bedrijvengroep_alldata', id = r.bedrijvengroep_id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'r': r, 'form': form}
    return render(request, 'stageapp/afdeling_detail.html', context)



@login_required
def contactpersonen_lijst(request, id):
    """ Genereer een form met alle contactpersonen voor geselecteerd bedrijfsgroep """
    """ Dit is een andere manier dan ContactPersonenLijst via listfiel"""
    contactpersonen = Contactpersonen.objects.filter(bedrijfsvestingen_id=id)
    bv = Bedrijfsvestingen.objects.get(id = id)
    context = {'contactpersonen': contactpersonen, 'bv': bv}
    return render(request, 'stageapp/contactpersonen_lijst.html', context)


@login_required
def contactpersonencreate(request, id):
    """ Aanmaken nieuwe contactpersoon via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    """ Nieuwe contact persoon moet aangemaakt worden voor een bedrijfsvesting """
    if request.method != 'POST':
        #no data submitted
        form = ContactPersoonForm()
    else:
        #POST submitted
        form = ContactPersoonForm(data=request.POST)
        if form.is_valid():
            nieuwe_record = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_record.created_by = request.user
            nieuwe_record.bedrijfsvestingen_id = id
            nieuwe_record.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Nieuwe contactpersoon is aangemaakt.')
        return redirect('stageapp:lijst_contactpersonen', id = id)
    #blank form
    bv = Bedrijfsvestingen.objects.get(id=id)
    context = {'form': form, 'bv': bv}
    return render(request, 'stageapp/contactpersoon_create.html', context)

@login_required
def delete_contactpersoon(request, id):
    """ Delete selected contactpersoon """
    r = Contactpersonen.objects.get(id=id)
    if request.method == 'POST':
        r.delete()
        return redirect('stageapp:lijst_contactpersonen', r.bedrijfsvestingen_id)
    context = {'obj': r} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_contactpersoon(request, id):
    """ Update/edit bestaande contactpersoon """
    r = Contactpersonen.objects.get(id=id)
    bv = Bedrijfsvestingen.objects.get(id = r.bedrijfsvestingen_id)
    bg = BedrijvenGroep.objects.get(id=bv.bedrijvengroep_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ContactPersoonForm(instance = r)
    else:
        # POST submitted, process data
        form = ContactPersoonForm(instance = r, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:lijst_contactpersonen', id = r.bedrijfsvestingen_id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'contact': r, 'form': form, 'bg': bg, 'vesting': bv}
    return render(request, 'stageapp/contactpersoon_detail.html', context)

@login_required
def evaluatietemplates_lijst(request, id):
    """ Genereer een form met alle templates voor de scholengroep waartoe de geselecteerde student toe behoort """
    """ id = stageopdracht id"""
    so = StageOpdrachten.objects.get(pk=id) #Provides the record stageopdrachten which contains the student that will execute
    student = Studenten.objects.get(id = so.studenten_id)
    #Klassen is een manytomany relationship, therefore print(student.klassen) returns stageapp.klassen.none.  We use value_list to extract the value of the dictionary
    #When we retrieve the klas, then within that record we have also the opleidingen_id

    #Retrieve the klas
    klas = student.klassen.all().values()
    opleiding_id = klas.values_list('opleidingen_id')[0][0] #[0][0] = First element of the dictionary list (we have only 1 opleidingen_id) and then the first value of the tuple

    opleiding = Opleidingen.objects.get(id = opleiding_id) #We retrieve now the opleiding record which contains the school
    school = Scholen.objects.get(id = opleiding.scholen_id) #We retrieve now the school record which contains the id of the scholengroep to which the school belongs.
    sg = ScholenGroep.objects.get(id = school.scholengroep_id) #We have now the ID of the scholengroep and then we can search and display the templates that are setup for this scholengroep

    #Now retrieve evaluatie templates
    et = EvaluatieTemplates.objects.prefetch_related('evaluatietemplatedetails').filter(scholengroep_id = sg.id)


    context = {'sg': sg, 'et': et, 'so': so}
    return render(request, 'stageapp/evaluatietemplate_lijst.html', context)


@login_required
def evaluatietemplate_details(request, id):
    """ Genereer een form met de template details voor de geselecteerde template """
    """ id = evaluatie template"""
    et = EvaluatieTemplates.objects.prefetch_related('evaluatietemplatedetails').get(id = id)
    etd = et.evaluatietemplatedetails.all().order_by('hoofddeel', 'subdeel')

    dic_data = {}
    lst_criteria = []
    dic_crit={}
    dic_sd = {}
    dic_hd = {}
    lst_sd = []
    lst_hd = []
    hd = ''
    sd = ''
    new_hd = ''
    new_sd = 'X'
    criteria_tuple = ()
    for el in etd:
        #print(el)
        new_hd = el.hoofddeel
        new_sd = el.subdeel
        crit = el.criteria
        score_range = el.score_range
        dic_crit = {'title': crit,
                    'score_range': score_range}

        if new_hd != hd:
            """This means a new main category of criteria.  When there are values, add the data from hoofddeel, subdeel and criteria/score to the data dictionary """
            if lst_criteria != []:
                """Data was collected, so not the first row.  Create dictionary of hd"""

                """This is not clean code but if dic_sd contains a value, then it is from a previous record that was not appended yet to lst_sd"""
                """do this first, then initialise again """
                if dic_sd != {}:
                    lst_sd.append(dic_sd)

                dic_hd = {'title': hd,
                          'subdelen': lst_sd}
                lst_hd.append(dic_hd)

                """ Initialise everything again"""
                hd = new_hd
                sd = new_sd
                dic_sd = {}
                dic_hd = {}
                lst_criteria = []
                lst_sd =[]
                lst_criteria.append(dic_crit)
            else:
                hd = new_hd
                sd = new_sd
                lst_criteria.append(dic_crit)
        else:
            """Check now subdeel"""
            if new_sd != sd:
                """This means new subdeel and data is to be written to dictionary """
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
                lst_sd.append(dic_sd)

                """ Initialise sd, criteria """
                sd = new_sd
                dic_sd = {}
                lst_criteria = []

                """ Create first set of criteria list """
                dic_crit = {'title': crit,
                            'score_range': score_range}
                lst_criteria.append(dic_crit)
                """Update the dictionary with the increased lst_criteria"""
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
            else:
                """Same HD & SD ==> Just another new criteria"""
                """Here is an issue: If next row is different hoofddeel, then the sd dictionary is incomplete because no dictionary is created"""
                lst_criteria.append(dic_crit)
                """Update the dictionary with the increased lst_criteria"""
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
    #Last record was read > Now to check how the last records is to be written
    """Create or update the last dic_hd """
    if lst_sd == []:
        """Last row is from a new main category > Built SD dictionary """
        dic_sd = {'title': sd,
                  'criteria': lst_criteria}
        lst_sd.append(dic_sd)

    """Create the last HD dictionary and append to the list of HD's"""
    dic_hd = {'title': hd,
                'subdelen': lst_sd}
    lst_hd.append(dic_hd)

    dic_data = {
        'hoofddelen': lst_hd
    }

    context = {'et':et, 'dic_data': dic_data}
    return render(request, 'stageapp/evaluatietemplate_details.html', context)


@login_required
def assign_template_details(request, id, id2):
    """ id = ID of the stageopdracht """
    """ id2 = Selected evaluatie template"""
    """ The details of this template are retrieved and then inserted models StageOpdrachtEvaluaties & StageOpdrachtEvaluatieDetails """
    et = EvaluatieTemplates.objects.prefetch_related('evaluatietemplatedetails').get(id = id2)
    etd = et.evaluatietemplatedetails.all()

    #First check if there is no template assigned yet to the stageopdracht
    if StageOpdrachtEvaluaties.objects.filter(stageopdrachten_id=id).exists():
        #print('ben je zeker?')
        messages.add_message(
            request,
            messages.SUCCESS,
            'Er is reeds een evaluatieformulier toegevoegd.')
        # Update template referentie, deleta all records from detail table = INSERT new records
    else:
        #Create the header record
        so_e = StageOpdrachtEvaluaties(
            stageopdrachten_id = id,
            evaluatietemplates_id = et.id,
            created_by = request.user)
        so_e.save()

        #Create all criteria line items based on the selected templates model
        for x in etd:
            so_ed = StageOpdrachtEvaluatieDetails(stageopdrachtevaluaties_id = so_e.id,
                                                  EvaluatieTemplateHoofddeel = x.hoofddeel,
                                                  EvaluatieTemplateSubdeel = x.subdeel,
                                                  EvaluatieCriteria = x.criteria,
                                                  EvaluatieScoreRange = x.score_range,
                                                  created_by = request.user)
            so_ed.save()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Evaluatie template is toegewezen aan de stageopdracht.')
    return redirect('stageapp:edit_so', id)

@login_required
def view_opdracht_evaluatie(request, id):
    """Check dat er reeds een evaluatie template is geselecteerd voor de stageopdracht.
    Indien niet: Open form op template te selecteren en toe te wijzen aan de stageopdracht
    Indien wel: Open header van opdracht evaluatie en details.
    ID = stageopdracht ID
     """

    # First check if there is no template assigned yet to the stageopdracht
    so = StageOpdrachten.objects.get(id=id)
    if StageOpdrachtEvaluaties.objects.filter(stageopdrachten_id=id).exists():
        #print("stageopdracht bestaat")
        soe =  StageOpdrachtEvaluaties.objects.get(stageopdrachten_id=id)
        if request.method != 'POST':
            # No data submitted
            # Check template is assigned already, if not open
            # form = OpdrachtEvaluatieForm(instance=soe)
            form = OpdrachtEvaluatieForm(instance=soe)
        else:
            # Post submitted
            form = OpdrachtEvaluatieForm(instance=soe, data=request.POST)
            if form.is_valid():
                oet = form.save(commit=False)
                oet.last_updated_by = User.objects.get(
                    username=request.user).username  # This returns a model instance User.objects.get(username=request.user)
                oet.save()
                return redirect('stageapp:edit_so', id)
        # blank form
        context = {'form': form, 'soe': soe, 'so': so}
        return render(request, 'stageapp/opdracht_evaluatie.html', context)
    else:
        """Er is nog geen template assigned ==> Oproepen functie om template toe te wijzen """
        return redirect('stageapp:opdracht_assign_evaluatie_template', so.id)

@login_required
def edit_opdracht_evaluatie_criteria(request, id):
    """
     ID = StageOpdrachtEvaluatieDetail ID

     Retrieve the evaluatie criteria from StageOpdrachtEvaluatieDetails
     """
    soed = StageOpdrachtEvaluatieDetails.objects.get(id = id)
    soe = StageOpdrachtEvaluaties.objects.get(id=soed.stageopdrachtevaluaties_id)
    so = StageOpdrachten.objects.get(id = soe.stageopdrachten_id)
    if request.method != 'POST':
        # No data submitted
        form = OpdrachtEvaluatieDetailForm(instance=soed)
    else:
        form = OpdrachtEvaluatieDetailForm(instance=soed, data=request.POST)
        if form.is_valid():
            oet = form.save(commit=False)
            oet.last_updated_by = User.objects.get(
                username=request.user).username  # This returns a model instance User.objects.get(username=request.user)
            oet.save()
            return redirect('stageapp:view_so_evaluatie_details', id = soe.id)
        else:
            return HttpResponse(form.errors.values())  # Validation failed
    # blank form
    context = {'form': form, 'soe': soe, 'so': so, 'soed': soed}
    return render(request, 'stageapp/edit_so_criteria.html', context)


@login_required
def create_soe_criteria(request, id):
    """
     ID = StageOpdrachtEvaluaties

     """
    soe = StageOpdrachtEvaluaties.objects.get(id=id)
    so = StageOpdrachten.objects.get(id = soe.stageopdrachten_id)
    if request.method != 'POST':
        # No data submitted
        form = OpdrachtEvaluatieDetailForm()
        form.fields['stageopdrachtevaluaties'].initial = id
    else:
        form = OpdrachtEvaluatieDetailForm(data=request.POST)
        if form.is_valid():
            oet = form.save(commit=False)
            oet.created_by = request.user  # This returns a model instance User.objects.get(username=request.user)
            oet.save()
            return redirect('stageapp:view_so_evaluatie_details', id = soe.id)
        else:
            return HttpResponse(form.errors.values())  # Validation failed
    # blank form
    context = {'form': form, 'soe': soe, 'so': so}
    return render(request, 'stageapp/create_so_criteria.html', context)

@login_required
def view_so_evaluatie_details(request, id):
    """ Genereer een form met de evaluatie criteria voor de geselecteerde stageopdracht """
    """ id = StageOpdrachtEvaluaties """
    soe = StageOpdrachtEvaluaties.objects.prefetch_related('stageopdrachtevaluatiedetails').get(id = id)
    soed = soe.stageopdrachtevaluatiedetails.all().order_by('EvaluatieTemplateHoofddeel', 'EvaluatieTemplateSubdeel')
    so = StageOpdrachten.objects.get(id = soe.stageopdrachten_id)

    dic_data = {}
    lst_criteria = []
    dic_crit={}
    dic_sd = {}
    dic_hd = {}
    lst_sd = []
    lst_hd = []
    hd = ''
    sd = ''
    new_hd = ''
    new_sd = 'X'
    for el in soed:
        print(el)
        new_hd = el.EvaluatieTemplateHoofddeel
        new_sd = el.EvaluatieTemplateSubdeel
        crit = el.EvaluatieCriteria
        score_range = el.EvaluatieScoreRange
        score = el.score
        score_nvt = el.score_nvt
        score_argumentatie = el.score_argumentatie
        score_opmerking = el.score_opmerking
        crit_id = el.id
        dic_crit = {'title': crit,
                    'score_range': score_range,
                    'score': score,
                    'score_nvt': score_nvt,
                    'score_argumentatie': score_argumentatie,
                    'score_opmerking': score_opmerking,
                    'id': crit_id}

        if new_hd != hd:
            """This means a new main category of criteria.  When there are values, add the data from hoofddeel, subdeel and criteria/score to the data dictionary """
            if lst_criteria != []:
                """Data was collected, so not the first row.  Create dictionary of hd"""

                """This is not clean code but if dic_sd contains a value, then it is from a previous record that was not appended yet to lst_sd"""
                """do this first, then initialise again """
                if dic_sd != {}:
                    lst_sd.append(dic_sd)
                    print(dic_sd)

                dic_hd = {'title': hd,
                          'subdelen': lst_sd}
                lst_hd.append(dic_hd)

                """ Initialise everything again"""
                hd = new_hd
                sd = new_sd
                dic_sd = {}
                dic_hd = {}
                lst_criteria = []
                lst_sd =[]
                lst_criteria.append(dic_crit)
            else:
                hd = new_hd
                sd = new_sd
                lst_criteria.append(dic_crit)
        else:
            """Check now subdeel"""
            if new_sd != sd:
                """This means new subdeel and data is to be written to dictionary """
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
                lst_sd.append(dic_sd)
                print(dic_sd)

                """ Initialise sd, criteria """
                sd = new_sd
                dic_sd = {}
                lst_criteria = []

                """ Create first set of criteria list """
                dic_crit = {'title': crit,
                            'score_range': score_range,
                            'score': score,
                            'score_nvt': score_nvt,
                            'score_argumentatie': score_argumentatie,
                            'score_opmerking': score_opmerking,
                            'id': crit_id}
                lst_criteria.append(dic_crit)
                """Update the dictionary with the increased lst_criteria"""
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
                print(dic_sd)
            else:
                """Same HD & SD ==> Just another new criteria"""
                """Here is an issue: If next row is different hoofddeel, then the sd dictionary is incomplete because no dictionary is created"""
                lst_criteria.append(dic_crit)
                """Update the dictionary with the increased lst_criteria"""
                dic_sd = {'title': sd,
                          'criteria': lst_criteria}
                print(dic_sd)
    #Last record was read > Now to check how the last records is to be written
    """Create or update the last dic_hd """
    if lst_sd == []:
        """Last row is from a new main category > Built SD dictionary """
        dic_sd = {'title': sd,
                  'criteria': lst_criteria}
        lst_sd.append(dic_sd)
        print(dic_sd)

    """Create the last HD dictionary and append to the list of HD's"""
    dic_hd = {'title': hd,
                'subdelen': lst_sd}
    lst_hd.append(dic_hd)

    dic_data = {
        'hoofddelen': lst_hd
    }

    context = {'so':so, 'dic_data': dic_data, 'soe':soe}
    return render(request, 'stageapp/opdracht_evaluatie_criteria.html', context)

@login_required
def delete_soe_criteria(request, id):
    """ Delete selected stage opdracht evaluatie criteria """
    o = StageOpdrachtEvaluatieDetails.objects.get(id=id)
    soe = StageOpdrachtEvaluaties.objects.get(id = o.stageopdrachtevaluaties_id)
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_so_evaluatie_details', id=soe.id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

"""In development"""
@login_required
def edit_so_calevents(request, id):
    """
     ID = StageOpdrachtCalevents ID

     Retrieve the calevent  from StageOpdrachtCalevents
     """
    soce = StageOpdrachtCalevents.objects.get(id = id)
    so = StageOpdrachten.objects.get(id = soce.stageopdrachten_id)
    if request.method != 'POST':
        # No data submitted
        form = OpdrachtCalEventForm(instance=soce)
    else:
        form = OpdrachtCalEventForm(instance=soce, data=request.POST, files=request.FILES)
        if form.is_valid():
            oet = form.save(commit=False)
            oet.last_updated_by = User.objects.get(
                username=request.user).username  # This returns a model instance User.objects.get(username=request.user)
            oet.save()
            return redirect('stageapp:view_so_calevents', id = so.id)
        else:
            return HttpResponse(form.errors.values())  # Validation failed
    # blank form
    context = {'form': form, 'soce': soce, 'so': so}
    return render(request, 'stageapp/edit_so_calevents.html', context)

@login_required
def create_so_calevents(request, id):
    so = StageOpdrachten.objects.get(id=id)
    if request.method != 'POST':
        # No data submitted
        form = OpdrachtCalEventForm()
        form.fields['stageopdrachten'].initial = id
    else:
        form = OpdrachtCalEventForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            oet = form.save(commit=False)
            oet.created_by = request.user  # This returns a model instance User.objects.get(username=request.user)
            oet.save()
            return redirect('stageapp:view_so_calevents', id = so.id)
        else:
            return HttpResponse(form.errors.values())  # Validation failed
    # blank form
    context = {'form': form, 'so': so}
    return render(request, 'stageapp/create_so_calevents.html', context)

@login_required
def view_so_calevents(request, id):
    """ Genereer een form met de verschillende cal events voor de geselecteerde stageopdracht """
    """ id = StageOpdrachten """
    so = StageOpdrachten.objects.prefetch_related('stageopdrachtcalevents').get(id = id)
    soce = so.stageopdrachtcalevents.all()

    context = {'so':so, 'soce': soce}
    return render(request, 'stageapp/view_so_calevents.html', context)

@login_required
def delete_so_calevents(request, id):
    """ Delete selected calevent """
    o = StageOpdrachtCalevents.objects.get(id=id)
    so = StageOpdrachten.objects.get(id = o.stageopdrachten_id)
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_so_calevents', id=so.id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)



@login_required
def delete_so(request, so_id):
    """ Delete selected stageopdracht """
    so = StageOpdrachten.objects.get(id=so_id)
    if request.method == 'POST':
        so.delete()
        return redirect('stageapp:stageopdrachten')
    context = {'obj': so} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

"""In development"""

@method_decorator(login_required, name = 'dispatch' )
class ScholenGroepLijst(ListView):
    model = ScholenGroep
    template_name = 'stageapp/scholengroep_lijst.html'

@login_required
def create_scholengroep(request):
    """ Aanmaken nieuwe scholengroep via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = ScholenGroepForm()
    else:
        #POST submitted
        form = ScholenGroepForm(data=request.POST)
        if form.is_valid():
            nieuwe_sg = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_sg.created_by = request.user
            nieuwe_sg.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Scholengroep is aangemaakt.')
        return redirect('stageapp:view_scholengroepen')
    #blank form
    context = {'form': form}
    return render(request, 'stageapp/create_scholengroep.html', context)

@login_required
def delete_scholengroep(request, id):
    """ Delete selected scholengroep """
    o = ScholenGroep.objects.get(id=id)
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_scholengroepen')
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_scholengroep(request, id):
    """ Update/edit bestaande scholengroep """
    sg = ScholenGroep.objects.get(id=id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ScholenGroepForm(instance = sg)
    else:
        # POST submitted, process data
        form = ScholenGroepForm(instance = sg, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:view_scholengroepen') #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'sg': sg, 'form': form}
    return render(request, 'stageapp/edit_scholengroep.html', context)

"""Voor scholen views"""
@login_required()
def view_scholen(request, id):
    """ Genereer een form met een overzicht van de scholen voor de geselecteerde scholengroep """
    """ id = Scholengroep """
    sg = ScholenGroep.objects.prefetch_related('scholen').get(id=id)
    scholen = sg.scholen.all()

    context = {'scholen': scholen, 'sg': sg}
    return render(request, 'stageapp/scholen_lijst.html', context)


@login_required
def create_school(request, id):
    sg = ScholenGroep.objects.get(id=id)
    """ Aanmaken nieuwe school via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = ScholenForm()
        form.fields['scholengroep'].initial = sg.id
    else:
        #POST submitted
        form = ScholenForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Scholengroep is aangemaakt.')
        return redirect('stageapp:view_scholen', id=id)
    #blank form
    context = {'form': form, 'sg': sg}
    return render(request, 'stageapp/create_school.html', context)

@login_required
def delete_school(request, id):
    """ Delete selected school """
    o = Scholen.objects.get(id=id)
    sg = ScholenGroep.objects.get(id = o.scholengroep_id)
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_scholen', id = sg.id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_school(request, id):
    """ Update/edit bestaande school """
    s = Scholen.objects.get(id=id)
    sg = ScholenGroep.objects.get(id=s.scholengroep_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ScholenForm(instance = s)
    else:
        # POST submitted, process data
        form = ScholenForm(instance = s, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:view_scholen', id = sg.id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'sg': sg, 'form': form, 's': s}
    return render(request, 'stageapp/edit_school.html', context)

"""Schooljaren"""
@login_required()
def view_schooljaren(request):
    """ Genereer een form met een overzicht van de schooljaren"""
    """ id = Scholengroep """
    sj = Schooljaren.objects.all()

    context = {'sj': sj}
    return render(request, 'stageapp/schooljaar_lijst.html', context)


@login_required
def create_schooljaar(request):
    """ Aanmaken nieuw schooljaar via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = SchooljaarForm()
    else:
        #POST submitted
        form = SchooljaarForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Scholengroep is aangemaakt.')
        return redirect('stageapp:view_schooljaren')
    #blank form
    context = {'form': form}
    return render(request, 'stageapp/create_schooljaar.html', context)

@login_required
def delete_schooljaar(request, id):
    """ Delete selected schooljaar """
    o = Schooljaren.objects.get(id=id)
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_schoojaren')
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_schooljaar(request, id):
    """ Update/edit bestaand schooljaar """
    sj = Schooljaren.objects.get(id=id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = SchooljaarForm(instance = sj)
    else:
        # POST submitted, process data
        form = SchooljaarForm(instance = sj, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:view_schooljaren') #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'sj': sj, 'form': form}
    return render(request, 'stageapp/edit_schooljaar.html', context)

"""Views voor klassen"""
@login_required()
def view_klassen(request, id):
    """ Genereer een form met een overzicht van de klassen voor de geselecteerde opleiding """
    """ id = opleiding    En een opleiding is dan weer gelinkt aan een school """
    opleiding =Opleidingen.objects.prefetch_related('klassen').get(id=id)
    klassen = opleiding.klassen.all()
    school = opleiding.scholen

    context = {'klassen': klassen, 'opleiding': opleiding, 'school': school}
    return render(request, 'stageapp/klassen_lijst.html', context)


@login_required
def create_klas(request, id):
    """Maak nieuwe klas aan voor de geselecteerde opleiding"""
    o = Opleidingen.objects.get(id=id)
    """ Aanmaken nieuwe klas via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = KlasForm()
        form.fields['opleidingen'].initial = id
    else:
        #POST submitted
        form = KlasForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Klas is aangemaakt.')
        return redirect('stageapp:view_klassen', id=id)
    #blank form
    context = {'form': form, 'opleiding': o}
    return render(request, 'stageapp/create_klas.html', context)

@login_required
def delete_klas(request, id):
    """ Delete selected klas """
    o = Klassen.objects.get(id=id)
    opleiding_id = o.opleidingen_id
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_klassen', id = opleiding_id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_klas(request, id):
    """ Update/edit bestaande klas """
    k = Klassen.objects.get(id=id)
    opleiding = Opleidingen.objects.get(id=k.opleidingen_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = KlasForm(instance = k)
    else:
        # POST submitted, process data
        form = KlasForm(instance = k, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            return redirect('stageapp:view_klassen', id = opleiding.id) #Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'klassen': k, 'form': form, 'opleiding': opleiding}
    return render(request, 'stageapp/edit_klas.html', context)

""" Views voor studenten """
@login_required()
def view_studenten(request, id):
    """ Genereer een form met een overzicht van de studenten voor de geselecteerde klas """
    """ id = klas  """
    klas =Klassen.objects.select_related('opleidingen').get(id=id)
    studenten = Studenten.objects.filter(klassen=klas).order_by('naam')
    opleiding = klas.opleidingen
    school = opleiding.scholen

    context = {'klas': klas, 'studenten': studenten, 'opleiding': opleiding, 'school':school}
    return render(request, 'stageapp/studenten_lijst.html', context)


@login_required
def create_student(request, id):
    """Maak nieuwe student aan voor de geselecteerde klas"""
    klas =Klassen.objects.select_related('opleidingen').get(id=id)
    opleiding = klas.opleidingen
    school = opleiding.scholen

    """ Aanmaken nieuwe student via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = StudentForm()
        form.fields['klassen'].initial = id
        form.fields['scholen'].initial = school
    else:
        #POST submitted
        form = StudentForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            form.save_m2m()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Student is aangemaakt.')
        return redirect('stageapp:view_studenten', id=id)
    #blank form
    context = {'form': form, 'klas': klas, 'opleiding': opleiding, 'school': school}
    return render(request, 'stageapp/create_student.html', context)

@login_required
def delete_student(request, id):
    """ Delete selected student """
    o = Studenten.objects.get(id=id)
    scholen_id = o.scholen_id
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_scholen', id = scholen_id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_student(request, id, id2):
    """ Update/edit bestaande student """
    """ klas_id is the parameter from which the view was accessed just to be able to return to the view from which the edit was initiated """
    student = Studenten.objects.get(id=id)
    school = Scholen.objects.get(id = student.scholen_id)
    sg = ScholenGroep.objects.get(id = school.scholengroep_id)
    klas = Klassen.objects.get(id = id2)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = StudentForm(instance = student)
    else:
        # POST submitted, process data
        form = StudentForm(instance = student, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            form.save_m2m()
            #return redirect('stageapp:view_scholen', id = sg.id) #Return to the view from which the request was launched
            return redirect('stageapp:view_studenten', id=id2)  # Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'student': student, 'form': form, 'school': school, 'sg': sg, 'klas': klas}
    return render(request, 'stageapp/edit_student.html', context)

""" Views voor leerkrachten """
@login_required()
def view_leerkrachten(request, id):
    """ Genereer een form met een overzicht van de leerkrachten voor de geselecteerde klas """
    """ id = klas  """
    klas =Klassen.objects.select_related('opleidingen').get(id=id)
    leerkrachten = Leerkrachten.objects.filter(klassen=klas).order_by('naam')
    opleiding = klas.opleidingen
    school = opleiding.scholen

    context = {'klas': klas, 'leerkrachten': leerkrachten, 'opleiding': opleiding, 'school':school}
    return render(request, 'stageapp/leerkrachten_lijst.html', context)


@login_required
def create_leerkracht(request, id):
    """Maak nieuwe leerkracht aan voor de geselecteerde klas"""
    klas =Klassen.objects.select_related('opleidingen').get(id=id)
    opleiding = klas.opleidingen
    school = opleiding.scholen

    """ Aanmaken nieuwe student via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = LeerkrachtForm()
        form.fields['klassen'].initial = id
        form.fields['scholen'].initial = school
    else:
        #POST submitted
        form = LeerkrachtForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            form.save_m2m()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Leerkacht is aangemaakt.')
        return redirect('stageapp:view_leerkrachten', id=id)
    #blank form
    context = {'form': form, 'klas': klas, 'opleiding': opleiding, 'school': school}
    return render(request, 'stageapp/create_leerkracht.html', context)

@login_required
def delete_leerkracht(request, id):
    """ Delete selected leerkracht """
    o = Leerkrachten.objects.get(id=id)
    scholen_id = o.scholen_id
    if request.method == 'POST':
        o.delete()
        return redirect('stageapp:view_scholen', id = scholen_id)
    context = {'obj': o} #The generic name obj allows to use the delete.html file to be used for all deletion instructions
    return render(request, 'stageapp/delete.html', context)

@login_required
def edit_leerkracht(request, id, id2):
    """ Update/edit bestaande leerkracht """
    """ klas_id is the parameter from which the view was accessed just to be able to return to the view from which the edit was initiated """
    leerkracht = Leerkrachten.objects.get(id=id)
    school = Scholen.objects.get(id = leerkracht.scholen_id)
    sg = ScholenGroep.objects.get(id = school.scholengroep_id)
    klas = Klassen.objects.get(id = id2)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = LeerkrachtForm(instance = leerkracht)
    else:
        # POST submitted, process data
        form = LeerkrachtForm(instance = leerkracht, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            form.save_m2m()
            #return redirect('stageapp:view_scholen', id = sg.id) #Return to the view from which the request was launched
            return redirect('stageapp:view_leerkrachten', id=id2)  # Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'leerkracht': leerkracht, 'form': form, 'school': school, 'sg': sg, 'klas': klas}
    return render(request, 'stageapp/edit_leerkracht.html', context)

"""Views voor leerkrachten maar dan vanuit de scholen views om te editeren """
@login_required()
def view_sch_leerkrachten(request, id):
    """ Genereer een form met een overzicht van de leerkrachten voor de geselecteerde school """
    """ id = SCHOOL  """
    school = Scholen.objects.get(id=id)
    sg = ScholenGroep.objects.get(id=school.scholengroep_id)
    leerkrachten = Leerkrachten.objects.filter(scholen_id=id).order_by('naam')

    context = {'leerkrachten': leerkrachten, 'school': school, 'sg': sg}
    return render(request, 'stageapp/sch_leerkrachten_lijst.html', context)


@login_required
def create_sch_leerkracht(request, id):
    """Maak nieuwe leerkracht aan voor de geselecteerde school"""
    school = Scholen.objects.get(id=id)
    sg = ScholenGroep.objects.get(id=school.scholengroep_id)

    """ Aanmaken nieuwe student via Crispy Forms based on ModelForm, hence, trying to save data via the model """
    if request.method != 'POST':
        #no data submitted
        form = LeerkrachtForm()
        form.fields['scholen'].initial = school
    else:
        #POST submitted
        form = LeerkrachtForm(data=request.POST)
        if form.is_valid():
            nieuwe_frm = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            nieuwe_frm.created_by = request.user
            nieuwe_frm.save()
            form.save_m2m()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Leerkacht is aangemaakt.')
        return redirect('stageapp:view_sch_leerkrachten', id=id)
    #blank form
    context = {'form': form, 'school': school, 'sg': sg}
    return render(request, 'stageapp/create_sch_leerkracht.html', context)

@login_required
def edit_sch_leerkracht(request, id, id2):
    """ Update/edit bestaande leerkracht """
    """ scholen_id is the parameter from which the view was accessed just to be able to return to the view from which the edit was initiated """
    leerkracht = Leerkrachten.objects.get(id=id)
    school = Scholen.objects.get(id = id2)
    sg = ScholenGroep.objects.get(id = school.scholengroep_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = LeerkrachtForm(instance = leerkracht)
    else:
        # POST submitted, process data
        form = LeerkrachtForm(instance = leerkracht, data=request.POST)
        if form.is_valid():
            updated_form = form.save(commit=False)
            # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
            updated_form.last_updated_by = User.objects.get(username=request.user).username  #This returns a model instance User.objects.get(username=request.user)
            updated_form.save()
            form.save_m2m()
            #return redirect('stageapp:view_scholen', id = sg.id) #Return to the view from which the request was launched
            return redirect('stageapp:view_sch_leerkrachten', id=id2)  # Return to the view from which the request was launched
        else:
            return HttpResponse(form.errors.values())  # Validation failed

    context = {'leerkracht': leerkracht, 'form': form, 'school': school, 'sg': sg}
    return render(request, 'stageapp/edit_sch_leerkracht.html', context)


"""Niet in gebruik"""

"""Werkt nog niet"""
class EvaluatieFormEditView(SingleObjectMixin, FormView):

    model = StageOpdrachtEvaluaties
    template_name = 'stageapp/evaluatietemplate_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=StageOpdrachtEvaluaties.objects.all())
        print(f"get {self.object} ")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=StageOpdrachtEvaluaties.objects.all())
        print(f"post  { self.object}")
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return EvaluatieFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        updated_form = form.save(commit=False)
        # Als hier bepaalde velden ingevuld moeten worden, bv de owner als het user model gebruikt wordt
        updated_form.created_by = self.request.user
        updated_form.last_updated_by = self.request.user  # This returns a model instance User.objects.get(username=request.user)

        updated_form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return True
        print("success")
        return reverse('stageapp:opdracht_evaluatie_edit', kwargs={'pk': self.object.pk})

""" NIET MEER IN GEBRUIK"""
@login_required
def stageopdrachten(request):
    """ Toon alle stageopdrachten """
    """ Zal niet meer gebruikt worden want te generiek"""
    so_en = StageOpdrachten.objects.all()
    context = {'so_en': so_en}
    return render(request, 'stageapp/stageopdrachten.html', context)
""" DEFINES URL  patterns for stageapp

URL configuration for stagetoolproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    3. Import static to access the uploaded attchments
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

#. means import from same directory as the urls.py file
from . import views

app_name = 'stageapp'

urlpatterns = [
    #home page
    path('', views.index, name = 'index'),
    path('bedrijfsgroepen/', views.BedrijvenGroepLijst.as_view(), name = 'lijst_bedrijfsgroepen'),
    path('bedrijvengroep_detail/<int:id>/', views.edit_bedrijvengroep, name='bedrijvengroep_detail'),
    path('delete_bedrijvengroep/<int:id>/', views.delete_bedrijvengroep, name='delete_bedrijvengroep'),
    path('nieuwe_bedrijvengroep/', views.BedrijvenGroepCreate, name='create_bedrijvengroep'),
    path('bedrijvengroep_alldata/<int:id>/', views.bedrijvengroep_alldata, name='bedrijvengroep_alldata'),
    path('vesting_detail/<int:id>/', views.edit_vesting, name='vesting_detail'),
    path('delete_vesting/<int:id>/', views.delete_vesting, name='delete_vesting'),
    path('nieuwe_vesting/<int:id>/', views.vestingCreate, name='create_vesting'),
    path('contactpersoon_detail/<int:id>/', views.edit_contactpersoon, name='contactpersoon_detail'),
    path('delete_contactpersoon/<int:id>/', views.delete_contactpersoon, name='delete_contactpersoon'),
    path('nieuwe_contactpersoon/<int:id>/', views.contactpersonencreate, name='create_contactpersoon'),
    path('contactpersonen/<int:id>/', views.contactpersonen_lijst, name='lijst_contactpersonen'),
    path('afdeling_detail/<int:id>/', views.edit_afdeling, name='afdeling_detail'),
    path('delete_afdeling/<int:id>/', views.delete_afdeling, name='delete_afdeling'),
    path('nieuwe_afdeling/<int:id>/', views.afdelingCreate, name='create_afdeling'),
    path('stageopdrachten/<int:id>/', views.stageopdrachten_lijst, name='lijst_stageopdrachten'),
    path('nieuwe_opdracht/<int:id>/', views.nieuwe_opdracht, name='nieuwe_opdracht'),
    path('edit_so/<int:so_id>/', views.edit_so, name='edit_so'),
    path('delete_so/<int:so_id>', views.delete_so, name='delete_so'),
    path('opdracht_evaluatie_assign_template/<int:id>/', views.evaluatietemplates_lijst, name='opdracht_assign_evaluatie_template'),
    path('view_evaluatie_template/<int:id>/', views.evaluatietemplate_details, name='view_evaluatie_template_details'),
    path('view_assign_evaluatie_templ_details/<int:id>/<int:id2>/', views.assign_template_details, name='assign_template_details'),
    path('opdracht_evaluatie/<int:id>/', views.view_opdracht_evaluatie, name='opdracht_evaluatie'),
    path('view_opdracht_evaluatie_criteria/<int:id>/', views.view_so_evaluatie_details, name='view_so_evaluatie_details'),
    path('edit_opdracht_evaluatie_criteria/<int:id>/', views.edit_opdracht_evaluatie_criteria, name='edit_opdracht_evaluatie_criteria'),
    path('delete_soe_criteria/<int:id>/', views.delete_soe_criteria, name='delete_soe_criteria'),
    path('view_scholengroepen/', views.ScholenGroepLijst.as_view(), name='view_scholengroepen'),
    path('edit_scholengroep/<int:id>/', views.edit_scholengroep, name='edit_scholengroep'),
    path('delete_scholengroep/<int:id>/', views.delete_scholengroep, name='delete_scholengroep'),
    path('create_scholengroep/', views.create_scholengroep, name='create_scholengroep'),
    path('view_scholen/<int:id>/', views.view_scholen, name='view_scholen'),
    path('edit_school/<int:id>/', views.edit_school, name='edit_school'),
    path('delete_school/<int:id>/', views.delete_school, name='delete_school'),
    path('create_school/<int:id>/', views.create_school, name='create_school'),
    path('view_so_calevents/<int:id>/', views.view_so_calevents,name='view_so_calevents'),
    path('edit_so_calevents/<int:id>/', views.edit_so_calevents,name='edit_so_calevents'),
    path('delete_so_calevents/<int:id>/', views.delete_so_calevents, name='delete_so_calevents'),
    path('create_so_calevents/<int:id>/', views.create_so_calevents, name='create_so_calevents'),
    path('edit_opleiding/<int:id>/', views.edit_opleiding, name='edit_opleiding'),
    path('delete_opleiding/<int:id>/', views.delete_opleiding, name='delete_opleiding'),
    path('view_opleidingen/<int:id>/', views.view_opleidingen, name='view_opleidingen'),
    path('create_opleiding/<int:id>/', views.create_opleiding, name='create_opleiding'),
    path('edit_schooljaar/<int:id>/', views.edit_schooljaar, name='edit_schooljaar'),
    path('delete_schooljaar/<int:id>/', views.delete_schooljaar, name='delete_schooljaar'),
    path('view_schooljaren/', views.view_schooljaren, name='view_schooljaren'),
    path('create_schooljaar/', views.create_schooljaar, name='create_schooljaar'),
    path('general_admin/', views.general_admin, name='general_admin'),
    path('view_klassen/<int:id>/', views.view_klassen, name='view_klassen'),
    path('edit_klas/<int:id>/', views.edit_klas, name='edit_klas'),
    path('delete_klas/<int:id>/', views.delete_klas, name='delete_klas'),
    path('create_klas/<int:id>/', views.create_klas, name='create_klas'),
    path('view_studenten/<int:id>/', views.view_studenten, name='view_studenten'),
    path('edit_student/<int:id>/<int:id2>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('create_student/<int:id>/', views.create_student, name='create_student'),
    #Next links are to check and edit data starting from the klasses views
    path('view_leerkrachten/<int:id>/', views.view_leerkrachten, name='view_leerkrachten'),
    path('edit_leerkracht/<int:id>/<int:id2>/', views.edit_leerkracht, name='edit_leerkracht'),
    path('delete_leerkracht/<int:id>/', views.delete_leerkracht, name='delete_leerkracht'),
    path('create_leerkracht/<int:id>/', views.create_leerkracht, name='create_leerkracht'),

    #In test
    path('create_soe_criteria/<int:id>/', views.create_soe_criteria, name='create_soe_criteria'),

    #Next links are to check and edit data starting from the scholen views
    path('view_sch_leerkrachten/<int:id>/', views.view_sch_leerkrachten, name='view_sch_leerkrachten'),
    path('edit_sch_leerkracht/<int:id>/<int:id2>/', views.edit_sch_leerkracht, name='edit_sch_leerkracht'),
    path('create_sch_leerkracht/<int:id>/', views.create_sch_leerkracht, name='create_sch_leerkracht'),



    # Werkt nog niet
    # path('opdracht_evaluatie/criteria_edit/<int:pk>', views.EvaluatieFormEditView.as_view(), name='opdracht_evaluatie_X'),



    #Test html
    path('test/', views.test, name = 'test'),

    #Niet meer in gebruik

    path('stageopdrachten/', views.stageopdrachten, name='stageopdrachten'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

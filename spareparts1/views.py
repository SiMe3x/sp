from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Lower
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from django.views.generic.list import ListView
from django.template.loader import render_to_string
from . import urls
from .models import Spare_part, Equipment, Belonging_equipment, Sup_emul, Import_from_excel
from django.db.models import Avg, Sum, Count, Value, Min, Max
from datetime import datetime
from django.core.paginator import Paginator




def index(request):
    print("hello")

    return render(request, 'spareparts1/dir_index/index.html')

def active_user_permis_def(request):
    active_user_permis = 0
    if request.user.groups.filter(name='Admin').exists():
        active_user_permis += 10
    if request.user.groups.filter(name='Tech').exists():
        active_user_permis += 10
    return (active_user_permis)

def user_loginnn(request):
    if (request.method == 'POST'):
        username = request.POST["username"] #'qwerty'  #
        password = request.POST["password"] # 'sfdfrrgfgdffsdf' #
        if (username != ''):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #print(user)
                #print(' Redirect to a success page.')
            else:
                print(" Return an 'invalid login' error message.")
        else:
            logout(request)

    if request.user.groups.filter(name__in =['Tech', 'Admin']).exists():
        print(request.user.username)
    #groups.filter(name__in=['Имя_группы_1', 'Имя_группы_2']).exists()
    #print(request.user.groups.filter(id='2').exists())
    #print(request.user.has_perm('eqipment.add_post'))
    #print(request.user.get_user_permissions())
    #print(Group.objects.get(name="техники").permissions.all())
    return render(request, 'spareparts1/user_login.html')

def findspareparts(request):
    #Spare_part_list = Spare_part.objects.all()[:10]
    #belonging_equipment_list = Belonging_equipment.objects.all()[:10]
    #sap_emul_list = Sup_emul.objects.all()[:10]
    sap_emul_list= 'null'
    if (request.method == 'POST') : 
        belonging_equipment_list = Belonging_equipment.objects.filter(
            belonging_equipment_key_equipment__specialty__icontains=request.POST['specialty_post'],
            belonging_equipment_key_equipment__work_process__icontains=request.POST['work_process_post'],
            belonging_equipment_key_equipment__model_equipment__icontains=request.POST['model_equipment_post'],
            belonging_equipment_key_equipment__node_equipment__icontains=request.POST['node_equipment_post'],
            belonging_equipment_key_spareparts__spare_part_name__icontains=request.POST['spare_part_name_post'],
            belonging_equipment_key_spareparts__type_part__icontains=request.POST['type_part_post'],
            belonging_equipment_key_spareparts__manufacturer__icontains=request.POST['manufacturer_post'],
            belonging_equipment_key_spareparts__criticality__icontains=request.POST['criticality_post'],
            belonging_equipment_key_spareparts__sap_Code1__icontains=request.POST['sap_Code1_post'],
            belonging_equipment_key_spareparts__sap_Code2__icontains=request.POST['sap_Code2_post'],

            belonging_equipment_key_spareparts__sap_analog__icontains=request.POST['sap_analog_post'],
            belonging_equipment_key_spareparts__for_order__icontains=request.POST['for_order_post']).exclude(
            belonging_equipment_key_equipment__node_equipment__icontains="00Все узлы")[:100]

    print(belonging_equipment_list.count())

    return render(request, 'spareparts1/dir_index/findspareparts.html', {'belonging_equipment_list': belonging_equipment_list, 'sap_emul_list':sap_emul_list})

def findresult(request):
    start_time = datetime.now()

    if (request.method == 'POST') : 
        belonging_equipment_list = Belonging_equipment.objects.filter(
            belonging_equipment_key_equipment__specialty__icontains=request.POST['specialty_post']).filter(
            belonging_equipment_key_equipment__work_process__icontains=request.POST['work_process_post']).filter(
            belonging_equipment_key_equipment__model_equipment__icontains=request.POST['model_equipment_post']).filter(
            belonging_equipment_key_equipment__node_equipment__icontains=request.POST['node_equipment_post']).filter(
            belonging_equipment_key_spareparts__spare_part_name__icontains=request.POST['spare_part_name_post']).filter(
            belonging_equipment_key_spareparts__type_part__icontains=request.POST['type_part_post']).filter(
            belonging_equipment_key_spareparts__manufacturer__icontains=request.POST['manufacturer_post']).filter(
            belonging_equipment_key_spareparts__criticality__icontains=request.POST['criticality_post']).filter(
            belonging_equipment_key_spareparts__sap_Code1__icontains=request.POST['sap_Code1_post']).filter(
            belonging_equipment_key_spareparts__sap_Code2__icontains=request.POST['sap_Code2_post']).filter(
            belonging_equipment_key_spareparts__sap_analog__icontains=request.POST['sap_analog_post']).filter(
            belonging_equipment_key_spareparts__for_order__icontains=request.POST['for_order_post']).distinct('belonging_equipment_key_spareparts__sap_Code1')[:10]

        
        sap_emul_list = Sup_emul.objects.filter(sap_code__in=[q.belonging_equipment_key_spareparts.sap_Code1 for q in belonging_equipment_list] + [q.belonging_equipment_key_spareparts.sap_Code2 for q in belonging_equipment_list] + [q.belonging_equipment_key_spareparts.sap_analog for q in belonging_equipment_list])
        
    print(datetime.now() - start_time)
    return render(request, 'spareparts1/dir_index/findresult.html', {'belonging_equipment_list': belonging_equipment_list, 'sap_emul_list':sap_emul_list})

def beedit(request):    #кажется не используется, убраз из урлов
    #belonging_equipment_edit = Belonging_equipment.objects.all()[:10]
    try:
        
        belonging_equipment_edit=Belonging_equipment.objects.all()[:1]
        list_specialty=Equipment.objects.all().distinct('specialty')
        list_work_process=Equipment.objects.all().distinct('work_process')
        list_model_equipment=Equipment.objects.all().distinct('model_equipment')
        list_node_equipment=Equipment.objects.all().distinct('node_equipment')
        print(list_work_process)

        if (request.method == 'POST'):

            if (request.POST['form_save']):
                #belonging_equipment_edit = Belonging_equipment.objects.filter(id=(request.POST['form_save']))
                belonging_equipment_edit = Belonging_equipment.objects.filter(id = request.POST['form_save'])

                case_specialty = Belonging_equipment.objects.values_list('belonging_equipment_key_equipment__specialty', flat=True).distinct('belonging_equipment_key_equipment__specialty').get(id = request.POST['form_save'])
                case_work_process = Belonging_equipment.objects.values_list('belonging_equipment_key_equipment__work_process', flat=True).distinct('belonging_equipment_key_equipment__work_process').get(id = request.POST['form_save'])
                case_model_equipment = Belonging_equipment.objects.values_list('belonging_equipment_key_equipment__model_equipment', flat=True).distinct('belonging_equipment_key_equipment__model_equipment').get(id = request.POST['form_save'])
                case_node_equipment = Belonging_equipment.objects.values_list('belonging_equipment_key_equipment__node_equipment', flat=True).distinct('belonging_equipment_key_equipment__node_equipment').get(id = request.POST['form_save'])

                list_model_equipment=Equipment.objects.filter(work_process = case_work_process).distinct('model_equipment')
                list_node_equipment=Equipment.objects.filter(work_process = case_work_process,model_equipment = case_model_equipment).distinct('node_equipment')

                spare_part_name_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__spare_part_name', flat=True).distinct('belonging_equipment_key_spareparts__spare_part_name').get(id = request.POST['form_save'])
                type_part_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__type_part', flat=True).distinct('belonging_equipment_key_spareparts__type_part').get(id = request.POST['form_save'])
                manufacturer_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__manufacturer', flat=True).distinct('belonging_equipment_key_spareparts__manufacturer').get(id = request.POST['form_save'])
                criticality_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__criticality', flat=True).distinct('belonging_equipment_key_spareparts__criticality').get(id = request.POST['form_save'])
                sap_Code1_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__sap_Code1', flat=True).distinct('belonging_equipment_key_spareparts__sap_Code1').get(id = request.POST['form_save'])
                sap_Code2_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__sap_Code2', flat=True).distinct('belonging_equipment_key_spareparts__sap_Code2').get(id = request.POST['form_save'])
                sap_analog_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__sap_analog', flat=True).distinct('belonging_equipment_key_spareparts__sap_analog').get(id = request.POST['form_save'])
                min_count_edit = Belonging_equipment.objects.values_list('min_count', flat=True).distinct('min_count').get(id = request.POST['form_save'])
                max_count_edit = Belonging_equipment.objects.values_list('max_count', flat=True).distinct('max_count').get(id = request.POST['form_save'])
                for_order_edit = Belonging_equipment.objects.values_list('belonging_equipment_key_spareparts__for_order', flat=True).distinct('belonging_equipment_key_spareparts__for_order').get(id = request.POST['form_save'])

            else:

                case_specialty=Equipment.objects.values_list('specialty', flat=True).distinct('specialty').get(specialty = request.POST['filter_specialty'])
                case_work_process = Equipment.objects.values_list('work_process', flat=True).distinct('work_process').get(work_process = request.POST['filter_work_process'])
                case_model_equipment = Equipment.objects.values_list('model_equipment', flat=True).distinct('model_equipment').get(model_equipment = request.POST['filter_model_equipment'])
                case_node_equipment = Equipment.objects.values_list('node_equipment', flat=True).distinct('node_equipment').get(node_equipment = request.POST['filter_node_equipment'])
                

                list_model_equipment=Equipment.objects.filter(work_process = case_work_process).distinct('model_equipment')
                list_node_equipment=Equipment.objects.filter(work_process = case_work_process, model_equipment = case_model_equipment).distinct('node_equipment')
                print(list_node_equipment)
                if not list_node_equipment :
                    list_node_equipment = Equipment.objects.filter(node_equipment='-').distinct('node_equipment')

                spare_part_name_edit = request.POST['spare_part_name_edit']
                type_part_edit = request.POST['type_part_edit']
                manufacturer_edit = request.POST['manufacturer_edit']
                criticality_edit = request.POST['criticality_edit']
                sap_Code1_edit = request.POST['sap_Code1_edit']
                sap_Code2_edit = request.POST['sap_Code2_edit']
                sap_analog_edit = request.POST['sap_analog_edit']
                min_count_edit = request.POST['min_count_edit']
                max_count_edit = request.POST['max_count_edit']
                for_order_edit = request.POST['for_order_edit']

            
        else:
            HttpResponse("<h2>page not found</h2>")
    except Belonging_equipment.DoesNotExist:
        return HttpResponseNotFound("<h2>page not found</h2>")
    #return HttpResponse(belonging_equipment_edit)
    return render(request, 'spareparts1/beedit.html', {
        'belonging_equipment_edit': belonging_equipment_edit,
        'list_specialty':list_specialty,
        'case_specialty':case_specialty, 
        'list_work_process':list_work_process, 
        'case_work_process':case_work_process,
        'list_model_equipment':list_model_equipment, 
        'case_model_equipment':case_model_equipment,
        'list_node_equipment':list_node_equipment,
        'case_node_equipment':case_node_equipment,
        'spare_part_name_edit':spare_part_name_edit,
        'type_part_edit':type_part_edit,
        'manufacturer_edit':manufacturer_edit,
        'criticality_edit':criticality_edit,
        'sap_Code1_edit':sap_Code1_edit,
        'sap_Code2_edit':sap_Code2_edit,
        'sap_analog_edit':sap_analog_edit,
        'min_count_edit':min_count_edit,
        'max_count_edit':max_count_edit,
        'for_order_edit':for_order_edit
        
        })




def detail(request, spare_part_name_id):
    try:
        belonging_equipment_list = Spare_part.objects.get(pk=spare_part_name_id)
        #belonging_equipment_list = Belonging_equipment.belonging_equipment_key_spareparts.spare_part_name.text('Теплообменник')
    except Spare_part.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'spareparts1/detail.html', {'spare_part_name_id': spare_part_name_id,'belonging_equipment_list': belonging_equipment_list})



def import_from_excel(request):
    import_list = Import_from_excel.objects.all()#[:100]
    imp_count_test=0

    for importing in import_list:        
#Импорт оборудования и узла
    #Механик/Электрик
        if (importing.meh_el_imp == ''): impspecialty = 0 
        else: impspecialty = importing.meh_el_imp.capitalize() 
    #Процесс
        if (importing.proc_imp == ''): impwork_process = 0 
        else: impwork_process = importing.proc_imp.capitalize()
    #Модель оборудования    
        if (importing.model_obor_imp == ''): impmodel_equipment = 0 
        else: impmodel_equipment = importing.model_obor_imp.capitalize()
    #Узел       
        if (importing.uzel_imp == ''): impnode_equipment = 0 
        else: impnode_equipment = importing.uzel_imp.capitalize()
    #Уровень критичности оборудования
        if (importing.kritichnost_obor_imp == None): impcategory = 0 
        else: impcategory = importing.kritichnost_obor_imp



        b = Equipment.objects.get_or_create(specialty = impspecialty, work_process = impwork_process, model_equipment = impmodel_equipment, node_equipment = impnode_equipment, start_index = False)
        if Equipment.objects.filter(specialty = impspecialty, work_process = impwork_process, model_equipment = impmodel_equipment, start_index=True).count()==0:
            Equipment.objects.get_or_create(specialty = impspecialty, work_process = impwork_process, model_equipment = impmodel_equipment, node_equipment="00Все узлы", start_index=True, category = impcategory)
        Equipment.objects.filter(specialty = impspecialty, work_process = impwork_process, model_equipment = impmodel_equipment, node_equipment = impnode_equipment).update(category = impcategory)
        #print(b)

#Импорт запчасти
    #Импорт SAP Кодов
        #Если нет сап кода присваиваем условный код для корректности работы
        impsap_Code1=importing.sup_imp
        if (importing.sup_imp == None):
            if (Spare_part.objects.filter(type_part=importing.tip_imp)):
                impsap_Code1=Spare_part.objects.filter(type_part=importing.tip_imp)[0].sap_Code1



            #    print ('!!!', impsap_Code1)
            #    print(importing.tip_imp)
            #    print(Spare_part.objects.filter(type_part=importing.tip_imp)[0])
            #    print("@@@@@@@@@@@@")

            else:
                #print('@@@')
                if Spare_part.objects.filter(sap_Code1=990000000):
                    impsap_Code1=Spare_part.objects.all().aggregate(Max('sap_Code1'))['sap_Code1__max'] + 1
                else:                
                    impsap_Code1=990000000                
        
            
        #Проверяем по сап коду создана ли деталь, если нет создаем            
        if Spare_part.objects.filter(sap_Code1=impsap_Code1):
            #print(impsap_Code1)
            c = Spare_part.objects.get_or_create(sap_Code1=impsap_Code1)
            #print('repeat')
            #print(c[0].id)
        else:
            #impsap_Code1 = importing.sup_imp
            if (importing.analog_imp == None): impsap_Code2 = 0 
            else: impsap_Code2 = importing.analog_imp
            if (importing.alt_sup_imp == None): impsap_Code3 = 0 
            else: impsap_Code3 = importing.alt_sup_imp        
        #Наименование
            if (importing.naimen_imp == ''): impspare_part_name = 0 
            else: impspare_part_name = importing.naimen_imp 
        #Тип
            if (importing.tip_imp == ''): imptype_part = 0 
            else: imptype_part = importing.tip_imp 
        #Производитель
            if (importing.proizv_imp == ''): impmanufacturer = 0 
            else: impmanufacturer = importing.proizv_imp 
        #Срок поставки           
            if (importing.srok_postavki_imp == ''): impdelivery_time = 90 
            else: impdelivery_time = importing.srok_postavki_imp 
            c = Spare_part.objects.get_or_create(spare_part_name=impspare_part_name, type_part=imptype_part, manufacturer=impmanufacturer, delivery_time=impdelivery_time, sap_Code1=impsap_Code1, sap_Code2=impsap_Code2, sap_analog=impsap_Code3, was_moderated=False )


    #Создаем связку запчасти и оборудования
        #if 
    #Критичность запчасти для оборудования
        if (importing.kritichnost_zapch_imp == None): impcriticality = 0 
        else: impcriticality = importing.kritichnost_zapch_imp


    #Мин/макс для оборудования
        if (importing.min_imp == None): impmin_count = 0 
        else: impmin_count = importing.min_imp
        if (importing.max_imp == None): impmax_count = 0 
        else: impmax_count = importing.max_imp

    #Суммарно на узле
        if (importing.summ_kol_imp == None): impin_node_count = 0 
        else: impin_node_count = importing.summ_kol_imp



        d = Belonging_equipment.objects.get_or_create(belonging_equipment_key_spareparts=Spare_part.objects.get(id=c[0].id), belonging_equipment_key_equipment=Equipment.objects.get(id=b[0].id), criticality=impcriticality, min_count=impmin_count, max_count=impmax_count, in_node_count=impin_node_count)
        #print(Spare_part.objects.get(id=c[0].id))
#####___Обновляем общее количество 

        list_spare_parts = Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=impspecialty,
                                                      belonging_equipment_key_equipment__work_process=impwork_process,
                                                      belonging_equipment_key_equipment__model_equipment=impmodel_equipment,
                                                      belonging_equipment_key_spareparts__id=c[0].id,
                                                      belonging_equipment_key_equipment__start_index=False
                                                      ).aggregate(Max('criticality'), Min('min_count'), Max('max_count'), Sum('in_node_count'))
        if Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=impspecialty,
                                                      belonging_equipment_key_equipment__work_process=impwork_process,
                                                      belonging_equipment_key_equipment__model_equipment=impmodel_equipment,
                                                      belonging_equipment_key_spareparts__id=c[0].id,
                                                      belonging_equipment_key_equipment__start_index=True):
            Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=impspecialty,
                                                      belonging_equipment_key_equipment__work_process=impwork_process,
                                                      belonging_equipment_key_equipment__model_equipment=impmodel_equipment,
                                                      belonging_equipment_key_spareparts__id=c[0].id,
                                                      belonging_equipment_key_equipment__start_index=True).update(criticality=list_spare_parts['criticality__max'], min_count=list_spare_parts['min_count__min'], max_count=list_spare_parts['max_count__max'], in_node_count=list_spare_parts['in_node_count__sum'])
        else:
            equipment_start_index=Equipment.objects.get(specialty=impspecialty,
                                                        work_process=impwork_process,
                                                        model_equipment=impmodel_equipment,                                          
                                                        start_index=True).id
            Belonging_equipment.objects.create(belonging_equipment_key_spareparts=Spare_part.objects.get(id=c[0].id),
                                               belonging_equipment_key_equipment=Equipment.objects.get(id=equipment_start_index),
                                               criticality=list_spare_parts['criticality__max'], 
                                               min_count=list_spare_parts['min_count__min'], 
                                               max_count=list_spare_parts['max_count__max'], 
                                               in_node_count=list_spare_parts['in_node_count__sum'])
        





        #print(d)
        #print(b[0].id, c[0].id, d[0].id)
        
        Import_from_excel.objects.filter(id=importing.id).delete()
        #print(importing.id)
        imp_count_test+=1
        #print(imp_count_test)

    
    for update_count_list in Spare_part.objects.all():#filter(sap_Code1__lt = 990000000):

        #print(update_count_list.sap_Code1)

        #обновляем общее количество в списке запчастей из САП 
        #Строим минимумы 
        #Строим максимумы        
        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(sap_count_total = Sup_emul.objects.filter(sap_code = update_count_list.sap_Code1).aggregate(Sum('sap_count'))['sap_count__sum'], 
                                                                                  min_count = Belonging_equipment.objects.filter(belonging_equipment_key_spareparts__sap_Code1 = update_count_list.sap_Code1).aggregate(Min('min_count'))['min_count__min'],
                                                                                  max_count = Belonging_equipment.objects.filter(belonging_equipment_key_spareparts__sap_Code1 = update_count_list.sap_Code1).aggregate(Max('max_count'))['max_count__max'],
                                                                                  criticality = Belonging_equipment.objects.filter(belonging_equipment_key_spareparts__sap_Code1 = update_count_list.sap_Code1).aggregate(Max('criticality'))['criticality__max'])
        cc = Spare_part.objects.get(sap_Code1=update_count_list.sap_Code1)
        if type(cc.sap_count_total)==int and (cc.min_count>cc.sap_count_total) :
            ca=cc.max_count - cc.sap_count_total
            if ca<0: ca = 0
            
        else:
            ca=0
        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(for_order=ca)
        
 





        #print(type(update_count_list.min_count))
        #if (type(update_count_list.min_count) == int) and (type(update_count_list.sap_count_total) == int): 
        #    if (update_count_list.min_count > update_count_list.sap_count_total) and (update_count_list.max_count > 0): 
        #        #print(update_count_list.min_count, "@@@", update_count_list.sap_count_total )
        #        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(for_order=update_count_list.max_count - update_count_list.sap_count_total)
                
        #    else:
        #        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(for_order=0)
                #if (update_count_list.min_count > update_count_list.sap_count_total):
                #    print("!!!")
        #else:
        #    if update_count_list.max_count > 0:
        #        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(for_order=None)
        #    else:
        #        Spare_part.objects.filter(sap_Code1 = update_count_list.sap_Code1).update(for_order=0)
        #print(update_count_list.sap_Code1, "@@@", update_count_list.min_count, "@@@", update_count_list.sap_count_total, "@@@", update_count_list.for_order)
        #print(update_count_list.sap_count_total)
        #print(Belonging_equipment.objects.filter(belonging_equipment_key_spareparts__sap_Code1 = update_count_list.sap_Code1).aggregate(Min('min_count'))['min_count__min'])

        #print(belonging_equipment_key_equipment__specialty, belonging_equipment_key_equipment__work_process, belonging_equipment_key_equipment__model_equipment, belonging_equipment_key_equipment__node_equipment)


        #belonging_equipment_key_equipment__specialty__icontains = import_list.meh_el_imp

 #   print("start connection")
 #   client = Client('http://10.195.100.23/TestWcf/Service.svc?wsdl')
 #   print(client)
 #
 #  result = client.service.GetDataUsingDataContract("Hello", 2)
 #   print(result)   
 #
 #   print("end connection")
    return HttpResponse()


def listspareparts(request):
    
    #list_spare_part = Spare_part.objects.exclude(for_order = 0)
    #list_spare_partt = Spare_part.objects.all().order_by('-id')[1890:2000]#.annotate(qwe = Value(123))
    #list_spare_part = Spare_part.objects.all().order_by('-id')[1890:2000].annotate(qwe = Sum(123))
    #list_spare_partt  = Sup_emul.objects.filter(sap_code__in = ([q.sap_Code1 for q in list_spare_part])).values('sap_code')
    #print(list_spare_partt)
    #list_spare_part = Spare_part.objects.all().order_by('-id')[1890:2000].annotate(qwe = Value(list_spare_part))
    #print(list_spare_parttt)
    #list_spare_part = Spare_part.objects.all().order_by('-id')[1800:2000]
    #list_sup_count = Sup_emul.objects.filter(sap_code__in=([q.sap_Code1 for q in list_spare_part]))
    active_user_permis = active_user_permis_def(request)
    
    return render(request, 'spareparts1/dir_listspareparts/listspareparts.html',
                  {'active_user_permis': active_user_permis})


def listsparepartsdata(request):    
    list_spare_part = Spare_part.objects.all().order_by('id')[1800:2000]#.annotate(qwe = Value(123))
    #list_spare_part = Spare_part.objects.all()[:100]
    #print(request.POST['checked_count'])

    
#фильтр для выбора деталей необходимых к заказу 
    if request.POST['for_order_post'] == 'true':
        rrr=1 
    else: 
        rrr=0
##Замороченый фильтр для выпадающего списка "минимум проверен"        
    if request.POST['checked_count_post'] == '2':
        a=b=0        
    elif request.POST['checked_count_post'] == '3':
        a=b=1        
    else:
        a=1
        b=0

    #иначе не работает без icontains, а с ним захватывает лишнее
    if request.POST['delivery_time_post'] != '':
        delivery_time_post_x = delivery_time_post_y= request.POST['delivery_time_post']

    else:
        delivery_time_post_y = 0
        delivery_time_post_x=10000


    list_spare_part = Spare_part.objects.filter((Q(checked_count=a) | Q(checked_count=b)),
                                                spare_part_name__icontains=request.POST['spare_part_name_post'], 
                                                type_part__icontains=request.POST['type_part_post'],
                                                manufacturer__icontains=request.POST['manufacturer_post'],
                                                sap_Code1__icontains=request.POST['sap_Code1_post'],
                                                sap_Code2__icontains=request.POST['sap_Code2_post'],
                                                sap_analog__icontains=request.POST['sap_analog_post'],
                                                delivery_time__range=(delivery_time_post_y,delivery_time_post_x),
                                                criticality__icontains=request.POST['criticality_post'],
                                                min_count__icontains=request.POST['min_count_post'],
                                                max_count__icontains=request.POST['max_count_post'],
                                                sap_count_total__icontains=request.POST['sap_count_total_post'],
                                                for_order__gte=rrr
                                                )[:200]
    

    return render(request, 'spareparts1/dir_listspareparts/listsparepartsdata.html', {'list_spare_part': list_spare_part})



def listsparepartsadd(request):
    spare_part_name_add=''
    type_part_add=''
    manufacturer_add=''
    sap_Code1_add=''
    sap_Code2_add=''
    sap_analog_add=''
    delivery_time_add=''

    if (request.method == 'POST') and (request.POST['actionsp']=='addsp'):
        #print("yyy")
        if (Spare_part.objects.filter(sap_Code1=request.POST['sap_Code1_add'])):
            print(request.POST['sap_Code1_add'])
            spare_part_name_add=request.POST['spare_part_name_add']
            type_part_add=request.POST['type_part_add']
            manufacturer_add=request.POST['manufacturer_add']
            sap_Code1_add=request.POST['sap_Code1_add']
            sap_Code2_add=request.POST['sap_Code2_add']
            sap_analog_add=request.POST['sap_analog_add']
            delivery_time_add=request.POST['delivery_time_add']
            operation_status="Данный сап код уже существует"
        else:
            operation_status="отправлено на модерацию " + request.POST['spare_part_name_add'] +" " + request.POST['type_part_add']   +" " + request.POST['manufacturer_add']  +" " + request.POST['sap_Code1_add'] +" " + request.POST['sap_Code2_add'] +" " + request.POST['sap_analog_add']#"Успешно отправлено на модерацию"+ spare_part_name_add
            if request.POST['sap_Code2_add'].isnumeric(): sap_Code2_add=request.POST['sap_Code2_add']
            else: sap_Code2_add=None
            if request.POST['sap_analog_add'].isnumeric(): sap_analog_add=request.POST['sap_analog_add']
            else: sap_analog_add=None
            Spare_part.objects.get_or_create(spare_part_name=request.POST['spare_part_name_add'], type_part=request.POST['type_part_add'], manufacturer=request.POST['manufacturer_add'], sap_Code1=request.POST['sap_Code1_add'], sap_Code2=sap_Code2_add, sap_analog=sap_analog_add, delivery_time=request.POST['delivery_time_add'], criticality="4", min_count="0",max_count="0", checked_count=False, sap_count_total="0", for_order=False, was_moderated=False )
            spare_part_name_add=""
            type_part_add=""
            manufacturer_add=""
            sap_Code1_add=""
            sap_Code2_add=""
            sap_analog_add=""
            
            print("eee")
    elif (request.method == 'POST') and (request.POST['actionsp']=='editsp'):
        #print(Spare_part.objects.get(id=request.POST['id_post_edit']).id, Spare_part.objects.get(id=request.POST['id_post_edit']))
        Spare_part.objects.filter(id=request.POST['id_post_edit']).update(spare_part_name=request.POST['spare_part_name_edit'],
                                                                       type_part=request.POST['type_part_post_edit'], 
                                                                       manufacturer=request.POST['manufacturer_post_edit'], 
                                                                       sap_Code1=request.POST['sap_Code1_post_edit'], 
                                                                       sap_Code2=request.POST['sap_Code2_post_edit'], 
                                                                       sap_analog=request.POST['sap_analog_post_edit'],
                                                                       delivery_time=request.POST['delivery_time_post_edit'], 
                                                                       criticality="4", 
                                                                       min_count="0",
                                                                       max_count="0", 
                                                                       checked_count=False, 
                                                                       sap_count_total="0", 
                                                                       for_order=False, 
                                                                       was_moderated=False )
        
        print(request.POST['spare_part_name_edit'])
        print(request.POST['type_part_post_edit'])
        print(request.POST['manufacturer_post_edit'])
        print(request.POST['sap_Code1_post_edit'])
        print(request.POST['sap_Code2_post_edit'])
        print(request.POST['sap_analog_post_edit'])

        operation_status="X3"
    else:

        operation_status="insert data"
        print("eee")
    return render(request, 'spareparts1/dir_listspareparts/listsparepartsadd.html',{
        'spare_part_name_add':spare_part_name_add,
        'type_part_add':type_part_add,
        'manufacturer_add':manufacturer_add,
        'sap_Code1_add':sap_Code1_add,
        'sap_Code2_add':sap_Code2_add,
        'sap_analog_add':sap_analog_add,
        'operation_status':operation_status
        })


def listequipment(request):
    start_time = datetime.now()
    if (request.method == 'POST'):
        #case_specialty = Belonging_equipment.objects.values_list('belonging_equipment_key_equipment__specialty', flat=True).distinct('belonging_equipment_key_equipment__specialty').get(id = request.POST['form_save'])
        lst_specialty=Equipment.objects.distinct('specialty')
        list_specialty=sorted(lst_specialty, key= lambda t: t.specialty, reverse=False)
        case_specialty=request.POST['filter_specialty']

        
        lst_work_process=lst_specialty.filter(specialty = case_specialty).distinct('work_process')
        list_work_process=sorted(lst_work_process, key= lambda t: t.work_process, reverse=False)
        try:
            case_work_process= request.POST['filter_work_process']
        except Exception as e:
            case_work_process=''
        lst_model_equipment=lst_work_process.filter(work_process = case_work_process).distinct('model_equipment')
        list_model_equipment=sorted(lst_model_equipment, key= lambda t: t.model_equipment, reverse=False)        
        try:
            case_model_equipment= request.POST['filter_model_equipment']
        except Exception as e:
            case_model_equipment=''
        lst_node_equipment=lst_model_equipment.filter(model_equipment = case_model_equipment).distinct('node_equipment')
        list_node_equipment=sorted(lst_node_equipment, key= lambda t: t.start_index, reverse=True)
        try:
            case_node_equipment=request.POST['filter_node_equipment']
        except Exception as e:
            case_node_equipment=''


    else:
        

        lst_specialty=Equipment.objects.distinct('specialty')
        list_specialty=sorted(lst_specialty, key= lambda t: t.specialty, reverse=False)
        case_specialty=list_specialty[0].specialty

        lst_work_process=lst_specialty.filter(specialty = case_specialty).distinct('work_process')
        list_work_process=sorted(lst_work_process, key= lambda t: t.work_process, reverse=False)
        case_work_process=list_work_process[0].work_process

        lst_model_equipment=lst_work_process.filter(work_process = case_work_process).distinct('model_equipment')
        list_model_equipment=sorted(lst_model_equipment, key= lambda t: t.model_equipment, reverse=False)
        case_model_equipment=list_model_equipment[0].model_equipment


        lst_node_equipment=lst_model_equipment.filter(model_equipment = case_model_equipment).distinct('node_equipment')
        list_node_equipment=sorted(lst_node_equipment, key= lambda t: t.start_index, reverse=True)
        case_node_equipment=list_node_equipment[0].node_equipment

        
    try:
        editing = Equipment.objects.filter(specialty = case_specialty, work_process = case_work_process, model_equipment = case_model_equipment, node_equipment=case_node_equipment)
        category = editing.values_list('category', flat=True)[0]
        count_model_equipment = editing.values_list('count_model_equipment', flat=True)[0]
        editing = editing.values_list('pk', flat=True)[0]
        
    except:
        category = count_model_equipment = editing=''

    
    try:
        list_spare_parts=Belonging_equipment.objects.filter(belonging_equipment_key_equipment = editing)
        #print(list_spare_parts.values_list('id'))
    except:
        list_spare_parts=''

    try:        
        start_index = Equipment.objects.get(id=editing).start_index
    except:
        start_index=True



    print(datetime.now() - start_time)

    active_user_permis=active_user_permis_def(request)

    return render(request, 'spareparts1/dir_listeqipment/listequipment.html', {
        'list_specialty':list_specialty,
        'case_specialty':case_specialty, 
        'list_work_process':list_work_process, 
        'case_work_process':case_work_process,
        'list_model_equipment':list_model_equipment, 
        'case_model_equipment':case_model_equipment,
        'list_node_equipment':list_node_equipment,
        'case_node_equipment':case_node_equipment,
        'editing':editing,
        'list_spare_parts':list_spare_parts,
        'start_index': start_index,
        'category': category,
        'count_model_equipment':count_model_equipment,
        'active_user_permis':active_user_permis
        })


def fororder(request):
    start_time = datetime.now()
    fororder = Spare_part.objects.exclude(for_order = 0).exclude(for_order = None).order_by('-checked_count', '-criticality')#[:100]
    #fororder=Paginator(fororderrr, 11).page(1)

    
    print(datetime.now() - start_time)  
    return render(request, 'spareparts1/dir_fororder/fororder.html', {'fororder': fororder})




def addequipment(request):
    start_time = datetime.now()
    case_specialty=request.POST['filter_specialty']
    case_work_process= request.POST['filter_work_process']
    case_model_equipment= request.POST['filter_model_equipment']
    case_node_equipment=request.POST['filter_node_equipment']
    case_count_model_equipment=request.POST['filter_count_model_equipment']
    print(case_count_model_equipment)
    actionnn=request.POST['actionnn']
    
    


    if actionnn=='1':
        #add equipment
        
        if Equipment.objects.filter(specialty=case_specialty, work_process=case_work_process, model_equipment=case_model_equipment, start_index=True).count()==0:
            Equipment.objects.get_or_create(specialty=case_specialty, work_process=case_work_process, model_equipment=case_model_equipment, node_equipment="00Все узлы", start_index=True)
        Equipment.objects.get_or_create(specialty=case_specialty, work_process=case_work_process, model_equipment=case_model_equipment, node_equipment=case_node_equipment)
        
    elif actionnn=='2':
        #edit equipment
        
        #print(before_update[0].specialty)
        #print(Equipment.objects.filter(specialty=before_update[0].specialty, work_process = before_update[0].work_process))
        
        #Equipment.objects.filter(specialty=case_specialty, work_process = case_work_process, model_equipment = case_model_equipment).update(specialty = case_specialty, work_process = case_work_process, model_equipment = case_model_equipment, node_equipment=case_node_equipment)
        try:            
            a=Equipment.objects.filter(pk=request.POST['editing'])[0].specialty
            b=Equipment.objects.filter(pk=request.POST['editing'])[0].work_process
            c=Equipment.objects.filter(pk=request.POST['editing'])[0].model_equipment
#ОПТИМИЗИРОВАТЬ!!!!!!!!!!! ППЦ сколько лишних запросов
            #обновляем кскадно      специальность, процесс, модель
            Equipment.objects.filter(specialty=a, work_process = b, model_equipment = c).update(specialty = case_specialty, work_process = case_work_process, model_equipment = case_model_equipment, count_model_equipment = case_count_model_equipment)
            # обновляем кскадно     специальность, процесс
            Equipment.objects.filter(specialty=a, work_process = b).update(specialty = case_specialty, work_process = case_work_process)
            # обновляем кскадно     специальность
            Equipment.objects.filter(specialty=a).update(specialty = case_specialty)
            # обновляем целевую запись
            Equipment.objects.filter(pk=request.POST['editing']).update(specialty = case_specialty, work_process = case_work_process, model_equipment = case_model_equipment, node_equipment=case_node_equipment)            

        except:
            print('UPSsss')

        print('2222000' + request.POST['actionnn'])

    elif actionnn=='3':
        #delete equipment
        try:
            Equipment.objects.filter(pk=request.POST['editing']).delete()
            #prorabotat monitoring udalenuya
        except:
            print('3333000' + request.POST['actionnn'])
    else:
        #unknown action
        print('000000' + request.POST['actionnn'])

    print(datetime.now() - start_time) 
    return render(request, 'spareparts1/addequipment.html', {
    
    'case_specialty':case_specialty, 
    
    'case_work_process':case_work_process,
    
    'case_model_equipment':case_model_equipment,
    
    'case_node_equipment':case_node_equipment,
    })

def addbe(request):
    actionnn=request.POST['actionnn']
    a = Belonging_equipment.objects.get(id=request.POST['BEid'])
    if actionnn=='1':
        #edit 
        Belonging_equipment.objects.filter(id=request.POST['BEid']).update(criticality=request.POST['criticality'], min_count=request.POST['min_count'], max_count=request.POST['max_count'], in_node_count=request.POST['in_node_count'])
        
        list_spare_parts = Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=a.belonging_equipment_key_equipment.specialty,
                                                 belonging_equipment_key_equipment__work_process=a.belonging_equipment_key_equipment.work_process,
                                                 belonging_equipment_key_equipment__model_equipment=a.belonging_equipment_key_equipment.model_equipment,
                                                 belonging_equipment_key_spareparts__id=a.belonging_equipment_key_spareparts.id,
                                                 belonging_equipment_key_equipment__start_index=False
                                                 ).aggregate(Max('criticality'), Min('min_count'), Max('max_count'), Sum('in_node_count'))
        Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=a.belonging_equipment_key_equipment.specialty,
                                           belonging_equipment_key_equipment__work_process=a.belonging_equipment_key_equipment.work_process,
                                           belonging_equipment_key_equipment__model_equipment=a.belonging_equipment_key_equipment.model_equipment,
                                           belonging_equipment_key_spareparts__id=a.belonging_equipment_key_spareparts.id,
                                           belonging_equipment_key_equipment__start_index=True
                                           ).update(criticality=list_spare_parts['criticality__max'], min_count=list_spare_parts['min_count__min'], max_count=list_spare_parts['max_count__max'], in_node_count=list_spare_parts['in_node_count__sum'])
         

    elif actionnn=='2':
        #delete         
        Belonging_equipment.objects.filter(id=request.POST['BEid']).delete()

        b =Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=a.belonging_equipment_key_equipment.specialty,
                                         belonging_equipment_key_equipment__work_process=a.belonging_equipment_key_equipment.work_process,
                                         belonging_equipment_key_equipment__model_equipment=a.belonging_equipment_key_equipment.model_equipment,
                                         belonging_equipment_key_spareparts__id=a.belonging_equipment_key_spareparts.id,
                                         belonging_equipment_key_equipment__start_index=False
                                         ).count()
        if b==0:
            Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=a.belonging_equipment_key_equipment.specialty,
                                         belonging_equipment_key_equipment__work_process=a.belonging_equipment_key_equipment.work_process,
                                         belonging_equipment_key_equipment__model_equipment=a.belonging_equipment_key_equipment.model_equipment,
                                         belonging_equipment_key_spareparts__id=a.belonging_equipment_key_spareparts.id,
                                         belonging_equipment_key_equipment__start_index=True
                                         ).delete()
        else:
            Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=a.belonging_equipment_key_equipment.specialty,
                                           belonging_equipment_key_equipment__work_process=a.belonging_equipment_key_equipment.work_process,
                                           belonging_equipment_key_equipment__model_equipment=a.belonging_equipment_key_equipment.model_equipment,
                                           belonging_equipment_key_spareparts__id=a.belonging_equipment_key_spareparts.id,
                                           belonging_equipment_key_equipment__start_index=True
                                           ).update(criticality=list_spare_parts['criticality__max'], min_count=list_spare_parts['min_count__min'], max_count=list_spare_parts['max_count__max'], in_node_count=list_spare_parts['in_node_count__sum'])
         




        #print(actionnn)
    else:
        print('qqqqqq')
    
    editing=request.POST['actionnn']
    return render(request, 'spareparts1/dir_listeqipment/listequipment.html', {
        'editing':editing

        })

def addsparepart(request):
    editing=request.POST['editing']
    
    if (request.POST['aaa']=='1'):
        list_spare_parts=Spare_part.objects.all()[:20]
    elif (request.POST['aaa']=='2'):
        list_spare_parts=Spare_part.objects.filter(
            spare_part_name__icontains=request.POST['spare_part_name_post'],
            type_part__icontains=request.POST['type_part_post'],
            manufacturer__icontains=request.POST['manufacturer_post']).filter(
            sap_Code1__icontains = request.POST['sap_Code1_post'],
            sap_Code2__icontains=request.POST['sap_Code2_post'],
            sap_analog__icontains=request.POST['sap_analog_post'])
    elif (request.POST['aaa']=='3'):
        print(request.POST['aaa'])
    else:
        print('oops')
    print(request.POST['aaa'])    
    return render(request, 'spareparts1/dir_listeqipment/addsparepart.html', {
        'editing':editing,
        'list_spare_parts': list_spare_parts

        })
def addsptoeq(request):
    #try:
     #   Belonging_equipment.objects.filter(belonging_equipment_key_spareparts=request.POST['key_sp_post'], belonging_equipment_key_equipment=request.POST['key_eq_post'])[0]
    #except:
    #print(request.POST['key_sp_post'])
    #print(request.POST['key_eq_post'])
    #print(request.POST['in_node_count'])
    #print(Spare_part.objects.get(id=request.POST['key_sp_post']).id)
    #print(Belonging_equipment.objects.filter(belonging_equipment_key_equipment=request.POST['key_eq_post']))


    #Проверям существует ли создаваемая связка запчасти и станка, если нет то создаем
    if Belonging_equipment.objects.filter(belonging_equipment_key_spareparts=Spare_part.objects.get(id=request.POST['key_sp_post']),belonging_equipment_key_equipment=Equipment.objects.get(id=request.POST['key_eq_post'])):
        print('object exist')
    else:
        Belonging_equipment.objects.create(belonging_equipment_key_spareparts=Spare_part.objects.get(id=request.POST['key_sp_post']),
            belonging_equipment_key_equipment=Equipment.objects.get(id=request.POST['key_eq_post']),
            criticality=request.POST['criticality_post'],
            min_count=request.POST['min_count_post'],
            max_count=request.POST['max_count_post'],
            in_node_count=request.POST['in_node_count']
            )
        print('ok')

    start_time = datetime.now()

    #берем данные об оборудовании из скрытых списков полученых при загрузке страницы, которые пользователь не может менять
    list_spare_parts = Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=request.POST['hfilter_specialty'],
                                                          belonging_equipment_key_equipment__work_process=request.POST['hfilter_work_process'],
                                                          belonging_equipment_key_equipment__model_equipment=request.POST['hfilter_model_equipment'],
                                                          belonging_equipment_key_spareparts__id=request.POST['key_sp_post'],
                                                          belonging_equipment_key_equipment__start_index=False
                                                          ).aggregate(Max('criticality'), Min('min_count'), Max('max_count'), Sum('in_node_count'))
    #Проверяем созданоли общее поле для всех узлов, и изменяем имеющиеся при наличии иначе создаем новое и вносим данные
    if Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=request.POST['hfilter_specialty'],
                                          belonging_equipment_key_equipment__work_process=request.POST['hfilter_work_process'],
                                          belonging_equipment_key_equipment__model_equipment=request.POST['hfilter_model_equipment'],
                                          belonging_equipment_key_spareparts__id=request.POST['key_sp_post'],
                                          belonging_equipment_key_equipment__start_index=True):

        Belonging_equipment.objects.filter(belonging_equipment_key_equipment__specialty=request.POST['hfilter_specialty'],
                                           belonging_equipment_key_equipment__work_process=request.POST['hfilter_work_process'],
                                           belonging_equipment_key_equipment__model_equipment=request.POST['hfilter_model_equipment'],
                                           belonging_equipment_key_spareparts__id=request.POST['key_sp_post'],
                                           belonging_equipment_key_equipment__start_index=True
                                           ).update(criticality=list_spare_parts['criticality__max'], min_count=list_spare_parts['min_count__min'], max_count=list_spare_parts['max_count__max'], in_node_count=list_spare_parts['in_node_count__sum'])

        print('est takaya zapchast*********************')
    else:
        equipment_start_index=Equipment.objects.get(specialty=request.POST['hfilter_specialty'],
                                                    work_process=request.POST['hfilter_work_process'],
                                                    model_equipment=request.POST['hfilter_model_equipment'],                                          
                                                    start_index=True).id
        Belonging_equipment.objects.create(belonging_equipment_key_spareparts=Spare_part.objects.get(id=request.POST['key_sp_post']),
                                           belonging_equipment_key_equipment=Equipment.objects.get(id=equipment_start_index),
                                           criticality=list_spare_parts['criticality__max'], 
                                           min_count=list_spare_parts['min_count__min'], 
                                           max_count=list_spare_parts['max_count__max'], 
                                           in_node_count=list_spare_parts['in_node_count__sum'])


        print('net zapchasty*******************************')




    print(datetime.now() - start_time)  
    print('__________________________________________________________')
    print(list_spare_parts)
    #print(list_spare_parts1)
 






    print('__________________________________________________________')
    print(list_spare_parts['in_node_count__sum'])
    return HttpResponse(status=200)

def spdetail(request):
    print(request.POST['Spare_part.id'])
    spare_part=Spare_part.objects.get(id=request.POST['Spare_part.id'])
    list_spare_parts=Belonging_equipment.objects.filter(belonging_equipment_key_spareparts=Spare_part.objects.get(id=request.POST['Spare_part.id'])).order_by('-belonging_equipment_key_equipment__model_equipment','-belonging_equipment_key_equipment__start_index').exclude(belonging_equipment_key_equipment__node_equipment="00Все узлы")
    print(list_spare_parts)
    
    return render(request, 'spareparts1/dir_listspareparts/spdetail.html',{ 'list_spare_parts': list_spare_parts, 'spare_part': spare_part})

def detalesbe(request):
    start_time = datetime.now()

    list_spare_parts = Belonging_equipment.objects.filter(belonging_equipment_key_spareparts=Belonging_equipment.objects.filter(id=request.POST['BEid'])[0].belonging_equipment_key_spareparts,
                                                         belonging_equipment_key_equipment__specialty=Belonging_equipment.objects.filter(id=request.POST['BEid'])[0].belonging_equipment_key_equipment.specialty,
                                                         belonging_equipment_key_equipment__work_process=Belonging_equipment.objects.filter(id=request.POST['BEid'])[0].belonging_equipment_key_equipment.work_process,
                                                         belonging_equipment_key_equipment__model_equipment=Belonging_equipment.objects.filter(id=request.POST['BEid'])[0].belonging_equipment_key_equipment.model_equipment
                                                         ).order_by('-belonging_equipment_key_equipment__start_index')
    print(datetime.now() - start_time)
    print(request.POST['BEid'])
    print(list_spare_parts)
    print(list_spare_parts.aggregate(Sum('in_node_count'))['in_node_count__sum'])
    print(list_spare_parts)
    return render(request, 'spareparts1/dir_listeqipment/detalesbe.html',{ 'list_spare_parts': list_spare_parts})

def for_moderation(request):
    print()
    return render(request, 'spareparts1/for_moderation/for_moderation.html',{})


def categories(request):
    a=Equipment.objects.distinct('work_process', 'model_equipment')
    #print(Equipment.objects.distinct('work_process', 'model_equipment').count())
    return render(request, 'spareparts1/dir_categories/categories.html',{'a':a})
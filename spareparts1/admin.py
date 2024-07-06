from django.contrib import admin
from .models import Belonging_equipment, Spare_part, Equipment, Sup_emul, Import_from_excel



#admin.site.register(Belonging_equipment)
@admin.register(Spare_part)
class Spare_partAdmin(admin.ModelAdmin):
    list_display = ('spare_part_name', 'type_part','manufacturer','sap_Code1')

    
@admin.register(Import_from_excel)
class Import_from_excel(admin.ModelAdmin):
	list_display = ('sup_imp','analog_imp','localiz_imp','alt_sup_imp','naimen_imp','tip_imp','proc_imp','model_obor_imp','uzel_imp','edin_izm_imp','summ_kol_imp','min_imp','max_imp','ver_polomki_imp','kritichnost_obor_imp','obshiy_krit_imp','meh_el_imp')




#admin.site.register(Equipment)
@admin.register(Equipment)
class Equipment(admin.ModelAdmin):
    list_display = ('specialty', 'work_process','model_equipment','node_equipment')

@admin.register(Sup_emul)
class Sup_emul(admin.ModelAdmin):
	list_display = ('sap_code', 'sap_name','sap_warehouse','sap_end_point','sap_count')


class Belonging_equipment(admin.ModelAdmin):
	list_display= ('id', 'belonging_equipment_key_spareparts', 'belonging_equipment_key_equipment')




# Register your models here.

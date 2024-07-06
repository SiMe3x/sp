from django.db import models
#import django_tables2 as tables



class Spare_part(models.Model):	
	spare_part_name = models.CharField(max_length=150, default="")	#Статическое значение
	type_part = models.CharField(max_length=189, default="")		#Статическое значение
	manufacturer = models.CharField(max_length=90, default="")		#Статическое значение
	criticality = models.PositiveSmallIntegerField(default=0)		#Вычисляемое значение
	delivery_time = models.PositiveIntegerField(null="true")		#Статическое значение
	sap_Code1 = models.PositiveIntegerField(default="0")			#Статическое значение
	sap_Code2 = models.PositiveIntegerField(default="0", blank=True, null=True) 		#Статическое значение
	sap_analog = models.PositiveIntegerField(default="0", blank=True, null=True)		#Статическое значение
	min_count = models.PositiveIntegerField(default=0)				#Вычисляемое значение
	max_count = models.PositiveIntegerField(default=0)				#Вычисляемое значение
	checked_count = models.BooleanField(default=False)				#Статическое значение
	for_order = models.PositiveIntegerField(default=0, null="true") #Вычисляемое значение
	sap_count_total = models.PositiveIntegerField(default=0, null="true")#Вычисляемое значение
	was_moderated = models.BooleanField(default=False)				#Статическое значение

	def __str__(self):
		return f"{self.spare_part_name}, {self.manufacturer},{self.type_part}"






class Equipment(models.Model):
	specialty = models.CharField(max_length=10)						#Статическое значение ##Специальность
	work_process = models.CharField(max_length=50)					#Статическое значение ##Рабочий процесс
	model_equipment = models.CharField(max_length=50)				#Статическое значение ##Модель оборудования
	node_equipment = models.CharField(max_length=291)				#Статическое значение ##Узел оборудования
	start_index = models.BooleanField(default=False)				#Вычисляемое значение ##Стартовый индекс, определяет поле с суммарной информацией по оборудованию
	category = models.PositiveIntegerField(default=0)				#Статическое значение ##Каткгория оборудования
	count_model_equipment=models.PositiveIntegerField(default=1)	#Статическое значение ##Количество единиц оборудования 

	def __str__(self):
		return f"{self.specialty},{self.work_process},{self.model_equipment},{self.node_equipment},{self.start_index}"

class Belonging_equipment(models.Model):
	belonging_equipment_key_spareparts = models.ForeignKey(Spare_part, on_delete=models.CASCADE)
	belonging_equipment_key_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
	criticality = models.PositiveSmallIntegerField(default=0)			#Статическое значение
	min_count = models.PositiveIntegerField(default=0)			#Статическое значение
	max_count = models.PositiveIntegerField(default=0)			#Статическое значение
	in_node_count = models.PositiveIntegerField(default=0)			#Статическое значение
	on_model_count = models.PositiveIntegerField(default=0)			#Вычисляемое значение
	

	def __str__(self):
		return f"{self.id},{self.belonging_equipment_key_spareparts},{self.belonging_equipment_key_equipment}"




class Sup_emul(models.Model):
	sap_code = models.PositiveIntegerField(blank="true")
	sap_name = models.CharField(max_length=90, blank="true")
	sap_warehouse = models.CharField(max_length=90,blank="true")
	sap_end_point = models.CharField(max_length=90, blank="true")
	sap_count = models.PositiveIntegerField(blank="true")
	sap_unit = models.CharField(max_length=90, blank="true")
	sap_price = models.PositiveIntegerField(blank="true")
	sap_currency = models.CharField(max_length=90, blank="true")
	
	def __str__(self):
		return f"{self.sap_code},{self.sap_name},{self.sap_count}"

class Import_from_excel(models.Model):
	#number_imp = models.PositiveIntegerField(null="true")
	sup_imp = models.PositiveIntegerField(null="true")
	analog_imp = models.PositiveIntegerField(null="true")
	localiz_imp = models.CharField(max_length=10, null="true")
	alt_sup_imp = models.PositiveIntegerField(null="true")
	naimen_imp = models.CharField(max_length=150, null="true") #long values
	tip_imp = models.CharField(max_length=189, null="true") #long values
	proizv_imp = models.CharField(max_length=90, null="true")
	proc_imp = models.CharField(max_length=90, null="true")
	model_obor_imp = models.CharField(max_length=90, null="true")
	uzel_imp = models.CharField(max_length=291, null="true") #long values
	edin_izm_imp = models.CharField(max_length=11, null="true")
	summ_kol_imp = models.PositiveIntegerField(null="true")
	min_imp = models.PositiveIntegerField(null="true")
	max_imp = models.PositiveIntegerField(null="true")
	ver_polomki_imp = models.PositiveIntegerField(null="true")
	kritichnost_obor_imp = models.PositiveIntegerField(null="true")
	obshiy_krit_imp = models.PositiveIntegerField(null="true")
	meh_el_imp = models.CharField(max_length=10, null="true")
	kritichnost_zapch_imp = models.PositiveIntegerField(null="true")
	srok_postavki_imp = models.PositiveIntegerField(null="true")


#SAP код	Наименование	Склад	Место	Количество	Единица изм	Стоимость за единицу	Валюта
#1186432	ДАТЧИК E2E-X5F1	LRUB	BB3-3-3	3	шт	910,71	RUB




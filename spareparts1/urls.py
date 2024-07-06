from django.urls import path
#from spareparts1.views import PersonListView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('findspareparts/', views.findspareparts, name='findspareparts'),
    path('user_login/', views.user_loginnn, name='user_login'),
    path('findresult/', views.findresult, name='findresult'),
    #path('beedit/', views.beedit, name='beedit'),
    path('addbe/', views.addbe, name='addbe'),
    path('importfromexcel/', views.import_from_excel, name='import_from_excel'),
    path('listspareparts/', views.listspareparts, name='listspareparts'),
    path('listspareparts/listsparepartsdata/', views.listsparepartsdata, name='listsparepartsdata'),
    path('listspareparts/add/', views.listsparepartsadd, name='listsparepartsadd'),
    path('listspareparts/listsparepartsdata/spdetail/', views.spdetail, name='spdetail'),    
    path('listequipment/', views.listequipment, name='listequipment'),
    path('categories/', views.categories, name='categories'),
    path('detalesbe/', views.detalesbe, name='detalesbe'),
    path('addequipment/', views.addequipment, name='addequipment'),
    path('addsparepart/', views.addsparepart, name='addsparepart'),
    path('addsptoeq/', views.addsptoeq, name='addsptoeq'),
    path('fororder/', views.fororder, name='fororder'),
    path('for_moderation/', views.for_moderation, name='for_moderation'),
    path('<int:spare_part_name_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:name_temp_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:name_temp_id>/vote/', views.vote, name='vote'),
    #path("spare_part/", PersonListView.as_view()),

]


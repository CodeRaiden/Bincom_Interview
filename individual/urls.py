from django.urls import path
from . import views

urlpatterns = [
 path('', views.individual_result, name='individual'),
 path('summed/', views.summed_total, name='summed'),
 path('summedresult/', views.summed_total, name='summed'),
 path('addparty/', views.add_party, name='addparty'),
 path('allpuresult/', views.all_results, name='allpuresult'),
 path('pollresults/', views.all_results, name='pollresults'),
]
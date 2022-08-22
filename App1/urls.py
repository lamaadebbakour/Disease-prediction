from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from App1 import views
urlpatterns=[
  
   url(r'Sick/$',views.sickApi),
   url(r'Sick/([0-9]+)$',views.sickApi),

   url(r'Docktur/$',views.DocApi),
   url(r'Docktur/([0-9]+)$',csrf_exempt(views.DocApi)),


   url(r'Diseases/$',views.DisApi),
   url(r'Diseases/([0-9]+)$',csrf_exempt(views.DisApi)),


   url(r'Recommender/$',views.RecommenderAPI),
   url(r'Recommender/([0-9]+)$',csrf_exempt(views.RecommenderAPI)),


]
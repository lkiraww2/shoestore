from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from shop import views 
from rest_framework import routers
from paypal.standard.ipn.views import ipn

# from shop.views import Shoeviews

# router = routers.DefaultRouter()
# router.register(r'Shoe', Shoeviews)
urlpatterns=[
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('shoe',views.Shoe_list,name='Shoe'),
    path('shoes',views.add_shoe,name='add_shoe'),
    path('payment_success/',views.payment_success,name='payment_success'),
    path('create_payment_intent/',views.create_payment_intent,name='create_payment_intent'),
    path('payment/',views.payment,name='payment'),
    path('paypal-ipn/', ipn, name='paypal-ipn'),
   path('payment_error/', views.payment_error, name='payment_error'),
      
    # path('api/',views.apiApplication,name='apiApplication'),
    # path('api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
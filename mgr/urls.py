from django.urls import path
from mgr import customer,sign_in_out,img

urlpatterns=[
  
    path('customers',customer.dispatcher),
    path('signin',sign_in_out.signin),
    path('signout',sign_in_out.signout),
    path('img',img.imgc),
   
    
]

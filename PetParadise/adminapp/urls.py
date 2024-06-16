from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path("checksignup",views.checksignup,name="checksignup"),
    path("checklogin", views.checklogin, name="checklogin"),
    path("checkchangepassword",views.checkchangepassword,name="checkchangepassword"),
    path("logincheckchangepassword",views.logincheckchangepassword,name="logincheckchangepassword"),
    path("loginadmincheckchangepassword",views.loginadmincheckchangepassword,name="loginadmincheckchangepassword"),
    path('addtocart/<str:item_name>/<int:item_cost>/', views.addtocart, name='addtocart'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


hello

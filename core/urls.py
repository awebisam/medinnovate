from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/profile/', views.profile, name='profile'),
    path("about/", views.about, name="about"),
    path("docform/27hs782h278ns782h278h287n7H77J&Jshfhafndjbdhjbndbkhjb?ks=dd/",
         views.doctorform, name="doctorform"),
    path('profileform/djnjdnejsjsjhbkyuswbcbvfjyebviubewb72t367dw3jhbhwc?ks=pp',
         views.personform, name="personform"),
    path("doctors/", views.doctors, name="doctors")
]

"""
URL configuration for Kurssi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import tuotelistaview, toimittajalistaview, tuotteet_filtered
from .views import lisäätoimittaja, lisäätuote, tuotepoisto, vahvistatuotepoisto
from .views import edit_tuote_get, edit_tuote_post, etsitoimittaja
from .views import loginview, login_action, logout_action

# syntaksi: Mikä osoite polku: '' sovelluksen juuri: landingview (renderöidään landingview). App kansion sisältä, view tiedostosta importataan landingview
urlpatterns = [
  
    # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

     # Tuote url´s
    path('tuotteet/', tuotelistaview),
    path('lisää-tuote/', lisäätuote),
    path('poista-tuote/<int:id>/', tuotepoisto),
    path('vahvista-tuote-poisto/<int:id>/', vahvistatuotepoisto),
    path('edit-tuote-get/<int:id>/', edit_tuote_get),
    path('edit-tuote-post/<int:id>/', edit_tuote_post),
    path('tuote-toimittajan-mukaan/<int:id>/', tuotteet_filtered),

    # Toimittaja url´s
    path('toimittajat/', toimittajalistaview),
    path('lisää-toimittaja/', lisäätoimittaja),
    path('etsi-toimittaja/', etsitoimittaja),

]
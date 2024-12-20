# Render = Renderöidään tietty html templates kansiosta
# Redirect = Ohjataan ohjelman suoritus johonkin toiseen view functioon
from django.shortcuts import render, redirect
from .models import Toimittaja, Tuote
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# Loginpage
def loginview(request):
    return render (request, "loginpage.html")


# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'paasivu.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# 'Request' on views näkymä funktioiden ensimmäinen parametri minkä ottavat vastaan

# Tuote views
def tuotelistaview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        tuotelista = Tuote.objects.all()
        toimittajalista = Toimittaja.objects.all()
        context = {'tuotteet': tuotelista, 'toimittajat': toimittajalista}
        return render (request,"tuotelista.html",context)


def lisäätuote(request):
    a = request.POST['tuotenimi']
    b = request.POST['painoperkappale']
    c = request.POST['kappalehinta']
    d = request.POST['tuotteitavarastossa']
    e = request.POST['toimittaja']
    
    Tuote(tuotenimi = a, painoperkappale = b, kappalehinta = c, tuotteitavarastossa = d, toimittaja = Toimittaja.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def vahvistatuotepoisto(request, id):
    tuote = Tuote.objects.get(id = id)
    context = {'tuote': tuote}
    return render (request,"tuotepoisto.html",context)


def tuotepoisto(request, id):
    Tuote.objects.get(id = id).delete()
    return redirect(tuotelistaview)


def edit_tuote_get(request, id):
        tuote = Tuote.objects.get(id = id)
        context = {'tuote': tuote}
        return render (request,"edit_tuote.html",context)


def edit_tuote_post(request, id):
        item = Tuote.objects.get(id = id)
        item.kappalehinta = request.POST['kappalehinta']
        item.tuotteitavarastossa = request.POST['tuotteitavarastossa']
        item.save()
        return redirect(tuotelistaview)


def tuotteet_filtered(request, id):
    tuotelista = Tuote.objects.all()
    filteredtuotteet = tuotelista.filter(toimittaja = id)
    context = {'tuotteet': tuotteet_filtered}
    return render (request,"tuotelista.html",context)



# Toimittaja views
def toimittajalistaview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        toimittajalista = Toimittaja.objects.all()
        context = {'toimittajat': toimittajalista}
        return render (request,"toimittajalista.html",context)


def lisäätoimittaja(request):
    a = request.POST['yritysnimi']
    b = request.POST['yhteyshenkiö']
    c = request.POST['osoite']
    d = request.POST['puhelin']
    e = request.POST['sähköposti']
    f = request.POST['maa']
    Toimittaja(yritysnimi = a, yhteyshenkiö = b, osoite = c, puhelin = d, sähköposti = e, maa = f).save()
    return redirect(request.META['HTTP_REFERER'])


def etsitoimittaja(request):
    search = request.POST['search']
    filtered = Toimittaja.objects.filter(yritysnimi__icontains=search)
    context = {'toimittajat': filtered}
    return render (request,"toimittajalista.html",context)
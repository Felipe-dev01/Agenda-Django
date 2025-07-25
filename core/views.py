from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.

# def index(request):
#    return redirect('/agenda/')

def cadastrar_user(request):
    return render(request, 'user.html')

def submit_cadastrar_user(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        #? Verifica se o usuário existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "O Username já existe")
            return redirect("/cadastro")
    
        #? Verifica se o email existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "O Email já existe")
            return redirect("/cadastro")
        
        #? Cria Usuário
        else:
            User.objects.create_user(
                username = username,
                email = email,
                password = password,
            )
            
    return redirect('/')



def login_user(request):
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/")


def submit_login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("/")
        else:
            messages.error(request, "Usuário ou Senha Inválidos")
            
    return redirect("/")


@login_required(login_url="/login/")
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)

    #! Busca todas os eventos com datas maiores que a atual 
    #? __gt = maiores que!
    #? __lt = menor que!
    evento = Evento.objects.filter(usuario = usuario, data_evento__gt=data_atual)
    dados = {"eventos": evento}
    return render(request, "agenda.html", dados)


@login_required(login_url="/login/")
def evento(request):
    id_evento = request.GET.get("id")
    dados = {}
    if id_evento:
        dados["evento"] = Evento.objects.get(id=id_evento)
        
    return render(request, "evento.html", dados)


@login_required(login_url="/login/")
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get("titulo")
        data_evento = request.POST.get("data_evento")
        descricao = request.POST.get("descricao")
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        
        if id_evento:
            
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
        else:
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario
            )
    return redirect("/")


@login_required(login_url="/login/")
def delete_evento(request, id_evento):
    usuario = request.user

    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    
    if usuario == evento.usuario:
        evento.delete()
        
    else:
        raise Http404()
        
    return redirect("/")

#! Fazendo uma função como se fosse uma API Externa
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario = usuario).values('id', 'titulo')
    dados = {"eventos": evento}
    return JsonResponse(list(evento), safe=False)


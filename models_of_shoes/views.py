from django.shortcuts import render, redirect, get_object_or_404
from .models import Models_of_shoes, Arhiv
from .forms import Models_shoesForm, SizeForm, ArticulForm, ArhivForm
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required

class ShoesDetailView(DetailView):
    model = Models_of_shoes
    template_name_suffix = '_detail'

@login_required(login_url='/auth/login/')
def index(request):
    templ = 'models_of_shoes/index.html'
    objs = Models_of_shoes.objects.select_related('season','sclad')
    print(objs)
    paginator = Paginator(objs, 10)
    ph_number = request.GET.get('page')
    page_obj = paginator.get_page(ph_number)
    context = {'page_obj': page_obj}
    return render(request, templ, context)


# Create your views here.
@login_required(login_url='/auth/login/')
@permission_required('models_of_shoes.add_models_of_shoes', raise_exception=True)
def add(request):
    form = Models_shoesForm(request.POST or None)
    templ = 'models_of_shoes/model_shoes.html'
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('models_of_shoes:index')
    return render(request, templ, context)

@login_required(login_url='/auth/login/')
@permission_required('models_of_shoes.change_models_of_shoes', raise_exception=True)
def edit(request, pk):
    instance = get_object_or_404(Models_of_shoes, id=pk)
    print(instance)
    form = Models_shoesForm(request.POST or None, instance=instance)
    context = {'form': form}
    templ = 'models_of_shoes/model_shoes.html'
    if form.is_valid():
        form.save()
        return redirect('models_of_shoes:index')
    return render(request, templ, context)


def models_of_shoes(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Models_of_shoes, id=pk)
    else:
        instance = None
    form = Models_shoesForm(request.POST or None, instance=instance)
    context = {'form': form}
    templ = 'models_of_shoes/model_shoes.html'
    if form.is_valid():
        form.save()
        return redirect('models_of_shoes:index')
    return render(request, templ, context)

@login_required(login_url='/auth/login/')
@permission_required('models_of_shoes.delete_models_of_shoes', raise_exception=True)
def delete_model(request, pk):
    instance = get_object_or_404(Models_of_shoes, id=pk)
    form = Models_shoesForm(instance=instance)
    context = {'form': form}
    templ = 'models_of_shoes/model_shoes.html'
    if request.method == 'POST':
        Arhiv.objects.create(
            articul=instance.articul,
            model_s=instance.model_s,
            color=instance.color,
            short=instance.short,
            sex=instance.sex,
            size_f=instance.size_f,
            size_r=instance.size_r,
            season=instance.season,
            amount=instance.amount,
            sclad=instance.sclad,
            picture=instance.picture,
            picture_2=instance.picture_2


        )


        instance.delete()
        return redirect('models_of_shoes:index')
    return render(request, templ, context)


def find_articul(request):
    templ = 'models_of_shoes/find.html'
    form = ArticulForm(request.GET or None)
    context = {'form': form}
    if form.is_valid():
        print('form.is_valid()')
        objs = Models_of_shoes.objects.filter(articul=request.GET.get('articul'))
        templ = 'models_of_shoes/index.html'
        context = {'page_obj': objs}
        return render(request, templ, context)
    return render(request, templ, context)


def find_size(request):
    templ = 'models_of_shoes/find.html'
    form = SizeForm(request.GET or None)
    context = {'form': form}
    if form.is_valid():
        print('form.is_valid()')
        objs = Models_of_shoes.objects.filter(size_r=request.GET.get('size'))
        templ = 'models_of_shoes/index.html'
        context = {'page_obj': objs }
        return render(request, templ, context)
    return render(request, templ, context)


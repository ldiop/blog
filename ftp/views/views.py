from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..forms.forms import TuserForms
from ..models.models import T_user
from ..filters import T_userFilter
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

@login_required(login_url='acceslogin')
def index(request):
    ftpuser_list = T_user.objects.all()
    filter = T_userFilter(request.GET, queryset=ftpuser_list)
    ftpuser_list = filter.qs
    paginator = Paginator(ftpuser_list, 12)
    page = request.GET.get('page')
    ftpuser = paginator.get_page(page)
    return render(request, 'index.html',{'comptes':ftpuser, 'filter':filter})

@login_required(login_url='acceslogin')
def t_user_detail(request, pk):
    userdetail = get_object_or_404(T_user,pk=pk)
    context = { 'userdetail':userdetail}
    return render(request, 'ftp_detail.html',context)

@login_required(login_url='acceslogin')
def t_user_add(request):
    form = TuserForms()
    if request.method == "POST":
        form = TuserForms(request.POST)
        if form.is_valid():
            new_ftp = form.save()
            messages.success(request, 'Nouveau compte FTP ' + new_ftp.ftpUsername + ' ' + new_ftp.societe)
            context = {'userdetail': new_ftp}
            return render(request, 'ftp_detail.html', context)
        else:
            messages.error(request, "Error")

    context = {'form': form}
    return render(request, 'ftp_ajout.html', context)



@login_required(login_url='acceslogin')
def t_user_edit(request, pk):
    tuser = get_object_or_404(T_user, pk=pk)
    if request.method == "POST":
        form = TuserForms(request.POST, instance=tuser)
        if form.is_valid():
            tuser = form.save(commit=False)
            tuser.save()
            return redirect('t_user_detail', pk=tuser.pk)
    else:
        form = TuserForms(instance=tuser)
    return render(request, 'ftp_ajout.html', {'form': form})



@login_required(login_url='acceslogin')
def t_user_delete(request, pk):
    tuserdel = T_user.objects.get(pk=pk)
    if request.method == 'POST':
        tuserdel.delete()
        return redirect('/')
    context = {'item':tuserdel}
    return render(request, 'ftp_delete.html', context)

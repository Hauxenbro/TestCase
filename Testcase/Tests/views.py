from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout, get_user
import django_filters
from .models import Cards, Status, History
from .forms import AddCard, AddUser, LoginUser, EditForm


class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Cards
        fields = ['seria', 'number', 'creation_date', 'finish_date', 'status']


class CardsList(ListView):
    model = Cards
    template_name = 'Tests/cards.html'
    context_object_name = 'cards'

    def get_queryset(self):
        f = CardFilter(self.request.GET, queryset=Cards.objects.all())
        return f


class CardView(DetailView):
    model = Cards
    pk_url_kwarg = 'card_id'
    template_name = 'Tests/card.html'
    context_object_name = 'card'


class AddCard(CreateView):
    form_class = AddCard
    template_name = 'Tests/add_card.html'


def history(request, pk):
    model = History.objects.filter(card_id=pk)
    template_name = 'Tests/history.html'
    return render(request, 'Tests/history.html', {'history': model})


def activate_card(request, pk):
    try:
        card = Cards.objects.get(pk=pk)
        if card.status != Status.objects.get(pk=2):
            card.status = Status.objects.get(pk=2)
            card.save()
        return redirect('home')
    except Cards.DoesNotExist:
        return render(request, 'Tests/nocard.html')


def delete_card(request, pk):
    try:
        card = Cards.objects.get(pk=pk)
        card.delete()
        return redirect('home')
    except Cards.DoesNotExist:
        return render(request, 'Tests/nocard.html')


def registrate_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = AddUser()
    return render(request, 'Tests/registr.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUser()
    return render(request, 'Tests/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

def change(request, pk):
    try:
        card = Cards.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditForm(data=request.POST)
            if form.is_valid():
                card.seria = request.POST.get('seria')
                card.number = request.POST.get('number')
                card.finish_date = request.POST.get('finish_date')
                card.save()
                return redirect('home')
        else:
            form = EditForm(data={
                'seria':card.seria,
                'number':card.number,
                'finish_date':card.finish_date,
            })
        return render(request, 'Tests/edit_card.html', {'form':form})
    except Cards.DoesNotExist:
        return render(request, 'Tests/nocard.html')

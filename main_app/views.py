from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Coach
from .forms import TrainingForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlayerCreate(LoginRequiredMixin, CreateView):
  model = Player
  fields = ['name', 'position', 'country', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UpdateView):
  model = Player
  fields = ['position', 'country', 'age']

class PlayerDelete(LoginRequiredMixin, DeleteView):
  model = Player
  success_url = '/players/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    # players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})

@login_required
def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    coaches_player_doesnt_have = Coach.objects.exclude(id__in = player.coaches.all().values_list('id'))
    training_form = TrainingForm()
    return render(request, 'players/detail.html', {
        'player': player, 'training_form': training_form,
        'coaches': coaches_player_doesnt_have
    })

@login_required
def add_training(request, player_id):
  form = TrainingForm(request.POST)
  if form.is_valid():
    new_training = form.save(commit=False)
    new_training.player_id = player_id
    new_training.save()
  return redirect('detail', player_id=player_id)

@login_required
def assoc_coach(request, player_id, coach_id):
  Player.objects.get(id=player_id).coaches.add(coach_id)
  return redirect('detail', player_id=player_id)

class CoachList(LoginRequiredMixin, ListView):
  model = Coach

class CoachDetail(LoginRequiredMixin, DetailView):
  model = Coach

class CoachCreate(LoginRequiredMixin, CreateView):
  model = Coach
  fields = '__all__'

class CoachUpdate(LoginRequiredMixin, UpdateView):
  model = Coach
  fields = ['name', 'position']

class CoachDelete(LoginRequiredMixin, DeleteView):
  model = Coach
  success_url = '/coaches/'



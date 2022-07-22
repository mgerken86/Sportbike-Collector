from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Sportbike, Colors, Photo
from .forms import TrimForm
import os


class SportbikeCreate(LoginRequiredMixin, CreateView):
    model = Sportbike
    fields = ['make', 'name', 'displacement', 'skill_lvl']

    def form_valid(self, form):
      # form.instance is the sportbike being made
      form.instance.user = self.request.user  
      return super().form_valid(form)



class SportbikeUpdate(LoginRequiredMixin, UpdateView):
    model = Sportbike
    fields = ['displacement', 'skill_lvl']


class SportbikeDelete(LoginRequiredMixin, DeleteView):
    model = Sportbike
    success_url = '/sportbikes/'


class ColorsList(LoginRequiredMixin, ListView):
    model = Colors


class ColorsDetail(LoginRequiredMixin, DetailView):
    model = Colors


class ColorsCreate(LoginRequiredMixin, CreateView):
    model = Colors
    fields = ["color1", "color2"]
    success_url = '/colors/'


class ColorsUpdate(LoginRequiredMixin, UpdateView):
    model = Colors
    fields = ["color1", "color2"]


class ColorsDelete(LoginRequiredMixin, DeleteView):
    model = Colors
    success_url = '/colors/'


def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def sportbikes_index(request):
    sportbikes = Sportbike.objects.filter(user=request.user)
    return render(request, 'sportbikes/index.html', {'sportbikes': sportbikes})

@login_required
def sportbikes_detail(request, sportbike_id):
    sportbike = Sportbike.objects.get(id=sportbike_id)
    trim_form = TrimForm()
    id_list = sportbike.colors.all().values_list('id')
    colors_bike_doesnt_have = Colors.objects.exclude(id__in=id_list)
    return render(request, 'sportbikes/detail.html', {
        'sportbike': sportbike, 'trim_form': trim_form,
        'colors': colors_bike_doesnt_have
    })

@login_required
def add_trim(request, sportbike_id):
    form = TrimForm(request.POST)
    if form.is_valid():
        new_trim = form.save(commit=False)
        print(new_trim)
        new_trim.sportbike_id = sportbike_id
        new_trim.save()
    return redirect('detail', sportbike_id=sportbike_id)

@login_required
def assoc_colors(request, sportbike_id, colors_id):
    Sportbike.objects.get(id=sportbike_id).colors.add(colors_id)
    return redirect('detail', sportbike_id=sportbike_id)

@login_required
def add_photo(request, sportbike_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, sportbike_id=sportbike_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', sportbike_id=sportbike_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else: 
      error_message = 'Invalid sign-up, please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
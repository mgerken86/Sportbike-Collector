from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Sportbike, Colors, Photo
from .forms import TrimForm
import os


class SportbikeCreate(CreateView):
    model = Sportbike
    fields = '__all__'
    success_url = '/sportbikes/'


class SportbikeUpdate(UpdateView):
    model = Sportbike
    fields = ['displacement', 'skill_lvl']


class SportbikeDelete(DeleteView):
    model = Sportbike
    success_url = '/sportbikes/'


class ColorsList(ListView):
  model = Colors

class ColorsDetail(DetailView):
  model = Colors

class ColorsCreate(CreateView):
  model = Colors
  fields = '__all__'

class ColorsUpdate(UpdateView):
  model = Colors
  fields = ['name', 'colors']

class ColorsDelete(DeleteView):
  model = Colors
  success_url = '/colors/'




def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def sportbikes_index(request):
    sportbikes = Sportbike.objects.all()
    return render(request, 'sportbikes/index.html', {'sportbikes': sportbikes})


def sportbikes_detail(request, sportbike_id):
    bike = Sportbike.objects.get(id=sportbike_id)
    trim_form = TrimForm()
    return render(request, 'sportbikes/detail.html', {
        'sportbike': bike, 'trim_form': trim_form
    })

def add_trim(request, sportbike_id):
  form = TrimForm(request.POST)
  if form.is_valid():
    new_trim = form.save(commit=False)
    print(new_trim)
    new_trim.sportbike_id = sportbike_id
    new_trim.save()
  return redirect('detail', sportbike_id=sportbike_id)


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



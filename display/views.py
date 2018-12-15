from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Photos



def index(request):
    return HttpResponse("This is photography fight club.")

def fight_club(request):
    photos_list = Photos.objects.order_by('-photo_id')
    template = loader.get_template('display\fight-club.html')
    return HttpResponse("fight club!")

def signup_user(request):
    return HttpResponse("user signup")

def upload_image(request):
    return HttpResponse("image upload")

def view_images(request):
    return HttpResponse("user's own images")

def view_leaderboards(request):
    return HttpResponse("leaderboards by topic")

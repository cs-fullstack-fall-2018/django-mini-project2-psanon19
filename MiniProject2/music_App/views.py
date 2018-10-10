from django.shortcuts import render
from .models import SubmissionModel


def index(request):
    song_list = SubmissionModel.objects.all
    context = {'song_list': song_list}
    return render(request, 'music_App/index.html', context)
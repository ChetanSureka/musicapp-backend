from django.shortcuts import render
from django.http import JsonResponse
from .utils.script import get_video, search
from django.views.decorators.csrf import csrf_exempt
import json


def Video(request, videoId, title):
    context = {
        "video": videoId,
        "title": title
    }
    return render(request, 'music/video.html', context)


def home(request):
    context = {}
    if request.GET.get('query'):
        query = request.GET.get('query')
        context = {"query": query}
    else:
        query = "trending songs"
    search_results = search(query)
    context["recommended"] = search_results
    return render(request, 'music/home.html', context)

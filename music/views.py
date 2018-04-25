from django.shortcuts import render
from music.models import Album,Song
from django.http import HttpResponse
from django.template import loader

def index(request):
    html = ""
    all_albums = Album.objects.all()
    # create template dir and music dir(same name as the app) then create index.html in it to write your display code
    template = loader.get_template('music/index.html')
    context =  {
        'all_albums':all_albums,
    }
    # connecting to a database
    # for album in all_albums:
    #     url = '/music/'+str(album.id)+'/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    # return HttpResponse(html)
    return HttpResponse(template.render(context,request))

def detail(request,album_id):
    return HttpResponse("<h2> Details for Album Id: "+ str(album_id) +"</h2>")

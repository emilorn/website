from django.shortcuts import render, get_object_or_404
from .models import Album, Song



def index(request):
    allAlbums=Album.objects.all()

    context = {
        'allAlbums': allAlbums,

    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album' : album})

def favorite(request, album_id):
    album= get_object_or_404(Album, pk=album_id)
    try:
        selectedSong = album.song_set.get(pk=request.POST['song'])

    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album' :album},{ 'error_message' : "you didn't pick nuthin.",})
    else:
        selectedSong.is_favorite = True
        selectedSong.save()
        return render(request, 'music/details.html', {'album':album})





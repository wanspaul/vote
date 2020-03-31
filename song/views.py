from django.http import HttpResponseRedirect, JsonResponse
from django.template.response import TemplateResponse
from django.views import View

from song.models import ApplySong


class VoteList(View):
    def get(self, request):
        return TemplateResponse(request, 'vote_list.html', {
            'apply_songs': ApplySong.objects.filter(is_hidden=False).order_by('-vote_count')
        })


class AddSong(View):
    def post(self, request):
        ApplySong.objects.create(
            title=request.POST.get('title'),
            artist=request.POST.get('artist'),
        )
        return HttpResponseRedirect('/')


class VoteSong(View):
    def post(self, request):
        try:
            apply_song = ApplySong.objects.get(pk=request.POST.get('id'))
            apply_song.vote_count += 1
            apply_song.save(update_fields=['vote_count'])
            status = 0
        except:
            status = 500
        return JsonResponse({'status': status})


class CoveredSong(View):
    def get(self, request):
        return TemplateResponse(request, 'play_list.html', {
            'covered_songs': ApplySong.objects.filter(cover_complete=True, is_hidden=False).order_by('-vote_count')
        })

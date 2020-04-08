from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.template.response import TemplateResponse
from django.views import View

from song.models import ApplySong, VoteLimit
from song.utils import get_client_ip, get_user_agent, check_recaptcha


class VoteList(View):
    def get(self, request):
        return TemplateResponse(request, 'vote_list.html', {
            'apply_songs': ApplySong.objects.filter(is_hidden=False, cover_complete=False).order_by('-vote_count')
        })


class AddSong(View):
    def post(self, request):
        try:
            result = check_recaptcha(request)
            if not result:
                raise ValidationError
        except ValidationError as e:
            return HttpResponseRedirect('/')

        ApplySong.objects.create(
            title=request.POST.get('title'),
            artist=request.POST.get('artist'),
        )
        return HttpResponseRedirect('/')


class VoteSong(View):
    def post(self, request):
        try:
            client_ip = get_client_ip(request)
            user_agent = get_user_agent(request)
            result = check_recaptcha(request)
            if not result:
                raise ValidationError
            vote_limits = VoteLimit.objects.filter(client_ip=client_ip).count()
            if vote_limits >= 3:
                raise ValueError("하루에 3번까지 투표하실 수 있습니다.")
            else:
                VoteLimit.objects.create(
                    client_ip=client_ip,
                    user_agent=user_agent
                )

            apply_song = ApplySong.objects.get(pk=request.POST.get('id'))
            apply_song.vote_count += 1
            apply_song.save(update_fields=['vote_count'])
            status = 0
        except ValidationError as e:
            status = 405
        except ValueError as e:
            status = 400
        except:
            status = 500
        return JsonResponse({'status': status})


class CoveredSong(View):
    def get(self, request):
        return TemplateResponse(request, 'play_list.html', {
            'covered_songs': ApplySong.objects.filter(cover_complete=True, is_hidden=False).order_by('-vote_count')
        })

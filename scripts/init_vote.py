from song.models import ApplySong


def run():
    ApplySong.objects.filter(vote_count__lte=20).update(is_hidden=True)

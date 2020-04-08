from song.models import ApplySong


def run():
    ApplySong.objects.filter(cover_complete=False, vote_count__lte=20).update(is_hidden=True)
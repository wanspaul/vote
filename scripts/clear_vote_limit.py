from song.models import VoteLimit


def run():
    VoteLimit.objects.all().delete()

from django.db import models


class ApplySong(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)
    play_link = models.CharField(max_length=255, null=True)
    cover_complete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "apply_song"


class VoteLimit(models.Model):
    client_ip = models.CharField(max_length=40, db_index=True)
    user_agent = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "vote_limit"

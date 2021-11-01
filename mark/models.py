from django.db import models
from main.models import MainPost
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.conf import settings


class Mark(models.Model):
    mark_id = models.IntegerField(primary_key=True)
=======


class Mark(models.Model):
    mark_id = models.CharField(max_length=250, blank =True)
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    date_added = models.DateField(auto_now_add = True)
    class Meta:
        db_table = 'mark'
        ordering = ['date_added']

    def __str__(self):
        return self.mark_id

class MarkItem(models.Model):
    MainPost = models.ForeignKey(MainPost, on_delete=models.CASCADE)
<<<<<<< HEAD
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default = True)
    
=======
    mark = models.ForeignKey(Mark,db_column="mark_id", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default = True)
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    class Meta:
        db_table = 'markitem'
    def __ste__(self):
        return self.post

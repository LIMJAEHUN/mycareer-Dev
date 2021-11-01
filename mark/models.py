from django.db import models
from main.models import MainPost


class Mark(models.Model):
    mark_id = models.CharField(max_length=250, blank =True)
    date_added = models.DateField(auto_now_add = True)
    class Meta:
        db_table = 'mark'
        ordering = ['date_added']

    def __str__(self):
        return self.mark_id

class MarkItem(models.Model):
    MainPost = models.ForeignKey(MainPost, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark,db_column="mark_id", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default = True)
    class Meta:
        db_table = 'markitem'
    def __ste__(self):
        return self.post

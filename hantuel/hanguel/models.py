from django.db import models

class Word_tbl(models.Model):
    wid = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length=32, null=False)
    wordDesc = models.(null=False)

    class Meta:
        db_table = "word_tbl"

class Writing_tbl(models.Model):
    rid = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=28, null=False)
    wid = models.ForeignKey(Word_tbl, to_field='wid')
    date = models.TextField(null=False)
    writing = models.TextField(null=False)




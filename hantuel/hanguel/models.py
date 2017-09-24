from django.db import models

class Word_tbl(models.Model):
    wid = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length=32, null=False)
    wordDesc = models.TextField(null=False)

    class Meta:
        db_table = "word_tbl"


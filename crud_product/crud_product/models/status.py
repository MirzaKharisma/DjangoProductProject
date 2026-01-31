from django.db import models

class Status(models.Model):
    id_status=models.BigAutoField(primary_key=True)
    nama_status = models.CharField(max_length=100, unique=True, null=False)
    class Meta:
        db_table = "status"
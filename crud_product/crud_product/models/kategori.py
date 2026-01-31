from django.db import models

class Kategori(models.Model):
    id_kategori=models.BigAutoField(primary_key=True, db_column='id_kategori')
    nama_kategori=models.CharField(max_length=100, unique=True, null=False)
    class Meta:
        db_table="kategori"
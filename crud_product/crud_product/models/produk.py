from django.db import models
from .kategori import Kategori
from .status import Status

class Produk(models.Model):
    id_produk=models.BigAutoField(primary_key=True)
    nama_produk=models.CharField(max_length=100)
    harga=models.BigIntegerField()
    kategori=models.ForeignKey(Kategori, on_delete=models.RESTRICT)
    status=models.ForeignKey(Status, on_delete=models.RESTRICT)
    class Meta:
        db_table="produk"
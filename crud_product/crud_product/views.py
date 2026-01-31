from django.shortcuts import render
from django.shortcuts import redirect
from .models.produk import Produk
from .models.kategori import Kategori
from .models.status import Status
from django.contrib import messages
from .forms import ProdukForm

def show_produk(request):
    showall=Produk.objects.filter(status__id_status=1)

    return render(request, 'Index.html', {"data": showall})

def insert_produk(request):
    data_kategori = Kategori.objects.all()
    data_status = Status.objects.all()
    if request.method == "POST":
        if request.POST.get("nama_produk") and request.POST.get("harga") and request.POST.get("kategori_id") and request.POST.get("status_id"):
            saverecord=Produk()
            saverecord.nama_produk = request.POST.get("nama_produk")
            saverecord.harga = request.POST.get("harga")
            saverecord.kategori_id = request.POST.get("kategori_id")
            saverecord.status_id = request.POST.get("status_id")
            saverecord.save()
            messages.success(request, "Produk " + saverecord.nama_produk + " berhasil ditambahkan")
            return render(request, "Insert.html", {"data_kategori": data_kategori, "data_status": data_status})
    else:
        return render(request, "Insert.html", {"data_kategori": data_kategori, "data_status": data_status})
    
def edit_produk(request, id):
    product = Produk.objects.get(id_produk=id)
    data_kategori = Kategori.objects.all()
    data_status = Status.objects.all()
    return render(request, 'Edit.html', {"Produk": product, "data_kategori": data_kategori, "data_status": data_status})

def update_produk(request, id):
    product_updated = Produk.objects.get(id_produk=id)
    form = ProdukForm(request.POST, instance=product_updated)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diupdate")
        return redirect('edit_produk', id=id)
    else:
        return redirect('edit_produk', id=id)
    
def delete_produk(request, id):
    product_deleted = Produk.objects.get(id_produk=id)
    product_deleted.delete()
    messages.success(request, "Produk " + product_deleted.nama_produk +" berhasil dihapus")
    showall=Produk.objects.filter(status__id_status=1)
    return redirect('show_produk')


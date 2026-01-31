def transform(raw_list):
    result = []

    for raw in raw_list:
        result.append({
            "id_produk": int(raw["id_produk"]),
            "nama_produk": raw["nama_produk"].strip(),
            "kategori": raw["kategori"].strip(),
            "status": raw["status"].strip(),
            "harga": int(raw["harga"])
        })

    return result

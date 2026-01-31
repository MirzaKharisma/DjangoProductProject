# 📦 Django Product Project (ETL & CRUD)

Project ini terdiri dari dua bagian utama:
- **ETL Product** → untuk memproses dan mengirim data ke PostgreSQL
- **CRUD Product** → aplikasi Django untuk mengelola dan menampilkan data

Ikuti langkah-langkah di bawah ini untuk menjalankan project dengan benar.

---

## 🛠️ Prerequisites

Pastikan sudah terinstall:
- Python (disarankan Python 3.9+)
- PostgreSQL
- Git (opsional)
- Virtual Environment (venv)

---

## 🚀 Cara Menjalankan Project

### 1️⃣ Buat Tabel & Constraint Database
- Jalankan file **`.sql`** yang sudah disediakan ke dalam PostgreSQL.
- Pastikan:
  - Nama database sesuai
  - Semua table dan constraint berhasil dibuat tanpa error

Contoh menjalankan file SQL:
```sql
\i path/to/file.sql
```

---

### 2️⃣ Konfigurasi File `.env`
Sesuaikan file **`.env`** pada:
- Folder **ETL Product**
- Folder **CRUD Product**

Pastikan konfigurasi berikut sudah sesuai:
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

---

### 3️⃣ Buat Virtual Environment
Buka terminal pada root project, lalu jalankan:
```bash
python -m venv myworld
```

---

### 4️⃣ Aktifkan Virtual Environment
Jalankan perintah berikut di terminal:
```bash
myworld\Scripts\activate.bat
```

Jika berhasil, nama environment akan muncul di awal terminal.

---

### 5️⃣ Jalankan Proses ETL
Masih di terminal yang sama, jalankan:
```bash
python etl_product/main.py
```

Tunggu hingga muncul pesan:
```
ETL success
```

---

### 6️⃣ Cek Data di Database
- Pastikan data sudah masuk ke tabel PostgreSQL
- Data dapat dicek menggunakan:
  - PgAdmin
  - DBeaver
  - Query SQL manual

---

### 7️⃣ Jalankan Project CRUD Django
Jika data sudah tersedia di database, jalankan:
```bash
python manage.py runserver
```

---

### 8️⃣ Akses Aplikasi
Buka browser dan akses:
```
http://127.0.0.1:8000
```

🎉 Project Django berhasil dijalankan.

---

## 📌 Catatan
- Pastikan virtual environment **aktif** setiap kali menjalankan ETL atau Django
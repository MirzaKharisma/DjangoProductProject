import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_produk_db(produk):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()

    for stat in produk:
        cur.execute("""
            INSERT INTO status (nama_status)
            SELECT %s
            WHERE NOT EXISTS (
                SELECT 1 FROM status WHERE nama_status = %s
            )
        """, (stat["status"], stat["status"]))

    for k in produk:
        cur.execute("""
            INSERT INTO kategori (nama_kategori)
            SELECT %s
            WHERE NOT EXISTS (
                SELECT 1 FROM kategori WHERE nama_kategori = %s
            )
        """, (k["kategori"], k["kategori"]))

    for prod in produk:
        cur.execute("""
            INSERT INTO produk (id_produk, nama_produk, harga, kategori_id, status_id)
            SELECT %s, %s, %s, k.id_kategori, s.id_status
            FROM kategori k, status s
            WHERE k.nama_kategori = %s
            AND s.nama_status = %s
        """, (
            prod["id_produk"],
            prod["nama_produk"],
            prod["harga"],
            prod["kategori"],
            prod["status"]
        ))
    
    conn.commit()
    cur.close()
    conn.close()
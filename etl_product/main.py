from extract import extract_data
from transform import transform
from load import load_to_produk_db

def run_etl():
    raw = extract_data()
    cleaned = transform(raw)
    load_to_produk_db(cleaned)
    print("ETL sukses 🚀")

if __name__ == "__main__":
    run_etl()
CREATE TABLE Kategori(
	id_kategori bigserial PRIMARY KEY,
	nama_kategori varchar(100) UNIQUE NOT NULL
)

CREATE TABLE Status(
	id_status bigserial PRIMARY KEY,
	nama_status varchar(100) UNIQUE NOT NULL
)

CREATE TABLE Produk(
	id_produk bigint PRIMARY KEY,
	nama_produk varchar(225),
	harga bigint,
	kategori_id bigint REFERENCES Kategori(id_kategori),
	status_id bigint REFERENCES Status(id_status)
)

CREATE SEQUENCE produk_id_produk_seq
START WITH 73;

ALTER TABLE produk
ALTER COLUMN id_produk SET DEFAULT nextval('produk_id_produk_seq');

ALTER SEQUENCE produk_id_produk_seq
OWNED BY produk.id_produk;
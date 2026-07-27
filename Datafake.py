import mysql.connector
from faker import Faker
import random

fake = Faker('id_ID')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="catat_uang_sendiri"
)
cursor = conn.cursor()

cursor.execute("SELECT pengguna_id FROM pengguna")
pengguna_ids = [row[0] for row in cursor.fetchall()]


cursor.execute("SELECT kategori_id, jenis FROM kategori_transaksi")
kategori_list = cursor.fetchall()  # list of (kategori_id, jenis)

jumlah_data = 2500

for _ in range(jumlah_data):
    pengguna_id = random.choice(pengguna_ids)
    kategori_id, jenis = random.choice(kategori_list)
    
    jumlah = round(random.uniform(10000, 5000000), 2)
    tanggal = fake.date_between(start_date='-2y', end_date='today')
    deskripsi = fake.sentence(nb_words=6)
    dibuat = fake.date_time_between(start_date='-2y', end_date='now')
    
    cursor.execute(
        """INSERT INTO transaksi 
           (pengguna_id, kategori_id, jenis_transaksi, jumlah, tanggal_transaksi, deskripsi, dibuat) 
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (pengguna_id, kategori_id, jenis, jumlah, tanggal, deskripsi, dibuat)
    )

conn.commit()
cursor.close()
conn.close()

print(f"Selesai! {jumlah_data} baris data transaksi berhasil di-insert.")
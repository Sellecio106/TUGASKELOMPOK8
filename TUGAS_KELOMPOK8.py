import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

def buat_database():
    db = connect_db() 
    cursor = db.cursor() 
    cursor.execute("CREATE DATABASE IF NOT EXISTS tugaskelompok13")  
    cursor.execute("USE tugaskelompok13")  
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255) NOT NULL,
        kota VARCHAR(255) NOT NULL
    )
    """)
    db.close()  

def Tambah_data(name, kota):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE tugaskelompok13") 
    cursor.execute("INSERT INTO mahasiswa (name, kota) VALUES (%s, %s)", (name, kota))  
    db.commit()  
    db.close()  

def Tampilkan_data():
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE tugaskelompok13")  
    cursor.execute("SELECT * FROM mahasiswa")  
    results = cursor.fetchall()  
    for row in results:
        print(row)  
    db.close()  

def update_data(id, name, kota):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE tugaskelompok13")  
    cursor.execute("UPDATE mahasiswa SET name = %s, kota = %s WHERE id = %s", (name, kota, id))  
    db.commit()  
    db.close()  

def delete_data(id):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE tugaskelompok13")  
    cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))  
    db.commit()  
    db.close()  

def Cari_data(name):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE tugaskelompok13")  
    cursor.execute("SELECT * FROM mahasiswa WHERE name = %s", (name,))  
    results = cursor.fetchall()  
    for row in results:
        print(row)  
    db.close()  


def main():
    buat_database()

    while True:
        db = connect_db()  
        cursor = db.cursor()  
        cursor.execute("USE tugaskelompok13")  
        cursor.execute("SELECT * FROM mahasiswa")  
        results = cursor.fetchall()  
        for row in results:
            print(row)  
        print("=== APLIKASI PYTHON KELOMPOK 13===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("0. Keluar")
        pilihan = input("Pilih menu > ")

        if pilihan == "1":
            name = input("Nama: ")
            kota = input("Kota: ")
            Tambah_data(name, kota)
        elif pilihan == "2":
            Tampilkan_data()
        elif pilihan == "3":
            id = input("ID: ")
            name = input("Nama baru: ")
            kota = input("Kota baru: ")
            update_data(id, name, kota)
        elif pilihan == "4":
            id = input("ID: ")
            delete_data(id)
        elif pilihan == "5":
            name = input("Nama: ")
            Cari_data(name)
        elif pilihan == "0":
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()
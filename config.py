import pymysql

def buat_koneksi():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='kepaladinas',
            database='lokomotif',
            cursorclass=pymysql.cursors.Cursor
        )
        return conn
    except pymysql.MySQLError as e:
        print("Koneksi database gagal:", e)
        return None

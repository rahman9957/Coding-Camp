from flask import Flask, request, jsonify
from config import buat_koneksi

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Selamat Datang di API Lokomotif</h1>'

# ==================================================
# BACA DATA
# ==================================================
@app.route('/baca_data', methods=['GET'])
def baca_data():
    try:
        conn = buat_koneksi()
        if conn is None:
            return jsonify({"error": "Koneksi database gagal"}), 500

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_lokomotif")
        hasil = cursor.fetchall()
        cursor.close()
        conn.close()

        data = []
        for row in hasil:
            data.append({
                "id_lokomotif": row[0],
                "jenis_lokomotif": row[1],
                "no_seri": row[2],
                "tahun_produksi": row[3]
            })

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# TAMBAH DATA
# ==================================================
@app.route('/tambah_data', methods=['POST'])
def tambah_data():
    try:
        jenis_lokomotif = request.form.get('jenis_lokomotif')
        no_seri = request.form.get('no_seri')
        tahun_produksi = request.form.get('tahun_produksi')

        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "INSERT INTO data_lokomotif (jenis_lokomotif, no_seri, tahun_produksi) VALUES (%s, %s, %s)"
        cursor.execute(sql, (jenis_lokomotif, no_seri, tahun_produksi))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data lokomotif berhasil ditambahkan!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# EDIT DATA
# ==================================================
@app.route('/edit/<id_lokomotif>', methods=['POST'])
def edit_data(id_lokomotif):
    try:
        jenis_lokomotif = request.form.get('jenis_lokomotif')
        no_seri = request.form.get('no_seri')
        tahun_produksi = request.form.get('tahun_produksi')

        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "UPDATE data_lokomotif SET jenis_lokomotif=%s, no_seri=%s, tahun_produksi=%s WHERE id_lokomotif=%s"
        cursor.execute(sql, (jenis_lokomotif, no_seri, tahun_produksi, id_lokomotif))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data lokomotif berhasil diubah!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# HAPUS DATA
# ==================================================
@app.route('/hapus/<id_lokomotif>', methods=['DELETE'])
def hapus_data(id_lokomotif):
    try:
        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "DELETE FROM data_lokomotif WHERE id_lokomotif=%s"
        cursor.execute(sql, (id_lokomotif,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data lokomotif berhasil dihapus!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

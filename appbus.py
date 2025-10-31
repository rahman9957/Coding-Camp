from flask import Flask, jsonify, request

app = Flask(__name__)

data_tiket = [
    {"nomor_tiket": 1, "nama_penumpang": "Rahman", "tujuan": "Banyuwangi - Surabaya", "bus": "Gunung Harta"},
    {"nomor_tiket": 2, "nama_penumpang": "Tiara", "tujuan": "Banyuwangi - Jember", "bus": "Damri"},
    {"nomor_tiket": 3, "nama_penumpang": "Rizki", "tujuan": "Banyuwangi - Malang", "bus": "Gunung Harta"},
]

@app.route('/data', methods=['GET'])
def tampil_data():
    return jsonify(data_tiket)

@app.route('/tambah', methods=['POST'])
def tambah_data():
    data_baru = request.get_json()
    data_tiket.append(data_baru)
    return jsonify(data_tiket)

@app.route('/hapus/<nomor_tiket>', methods=['DELETE'])
def hapus_data(nomor_tiket):
    for d in data_tiket:
        if d["nomor_tiket"] == int(nomor_tiket):
            data_tiket.remove(d)
            break
    return jsonify(data_tiket)

if __name__ == '__main__':
    app.run(debug=True)

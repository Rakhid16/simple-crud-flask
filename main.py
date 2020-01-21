from flask_mysqldb import MySQL
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
mysql = MySQL(app)

# AGAR NYAMBUNG KE DATABASE
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'simple_crud'

@app.route('/')
def index():
  return render_template('halaman_utama.html')

# MENAMBAH DATA - CREATE
@app.route('/tambah-data', methods=['GET','POST'])
def tambah_data():
  if request.method == "POST":
    add_data = mysql.connection.cursor()

    add_data.execute('INSERT INTO data_buku VALUES (NULL, %s, %s, %s)',
    (request.form['judul'], request.form['penulis'], request.form['jumlah']))
    mysql.connection.commit()

    return render_template('tambah_data.html', pesan="Tambah data berhasil!")

  return render_template('tambah_data.html')

# MELIHAT DATA - READ
@app.route('/lihat-data', methods=['GET','POST'])
def lihat_data():
  get_data = mysql.connect.cursor()
  get_data.execute("SELECT * FROM data_buku")

  data = get_data.fetchall()
  return render_template('lihat_data.html', data = data)

# MEMPERBARUI DATA - UPDATE
@app.route('/edit-data', methods=['GET', 'POST'])
def edit_data():
  if request.method == "POST":
    update_data = mysql.connection.cursor()

    update_data.execute("UPDATE data_buku SET judul=%s, penulis=%s, jumlah=%s WHERE id=%s",
    (request.form['judul'], request.form['penulis'], request.form['jumlah'], request.form['id']))
    mysql.connection.commit()

    return render_template('edit_data.html', pesan="Edit data berhasil!")

  return render_template('edit_data.html')

# MENGHAPUS DATA - DELETE
@app.route('/hapus-data', methods=['GET', 'POST'])
def hapus_data():
  if request.method == "POST":
    hapus_data = mysql.connection.cursor()

    hapus_data.execute("DELETE FROM data_buku WHERE id=%s", (request.form['id'],))
    mysql.connection.commit()

    return render_template('hapus_data.html', pesan="Hapus data berhasil!")

  return render_template('hapus_data.html')

# KALAU MAU DEPLOY NILAI PADA VARIABEL "debug" KUDU DIGANTI JADI "False"
# ATAU BARIS DI BAWAH INI HAPUS AJA SEMUA JUGA GA MASALAH :P
app.run(debug=True)
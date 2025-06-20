from Koneksi import Koneksi

class Crud(Koneksi):
  def __init__(input,query):
    Koneksi.__init__(input)
    input.query = query

  def select(input,jenis):
    db = input.konfigurasi()
    cursor = db.cursor()
    cursor.execute(input.query)
    if jenis == 'result':
      result = cursor.fetchall()
      return result
    elif jenis == 'row':
      result = cursor.fetchone()
      return result
  
  def inputUpdateDelData(input,value,jenis):
    db = input.konfigurasi()
    cursor = db.cursor()
    cursor.execute(input.query,value)
    if jenis == "Tambah":
      if cursor.rowcount > 0:
        print("Berhasil Tambah Data")
        return db.commit()
      else :
        print("Belum Berhasil Tambah Data")
    elif jenis == "Update":
      if cursor.rowcount > 0:
        print("Berhasil Update Data")
        return db.commit()
      else :
        print("Belum Berhasil Update Data")
    elif jenis == "Delete":
      if cursor.rowcount > 0:
        print("Berhasil Delete Data")
        return db.commit()
      else :
        print("Belum Berhasil Delete Data")

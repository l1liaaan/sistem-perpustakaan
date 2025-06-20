import mysql.connector

class Koneksi:
  
  def __init__(input):
    input.__host = "localhost"
    input.__user = "root"
    input.__pass = ""
    input.__db = "sistem_perpustakaan"

  def konfigurasi(input):
    mydb = mysql.connector.connect(
        host=input.__host,
        user=input.__user,
        password=input.__pass,
        database=input.__db
    )
    return mydb

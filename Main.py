from Crud import Crud

class Main(Crud):
    def __init__(input):
      input.query = ""
      Crud.__init__(input,input.query)
    
    def CetakHeader(input):
       print("====================================")
       print("                                    ")
       print("      📚 APLIKASI PERPUSTAKAAN 📚     ")
       print("                                    ")
       print("====================================\n\n")
       print("🔧    Daftar Fitur yang Tersedia:   " )
       print("------------------------------------")
       print("1. Daftar Pengunjung")
       print("2. Tambah Pengunjung")
       print("3. Edit Pengunjung")
       print("4. Hapus Pengunjung")
       print("5. Daftar Buku")
       print("6. Tambah Buku")
       print("7. Edit Buku")
       print("8. Hapus Buku")
       print("9. Pinjam Buku")
       print("10. Laporan total peminjaman Buku")
       print("11. STOP\n")

    def DaftarFitur(self):
       while True:
         print("=======================================")
         inpFitur = int(input("Pilih Fitur : "))
         print("=======================================\n")

         if inpFitur == 1 :
            self.DaftarPengunjung()
         elif inpFitur == 2 :
            self.InputPengunjung()
         elif inpFitur == 3 :
            self.UpdatePengunjung()
         elif inpFitur == 4 :
            self.DelPengunjung()
         elif inpFitur == 5 :
            self.DaftarBuku()
         elif inpFitur == 6 :
            self.InputBuku()
         elif inpFitur == 7 :
            self.UpdateBuku()
         elif inpFitur == 8 :
            self.DelBuku()
         elif inpFitur == 9 :
            self.PinjamBuku()
         elif inpFitur == 10 :
            self.LaporanTotalPinjamBuku()
         elif inpFitur == 11:
                print("Terima kasih Telah Menggunakan Sistem Perpustakaan Kami \n\n")
                break
         else:
                print("Pilihan tidak valid. Coba lagi.")
         
    def DaftarPengunjung(input):
       input.query = 'SELECT count(id) as jml FROM input_pengunjung'
       getPengunjung = Crud(input.query)
       jmlPengunjung = getPengunjung.select('row')
       print("__________________________________________________________")
       print(f"DAFTAR PENGUNJUNG (TOTAL PENGUNJUNG : {jmlPengunjung[0]})")
       print(f"_______________________________________________________\n")
       input.query = 'SELECT * FROM input_pengunjung'
       selectPengunjung = Crud(input.query)
       result = selectPengunjung.select('result')
       for row in result:
        print(f"Id : {row[0]}")
        print(f"Nama : {row[1]}")
        print(f"Email : {row[2]}\n")
    
    def InputPengunjung(self):
       print("___________________")
       print("INPUT PENGUNJUNG")
       print("___________________")
       inpIdPeng = int(input("INPUT ID PENGUNJUNG : "))
       inpNamaPeng = input("INPUT NAMA PENGUNJUNG : ")
       inpEmailPeng = input("INPUT EMAIL PENGUNJUNG : ")
       prosesInpPeng = Crud("INSERT INTO input_pengunjung (id,nama,email) VALUES (%s,%s,%s)")
       dataInpPeng = (inpIdPeng,inpNamaPeng,inpEmailPeng)
       prosesInpPeng.inputUpdateDelData(dataInpPeng,"Tambah")
    
    def UpdatePengunjung(self):
       print("___________________")
       print("UPDATE PENGUNJUNG")
       print("___________________")
       inpIdPeng = int(input("INPUT Id PENGUNJUNG : "))
       inpNamaPengBaru = input("UPDATE NAMA PENGUNJUNG : ")
       inpEmailPengBaru = input("UPDATE EMAIL PENGUNJUNG : ")
       prosesUpdatePeng = Crud("UPDATE input_pengunjung SET nama = %s,email = %s WHERE id = %s")
       dataUpdatePeng = (inpNamaPengBaru, inpEmailPengBaru,inpIdPeng)
       prosesUpdatePeng.inputUpdateDelData(dataUpdatePeng,'Update')
    
    def DelPengunjung(self):
       print("___________________")
       print("DELETE PENGUNJUNG")
       print("___________________")
       inpIdPeng = int(input("INPUT Id PENGUNJUNG : "))
       prosesDelPeng = Crud("DELETE FROM input_pengunjung WHERE id = %s")
       dataDelPeng = (inpIdPeng,)
       prosesDelPeng.inputUpdateDelData(dataDelPeng,'Delete')

    def DaftarBuku(input):
       input.query = 'SELECT count(isbn) as jml FROM input_buku'
       getBuku = Crud(input.query)
       jmlBuku = getBuku.select('row')
       print("______________________________")
       print(f"DAFTAR BUKU (TOTAL BUKU : {jmlBuku[0]})")
       print(f"______________________________\n")
       input.query = 'SELECT * FROM input_buku'
       selectBuku = Crud(input.query)
       result = selectBuku.select('result')
       for row in result:
        print(f"Isbn : {row[0]}")
        print(f"Nama : {row[1]}")
        print(f"Jumlah Halaman : {row[2]}")
        print(f"Tanggal Terbit : {row[3]}\n")        

    def InputBuku(self):
       print("___________________")
       print("INPUT DATA BUKU")
       print("___________________")
       inpIsbnBuku = int(input("INPUT ISBN BUKU : "))
       inpNamaBuku = input("INPUT Nama BUKU : ")
       inpJmlHalBuku = int(input("INPUT Jumlah Halaman BUKU : "))
       inpTglTerbit = input("INPUT Tanggal Terbit : ")
       prosesInp = Crud("INSERT INTO input_buku (isbn, nama, jml_halaman, tgl_terbit) VALUES (%s,%s,%s,%s)")
       dataInp = (inpIsbnBuku,inpNamaBuku,inpJmlHalBuku,inpTglTerbit)
       prosesInp.inputUpdateDelData(dataInp,"Tambah")
    
    def UpdateBuku(self):
       print("___________________")
       print("UPDATE DATA BUKU")
       print("___________________")
       inpIsbnBuku = int(input("INPUT ISBN BUKU : "))
       inpNamaBukuBaru = input("Rubah Nama BUKU : ")
       inpJmlHalBukuBaru = int(input("Rubah Jumlah Halaman BUKU : "))
       inpTglTerbitBaru = input("Rubah Tanggal Terbit : ")
       prosesUpdate = Crud("UPDATE input_buku SET nama = %s, jml_halaman = %s, tgl_terbit = %s WHERE isbn = %s")
       dataUpdate = (inpNamaBukuBaru,inpJmlHalBukuBaru,inpTglTerbitBaru,inpIsbnBuku)
       prosesUpdate.inputUpdateDelData(dataUpdate,'Update')
    
    def DelBuku(self):
       print("___________________")
       print("DELETE DATA BUKU")
       print("___________________")
       inpIsbnBuku = int(input("INPUT ISBN BUKU : "))
       prosesDel = Crud("DELETE FROM input_buku WHERE isbn = %s")
       dataDel = (inpIsbnBuku,)
       prosesDel.inputUpdateDelData(dataDel,'Delete')
    
    def PinjamBuku(self):
      print("___________________")
      print("    PINJAM BUKU    ")
      print("___________________")
      print("\n----------------------------- Daftar Pengunjung -----------------------------\n")
      query_pengunjung = "SELECT * FROM input_pengunjung"
      result_pengunjung = Crud(query_pengunjung).select("result")
      for row in result_pengunjung:
         print(f"ID: {row[0]} | Nama: {row[1]} | Email: {row[2]}")
      inpIdPeng = int(input("\nINPUT ID PENGUNJUNG : "))
      print("\n--- Daftar Buku ---")
      query_buku = "SELECT isbn, nama FROM input_buku"
      result_buku = Crud(query_buku).select("result")
      for row in result_buku:
         print(f"ISBN: {row[0]} | Judul: {row[1]}")
      inpIsbnBuku = int(input("\nINPUT ISBN BUKU : "))
      inpDurasiPin = int(input("INPUT DURASI PINJAM: "))
      inptgl_pinjam = input("INPUT TANGGAL PINJAM: ")
      query = "INSERT INTO pinjam_buku (id, isbn, durasi_pinjam, tgl_pinjam) VALUES (%s, %s, %s, %s)"
      data = (inpIdPeng, inpIsbnBuku, inpDurasiPin, inptgl_pinjam)
      proses = Crud(query)
      proses.inputUpdateDelData(data, "Tambah")


    def LaporanTotalPinjamBuku(self):
      print("__________________________")
      print("LAPORAN PEMINJAMAN BUKU")
      print("__________________________")
      print("\n----------------------------- Daftar Peminjaman -----------------------------\n")
      query_laporan = "SELECT * FROM pinjam_buku"
      result_laporan = Crud(query_laporan).select("result")
      for row in result_laporan:
         print(f"ID: {row[0]} | Isbn: {row[1]} | Durasi Pinjam: {row[2]} | Tgl Pinjam: {row[3]}")
      print("\n=== Laporan Total Peminjaman Buku ===")
      print("1. Per Hari")
      print("2. Per Bulan")
      print("3. Per Tahun")
      print("4. Fitur Utama\n")
      while True:               # selama kondisinya True, maka kode di dalamnya terus diulang.
         pilihan = input("\nPilih jenis laporan (1/2/3/4): ")
         
         if pilihan == "1":
            query = """
                  SELECT tgl_pinjam, COUNT(*) as total_pinjam                 # tgl_pinjam adalah nama kolom (field) di dalam tabel pinjam_buku
                  FROM pinjam_buku
                  GROUP BY tgl_pinjam
                  ORDER BY tgl_pinjam DESC
            """
            hasil = Crud(query).select("result")
            print("\n=== Laporan Per Hari ===")
            for row in hasil: # perulangan untuk baca tiap baris hasil query SQL.
                  print(f"Tanggal: {row[0]} - Total Pinjam: {row[1]}") 

         elif pilihan == "2":
            query = """
                  SELECT DATE_FORMAT(tgl_pinjam, '%Y-%m') as bulan, COUNT(*) as total_pinjam   # %Y-%m artinya ambil tahun dan bulan saja
                  FROM pinjam_buku
                  GROUP BY bulan                 # GROUP BY: dikelompokkan berdasarkan tgl_pinjam
                  ORDER BY bulan DESC            # ditampilkan dari tanggal terbaru ke lama.
            """
            hasil = Crud(query).select("result") # Ini memanggil class Crud, lalu menjalankan method select("result") dengan query yang sudah kamu buat.
            print("\n=== Laporan Per Bulan ===") # "result" artinya kamu mau ambil banyak baris data (biasanya pakai fetchall() di dalamnya).
            for row in hasil:
                  print(f"Bulan: {row[0]} - Total Pinjam: {row[1]}")

         elif pilihan == "3":
            query = """
                  SELECT YEAR(tgl_pinjam) as tahun, COUNT(*) as total_pinjam                 # YEAR(tgl_pinjam), Akan mengubah 2025-06-19 jadi 2025 (hanya tahun)
                  FROM pinjam_buku
                  GROUP BY tahun                # GROUP BY tahun: kelompok berdasarkan tahun.
                  ORDER BY tahun DESC           # ditampilkan dari terbaru ke lama.
            """
            hasil = Crud(query).select("result")
            print("\n=== Laporan Per Tahun ===")
            for row in hasil:
                  print(f"Tahun: {row[0]} - Total Pinjam: {row[1]}")

         elif pilihan == "4":
            print("\nKembali Ke Fitur Utama")
            break # buat menghentikan loop secara paksa ketika syarat tertentu terpenuhi.

         else:
            print("\nPilihan tidak valid!")

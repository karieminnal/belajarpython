import csv

class innalkariem(object):
    def nilai(self):
        with open('./kelas_2b/innal2.csv', 'r') as file:
            anggka = csv.reader(file, delimiter=',')
            for r in anggka:
                  print ("kode-kode dalam NPM")
                  print (r[0])
                  print (int(r[0][+3]), "kode jurusan")
                  print (int(r[0][+4]), int(r[0][+5]), "tahun masuk")
                  print (int(r[0][+6]), "kode ")
                  print (int(r[0][+7]), int(r[0][+8]), int(r[0][+9]),"urutan pendaftaran")
                  
print("hello word")
print("nama :fahrel azki darmawan")
print("nim :2510933028")
print("kelompok :9A")
print("asisten pembimbing :viona aura rianni")

NIM = 3028
dua_angka_awal = bulan_pertama = AB = 30
dua_angka_akhir = bulan_kedua = CD = 28

biaya_energi = 1500
biaya_beban_tetap_perbulan =2000
pajak_penggunaan_listrik_perbulan = 0.05

#1.tentukan nilai AB dan CD
print("nilai AB:",(AB))
print("nilai CD:",(CD))

#2.tentukan total pemakaian kWh dalam 2 bulan
total_kWh = AB + CD
print("total pemakaian kWh dalam 2 bulan:", total_kWh, 'kWh')

#3.hitung biaya energi yang dikeluarkan pada masing masing bulan
biaya_energi_bulan_1 = AB * 1500
print("total pemakaian energi pada bulan pertama adalah", 'Rp', biaya_energi_bulan_1)
biaya_energi_bulan_2 = CD * 1500
print("total pemakaian energi pada bulan kedua adalah", 'Rp', biaya_energi_bulan_2)

#4.hitung biaya yang dikeluarkan selama 2 bulan sebelum adanya pajak dan biaya administrasi
biaya_energi_total = biaya_energi_bulan_1 + biaya_energi_bulan_2
print("total biaya energi 2 bulan", 'Rp', biaya_energi_total)

#5.hitung pajak yang dikeluarkan pada total kedua bulan
pajak_total_kedua_bulan = (0.05 * biaya_energi * AB) + (0.05 * biaya_energi * CD) 
print("pajak total 2 bulan:", 'Rp', (pajak_total_kedua_bulan))

#6.hitung biaya administrasi yang dikeluarkan pada total kedua bulan
biaya_administrasi_kedua_bulan = 0.02 * (biaya_energi_total + pajak_total_kedua_bulan + (biaya_beban_tetap_perbulan * 2))
print("biaya administrasi per bulan:", 'Rp', (biaya_administrasi_kedua_bulan))

#7.hitung total tagihan dari biaya yang dikeluarkan pada total kedua bulan
total_tagihan_selama_dua_bulan = biaya_energi_total + (biaya_beban_tetap_perbulan * 2) + pajak_total_kedua_bulan + biaya_administrasi_kedua_bulan
print("total tagihan dari biaya yang dikeluarkan kedua bulan", 'Rp', total_tagihan_selama_dua_bulan )

# Database Schema - Aplikasi Sistem Informasi Manajemen Pemesanan Produk

## 1. Tabel Users
Digunakan untuk menyimpan data pengguna yang dapat melakukan login ke sistem.

Kolom:
- id_user : ID unik pengguna
- username : nama pengguna untuk login
- password : kata sandi pengguna
- email : email pengguna
- role : hak akses pengguna (admin/customer)
- created_at : waktu data dibuat


## 2. Tabel Products
Digunakan untuk menyimpan data produk yang tersedia.

Kolom:
- id_product : ID unik produk
- nama_produk : nama produk
- deskripsi : detail produk
- harga : harga produk
- stok : jumlah stok tersedia
- gambar : lokasi gambar produk


## 3. Tabel Orders
Digunakan untuk menyimpan data transaksi pemesanan.

Kolom:
- id_order : ID unik pesanan
- id_user : pengguna yang melakukan pemesanan
- tanggal_order : waktu pemesanan
- total_harga : total pembayaran
- status_order : status pesanan


## 4. Tabel Order_Detail
Digunakan untuk menyimpan detail produk dalam setiap pesanan.

Kolom:
- id_detail : ID detail pesanan
- id_order : referensi pesanan
- id_product : referensi produk
- jumlah : jumlah produk yang dibeli
- subtotal : total harga produk


## 5. Tabel Payments
Digunakan untuk menyimpan informasi pembayaran.

Kolom:
- id_payment : ID pembayaran
- id_order : pesanan terkait
- metode_pembayaran : metode pembayaran
- status_pembayaran : status pembayaran
- tanggal_pembayaran : waktu pembayaran

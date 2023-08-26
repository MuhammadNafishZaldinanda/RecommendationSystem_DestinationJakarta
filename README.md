# **Sistem Rekomendasi Destinasi Wisata DKI Jakarta**
# Domain Proyek
---

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/bd48a792-83f5-4446-8f03-05cc7532995a)
Gambar 1. [**Museum Fatahillah, Kota Tua, Jakarta Merupakan Salah Satu Destinasi Wisata Budaya di Kota Jakarta (Photo by Hanna Meyra Anggitha)**](https://www.kompasiana.com/hannameyra/62c41ff0297d68123878d5f2/melihat-lanjut-nilai-kesenian-di-kota-tua-jakarta) 

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/6f0d248a-fe0f-4081-8686-5606b7b2104a)
Gambar 2. Taman Mini Indonesia Indah (TMII) adalah Salah Satu Destinasi Wisata Taman Hiburan Legendaris di Kota Jakarta

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/9898ae90-8a32-4cb0-a068-e0fae693e9ce)

Gambar 3. Kebun Binatang Ragunan Merupakan Destinasi Wisata Cagar Alam di Kota Jakarta

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/0cd57a3e-5697-4df0-8495-5495d6f3f81b)

Gambar 4. Pulau Tidung Adalah Salah Satu Spot Wisata Bahari di Kota Jakarta

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/f57245e6-353f-4a07-bea9-a56209af01cb)

Gambar 5. Pasar Tanah Abang Merupakan Pusat Perbelanjaan Grosir Terbesar di ASEAN Bisa Dijadikan Destinasi Wisata

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/949eefa1-6935-40cc-9bb7-62b71d6189a8)

Gambar 6. Masjid Istiqlal Menjadi Destinasi Wisata Religi Pilihan di Kota Jakarta Untuk Umat Muslim di Seluruh Indonesia


DKI Jakarta adalah ibu kota Indonesia yang kaya akan sejarah, budaya, dan kehidupan perkotaan yang serba cepat. Terletak di pesisir utara Pulau Jawa, kota ini menawarkan berbagai destinasi wisata yang menarik seperti situs bersejarah, budaya, bahari, taman, mall, restoran, dan tempat hiburan lainnya [1]. Namun, dengan banyaknya pilihan yang tersedia, seringkali pengunjung merasa bingung dalam memilih destinasi yang sesuai dengan minat dan preferensi mereka.

Untuk mengatasi tantangan ini, pengembangan sistem rekomendasi destinasi wisata Jakarta menjadi sangat penting. Sistem rekomendasi dapat membantu pengunjung dalam menemukan dan memilih destinasi wisata yang sesuai dengan minat mereka, berdasarkan preferensi sebelumnya, ulasan pengguna, atau data lainnya.

Dalam proyek ini, akan dilakukan pengolahan data destinasi wisata Jakarta yang mencakup informasi seperti lokasi, kategori, ulasan pengguna, dan lain-lain. Data ini akan digunakan sebagai dasar untuk mengembangkan model rekomendasi yang dapat memberikan rekomendasi destinasi wisata yang relevan dan disesuaikan dengan preferensi pengguna.

Sistem rekomendasi destinasi wisata Jakarta diharapkan dapat memberikan pengalaman yang lebih baik bagi para pengunjung, membantu mereka menemukan destinasi yang menarik dan sesuai dengan minat mereka, serta meningkatkan kepuasan mereka dalam melakukan perjalanan wisata di Jakarta.


# Bussines Understanding
---
***Problem Statement***

Rumusan Masalah
1. Bagaimana cara membangun sebuah sistem rekomendasi destinasi wisata DKI Jakarta?
2. Bagaimana cara menampilkan daftar rekomendasi hasil dari sistem rekomendasi yang telah dibuat?
3. Bagaimana sistem dapat menyesuaikan rekomendasi berdasarkan preferensi pengunjung?

Tujuan Proyek
1. Mengetahui cara membangun sebuah sistem rekomendasi destinasi wisata DKI Jakarta.
2. Mengetahui cara menampilkan daftar rekomendasi hasil dari sistem rekomendasi yang telah dibuat.
3. Mengetahui cara kerja sistem dalam menentukan rekomendasi kepada pengunjung berdasarkan preferensi tertentu.

***Solution Statement***
- Pada Proyek ini akan menggunakan pendekatan ***Content Based Filtering*** dalam pembangunan sistem rekomendasi.
- Pada Proyek ini akan menggunakan pemrosesan seperti ***TF-IDF*** dan ***Cosine-Similarity***.

# Data Understanding
---
Data yang digunakan pada proyek ini adalah data destinasi wisata dari 5 kota besar di Indonesia yaitu Jakarta, Yogyakarta, Semarang, Bandung, Surabaya. Pada proyek ini akan menggunakan dataset destinasi wisata hanya pada kota Jakarta. Dataset berisikan parameter seperti nama tempat destinasi wisata, harga, kategori. Berikut ini link dataset yang berektensi csv yang akan digunakan pada proyek ini [**Dataset**](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination)

Pada proyek ini, dataset akan dilakukan pemilihan terlebih dahulu, dimana dataset yang digunakan hanya pada kota ("City") Jakarta. Terdapat 3 dataset yang digunakan yaitu:
1. Dataset destination
   - Terdiri dari 84 Sampel dan 11 Fitur
   - Terdapat 4 fitur bertipe data float64, 2 fitur bertipe data int64, dan  5 fitur bertipe data object
2. Dataset destination_rating
   - Terdiri dari 1920 Sampel dan 3 Fitur
   - Ketiga fitur bertipe data int64
3. Dataset user
   - Terdiri dari 300 sampel dan 3 fitur
   - Terdapat 2 fitur bertipe data int64, 1 fitur bertipe data object
   
**Variabel pada Dataset**:
1. Dataset destination
   
   Place_Id = Identifikasi unik tempat wisata.

   Place_Name = Nama tempat wisata.

   Description= Deskripsi tempat wisata.

   Category = Kategori tempat wisata.

   City = Kota tempat wisata.

   Price = Harga tiket masuk.

   Rating = Rating tempat wisata.

   Time_Minutes = Waktu tempuh

   Coordinate = Koordinat tempat wisata.

   Lat = Latitude tempat wisata.

   Long = Longitude tempat wisata.
2. Dataset destination_rating
   
   User_Id = Identifikasi unik *user*.

   Place_Id = Identifikasi unik tempat wisata yang diberi rating oleh *user*

   Place_Ratings = Rating tempat wisata oleh *user*.
1. Dataset *user*
   
   User_Id = Identifikasi unik *user*.

   Location = Kota asal *user*.

   Age = Usia *user*.

# Data Preparation
1. Pemilihan dataset hanya pada tempat wisata di kota Jakarta, Dengan cara membuang atau menghapus data yang bukan destinasi wisata di Kota Jakarta.
2. Menghapus kolom fitur yang tidak digunakan pada proyek ini yaitu Time_Minutes karena pada fitur ini terdapat banyak *missing value* dan pada proyek ini sistem akan memberikan rekomendasi berdasarkan preferensi kemiripan dan *rating* *user* terhadap tempat wisata sebelumnya. Serta kolom 'Unnamed: 11','Unnamed: 12', dimana pada kolom tersebut tidak terdapat data atau kosong.
3. Pemilihan dataset destination_rating sehingga berisi *rating* destinasi wisata untuk kota Jakarta saja.
4. Pemilihan Dataset (user) Hanya User yang Memberikan Ulasan Destinasi Wisata Kota Jakarta Saja dengan Menyocokkan dataset destination_rating dan dataset user.
5. Poin 3 dan 4 dilakukan dengan fungsi Right join dengan menggabungkan baris-baris dari kedua DataFrame berdasarkan nilai kunci pada kolom yang diberikan, dan hanya mempertahankan baris-baris dari DataFrame yang ada di sebelah kanan (DataFrame kedua) dan mempertahankan nilai-nilai dari DataFrame pertama jika ada nilai kunci yang cocok.
6. Menghapus duplikat data User_Id pada dataset *user* dan destination_rating degnan menggunakan drop.duplicate sehingga dapat menghindari munculnya data yang sama sebanyak 2 kali atau lebih pada sistem rekomendasi 

# ***Exploratory Data Analysis (EDA)***
Pada proyek ini akan menggunakan dua metode analisis statistik yaitu *univariate analysis* dan *multivariate analysis*. 

***Univariate Analysis***

*Univariate analysis* adalah metode analisis statistik yang digunakan untuk memahami dan menganalisis data dari satu variabel tunggal [2]. Dalam univariate analysis, fokus diberikan pada variabel tunggal dan statistik deskriptif digunakan untuk meringkas dan memahami karakteristik dari variabel tersebut.


**Dataset destination**

Tabel 1. Analisis Fitur Dataset destination
|       | Place_Id | Price     | Rating | Lat   | Long   |
|-------|----------|-----------|--------|-------|--------|
| count | 84.00    | 84.00     | 84.00  | 84.00 | 84.00  |
| mean  | 42.50    | 45130.95  | 4.49   | -6.09 | 106.78 |
| std   | 24.39    | 115657.34 | 0.20   | 0.80  | 0.32   |
| min   | 1.00     | 0.00      | 4.00   | -6.38 | 103.93 |
| 25%   | 21.75    | 0.00      | 4.40   | -6.21 | 106.81 |
| 50%   | 42.50    | 4500.00   | 4.50   | -6.18 | 106.82 |
| 75%   | 63.25    | 25000.00  | 4.60   | -6.13 | 106.84 |
| max   | 84.00    | 900000.00 | 5.00   | 1.08  | 106.96 |

Pada dataset destination, pada fitur "Price" menunjukkan harga tiket masuk dari 84 tempat wisata di kota Jakarta didapatkan bahwa harga tiket masuk termurah yaitu Rp. 0 atau menunjukan bahwa tempat wisata tersebut gratis tiket masuk, sedangkan untuk harga tiket masuk termahal yaitu sebesar Rp. 900.0000. Pada fitur "Rating", didapatkan bahwa *rating* terendah untuk tempat wisata di kota Jakarta adalah 4.0 dan *rating*  tertinggi adalah 5.0 dari skala *rating*  0.0 - 5.0, dengan rata-rata *rating*  dari 84 tempat wisata di kota Jakarta sebesar 4.49.
![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/edc68b5d-1955-4a62-bcb3-6912eee4f82f)
Gambar 7. Distribusi Rata-Rata Rating Destinasi

Pada fitur "Category", menunjukkan kategori tempat wisata di kota Jakarta yang terdiri dari 6 kategori yaitu Budaya, Taman Hiburan, Cagar Alam, Bahari, Pusat Perbelanjaan, Tempat Ibadah. Berikut ini persebaran jumlah tempat wisata berdasarkan kategori:

![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/dc302099-bb99-4284-9eee-780e11de1ada)
Gambar 8. Persebaran Jumlah Tempat Wisata Berdasarkan Kategori

Dari visualisasi persebaran jumlah tempat wisata berdasarkan kategori, didapatkan bahwa mayoritas tempat wisata di kota Jakarta berkategori Budaya dengan persentase 38.1%, dimana pada kategori ini berisi tempat wisata seperti museum sejarah, tempat bersejarah peninggalan kolonial, monumen, tempat budaya dari beberapa etnis seperti tionghoa, betawi dan lain-lain. kategori kedua yang memiliki jumlah tempat wisata terbanyak dengan persentase 32.1% adalah kategori Taman Hiburan seperti taman kota, taman bermain dan lain-lain. Kategori Cagar Alam dengan persentase 11.9% seperti daerah konservasi, kemudian kategori Bahari yang merupakan kategori yang termasuk wisata pesisir dan laut di kota Jakarta dengan persentase 9.5%, kategori Pusat Perbelanjaan dengan persentase 4.8% seperti mall, pasar grosir dan kategori tempat ibadah dengan persentase 3.6% seperti masjid, katedral, dan klenteng. 


**Dataset destination_rating**

Tabel 2. Analisis Fitur Dataset destination_rating
|       | User_Id | Place_Id | Place_Ratings |
|-------|---------|----------|---------------|
| count | 1920.00 | 1920.00  | 1920.00       |
| mean  | 150.45  | 42.62    | 3.01          |
| std   | 86.93   | 23.95    | 1.38          |
| min   | 1.00    | 1.00     | 1.00          |
| 25%   | 74.00   | 22.75    | 2.00          |
| 50%   | 150.00  | 42.00    | 3.00          |
| 75%   | 224.25  | 63.00    | 4.00          |
| max   | 300.00  | 84.00    | 5.00          |

Pada dataset destination_rating terdapat 1920 ulasan dari *user* berupa *rating* untuk tempat wisata di kota Jakarta dengan *rating* terendah yang diberikan *user* adalah 1.0 dan *rating* tertinggi sebesar 5.0. 

**Dataset *user***

Tabel 3. Analisis Fitur Dataset *user*
|       | User_Id    | Age        |
|-------|------------|------------|
| count | 300.000000 | 300.000000 |
| mean  | 150.500000 | 28.700000  |
| std   | 86.746758  | 6.393716   |
| min   | 1.000000   | 18.000000  |
| 25%   | 75.750000  | 24.000000  |
| 50%   | 150.500000 | 29.000000  |
| 75%   | 225.250000 | 34.000000  |
| max   | 300.000000 | 40.000000  |

Dari dataset *user* tersebut, terdapat 300 pengguna atau *user*. Rata-rata usia dari seluruh pengguna adalah 28.7 tahun, dengan usia *user* termuda 18 tahun dan usia *user* tertua 40 tahun.


***Multivariate Analysis***

*Multivariate Analysis* adalah metode statistik yang digunakan untuk menganalisis hubungan antara dua atau lebih variabel secara simultan [2]. Ini memungkinkan pengkajian yang lebih komprehensif dan mendalam tentang pola, korelasi, dan pengaruh antara variabel-variabel tersebut.

**Rata-Rata Harga Tiket Masuk Pada Setiap Kategori Destinasi Wisata**

Tabel 4. Rerata Harga Tiket Masuk Berdasarkan Kategori Wisata
| Category           | Mean Price |
|--------------------|------------|
| Bahari             | 181250.00  |
| Taman Hiburan      | 75259.26   |
| Cagar Alam         | 26000.00   |
| Budaya             | 6406.25    |
| Pusat Perbelanjaan | 0.00       |
| Tempat Ibadah      | 0.00       |

Dari tabel tersebut, dapat disimpulkan bahwa kategori destinasi wisata Bahari memiliki rerata harga tiket masuk termahal sebesar Rp. 181.250. Sementara itu, kategori Pusat Perbelanjaan dan Tempat Ibadah tidak memerlukan tiket masuk atau gratis, sehingga dapat dianggap sebagai harga tiket masuk termurah.

**Top 10 Destinasi Wisata dengan Harga Tiket Masuk Termahal**
![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/da0eddaf-3b85-45a9-aa02-46eaad5311f3)
Gambar 9. Destinasi Wisata dengan Harga Tiket Masuk Termahal

Pulau Pelangi merupakan destinasi wisata dengan harga tiket masuk paling mahal di kota Jakarta dengan harga tiket masuk sebesar Rp. 900.000

**Top 10 Destinasi Wisata dengan Jumlah Ulasan (Rating) Terbanyak**
![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/514ef2d1-cffa-4b20-9578-23599e0b5546)
Gambar 10. Destinasi Wisata dengan Jumlah Ulasan (Rating) Terbanyak

Berdasarkan data yang diberikan, Wisata Kuliner Pecenongan menjadi tempat wisata yang paling banyak diulas oleh pengguna dengan total ulasan sebanyak 33 ulasan. Banyaknya ulasan ini dapat menunjukkan bahwa Wisata Kuliner Pecenongan cukup populer dan sering dikunjungi oleh pengunjung. Hal ini dapat mengindikasikan minat dan popularitas destinasi wisata kuliner tersebut di kalangan pengunjung.

**Jumlah *User* dari Tiap Kota Asal**
![image](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/d190e795-e9b7-4684-b526-4449bb85bf96)

Gambar 11. Jumlah User dari Tiap Kota Asal

Dalam dataset *user*, terdapat fitur Location yang memberikan informasi tentang asal daerah pengguna. Berdasarkan dataset tersebut, didapatkan informasi bahwa terdapat *user* yang berasal dari 28 kota yang berbeda. Jumlah *user* terbanyak berasal dari kota Bekasi dengan jumlah sebanyak 39 *user*. Kemudian diikuti oleh kota Semarang, Yogyakarta, Lampung, dan Bogor sebagai kota-kota dengan jumlah *user* tertinggi setelah Bekasi.

# Modelling
--- 
Dalam proyek sistem rekomendasi ini, menggunakan pendekatan *content-based filtering* untuk menghasilkan rekomendasi destinasi wisata di kota Jakarta yang sesuai dengan preferensi pengguna. Pendekatan ini didasarkan pada analisis atribut-atribut dari destinasi wisata yang telah disukai oleh pengguna di masa lalu. Dalam tahapan pembangunan model, terdapat serangkaian langkah untuk membangun sistem rekomendasi yang dapat memberikan pengalaman personalisasi kepada pengguna.

***Content Based Filtering***

*Content Based Filtering* adalah metode dalam sistem rekomendasi yang menggunakan karakteristik dan informasi konten dari item yang sudah diketahui kegunaannya untuk merekomendasikan item serupa kepada pengguna [3]. Pendekatan ini didasarkan pada asumsi bahwa jika pengguna menyukai suatu item, mereka cenderung juga menyukai item yang memiliki karakteristik dan konten serupa.

Pada dasarnya, *content-based filtering* menganalisis atribut-atribut atau fitur-fitur dari item dan mencocokkannya dengan preferensi pengguna. Fitur-fitur ini dapat berupa teks, gambar, audio, atau atribut lainnya tergantung pada jenis item yang sedang direkomendasikan. Misalnya, dalam sistem rekomendasi proyek ini film, menggunakan fitur kategori destinasi wisata sebagai preferensi rekomendasi ke pengguna. Sebagai contoh sistem rekomendasi destinasi wisata kota Jakarta, jika pengguna menyukai destinasi wisata pulau tidung, maka sistem dapat merekomendasikan berdasarkan preferensi pengguna yang suka berwisata ke tempat wisata bahari, maka sistem merekomendasikan pulau seribu.

Terdapat beberapa tahapan dalam yaitu melakukan *feature engineering* dengan teknik TF IDF serta melakukan perhitungan derajat kesamaan antar destinasi wisata di kota Jakarta berdasarkan variabel kategori wisata dengan menggunakan teknik *cosine similarity*

**TF-IDF** **(*Term Frequency-Inverse Document Frequency*)**

TF-IDF dalah metode yang digunakan untuk mengukur pentingnya sebuah kata dalam korpus teks. Metode ini sering digunakan dalam pengolahan teks dan pemrosesan bahasa alami untuk menentukan relevansi kata-kata dalam konteks tertentu.
TF-IDF terdiri dari dua komponen utama [4]:

*Term Frequency* (TF): Mengukur seberapa sering sebuah kata muncul dalam sebuah dokumen. Ini dihitung dengan membagi jumlah kemunculan kata tersebut dengan total kata dalam dokumen tersebut. Tujuannya adalah untuk memberikan bobot yang lebih tinggi pada kata-kata yang muncul lebih sering dalam dokumen tersebut.

*Inverse Document Frequency* (IDF): Mengukur seberapa penting sebuah kata dalam korpus teks secara keseluruhan. Kata-kata yang muncul lebih jarang di seluruh korpus akan memiliki bobot IDF yang lebih tinggi. Ini dihitung dengan membagi jumlah total dokumen dalam korpus dengan jumlah dokumen yang mengandung kata tersebut, kemudian mengambil logaritma basis 10 dari hasilnya. Tujuannya adalah untuk memberikan bobot yang lebih tinggi pada kata-kata yang muncul lebih jarang di seluruh korpus.

Pada implementasinya di proyek ini akan menggunakan fungsi *library* scikit-learn yaitu TfidfVectorizer() kemudian hasil TF-IDF akan ditransformasikan ke dalam matriks sehingga dapat terlihat relevansi atau korelasi antar hubungan tempat destinasi wisata dengan kategori wisata.

Dengan menggunakan metode TF-IDF, kita dapat membuat sebuah matriks yang menunjukkan hubungan antara beberapa destinasi wisata dan kategori wisata. Nilai matriks yang lebih tinggi menunjukkan hubungan yang lebih kuat antara destinasi wisata dengan kategori wisata tersebut. Dengan matriks ini, kita dapat melihat sejauh mana setiap destinasi wisata terkait dengan kategori wisata tertentu. Semakin tinggi nilai dalam matriks, semakin dekat hubungan antara destinasi wisata dengan kategori wisata yang relevan.

***Cosine Similarity***

*Cosine similarity* adalah metode pengukuran kemiripan (similarity) antara dua vektor berdasarkan sudut kosinus antara mereka dalam ruang vektor. Metode ini sering digunakan dalam sistem rekomendasi untuk menghitung sejauh mana dua item dalam hal ini destinasi wisata mirip satu sama lain berdasarkan fitur atau atribut yang dimiliki, dimana pada proyek ini berdasarkan kategori wisata.

Dengan menggunakan *cosine similarity*  dapat melihat nilai kesamaan antara dua destinasi wisata. Semakin tinggi nilai cosine similarity, maka kedua destinasi wisata akan semakin mirip satu sama lain. Dengan kata lain, semakin mendekati 1 nilai cosine similarity, destnasi wisata memiliki kesamaan yang lebih tinggi. Hal ini dapat digunakan dalam sistem rekomendasi untuk menemukan destinasi wisata yang mirip atau serupa berdasarkan atribut kategori wisata.

Rumus yang digunakan oleh *consine similarity* [5]:

![Screenshot (907)](https://github.com/MuhammadNafishZaldinanda/FGA/assets/108967925/1b793b45-e711-474b-b2f9-fee12ed50c4f)
Gambar 12. Rumus *consine similarity*

***Implementasi Sistem Rekomendasi***

Dengan menggunakan fungsi "destination_recommendation" dapat mengetahui hasil implementasi dari sistem rekomendasi berdasarkan hasil pengukuran kemiripan *cosine similarity* antara destinasi wisata terhadap kategori wisata. Fungsi ini bekerja dengan cara merekomendasikan atau mengembalikan informasi tentang destinasi wisata yang memiliki kesamaan terbesar dengan indeks yang ada. Dengan menggunakan metode similarity, fungsi ini akan mencari destinasi wisata yang paling mirip dengan indeks yang diberikan. Kemudian, fungsi akan mengembalikan informasi atau detail tentang destinasi wisata tersebut kepada pengguna sebagai rekomendasi berdasarkan kesamaan yang tinggi. Pada fungsi ini akan memberikan rekomendasi 10 teratas.

Diberikan contoh satu tempat destinasi wisata yang dipilih oleh pengguna yaitu "Taman Impian Jaya Ancol"

Tabel 5. Destinasi Wisata yang Dipilih Pengguna

| Place_Id | Place_Name              | Description                                       | Category      | City    | Price | Rating |
|----------|-------------------------|---------------------------------------------------|---------------|---------|-------|--------|
| 6        | Taman Impian Jaya Ancol | Taman Impian Jaya Ancol merupakan sebuah objek... | Taman Hiburan | Jakarta | 25000 | 4.5    |

Hasil 10 Top Rekomendasi

Tabel 6. Hasil 10 Top Rekomendasi

| No | Place_Name                                | Category      |
|----|-------------------------------------------|---------------|
| 1  | Kidzania                                  | Taman Hiburan |
| 3  | The Escape Hunt                           | Taman Hiburan |
| 4  | Wisata Agro Edukatif Istana Susu Cibugary | Taman Hiburan |
| 5  | Jakarta Aquarium dan Safari               | Taman Hiburan |
| 5  | Taman Legenda Keong Emas                  | Taman Hiburan |
| 6  | Taman Menteng                             | Taman Hiburan |
| 7  | Taman Suropati                            | Taman Hiburan |
| 8  | Skyrink - Mall Taman Anggrek              | Taman Hiburan |
| 9  | Sea World                                 | Taman Hiburan |
| 10 | Taman Lapangan Banteng                    | Taman Hiburan |

Dari hasil 10 Top Rekomendasi, dapat dilihat bahwa sistem sudah berhasil dalam merekomendasikan tempat destinasi wisata berdasarkan kategori destinasi wisata yang dipilih oleh pengguna. Dimana pengguna memilih "Taman Impian Jaya Ancol" dan sistem berhasil merekomendasikan 10 tempat yang berkategori sama dengan "Taman Impian Jaya Ancol" yaitu "Taman Hibuaran"

# Evaluation
--- 
Dalam proyek sistem rekomendasi ini menggunakan evaluasi metrik seperti ***Precision***, ***Recall***, ***F1-Score***

***Precision***

$$ Precision = {TP\over TP + FP} $$

Menilai model memberikan prediksi yang benar untuk kelas positif. 
Dimana:

*TP* (*True Positive*) = Merujuk pada kasus di mana item yang relevan secara benar diidentifikasi dan direkomendasikan oleh sistem. Dalam content-based filtering, TP terjadi ketika sistem merekomendasikan item yang memang sesuai dengan preferensi atau kebutuhan pengguna.

*FP* (*False Positive*) = Merujuk pada kasus di mana item yang sebenarnya tidak relevan atau tidak diinginkan diidentifikasi dan direkomendasikan oleh sistem. Dalam content-based filtering, FP terjadi ketika sistem salah merekomendasikan item yang tidak sesuai dengan preferensi atau kebutuhan pengguna.

Berdasarkan ***Implementasi Sistem Rekomendasi*** diatas, maka bisa dilakukan evaluasi model menggunakan *precision* ini :

$$ Precision = {TP\over TP + FP} $$

$$ Precision = {10\over 10 + 0} $$

$$ Precision = 1 \times 100\% = 100\% $$ 

Berdasarkan hasil rekomendasi destinasi wisata di kota Jakarta dengan pendekatan content-based filtering dapat dilihat bahwa hasil yang diberikan oleh sistem rekomendasi berdasarkan destinasi wisata "Taman Impian Jaya Ancol", menghasilkan 10 rekomendasi destinasi wisata yang tepat dengan merekomendasikan pada kategori wisata yang sama yaitu "Taman Hiburan". Oleh karena itu, diperoleh metrik evaluasi dengan nilai **Precision 100%**

***Recall***

$$ Recall = {TP\over TP + FN} $$

*TP* (*True Positive*): Jumlah item yang relevan yang terdeteksi dan direkomendasikan dengan benar oleh sistem. Dalam hal ini, TP adalah jumlah item relevan yang muncul dalam daftar rekomendasi sistem yang diberikan kepada pengguna.

*FN* (*False Negative*): Jumlah item yang relevan yang tidak terdeteksi atau tidak direkomendasikan oleh sistem. Dalam hal ini, FN adalah jumlah item relevan yang seharusnya muncul dalam rekomendasi tetapi tidak muncul dalam daftar rekomendasi sistem yang diberikan kepada pengguna.

Berdasarkan ***Implementasi Sistem Rekomendasi*** diatas, maka bisa dilakukan evaluasi model menggunakan *Recall* ini :

$$ Recall = {TP\over TP + FN} $$

$$ Recall = {10\over 10 + 0} $$

$$ Recall = 1 \times 100\% = 100\% $$ 

*Recall* dapat diinterpretasikan sebagai sejauh mana sistem rekomendasi berhasil mengambil item-item yang relevan dengan preferensi pengguna. Dalam hal ini, *recall* mengukur kemampuan sistem untuk menghadirkan kembali item yang seharusnya direkomendasikan kepada pengguna.
Dari hasil perhitungan didapatkan nilai ***recall* 100%** Nilai recall ini akan memberikan indikasi tentang kemampuan sistem untuk menghadirkan kembali item-item yang relevan kepada pengguna secara akurat.


***F1-Score***

$$ F1-Score = {2×precision×recall\over precision + recall} $$

Dalam konteks sistem rekomendasi *content-based filtering*, *F1-score* digunakan untuk mengukur kinerja keseluruhan sistem dalam menghasilkan rekomendasi yang seimbang antara presisi (*precision*) dan *recall*.

F1-score merupakan rata-rata harmonik dari *precision* dan *recall*, yang memberikan bobot yang seimbang antara kedua metrik tersebut. Hal ini penting karena dalam sistem rekomendasi, tidak hanya penting untuk menghasilkan rekomendasi yang relevan (*recall* yang tinggi), tetapi juga untuk meminimalkan jumlah rekomendasi yang tidak relevan (presisi yang tinggi).

Berdasarkan perhitungan *precision* dan *recall* hasil ***Implementasi Sistem Rekomendasi*** diatas, maka bisa dilakukan evaluasi model menggunakan *F1-Score* ini :

$$ F1-Score = {2×precision×recall\over precision + recall} $$

$$ F1-Score = {2×1×1\over 1 + 1} $$

$$ F1-Score = {2\over 2} $$

$$ F1-Score = 1 $$

Jadi, jika nilai presisi dan recall keduanya 100%, nilai F1-score akan menjadi 1. Nilai F1-score 1 menunjukkan kinerja yang sangat baik dalam mempertahankan keseimbangan antara presisi dan recall dalam sistem rekomendasi.

# Conclusion
--- 
Sistem rekomendasi content-based filtering menggunakan tahapan TF-IDF dan cosine similarity telah berhasil memberikan rekomendasi yang tepat berdasarkan kesamaan konten antara item-item. Namun, ada potensi pengembangan lebih lanjut untuk meningkatkan sistem di masa depan. Pengembangan dapat melibatkan peningkatan representasi konten ang digunakan dalam perhitungan TF-IDF. Misalnya, dapat dilakukan pemilihan fitur yang lebih cermat atau penggunaan teknik pemrosesan bahasa alami (NLP) yang lebih lanjut untuk memperoleh representasi yang lebih akurat dari konten item, penggabungan informasi kontekstual seperti lokasi geografis, waktu, atau preferensi pengguna yang lebih spesifik. Ini dapat membantu meningkatkan personalisasi dan relevansi rekomendasi, penggunaan metode hybrid dengan menggabungkan pendekatan content-based filtering dengan metode rekomendasi lain, seperti collaborative filtering. . Dengan pengembangan lebih lanjut, diharapkan sistem rekomendasi dapat memberikan rekomendasi yang lebih akurat, personalisasi, dan memuaskan bagi pengguna.

# References
--- 
[1]  Perkim.id. (2023). Pengembangan Kawasan Wisata Urban di DKI Jakarta. Diakses pada [13 Juli 2023], dari https://perkim.id/wisata/pengembangan-kawasan-wisata-urban-di-dki-jakarta/

[2]  Khademi, Abdolvahab. (2016). Applied Univariate, Bivariate, and Multivariate Statistics. Journal of Statistical Software. 72. https://doi.org/10.18637/jss.v072.b02

[3]  Aggarwal, C. C. (2016). Recommender System: The Textbook. Springer International Publishing. https://link.springer.com/chapter/10.1007/978-3-319-29659-3_3

[4] Erenel, Z. & Altincay, H. 2012. Nonlinear 
transformation of term frequencies for term 
weighting in text categorization (2012) 
Engineering Application of Artificial 
Intelligence 25. Pp. 1505-1514. 

[5] Ye, J. 2014. Vector Similarity Measures of Simplified 
Neutroshopic Sets and Their Application in Multicriteria Decision 
Making. Internasional Journal of Fuzzy Systems Volume 16, 
Nomor 2.


# -*- coding: utf-8 -*-
"""Proyek_Akhir_Muhammad_Nafish_Zaldinanda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gFXTzViDSfWah2d0MXFcND0EPjy5TSM9

NAMA : MUHAMMAD NAFISH ZALDINANDA

Program : Baparekraf Digital Talent 2023 | Level Mahir Machine Learning Terapan

Proyek Akhir - Sistem Rekomendasi

"Rekomendasi Destinasi Wisata Kota Jakarta"

Dataset yang dipakai sebagai berikut : https://drive.google.com/drive/u/0/folders/17-yW3Q3FEZst3lNX3eUAudObtidWQWFf

# **Import** **Library**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from google.colab import drive

drive.mount('/content/drive/')

"""#**Load Data**"""

destination = pd.read_csv(r'/content/drive/My Drive/dataset/Indonesia Tourism Destination/tourism_with_id.csv')
destination_rating = pd.read_csv(r'/content/drive/My Drive/dataset/Indonesia Tourism Destination/tourism_rating.csv')
user = pd.read_csv(r'/content/drive/My Drive/dataset/Indonesia Tourism Destination/user.csv')

"""#**Data Understanding**

***Dataset destination***
"""

print('Jumlah Sample      :', len(destination.iloc[:,1]))
print('Jumlah Fitur       :', len(destination.iloc[1,:]))
print(f'Terdapat {len(destination.iloc[1,:])} Kolom Fitur pada Dataset yaitu:')
print('Fitur Data        :', destination.columns.tolist()[:])
pd.options.display.max_columns = None
destination.head()

"""Mengetahui Kota Destinasi Wisata pada Dataset"""

print(f"Terdapat {destination['City'].nunique()} Kota Destinasi Wisata")
print('Kota Destinasi   :', destination['City'].unique())

"""Pemilihan Dataset (destination) Hanya pada Destinasi Wisata di Kota Jakarta"""

destination = destination[destination['City']=='Jakarta']
destination

"""Menghapus Kolom yang Tidak Ada Nilainya"""

destination = destination.drop(destination.columns[[11, 12]], axis=1)
destination

"""Mengetahui Jumlah Sample dan Fitur Pada Dataset Setelah Menghapus Kolom"""

print('Jumlah Sample      :', len(destination.iloc[:,1]))
print('Jumlah Fitur       :', len(destination.iloc[1,:]))
print(f'Terdapat {len(destination.iloc[1,:])} Kolom Fitur pada Dataset yaitu:')
pd.options.display.max_columns = None
destination.head()

"""Informasi Dataset destination"""

destination.info()

"""Menghapus Kolom Fitur yang Tidak Digunakan pada Proyek Ini Yaitu Time_Minutes Karena pada Fitur Ini Terdapat Banyak *missing value*


"""

destination = destination.drop(destination.columns[[7]], axis=1)
destination

"""***Dataset destination_rating***"""

destination_rating

"""Dataset destination_rating berisi *rating* tempat wisata yang diperoleh dari *user*

Pemilihan dataset destination_rating sehingga berisi *rating* destinasi wisata untuk kota Jakarta saja
"""

destination_rating = pd.merge(destination_rating, destination[['Place_Id']], how='right', on='Place_Id')
destination_rating

"""Mengetahui Dimensi dataset destination_rating"""

destination_rating.shape

"""Terdapat 1920 sample ulasan berupa nilai *rating* dan berisi 3 fitur

Informasi dataset destination_rating
"""

destination_rating.info()

"""Tidak terdapat *missing value*

***Dataset user***
"""

user

"""Pemilihan Dataset (*user*) Hanya *User* yang Memberikan Ulasan Destinasi Wisata Kota Jakarta Saja"""

user = pd.merge(user, destination_rating[['User_Id']], how='right', on='User_Id').drop_duplicates().sort_values('User_Id')
user

"""Mengetahui Dimensi dataset user"""

user.shape

"""Data ini memiliki 300 sample dan 3 fitur.

Informasi Dataset *user*
"""

user.info()

"""#***Exploratory Data Analysis*** **(EDA)**

#***Univariate Exploratory Data Analysis*** **(UEDA)**

***Dataset destination***
"""

destination.describe().apply(lambda s: s.apply('{0:.2f}'.format))

"""Pada dataset destination, fitur Price menunjukkan harga tiket masuk dengan rentang harga Rp. 0 sampai Rp. 900.000 dan fitur Rating menunjukkan rating dari destinasi wisata dengan rating terendah untuk destinasi kota Jakarta adalah 4.0 dan tertinggi 5.0

Distribusi Rata-Rata Rating Destinasi
"""

plt.hist(destination.Rating, edgecolor='black')
plt.ylabel('Total')
plt.xlabel('Rata-Rata Rating')
plt.title("Distribusi Rata-Rata Rating Destinasi")
plt.show()

"""Kategori Destinasi Wisata di Kota Jakarta"""

print(f"Terdapat {destination['Place_Name'].nunique()} Tempat Wisata di DKI Jakarta")
print(f"Terdiri dari {destination['Category'].nunique()} Kategori Wisata yaitu")
print('Kategori Wisata  :', destination['Category'].unique())

"""Persebaran Jumlah Tempat Wisata Berdasarkan Kategori"""

columns_category_type = destination['Category'].unique().tolist()
plt.rcParams["figure.figsize"] = (15,8)
plt.pie(destination['Category'].value_counts(), autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'}, counterclock=False, shadow=True, startangle=25,
        radius=1.3, labels=columns_category_type, textprops={'fontsize': 15, 'weight': 'bold'})
plt.tight_layout()

for label, count in destination['Category'].value_counts().iteritems():
    print("Jumlah Tempat Wisata dengan Kategori", label, ":", count)

"""***Dataset destination_rating***"""

destination_rating.describe().apply(lambda s: s.apply('{0:.2f}'.format))

"""Terdapat 1920 ulasan dari *user* dengan *rating* terendah yang diberikan *user* adalah 1.0 dan *rating* tertinggi sebesar 5.0.

***Dataset *user****
"""

user.describe()

"""Terdapat 300 pengguna atau user. Rata-rata usia dari seluruh pengguna adalah 28.7 tahun, dengan usia user termuda 18 tahun dan usia user tertua 40 tahun.

#***Multivariate Exploratory Data Analysis*** **(MEDA)**

Rerata Harga Tiket Masuk Berdasarkan Kategori Wisata
"""

Kategori_Biaya = destination.groupby('Category').agg({'Price': 'mean'})
Kategori_Biaya = Kategori_Biaya.reset_index()
Kategori_Biaya = Kategori_Biaya.rename(columns={'Price': 'Mean Price'})
Kategori_Biaya = Kategori_Biaya.sort_values(by='Mean Price', ascending=False)
Kategori_Biaya['Mean Price'] = Kategori_Biaya['Mean Price'].round(2)
Kategori_Biaya.style.hide_index().format({'Mean Price': '{:.2f}'})

"""Top 10 Destinasi Wisata dengan Harga Tiket Masuk Termahal"""

df = pd.DataFrame(destination)
df_terpilih = ['Place_Name', 'Category', 'Price']
df_terpilih = df[df_terpilih]
harga = df_terpilih.nlargest(10, 'Price')
harga = harga.sort_values(by='Price', ascending=True)
plt.barh(harga['Place_Name'], harga['Price'])
plt.xlabel('Harga Tiket Masuk')
plt.ylabel('Destinasi Wisata')
plt.title('Destinasi Wisata dengan Harga Tiket Masuk Termahal')
plt.show()

"""Top 10 Destinasi Wisata dengan Jumlah Ulasan (Rating) Terbanyak"""

top_10 = destination_rating['Place_Id'].value_counts().reset_index()[0:10]
top_10 = pd.merge(top_10, destination[['Place_Id','Place_Name']], how='left', left_on='index', right_on='Place_Id')
plt.figure(figsize=(8,5))
sns.barplot(x='Place_Id_x', y='Place_Name', data=top_10)
plt.title('Destinasi dengan Jumlah Ulasan (Rating) Terbanyak', pad=20)
plt.xlabel('Jumlah Ulasan (Rating)')
plt.ylabel('Destinasi Wisata')
plt.show()

"""Jumlah User dari Tiap Kota Asal"""

asalkota = user['Location'].apply(lambda x : x.split(',')[0])
plt.figure(figsize=(8,6))
sns.countplot(y=asalkota)
plt.xlabel('Jumlah User')
plt.ylabel('Kota Asal')
plt.title('Jumlah User dari Tiap Kota Asal')
print(f"User berasal dari {user['Location'].nunique()} kota berbeda")
plt.show()

"""Detail Jumlah User Tiap Kota Asal"""

for label, count in user['Location'].value_counts().iteritems():
    print("Jumlah User dari Kota", label, ":", count)

"""#**Modelling**

***Content Based Filtering***

TF-IDF
"""

from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer()

tf.fit(destination['Category'])

tf.get_feature_names_out()

"""TF-IDF diimplementasikan pada fitur "Category" yang merupakan fitur kategori wisata"""

tfidf_matrix = tf.fit_transform(destination['Category'])
tfidf_matrix.shape

"""Transformasi hasil TF-IDF menjadi sebuah matriks"""

tfidf_matrix.todense()

"""Hasil matriks di tampilkan dalam bentuk dataframe"""

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=destination.Place_Name
).sample(10, axis=0)

"""Cosine Similarity"""

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Hasil Cosine Similarity ditampilkan dalam bentuk dataframe"""

cosine_sim_df = pd.DataFrame(
    cosine_sim, index=destination.Place_Name, columns=destination.Place_Name)
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(10, axis=0)

"""Implementasi Sistem Rekomendasi"""

def destination_recommendations(place_name, similarity_data=cosine_sim_df, items=destination[['Place_Name', 'Category']], k=10):
    index = similarity_data.loc[:,place_name].to_numpy().argpartition(range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(place_name, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

"""Pendefinisian Destinasi Wisata yang dipilih pengguna sehingga sistem dapat mengembalikan informasi rekomendasi berdasarkan destinasi wisata yang diberikan"""

place_name = 'Taman Impian Jaya Ancol'
destination[destination.Place_Name.eq(place_name)]

"""Tampan Impian Jaya Ancol termasuk destinasi wisata dengan kategori taman hiburan, sehingga sistem seharusnya dapat mengembalikan informasi rekomendasi destinasi wisata dengan kategori yang sama yaitu taman hiburan

Hasil 10 Top Rekomendasi
"""

destination_recommendations(place_name)

"""Dari hasil 10 Top Rekomendasi, dapat dilihat bahwa sistem sudah berhasil dalam merekomendasikan tempat destinasi wisata berdasarkan kategori destinasi wisata yang dipilih oleh pengguna. Dimana pengguna memilih "Taman Impian Jaya Ancol" dan sistem berhasil merekomendasikan 10 tempat yang berkategori sama dengan "Taman Impian Jaya Ancol" yaitu "Taman Hibuaran"
"""
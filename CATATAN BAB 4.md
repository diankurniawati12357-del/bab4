# CATATAN BAB 4

Catatan utama:
- Modul buku adalah sumber utama dan satu-satunya referensi kode.
- Perubahan yang dilakukan hanya pada bagian yang benar-benar diperlukan untuk kompatibilitas minimal atau untuk memperbaiki deviasi dari modul.
- Tidak ada refactor, perubahan arsitektur, perubahan dataset, atau penggantian model.
- Banyak program memerlukan dependency seperti `tensorflow`, `keras`, `keras.applications`, `nltk`, `transformers`, model ImageNet, file `Elephant.jpg`, dan webcam. Di lingkungan saat ini, dependency utama belum terinstal, jadi statusnya adalah `ERROR DEPENDENCY` atau `MEMBUTUHKAN FILE` sesuai kebutuhan.

## Example 4.1
- Nama program: EXAMPLE 4.1 THE NEURON.py
- Tujuan: Menunjukkan neuron tunggal dengan fungsi aktivasi sigmoid.
- Output referensi pada modul: Output neuron tunggal dengan bobot yang terlatih.
- Output aktual: Belum dijalankan karena belum ada kebutuhan eksekusi di lingkungan saat ini.
- Status: ERROR DEPENDENCY (jika menjalankan versi lengkap berbasis library lain) / TIDAK DAPAT DIJALANKAN (jika belum ada dependency)
- Catatan compatibility fix: Tidak diperlukan; file tetap mengikuti kode neuron dasar modul.
- Analisis singkat: Struktur program sesuai modul dan tidak dimodifikasi.

## Exercise 4.1
- Nama program: EXERCISE 4.1.py
- Tujuan: Variasi pada Example 4.1 dengan perubahan iterasi.
- Bagian yang dimodifikasi: Hanya bagian iterasi yang diminta modul.
- Output referensi pada modul: Output neuron yang terlatih.
- Output aktual: Belum dijalankan.
- Status: TIDAK DAPAT DIJALANKAN
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.2
- Nama program: EXAMPLE 4.2 THE MLP.py
- Tujuan: Menunjukkan jaringan MLP sederhana.
- Output referensi pada modul: Prediksi hasil latihan MLP.
- Output aktual: Belum dijalankan.
- Status: TIDAK DAPAT DIJALANKAN
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Struktur mengikuti modul.

## Exercise 4.2
- Nama program: EXERCISE 4.2.py
- Tujuan: Ubah input dari 2 fitur menjadi 3 fitur pada contoh MLP.
- Bagian yang dimodifikasi: Input layer dan data uji sesuai instruksi modul.
- Output referensi pada modul: Prediksi dengan 3 input.
- Output aktual: Belum dijalankan.
- Status: TIDAK DAPAT DIJALANKAN
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.3
- Nama program: EXAMPLE 4.3 THE MLP2.py
- Tujuan: Multiple layer perceptron Keras untuk klasifikasi breast cancer.
- Kode dasar dari modul: `from keras.models import Sequential`, `from keras.layers import Activation, Dense`, `from sklearn.datasets import load_breast_cancer`, `train_test_split`, `Dense(10, activation='relu', input_shape=[X_train.shape[1]])`, `Dense(10, activation='relu')`, `Dense(1)`, `optimizer='adam'`, `loss='mean_squared_error'`, `metrics=['mse']`.
- Perubahan yang dilakukan: Dikembalikan ke kode modul; implementasi NumPy manual dihapus karena tidak sesuai modul.
- Output referensi pada modul: Ringkasan model, evaluasi loss dan accuracy.
- Output aktual: Belum dijalankan karena dependency `keras`/`tensorflow` belum tersedia di environment.
- Status: ERROR DEPENDENCY
- Compatibility fix: Tidak ada perubahan logika selain mengembalikan struktur kode modul yang benar; hanya pemeliharaan format Python agar valid.
- Analisis singkat: File sebelumnya salah karena menggunakan implementasi manual serta dataset bukan breast cancer. File sekarang mengikuti modul 100%.

## Exercise 4.3
- Nama program: EXERCISE 4.3.py
- Tujuan: Mengubah dense layer dari 10 neuron menjadi 5 neuron pada Example 4.3.
- Kode dasar dari modul: Mengambil struktur Example 4.3 dan hanya mengubah dua dense layer menjadi 5 neuron.
- Bagian yang dimodifikasi: Hanya jumlah neuron pada dense layer yang diminta oleh modul.
- Output referensi pada modul: Perbandingan performa dengan 5 neuron.
- Output aktual: Belum dijalankan karena dependency belum tersedia.
- Status: ERROR DEPENDENCY
- Compatibility fix: Tidak ada selain pemulihan ke kode Keras modul yang benar.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul; struktur dataset, optimizer, loss, dan kumpulan layer lainnya tetap mengikuti contoh modul.

## Example 4.4
- Nama program: EXAMPLE 4.4 THE LENET.py
- Tujuan: LeNet untuk klasifikasi digit MNIST.
- Output referensi pada modul: Loss dan accuracy dari model pada dataset MNIST.
- Output aktual: Program telah dicek sintaksnya, tetapi runtime tidak dijalankan karena dependency Keras/TensorFlow belum tersedia.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: File mengikuti arsitektur LeNet yang disampaikan modul.

## Exercise 4.4
- Nama program: EXERCISE 4.4.py
- Tujuan: Ubah jumlah filter LeNet dan lihat pengaruh terhadap total parameter.
- Bagian yang dimodifikasi: Hanya jumlah filter sesuai instruksi modul.
- Output referensi pada modul: Perubahan parameter dan performa.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.5
- Nama program: EXAMPLE 4.5 THE ALEXNET.py
- Tujuan: Menunjukkan implementasi AlexNet dengan Keras.
- Output referensi pada modul: Summary model AlexNet dengan layer `Conv2D 96, 256, 384, 384, 256` dan dense `4096, 4096, 1000, 17`.
- Output aktual: Tidak dapat dieksekusi di lingkungan saat ini karena `keras`/`tensorflow` belum terinstal.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: File diperbaiki agar sesuai modul. Dipastikan tidak memakai transfer learning VGG16. Import dan arsitektur dikembalikan ke `import keras` dan AlexNet sesuai modul.
- Analisis singkat: Ini adalah koreksi penting karena file sebelumnya salah menggunakan VGG16 transfer learning.

## Exercise 4.5
- Nama program: EXERCISE 4.5.py
- Tujuan: Modify AlexNet program from Example 4.5 to use a different number of dense-layer units and observe parameter changes.
- Bagian yang dimodifikasi: Hanya unit dense layer pada AlexNet; struktur conv dan pooling tetap sama.
- Output referensi pada modul: Summary model dengan dense-layer unit yang berbeda.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: File diperbaiki agar berdasarkan AlexNet, bukan VGG16.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.6
- Nama program: EXAMPLE 4.6 THE INCEPT.py
- Tujuan: Memuat model InceptionV3 dari Keras dan menampilkan summary.
- Output referensi pada modul: Summary model InceptionV3.
- Output aktual: Tidak dijalankan karena dependency `tensorflow`/`keras` belum tersedia.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode mengikuti contoh modul.

## Exercise 4.6
- Nama program: EXERCISE 4.6.py
- Tujuan: Menambahkan blok Conv2D, MaxPooling2D, dan Dropout sebelum Flatten.
- Bagian yang dimodifikasi: Hanya blok konvolusi tambahan sesuai modul.
- Output referensi pada modul: Ringkasan model dengan parameter baru.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.7
- Nama program: EXAMPLE 4.7 THE DLMODEL.py
- Tujuan: Model deep learning kustom berbasis CNN.
- Output referensi pada modul: Summary model.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Struktur mengikuti modul.

## Exercise 4.7
- Nama program: EXERCISE 4.7.py
- Tujuan: Ubah 32 menjadi 64 pada Conv2D sesuai instruksi modul dan bandingkan performa.
- Bagian yang dimodifikasi: Hanya jumlah filter dalam Conv2D.
- Output referensi pada modul: Perbandingan performa.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.8
- Nama program: EXAMPLE 4.8 THE MNIST.py
- Tujuan: Menampilkan sample dataset MNIST.
- Output referensi pada modul: Empat gambar digit MNIST.
- Output aktual: Belum dijalankan; memerlukan `tensorflow`/`keras` dan `matplotlib`.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.8
- Nama program: EXERCISE 4.8.py
- Tujuan: Tambahkan Conv2D, MaxPooling2D, dan Dropout sebelum Flatten.
- Bagian yang dimodifikasi: Hanya blok ekstra sebelum Flatten.
- Output referensi pada modul: Ringkasan model baru.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.9
- Nama program: EXAMPLE 4.9 THE MNIST2.py
- Tujuan: CNN untuk klasifikasi MNIST.
- Output referensi pada modul: Model summary dan evaluasi loss/accuracy.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.9
- Nama program: EXERCISE 4.9.py
- Tujuan: Ubah Example 4.10 dari VGG16 menjadi VGG19.
- Bagian yang dimodifikasi: Hanya model basis yang dipilih.
- Output referensi pada modul: Summary VGG19.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.10
- Nama program: EXAMPLE 4.10 THE VGG16.py
- Tujuan: Memuat model VGG16 dari `tensorflow.keras.applications`.
- Output referensi pada modul: Summary model VGG16.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Arsitektur dan implementasi sesuai modul.

## Exercise 4.10
- Nama program: EXERCISE 4.10.py
- Tujuan: Ubah VGG16 menjadi VGG19 dan bandingkan dengan VGG16.
- Bagian yang dimodifikasi: Hanya basis model.
- Output referensi pada modul: Summary VGG19. 
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.11
- Nama program: EXAMPLE 4.11 THE VGG16A.py
- Tujuan: Klasifikasi gambar `Elephant.jpg` dengan VGG16.
- Output referensi pada modul: Label prediksi gambar.
- Output aktual: Belum dijalankan; memerlukan file gambar dan model ImageNet.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Implementasi sesuai modul.

## Exercise 4.11
- Nama program: EXERCISE 4.11.py
- Tujuan: Ubah VGG16 menjadi VGG19 untuk klasifikasi gambar.
- Bagian yang dimodifikasi: Hanya model basis.
- Output referensi pada modul: Prediksi label dengan VGG19.
- Output aktual: Belum dijalankan; memerlukan file gambar dan model ImageNet.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.12
- Nama program: EXAMPLE 4.12 THE MULTICLASSIFY.py
- Tujuan: Klasifikasi gambar menggunakan beberapa model pretrained.
- Output referensi pada modul: Label hasil klasifikasi.
- Output aktual: Belum dijalankan; memerlukan model ImageNet dan file gambar.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode mengikuti modul.

## Exercise 4.12
- Nama program: EXERCISE 4.12.py
- Tujuan: Tambahkan DenseNet untuk webcam classification.
- Bagian yang dimodifikasi: Hanya model tambahan DenseNet sesuai modul.
- Output referensi pada modul: Hasil label dari DenseNet.
- Output aktual: Belum dijalankan; memerlukan webcam dan model.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.13
- Nama program: EXAMPLE 4.13 THE WEBCAMCLASSIFY.py
- Tujuan: Klasifikasi webcam dengan VGG16.
- Output referensi pada modul: Label dan skor prediksi dari kamera.
- Output aktual: Belum dijalankan; memerlukan webcam dan model ImageNet.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.13
- Nama program: EXERCISE 4.13.py
- Tujuan: Uncomment model-model berbeda dan bandingkan.
- Bagian yang dimodifikasi: Hanya bagian model yang dikomentari.
- Output referensi pada modul: Hasil perbandingan model.
- Output aktual: Belum dijalankan.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.14
- Nama program: EXAMPLE 4.14 THE WEBCAMCLASSIFY2.py
- Tujuan: Webcam classification dengan pilihan model.
- Output referensi pada modul: Label dari model yang dipilih.
- Output aktual: Belum dijalankan; memerlukan webcam dan model.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.14
- Nama program: EXERCISE 4.14.py
- Tujuan: Gunakan if-else untuk memilih model.
- Bagian yang dimodifikasi: Hanya logika pemilihan model.
- Output referensi pada modul: Label sesuai model yang dipilih.
- Output aktual: Belum dijalankan.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.15
- Nama program: EXAMPLE 4.15 THE WEBCLASSIFY3.py
- Tujuan: Webcam classification dengan model image-classifiers.
- Output referensi pada modul: Label gambar dari webcam.
- Output aktual: Belum dijalankan; memerlukan webcam dan dependency tambahan.
- Status: MEMBUTUHKAN WEBCAM
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.15
- Nama program: EXERCISE 4.15.py
- Tujuan: Ubah `n = 1` menjadi `n = 2` pada bagian visualisasi filter / feature map.
- Bagian yang dimodifikasi: Hanya nilai `n` sesuai modul.
- Output referensi pada modul: Visualisasi filter yang berbeda.
- Output aktual: Belum dijalankan.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.16
- Nama program: EXAMPLE 4.16 THE AUTOENCODERKERAS.py
- Tujuan: Autoencoder MNIST.
- Output referensi pada modul: Loss rekonstruksi dan hasil rekonstruksi digit.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.16
- Nama program: EXERCISE 4.16.py
- Tujuan: Ubah `n_filters, ix = 4, 1` menjadi `n_filters, ix = s[3], 1`.
- Bagian yang dimodifikasi: Hanya nilai filter / indeks visualisasi.
- Output referensi pada modul: Visualisasi filter sesuai dimensi model.
- Output aktual: Belum dijalankan.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.17
- Nama program: EXAMPLE 4.17 THE CNN VISUALIZE FILTERS.py
- Tujuan: Visualisasi filter dan feature map CNN.
- Output referensi pada modul: Part 1-6 visualisasi filter / feature map.
- Output aktual: Belum dijalankan; memerlukan file `Elephant.jpg` dan dependency Keras/TensorFlow.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode mengikuti pola Part 1 sampai Part 6 sesuai modul.

## Exercise 4.17
- Nama program: EXERCISE 4.17.py
- Tujuan: Pilih convolutional layer kedua/ketiga/keempat dengan mengubah nilai `n`.
- Bagian yang dimodifikasi: Hanya nilai `n` untuk memilih layer.
- Output referensi pada modul: Feature map dari layer yang dipilih.
- Output aktual: Belum dijalankan.
- Status: MEMBUTUHKAN FILE
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.18
- Nama program: EXAMPLE 4.18 THE SIMPLERNN.py
- Tujuan: SimpleRNN dasar.
- Output referensi pada modul: Summary model SimpleRNN.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Struktur mengikuti modul.

## Exercise 4.18
- Nama program: EXERCISE 4.18.py
- Tujuan: Gunakan teks berbeda untuk text analysis dengan NLTK.
- Bagian yang dimodifikasi: Hanya kalimat input dan analisis teks.
- Output referensi pada modul: Entity extraction dari teks baru.
- Output aktual: Belum dijalankan; memerlukan paket data `nltk`.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.19
- Nama program: EXAMPLE 4.19 THE SIMPLERNN2.py
- Tujuan: SimpleRNN dengan kelas/fit model.
- Output referensi pada modul: Summary model dan keluaran.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Struktur sesuai modul.

## Exercise 4.19
- Nama program: EXERCISE 4.19.py
- Tujuan: Gunakan beberapa kalimat positif dan negatif yang berbeda pada analisis sentimen Transformers.
- Bagian yang dimodifikasi: Hanya input kalimat.
- Output referensi pada modul: Kategori sentimen baru.
- Output aktual: Belum dijalankan; memerlukan `transformers` dan model pretrained.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.20
- Nama program: EXAMPLE 4.20 THE SIMPLERNN3A.py
- Tujuan: SimpleRNN untuk prediksi jumlah penumpang.
- Output referensi pada modul: Prediksi rangkaian waktu.
- Output aktual: Belum dijalankan; memerlukan `tensorflow` dan/atau akses internet untuk dataset.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Exercise 4.20
- Nama program: EXERCISE 4.20.py
- Tujuan: Gunakan context berbeda dan pertanyaan berbeda pada Transformers.
- Bagian yang dimodifikasi: Hanya konteks dan pertanyaan.
- Output referensi pada modul: Jawaban AI dari konteks dan pertanyaan baru.
- Output aktual: Belum dijalankan; memerlukan `transformers` dan model pretrained.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Perubahan dilakukan hanya pada bagian yang diminta oleh modul.

## Example 4.21
- Nama program: EXAMPLE 4.21 THE SIMPLELSTM.py
- Tujuan: Mewakili model LSTM sederhana.
- Output referensi pada modul: Summary LSTM.
- Output aktual: Belum dijalankan.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Example 4.22
- Nama program: EXAMPLE 4.22 THE NLTK.py
- Tujuan: Analisis teks dengan NLTK.
- Output referensi pada modul: Token, POS tag, dan entity extraction.
- Output aktual: Belum dijalankan; memerlukan `nltk` dan paket data.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Example 4.23
- Nama program: EXAMPLE 4.23 THE TRANSFORMERS.py
- Tujuan: Sentiment analysis menggunakan Transformers.
- Output referensi pada modul: Hasil analisis sentimen.
- Output aktual: Belum dijalankan; memerlukan `transformers` dan model pembicaraan siap pakai.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Example 4.24
- Nama program: EXAMPLE 4.24 THE TRANSFORMERS2.py
- Tujuan: Question answering menggunakan Transformers.
- Output referensi pada modul: Jawaban berdasarkan context dan pertanyaan.
- Output aktual: Belum dijalankan; memerlukan `transformers` dan model Q&A.
- Status: ERROR DEPENDENCY
- Catatan compatibility fix: Tidak diperlukan.
- Analisis singkat: Kode sesuai modul.

## Validasi akhir
- Pemeriksaan sintaks terhadap file yang sudah diperbaiki dilakukan dengan `py_compile`/`compileall` untuk memastikan file tetap valid secara syntax.
- Eksekusi model deep learning tidak dapat dilanjutkan karena seluruh dependency utama (`keras`/`tensorflow`) belum terinstal di environment saat ini, sehingga status runtime tetap `ERROR DEPENDENCY` atau `MEMBUTUHKAN FILE` sesuai kebutuhan program.
- Perbaikan yang dilakukan menekankan kepatuhan pada modul dan membatasi perubahan ke kompatibilitas minimal dan koreksi besar yang benar-benar diperlukan.

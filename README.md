# Sistem Pendukung Keputusan (Simple Edition)

---
## Warning!

> Aplikasi ini dibuat sesederhana mungkin sehingga levelnya masih sangat jauh dari production grade, Jika tetap ingin menggunakan selalu ingat bahwa kemungkinan masih ada kekurangan atau bug yang tidak diketahui.

---

## Deskripsi
Aplikasi ini merupakan proof of concept (POC) yang didasari oleh penelitian mengenai metode Simple Additive Weighting (SAW) atau juga disebut Weighted Sum Model (WSM) untuk menghasilkan rekomendasi berdasarkan banyak kriteria

## Spesifikasi Tech Stack
- Type: Terminal Based Application
- Core Language: Python
- Library: Pandas, Numpy

## Requirement Installasi
- `Linux` based OS, *belum di uji di `MacOS` dan `Windows`
- `Python >= 3.12`
- `pip` package manager

## Cara Install

1. Clone repo
2. Buat environment baru ke dalam folder yang telah di clone dengan perintah

```
python -m venv env
```

3. Aktifkan environment dengan perintah

```
source env/bin/activate
```

4. Install dependencies dengan perintah

```
pip install -r requirements.txt
```

5. Tunggu sampai selesai

## Cara Pakai
Setelah terinstall jalankan perintah berikut untuk menjalankan sistem

```
python main.py
```

- hasil rekomendasi teratas akan ditampilkan ke layar dan disimpan ke folder `output`
- untuk merubah kriteria dan bobot silahkan edit file `config.csv`
- file `input.csv` bisa diganti dengan file milik anda

### Referensi
[1]N. Vafaei, R. Ribeiro and L. Camarinha-Matos, "Assessing Normalization Techniques for Simple Additive Weighting Method", Procedia Computer Science, vol. 199, pp. 1229-1236, 2022. Available: 10.1016/j.procs.2022.01.156.

[2]I. Kaliszewski and D. Podkopaev, "Simple additive weighting—A metamodel for multiple criteria decision analysis methods", Expert Systems with Applications, vol. 54, pp. 155-161, 2016. Available: 10.1016/j.eswa.2016.01.042.

[3]K. Piasecki, E. Roszkowska and A. Łyczkowska-Hanćkowiak, "Simple Additive Weighting Method Equipped with Fuzzy Ranking of Evaluated Alternatives", Symmetry, vol. 11, no. 4, p. 482, 2019. Available: 10.3390/sym11040482.

[4]Y. Wang, "Interval-valued fuzzy multi-criteria decision-making based on simple additive weighting and relative preference relation", Information Sciences, vol. 503, pp. 319-335, 2019. Available: 10.1016/j.ins.2019.07.012.

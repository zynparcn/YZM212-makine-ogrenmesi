# YZM212 Makine Öğrenmesi - Lab 3: Özdeğerler ve Özvektörler

## 1. Makine Öğrenmesinde Matrisler, Özdeğerler ve Özvektörler

Makine öğrenmesi algoritmalarının temelinde veriyi anlamlandırmak yatar. Bilgisayarlar veriyi bizim gibi kavramsal olarak değil, sayısal diziler olarak anlar. İşte tam bu noktada matrisler ve doğrusal cebir (linear algebra) devreye girer.

### Temel Tanımlar
* **Matris Manipülasyonu:** Veri setlerinin satır (gözlemler) ve sütunlar (öznitelikler) halinde 2 boyutlu veya daha yüksek boyutlu tensörler olarak ifade edilip, bu yapılar üzerinde toplama, çarpma, devrik (transpose) alma veya ters (inverse) bulma gibi matematiksel işlemlerin yapılmasıdır. 
* **Özvektör (Eigenvector):** Karesel bir matris ile çarpıldığında (yani bir doğrusal dönüşüme uğradığında) yönü değişmeyen, sadece boyutu (skaler bir çarpan ile) değişen özel vektörlerdir. Bir dönüşümün temel eksenlerini temsil ederler.
* **Özdeğer (Eigenvalue):** İlgili özvektörün yönünde gerçekleşen dönüşümün ne kadar "büyüdüğünü" veya "küçüldüğünü" belirten skaler çarpandır. Veri bilimi bağlamında, o eksendeki bilginin (varyansın) büyüklüğünü ve önem derecesini gösterir.

### Makine Öğrenmesi ile İlişkisi ve Kullanım Alanları
Makine öğrenmesi modelleri, milyonlarca parametreyi eğitirken sürekli olarak matris manipülasyonları yapar. Özdeğer ve özvektörler ise verinin içindeki **"gizli kalıpları"** bulmamızı sağlar.

Bu kavramların en yoğun kullanıldığı makine öğrenmesi yaklaşımları şunlardır:
1. **Temel Bileşenler Analizi (PCA - Principal Component Analysis):** Boyut indirgeme yöntemlerinin en meşhurudur. Yüzlerce sütunluk (öznitelik) bir veri setinin "Kovaryans Matrisi" hesaplanır. Bu matrisin özvektörleri verinin en çok dağıldığı yeni eksenleri (temel bileşenleri), özdeğerleri ise bu eksenlerin ne kadar bilgi (varyans) taşıdığını söyler. En büyük özdeğerlere sahip özvektörler seçilerek veri seti boyut olarak küçültülürken bilgi kaybı minimize edilir.
2. **Spektral Kümeleme (Spectral Clustering):** Geleneksel algoritmaların (K-Means vb.) başarısız olduğu karmaşık şekilli kümeleri bulmak için verilerin "Benzerlik (Graf) Matrisi" oluşturulur ve bu matrisin özdeğer/özvektörlerine bakılarak kümeleme yapılır.
3. **Tekil Değer Ayrışımı (SVD - Singular Value Decomposition):** Tavsiye sistemlerinde (Netflix, Spotify algoritması) ve görüntü sıkıştırmada kullanıcı-ürün matrislerinin alt uzaylarını bulmak için kullanılır.

**Kaynaklar:**
1. Brownlee, J. (2018). *Introduction to Matrices and Matrix Arithmetic for Machine Learning*. Machine Learning Mastery.
2. Brownlee, J. (2018). *A Gentle Introduction to Eigenvalues and Eigenvectors for Machine Learning*. Machine Learning Mastery.

## 2. Numpy "linalg.eig" Fonksiyonunun İncelenmesi

Numpy kütüphanesinin lineer cebir modülünde yer alan `numpy.linalg.eig` fonksiyonu, karesel bir matrisin özdeğerlerini (eigenvalues) ve sağ özvektörlerini (right eigenvectors) hesaplamak için kullanılır.

### Dokümantasyon Özeti
Resmi dokümantasyona göre bu fonksiyon, `(M, M)` boyutlarında karesel bir matris alır ve geriye iki değer döndürür:
1.  **`w` (Özdeğerler):** Matrisin özdeğerlerini barındıran `(M,)` boyutunda bir dizi. Dokümantasyon, bu değerlerin her zaman belirli bir sırayla (örneğin büyükten küçüğe) dönmeyeceği konusunda uyarır.
2.  **`v` (Özvektörler):** Sütunları, `w` dizisindeki özdeğerlere karşılık gelen normalize edilmiş sağ özvektörlerden oluşan `(M, M)` boyutunda bir matris. (Yani `v[:, i]` sütun vektörü, `w[i]` özdeğerine aittir).

### Kaynak Kodunun Kaputunun Altı (Under the Hood)
Numpy'ın GitHub deposundaki `numpy/linalg/linalg.py` kaynak kodları incelendiğinde, `eig` fonksiyonunun bu ağır matematiği tek başına Python ile çözmediği görülür. Arka planda on yıllardır optimize edilen, devasa bir C/Fortran kütüphanesi olan **LAPACK** (Linear Algebra PACKage) rutinlerini çağırır.

Fonksiyonun kaynak kodundaki çalışma mantığı adım adım şöyledir:
1.  **Boyut ve Tip Kontrolü (`_assert_2d`, `_assert_square`):** Fonksiyon ilk olarak verilen matrisin en az 2 boyutlu ve karesel (satır sayısı = sütun sayısı) olup olmadığını denetler. Eğer matris karesel değilse `LinAlgError` hatası fırlatır.
2.  **Veri Tipi Dönüşümü (`common_type`):** Matrisin içindeki veriler tamsayı (integer) ise, işlemlerde hassasiyet kaybı olmaması için matrisi ondalıklı (float) veya karmaşık (complex) sayılara dönüştürür.
3.  **LAPACK Yönlendirmesi (`_geev` rutinleri):** Asıl işi yapan kısımdır. Numpy, matrisin veri tipine göre uygun LAPACK `geev` (General matrix Eigenvalue and Eigenvector) rutinini seçer:
    * `sgeev` (Single precision float)
    * `dgeev` (Double precision float - en sık kullanılan)
    * `cgeev` / `zgeev` (Complex numbers)
4.  **Sonuçların Formatlanması:** LAPACK'tan dönen ham vektör ve skaler sonuçlar alınıp, kullanıcının kolayca işleyebileceği o standart Numpy `array` formatına dönüştürülür ve fonksiyondan dışarı aktarılır.

Özetle; Numpy `eig` fonksiyonu, Python'ın kullanım kolaylığını, LAPACK kütüphanesinin muazzam işlem gücüyle birleştiren çok zeki bir aracı (wrapper) görevi görmektedir.
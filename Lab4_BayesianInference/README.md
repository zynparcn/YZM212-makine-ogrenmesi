# YZM212 Makine Öğrenmesi - 4. Laboratuvar Ödevi
**Uzak Bir Galaksinin Parlaklık Analizi (Bayesian Inference)**

Bu projede, gürültülü uzay gözlem verilerini kullanarak bir gök cisminin gerçek parlaklığını ve veri setindeki belirsizliği (standart sapma) emcee (MCMC) kütüphanesi ile Bayesyen çıkarım yöntemleri kullanılarak tahmin edilmiştir.

## 5.1. Parametre Karşılaştırma Tablosu

Aşağıdaki tablo, MCMC simülasyonu sonucunda hesaplanan Posterior (Sonsal) olasılık dağılımı metriklerini göstermektedir.

| Değişken | Gerçek Değer (Girdi) | Tahmin Edilen (Median) | Alt Sınır (%16) | Üst Sınır (%84) | Mutlak Hata |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$\mu$ (Parlaklık)** | 150.0 | 147.79 | 146.43 | 149.07 | 2.21 |
| **$\sigma$ (Hata Payı)** | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

---

## 6. Sonuçların Bilimsel Yorumu (Analiz Soruları)

### 6.1. Merkezi Eğilim ve Doğruluk (Accuracy) Analizi
Veri setimizde $\sigma=10.0$ gibi ciddi bir gürültü oranı olmasına rağmen, Bayesyen modelimiz $\mu$ (Parlaklık) değerini 147.79 olarak tahmin etmiştir. Mutlak hatanın sadece 2.21 birim olması, modelin gürültülü veriler içinden gerçek sinyali ayıklama konusunda oldukça yüksek bir doğruluğa (accuracy) sahip olduğunu göstermektedir.

### 6.2. Tahmin Hassasiyeti (Precision) Karşılaştırması
Tabloda $\mu$ (Parlaklık) parametresinin hata payı aralığının (146.43 - 149.07), varyans/hata tahmini olan $\sigma$'ya göre çok daha dar ve kesin olduğu görülmektedir. İstatistiksel olarak Merkezi Limit Teoremi gereği, veri sayısı ($n=50$) arttıkça ortalamanın ( $\mu$ ) tahmini etrafındaki belirsizlik (standart hata), varyansın ( $\sigma$ ) belirsizliğine kıyasla çok daha hızlı daralır. Bu nedenle ortalama tahmini her zaman daha hassastır.

### 6.3. Olasılıksal Korelasyon Analizi
Oluşturulan Corner Plot grafiğindeki 2D ( $\mu$ vs $\sigma$ ) kesişim elipsine bakıldığında, şeklin yatay veya dikey yönde aşırı bir eğime (skewness) sahip olmadığı, daha çok dairesel/dik bir formda dağıldığı görülmektedir. Bu durum, parlaklık tahmini ile gözlem hatası tahmini arasında güçlü bir doğrusal bağımlılık (korelasyon) olmadığını, parametrelerin birbirinden bağımsız şekilde iyi çözümlendiğini söyler.

---

## Ekstra Analizler (Prior ve Veri Miktarı Etkisi)
1. **Prior Etkisi:** Eğer parlaklık için 100-110 arası çok dar ve yanlış bir prior (ön bilgi) seçseydik, Bayes teoremi gereği modelimiz veriden ziyade bu katı ön bilgiye ağırlık verecekti. Bu durumda tahmin 150 civarına ulaşamayacak, posterior dağılımı zorla 110 civarında yığılarak bizi tamamen yanlış bir sonuca götürecekti.
2. **Veri Miktarı:** Gözlem sayısı ($n=50$) yerine 5'e düşürülseydi, Likelihood (Olabilirlik) fonksiyonunun etkisi zayıflayacaktı. Bu da posterior dağılımının (çan eğrilerinin) çok daha yayvan ve geniş olmasına, yani tahminlerimizdeki belirsizliğin ve hata aralığının devasa boyutlara ulaşmasına neden olurdu.
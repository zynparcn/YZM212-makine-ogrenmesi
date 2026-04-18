# YZM212 Makine Öğrenmesi - Lab 2: MLE ile Akıllı Şehir Planlaması

**Problem Tanımı:** Bir şehrin en yoğun ana caddesinden geçen araç sayısını modellemek ve gelecekteki trafik yoğunluğunu tahmin etmek. Bu modelleme için Poisson Dağılımı varsayılmış ve dağılımın en uygun parametresi olan $\lambda$ (beklenen araç sayısı), Maximum Likelihood Estimation (MLE) yöntemi ile bulunmuştur.

**Veri:** Elimizde 1 dakikada geçen araç sayılarını gösteren, 14 gözlemden oluşan bağımsız bir veri seti bulunmaktadır: `[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]`.

**Yöntem:** 1. **Analitik Yöntem:** Poisson dağılımı için Log-Likelihood fonksiyonu türetilmiş ve türevi sıfıra eşitlenerek analitik çözümün verilerin aritmetik ortalamasına eşit olduğu ispatlanmıştır.
2. **Sayısal Yöntem:** Python üzerinde `scipy.optimize` kütüphanesi kullanılarak Negatif Log-Olabilirlik (NLL) fonksiyonu minimize edilmiş ve $\lambda$ değeri sayısal yollarla hesaplanmıştır.

**Sonuçlar:** Hem analitik tahmin (aritmetik ortalama) hem de sayısal MLE tahmini birbiriyle milimetrik olarak eşleşmiş ve $\lambda$ = 12.14 olarak bulunmuştur. Elde edilen bu parametre ile çizilen Poisson PMF grafiği, gerçek veri histogramının üzerine oturtulduğunda yüksek bir uyum gözlemlenmiştir.

**Yorum / Tartışma (Outlier Analizi):** Veri setine 200 gibi aşırı uç bir hatalı gözlem (outlier) eklendiğinde, MLE formülü doğrudan aritmetik ortalamaya dayandığı için model aniden gerçek dışı yüksek bir trafik yoğunluğu öngörür. Medyanın aksine ortalama hesabının uç değerlere karşı dirençsiz olması, modelin yanıltıcı sonuçlar vermesine yol açar. Belediyenin trafik planlamasında bu durum, gereksiz yol genişletme çalışmaları veya bütçe israfı gibi devasa hatalara zemin hazırlayabilir. Bu nedenle MLE tabanlı optimizasyonlarda veri temizliğinin kritik öneme sahip olduğu görülmüştür.
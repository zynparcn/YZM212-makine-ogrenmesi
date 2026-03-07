# YZM212 Makine Öğrenmesi - İzole Kelime Tanıma Sistemi

## Proje Özeti
* **Problem Tanımı:** Sınırlı bir kelime dağarcığına ("EV" ve "OKUL") sahip bir sistemde, dışarıdan gelen ses frekanslarına (High, Low) göre doğru kelimeyi tahmin etmek.
* **Veri:** 1. Bölümde teorik olarak verilen geçiş ve emisyon matrisleri (A ve B matrisleri) ile test verisi olarak [0, 1, 1] (High, Low, Low) gözlem dizisi kullanılmıştır.
* **Yöntem:** Python üzerinde `hmmlearn` kütüphanesi kullanılarak Gizli Markov Modeli (HMM) kurulmuştur. Gelen sesin hangi modele ait olduğunu bulmak için Log-Likelihood skorları karşılaştırılmıştır.
* **Sonuç:** Test verisi modele sokulduğunda EV modelinin skoru (-1.3295), OKUL modelinin skorundan (-2.4210) daha yüksek çıkmış ve sistem doğru bir şekilde "EV" kelimesini tahmin etmiştir.

---

## Analiz ve Yorumlama

**Soru 1: Ses verisindeki "gürültü" (noise), HMM modelindeki Emisyon Olasılıklarını nasıl etkiler?**
Ses verisindeki gürültü, duyulan frekansların netliğini bozar. Bu durum, emisyon (yayılma) olasılıklarının keskinliğini kaybetmesine (örneğin 0.9'a 0.1 gibi net ayrımlar yerine, 0.6'ya 0.4 gibi birbirine yakın değerlere dönüşmesine) sebep olur. Modelin "emin olma" seviyesi düşer ve yanlış duruma (foneme) geçiş yapma ihtimali artar. Kısacası gürültü, emisyon olasılıklarındaki belirsizliği (entropiyi) artırarak modelin doğruluk oranını düşürür.

**Soru 2: Gerçek bir sistemde binlerce kelime olduğunu düşünürsek, Viterbi yerine neden daha karmaşık yapılar (Deep Learning gibi) tercih edilmeye başlanmıştır?**
Viterbi ve klasik HMM modelleri, her kelime ve her fonem için geçiş ve emisyon matrislerinin tek tek tanımlanmasını ve elde tutulmasını gerektirir. Kelime sayısı binlere veya milyonlara çıktığında bu matrisler hesaplanamayacak kadar büyür ve işlem maliyeti inanılmaz derecede artar. Derin öğrenme modelleri ise bu özellikleri manuel olarak tanımlamaya gerek kalmadan, devasa veriler üzerinden otomatik olarak öğrenebildikleri ve bağlamı çok daha iyi kavrayabildikleri için tercih edilmektedir.
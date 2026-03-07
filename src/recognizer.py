from hmmlearn import hmm
import numpy as np

# 1. 'EV' kelimesi için model tanımlama
model_ev = hmm.CategoricalHMM(n_components=2)
model_ev.startprob_ = np.array([1.0, 0.0])  # Başlangıç olasılığı (e harfi ile başlıyor)

# Geçiş Olasılıkları (A Matrisi)
model_ev.transmat_ = np.array([[0.6, 0.4],  # e'den e'ye, e'den v'ye
                               [0.2, 0.8]]) # v'den e'ye, v'den v'ye

# Emisyon Olasılıkları (B Matrisi) - 0: High, 1: Low frekans temsil etsin
model_ev.emissionprob_ = np.array([[0.7, 0.3],  # e durumundayken (High, Low)
                                   [0.1, 0.9]]) # v durumundayken (High, Low)

# 2. 'OKUL' kelimesi için model tanımlama
# Temsili eğitim verisi/değerleri
model_okul = hmm.CategoricalHMM(n_components=2)
model_okul.startprob_ = np.array([0.5, 0.5])
model_okul.transmat_ = np.array([[0.7, 0.3],
                                 [0.4, 0.6]])
model_okul.emissionprob_ = np.array([[0.5, 0.5],
                                     [0.8, 0.2]])

# 3. Test verisi (Yeni bir ses kaydı geldiğini varsayalım)
# Mikrofondan [0, 1, 1] yani [High, Low, Low] sinyali geldiğini farz ediyoruz.
test_data = np.array([[0, 1, 1]]).T # Gözlemlerin indexleri

# 4. Hangi model daha yüksek puan (Log-Likelihood) veriyor?
score_ev = model_ev.score(test_data)
score_okul = model_okul.score(test_data)

print(f"EV Modeli Puanı: {score_ev:.4f}")
print(f"OKUL Modeli Puanı: {score_okul:.4f}")
print("-" * 30)

if score_ev > score_okul:
    print("SİSTEM KARARI: Duyulan kelime büyük ihtimalle 'EV'")
else:
    print("SİSTEM KARARI: Duyulan kelime büyük ihtimalle 'OKUL'")
🧪 Minecraft Auto Pot Macro (Python)

Bu proje, Minecraft PvP için yapılmış basit bir Auto Pot macro scriptidir.
Belirlenen tuşlara basıldığında otomatik olarak sağ tık atar ve pot kullanır.

⚙️ Özellikler

2–6 arası tuşlara basınca otomatik sağ tık

Random delay 

Hafif ve stabil

Python ile yazılmıştır

Arka planda çalışır

🧠 Nasıl Çalışır?

Script çalışırken:

2, 3, 4, 5 veya 6 tuşuna bastığında

Rastgele 0.08 – 0.14 saniye gecikme ekler

1 kere sağ tık atar

Bu sayede pot kullanımı daha doğal görünür.

📦 Gereksinimler

Python 3.x

Gerekli kütüphaneler:

pip install pyautogui pynput

⌨️ Tuş Ayarları (ÖNEMLİ)

Aşağıdaki satırdan pot koyduğun hotbar tuşlarını değiştirebilirsin:

if key.char in ['2', '3', '4', '5', '6']:


Örnek:

Sadece 3 ve 4 olsun istiyorsan:

['3', '4']

⏱️ Delay Ayarları
def random_delay():
    return random.uniform(0.08, 0.14)


Daha hızlı için → 0.05, 0.1

Daha güvenli için → 0.12, 0.2

▶️ Kullanım

Uygulamayı çalıştır

potun hangi tuştaysa ona bas sağ tık basıyor otomatık atıyor.
2–6 tuşlarına bas

Auto Pot otomatik çalışır

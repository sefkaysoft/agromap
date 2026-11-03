import os
import random

def klasordeki_gorselleri_rastgele_isimlendir():
    # script ile aynı dizinde bulunan 'img' klasörünün mutlak yolu
    mevcut_dizin = os.path.dirname(os.path.abspath(__file__))
    klasor_yolu = os.path.join(mevcut_dizin, "img")
    
    # Desteklenen görsel uzantıları
    desteklenen_uzantilar = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG', '.bmp','.avif', '.webp')
    
    # Klasörün varlığını kontrol et
    if not os.path.exists(klasor_yolu):
        # Hata mesajı düzeltmesi burada yapıldı
        print(f"Hata: '{klasor_yolu}' klasörü bulunamadı! Lütfen script ile aynı dizinde 'img' klasörü olduğundan emin olun.")
        return

    # Klasördeki tüm görsel dosyalarını bul
    dosyalar = [
        f for f in os.listdir(klasor_yolu) 
        if f.lower().endswith(desteklenen_uzantilar)
    ]
    
    toplam_gorsel = len(dosyalar)
    
    if toplam_gorsel == 0:
        print(f"'{klasor_yolu}' klasöründe hiç görsel bulunamadı.")
        return

    print(f"İşlem yapılacak klasör: {klasor_yolu}")
    print(f"Toplam {toplam_gorsel} adet görsel tespit edildi. Rastgele isimlendirme başlatılıyor...")

    # Çakışmaları önlemek için önce tüm dosyaları geçici rastgele isimlere taşı
    gecici_dosyalar = []
    for dosya in dosyalar:
        uzanti = os.path.splitext(dosya)[1]
        eski_yol = os.path.join(klasor_yolu, dosya)
        
        gecici_isim = f"temp_{random.randint(100000, 999999)}{uzanti}"
        yeni_yol = os.path.join(klasor_yolu, gecici_isim)
        
        os.rename(eski_yol, yeni_yol)
        gecici_dosyalar.append((gecici_isim, uzanti))

    # Dosyaları tamamen karıştır (Rastgele sıralama)
    random.shuffle(gecici_dosyalar)

    # 1'den başlayarak sırayla yeniden adlandır
    for yeni_index, (gecici_isim, uzanti) in enumerate(gecici_dosyalar, start=1):
        eski_yol = os.path.join(klasor_yolu, gecici_isim)
        
        # Yeni dosya adı (Örn: 1.jpg, 2.png ...)
        yeni_ad = f"{yeni_index}{uzanti}"
        yeni_yol = os.path.join(klasor_yolu, yeni_ad)
        
        os.rename(eski_yol, yeni_yol)
        print(f"İsimlendirildi: {gecici_isim} -> {yeni_ad}")

    print(f"\nİşlem başarıyla tamamlandı! Toplam {toplam_gorsel} görsel rastgele numaralandırıldı.")

if __name__ == "__main__":
    klasordeki_gorselleri_rastgele_isimlendir()
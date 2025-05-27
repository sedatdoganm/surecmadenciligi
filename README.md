**Süreç Madenciliği Projesi**

Bu proje, süreç madenciliği (process mining) alanında temel analiz ve görselleştirme işlevlerini gerçekleştirmek üzere geliştirilmiş bir Python uygulamasıdır. Proje, organizasyonlardaki iş süreçlerinin adım adım nasıl ilerlediğini inceleyerek, süreçlerdeki darboğazları, geçiş frekanslarını ve zaman analizlerini ortaya koymayı hedefler.

**Proje Amacı**

Günümüzde birçok organizasyonun günlük operasyonları dijital sistemler aracılığıyla yürütülmektedir. Bu sistemlerde oluşan olay kayıtları (event logs), iş süreçlerinin analiz edilmesi için büyük fırsatlar sunar. Bu projede amaç:

Süreç adımlarının sıklık analizini yapmak,
Her bir sürecin toplam süresini hesaplamak,
Süreç adımları arasındaki geçiş sıklıklarını analiz etmek,
Tüm bu analizleri kullanıcıya görsel olarak sunmaktır.

**Proje Dosyaları**

süreç-madenciligi-projesi/
├── surec_analiz.py        # Verileri analiz eden ve grafiklerle görselleştiren Python scripti
├── surec_verisi.csv       # Örnek olay kayıtları (süreç adımları ve zaman bilgileri)
├── plotlar/               # Üretilen grafik görselleri (lokal çalıştırıldığında otomatik oluşur)
└── README.md              # Proje açıklamalarının bulunduğu dosya (bu dosya)

**Kullanılan Teknolojiler**

Python 3.x
Pandas (veri işleme)
Matplotlib (görselleştirme)
Seaborn (gelişmiş grafikler için)
CSV formatında veri girişi

**Analiz Adımları**

CSV dosyası okunur ve veri çerçevesine dönüştürülür.
Her bir aktivitenin kaç kez tekrarlandığı belirlenir.
Her bir sürecin toplam süresi hesaplanır.
Adımlar arasındaki geçiş frekansları tespit edilir.
Analiz sonuçları grafiklerle görselleştirilir.

**Oluşturulan Görseller**

1. *Aktivite Frekans Grafiği*: Her aktivitenin süreçler boyunca kaç kez tekrarlandığını gösterir.
   ![plot1](https://github.com/user-attachments/assets/3c5709cf-8868-429c-9774-911a3ba2bedb)

2. *Geçiş Matrisi Grafiği:* Süreç adımları arasındaki geçişlerin yoğunluk haritası.
   ![plot2](https://github.com/user-attachments/assets/084bb9fe-007b-420f-8666-2286ccdd8eed)


**Ek olarak** *Projede istenilenlerden biri olan proje çıktısı:*
![calisircikti](https://github.com/user-attachments/assets/cec683ca-ac03-4ccb-a21a-0825cb78d7e5)

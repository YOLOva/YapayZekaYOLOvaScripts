# label mapper
## kullanım
python label_mapper.py --labels_folder [label_klasörü_dizini] --label_map_file [label_map_dosyası_dizini] --output_folder [çıktı klasör dizini]



çıktı [label_klasörü_dizini]_new şeklinde oluşacaktır.
buradaki --labels_folder parametresi girilmesi zorunludur. 

Onun dışındaki parametrelerin girilmesi zorunlu değildir.


txt dosyaları içerisine verisetinin classes.txt dosyasını düzenleyerek her sınıfın yeni class id karşılığını satır başına belirtilir.

classid sınıf_adı



"-1" sayısı sınıfı yok saymak kullanmamak için kullanılmıştır.

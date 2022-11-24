# bir diğer klasörde bulunan dosyalarla aynı isimdeki dosyaları istenilen dizine taşır
# amaç: kullanılmak üzere temizlenmiş ama eski düzene göre uyarlanmış label dosyaları yerine henüz uyarlanmamış label dosyalarını kopyalayarak kullanıma hazır hale getirmek.

import os
import shutil

to_copy_files_path = "D:/Teknofest/CATAI/Verisetleri/VisDrone2019-DET-train/annotations"
to_look_files_path = "D:/Teknofest/CATAI/Verisetleri/Visdrone/VisDrone2019/labels"
destination = "D:/Teknofest/YOLOVA/Veriseti/Visdrone2019Det/annotations"

look_files = os.listdir(to_look_files_path)
for look_name in look_files:
    try:
        copy_file_path = f"{to_copy_files_path}/{look_name}"
        shutil.copyfile(copy_file_path, f"{destination}/{look_name}")
    except:
        print(f"error file, {look_name}")
from PIL import Image
import os
import shutil


version ="1.6"

PngFile = []
WebpFile = []
TxtFile = []
NcnFile = []
endpoint = ""

current_directory = os.getcwd()

def main():
    for file in os.listdir():
        if file.endswith('.png') or file.endswith('.PNG'):
            PngFile.append(file)
        if file.endswith('.webp') or file.endswith('.WEBP'):
            WebpFile.append(file)
        if file.endswith('.txt') or  file.endswith('.TXT'):
            TxtFile.append(file)
        if file.endswith('.ncn') or  file.endswith('.NCN'):
            NcnFile.append(file)


def TxtToNcn():
    main()
    for file in TxtFile:
        txtname = file
        os.rename(txtname, f"{txtname.split('.')[0]}.ncn")
        print("TXT To NCN")
        print(txtname)


def NcnToTxt():
    main()
    for file in NcnFile:
        ncnname = file
        os.rename(ncnname, f"{ncnname.split('.')[0]}.txt")
        print("NCN To TXT")
        print(ncnname)


            
def PngToWebp():
    main()

    for file in PngFile:
        # png dosyasını aç
        im = Image.open(file)
        # Çıktı dosyasının adını belirleyin (aynı dosya adıyla .webp uzantısı)
        image_webp = f"{file.split('.')[0]}.webp"
        # Çıktı dosyasını 'webptopng' klasörüne kaydet
        output_path = os.path.join(current_directory, image_webp)
        im.save(output_path, format="webp", lossless=True)
    
    # Listeyi temizleyin
    PngFile.clear()
    WebpFile.clear()


def WebpToPng():
    main()


    for file in WebpFile:
        # webp dosyasını aç
        im = Image.open(file)
        # Çıktı dosyasının adını belirleyin (aynı dosya adıyla .png uzantısı)
        image_png = f"{file.split('.')[0]}.png"
        # Çıktı dosyasını 'webtopng' klasörüne kaydet
        output_path = os.path.join(current_directory, image_png)
        im.save(output_path, format="png", lossless=True)
    
    # Listeyi temizleyin
    PngFile.clear()
    WebpFile.clear()



def PngToWebpAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".png"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".webp"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)

def WebpToPngAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".webp"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".png"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)

def PngToJpgAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".png"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".jpg"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)

def JpgToPngAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".jpg"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".png"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)

def WebpToJpgAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".webp"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".jpg"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)

def JpgToWebpAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".jpg"):
                print(file)
                source_file = os.path.join(root, file)
                webp_filepath = os.path.join(root, file)
                target_file = source_file[:-5] + ".webp"
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(webp_filepath)


def JpegToJpgAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.lower().endswith(".jpeg"):
                print(file)
                source_file = os.path.join(root, file)
                target_file = source_file[:-5] + ".jpg"  # "-5" çünkü ".jpeg" 5 karakter
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(source_file)


def JpgToJpegAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.lower().endswith(".jpg"):
                print(file)
                source_file = os.path.join(root, file)
                target_file = source_file[:-5] + ".jpeg"  # "-5" çünkü ".jpeg" 5 karakter
                image = Image.open(source_file)
                image.save(target_file)
                os.remove(source_file)


def copySingleFileFolders(folder_path, destination_folder):
    contents = os.listdir(folder_path)

    for item in contents:
        item_path = os.path.join(folder_path, item)

        # Eğer bir klasörse ve içinde sadece bir dosya varsa, içeriğini kopyala
        if os.path.isdir(item_path):
            if len(os.listdir(item_path)) == 1 and os.path.isfile(os.path.join(item_path, os.listdir(item_path)[0])):
                # Hedef klasörü oluştur
                destination_path = os.path.join(destination_folder, item)
                os.makedirs(destination_path, exist_ok=True)

                # Tek dosyayı kopyala
                file_to_copy = os.path.join(item_path, os.listdir(item_path)[0])
                shutil.copy(file_to_copy, destination_path)


def cutSingleFileFolders(folder_path, destination_folder):
    # Dizin içindeki tüm dosya ve klasörleri al
    contents = os.listdir(folder_path)

    for item in contents:
        # Dosya yolu oluştur
        item_path = os.path.join(folder_path, item)

        # Eğer bir klasörse ve içinde sadece bir dosya varsa, içeriğini kes
        if os.path.isdir(item_path):
            if len(os.listdir(item_path)) == 1 and os.path.isfile(os.path.join(item_path, os.listdir(item_path)[0])):
                # Hedef klasörü oluştur
                destination_path = os.path.join(destination_folder, item)
                os.makedirs(destination_path, exist_ok=True)

                # Tek dosyayı kes ve yapıştır
                file_to_move = os.path.join(item_path, os.listdir(item_path)[0])
                shutil.move(file_to_move, destination_path)


def copyFiles(current_directory, destination_folder):
    global endpoint
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith(f'.{endpoint}'):
            destination_path = os.path.join(destination_folder, file_name)
            shutil.copy(file_path, destination_path)

def moveFiles(current_directory, destination_folder):
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith(f'.{endpoint}'):
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(file_path, destination_path)


def deleteEmptyFolders(folder_path):
    contents = os.listdir(folder_path)

    for item in contents:
        item_path = os.path.join(folder_path, item)

        # Eğer bir klasörse ve içi boşsa, sil
        if os.path.isdir(item_path):
            if not os.listdir(item_path):
                print("Deleting empty folder:", item_path)
                shutil.rmtree(item_path)
            else:
                deleteEmptyFolders(item_path)


while True:
    chose = input(f'''
PNG to WEBP      (Sadece Alt Dizin)             [0]
WEBP to PNG      (Sadece Alt Dizin)             [1]
PNG to WEBP        (Tüm Dizin)                  [2]
WEBP to PNG        (Tüm Dizin)                  [3]
PNG to JPG         (Tüm Dizin)                  [4]
JPG to PNG         (Tüm Dizin)                  [5]
JPG to WEBP        (Tüm Dizin)                  [6]
WEBP to JPG        (Tüm Dizin)                  [7]
JPEG to JPG        (Tüm Dizin)                  [8]
JPG to JPEG        (Tüm Dizin)                  [9]
TXT to NCN       (Sadece Alt Dizin)            [10]
NCN to TXT       (Sadece Alt Dizin)            [11]
Tek Dosya Içeren Klasörlerin Içeriğini Kopyala [12]
Tek Dosya Içeren Klasörlerin Içeriğini Kes     [13]
Endswithe Göre Dosyaları Klasörüne Kopyala     [14]
Endswithe Göre Dosyaları Klasörüne Kes         [15]
Boş klasörleri Temizle                         [16]
    
Sayıyı Giriniz :''')
    try:
        chose = int(chose)
    except:
        print('\nLütfen sadece sayı giriniz')
    if chose == 0:PngToWebp(), print('\nPngToWebp')
    elif chose == 1: WebpToPng(), print('\nWebpToPng')
    elif chose == 2: PngToWebpAll(), print('\nPngToWebpAll')
    elif chose == 3: WebpToPngAll(), print('\nWebpToPngAll')
    elif chose == 4: PngToJpgAll(), print('\nPngToJpgAll')
    elif chose == 5: JpgToPngAll(), print('\nJpgToPngAll')
    elif chose == 6: JpgToWebpAll(), print('\nJpgToWebpAll')
    elif chose == 7: WebpToJpgAll(), print('\nWebpToJpgAll')
    elif chose == 8: JpegToJpgAll(), print('\nJpegToJpgAll')
    elif chose == 9: JpgToJpegAll(), print('\nJpgToJpegAll')
    elif chose == 10: TxtToNcn(), print('\nTxtToNcn')
    elif chose == 11: NcnToTxt(), print('\nNcnToTxt')
    elif chose == 12:
        try:
            destination_folder = input("Dosyaları Aktarılacak Dosyanın Ismi:")
        except:
            destination_folder = "singleFileFoldersContents"
        copySingleFileFolders(current_directory, destination_folder), print('\ncopySingleFileFolders')
    elif chose == 13:
        try:
            destination_folder = input("Dosyaları Aktarılacak Dosyanın Ismi:")
        except:
            destination_folder = "singleFileFoldersContents"
        cutSingleFileFolders(current_directory, destination_folder), print('\ncutSingleFileFolders')
    elif chose == 14:
        try:
            endpoint = input("Sonu nasıl dosyaları istiyorsun? (Ornegin: mp4) :")
        except:
            break
        destination_folder = f"{endpoint}_files"
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        copyFiles(current_directory, destination_folder)
        print(f"{endpoint} dosyaları {destination_folder} klasörüne kopyalandı.")

    elif chose == 15:
        try:
            endpoint = input("Sonu nasıl dosyaları istiyorsun? (Ornegin: mp4) :")
        except:
            break
        destination_folder = f"{endpoint}_files"
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        moveFiles(current_directory, destination_folder)
        print(f"{endpoint} dosyaları {destination_folder} klasörüne kesildi.")
    elif chose == 16: deleteEmptyFolders(current_directory)

    else:
        print("\nLütfen 0'dan 16'ya kadar giriniz.")





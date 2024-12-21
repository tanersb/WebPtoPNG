from PIL import Image
import os

version ="1.5"

PngFile = []
WebpFile = []
TxtFile = []
NcnFile = []


def main():
    for file in os.listdir():
        if file.endswith('.png') or file.endswith('.PNG'):# png
            PngFile.append(file)
        if file.endswith('.webp') or file.endswith('.WEBP'):# webp
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
    # 'webptopng' klasörünün varlığını kontrol et ve gerekirse oluştur
    output_folder = 'webptopng'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in PngFile:
        # png dosyasını aç
        im = Image.open(file)
        # Çıktı dosyasının adını belirleyin (aynı dosya adıyla .webp uzantısı)
        image_webp = f"{file.split('.')[0]}.webp"
        # Çıktı dosyasını 'webptopng' klasörüne kaydet
        output_path = os.path.join(output_folder, image_webp)
        im.save(output_path, format="webp", lossless=True)
    
    # Listeyi temizleyin
    PngFile.clear()
    WebpFile.clear()


def WebpToPng():
    main()
    # 'webtopng' klasörünün varlığını kontrol et ve gerekirse oluştur
    output_folder = 'webtopng'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in WebpFile:
        # webp dosyasını aç
        im = Image.open(file)
        # Çıktı dosyasının adını belirleyin (aynı dosya adıyla .png uzantısı)
        image_png = f"{file.split('.')[0]}.png"
        # Çıktı dosyasını 'webtopng' klasörüne kaydet
        output_path = os.path.join(output_folder, image_png)
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



while True:
    chose = input(f'''
Version:{version}
PNG to WEBP (Alt Dizin)[1]
WEBP to PNG (Alt Dizin)[2]
PNG to WEBP (Tüm Dizin)[3]
WEBP to PNG (Tüm Dizin)[4]
PNG to JPG  (Tüm Dizin)[5]
JPG to PNG  (Tüm Dizin)[6]
JPG to WEBP (Tüm Dizin)[7]
WEBP to JPG (Tüm Dizin)[8]
JPEG to JPG (Tüm Dizin)[9]
JPG to JPEG (Tüm Dizin)[0]
TXT to NCN (Alt Dizin)[10]
NCN to TXT (Alt Dizin)[11]
:''')
    try:
        chose = int(chose)
    except:
        print('\nLütfen sadece sayı giriniz')
    if chose == 1:PngToWebp(), print('\nPngToWebp')
    elif chose == 2: WebpToPng(), print('\nWebpToPng')
    elif chose == 3: PngToWebpAll(), print('\nPngToWebpAll')
    elif chose == 4: WebpToPngAll(), print('\nWebpToPngAll')
    elif chose == 5: PngToJpgAll(), print('\nPngToJpgAll')
    elif chose == 6: JpgToPngAll(), print('\nJpgToPngAll')
    elif chose == 7: JpgToWebpAll(), print('\nJpgToWebpAll')
    elif chose == 8: WebpToJpgAll(), print('\nWebpToJpgAll')
    elif chose == 9: JpegToJpgAll(), print('\nJpegToJpgAll')
    elif chose == 0: JpgToJpegAll(), print('\nJpgToJpegAll')
    elif chose == 10: TxtToNcn(), print('\nTxtToNcn')
    elif chose == 11: NcnToTxt(), print('\nNcnToTxt')
    else:
        print("\nLütfen 0'dan 11'e kadar giriniz.")





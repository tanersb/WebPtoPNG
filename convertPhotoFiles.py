from PIL import Image
import os

PngFile = []
WebpFile = []


def main():
    for file in os.listdir():
        if file == "cryptog.py" or file == 'key.txt' or file =='decrypt.py' or file =='encrypt.py' or file == "cryptog.exe" or file =='encrypt.exe' or file == 'key.key':
            continue
        if file.endswith('.png'):# png
            PngFile.append(file)
        if file.endswith('.webp'):# webp
            WebpFile.append(file)


def PngToWebp():
    main()
    for file in PngFile:
        image_webp = f"{file.split('.')[0]}.webp"
        im = Image.open(file)
        im.save(image_webp, format="webp", lossless=True)
    PngFile.clear()
    WebpFile.clear()

def WebpToPng():
    main()
    for file in WebpFile:
        image_png = f"{file.split('.')[0]}.png"
        im = Image.open(file)
        im.save(image_png, format="png", lossless=True)
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



while True:
    chose = input('''
PNG to WEBP (Alt Dizin)[1]
WEBP to PNG (Alt Dizin)[2]
PNG to WEBP (Tüm Dizin)[3]
WEBP to PNG (Tüm Dizin)[4]
PNG to JPG  (Tüm Dizin)[5]
JPG to PNG  (Tüm Dizin)[6]
JPG to WEBP (Tüm Dizin)[7]
WEBP to JPG (Tüm Dizin)[8]
:  ''')
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
    else:
        print('\nLütfen 1den 4e kadar giriniz.')





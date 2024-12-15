from PIL import Image, ImageSequence
import os


PngFile = []
WebpFile = []

def main():
    for file in os.listdir():
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

def WebpToGifAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".webp"):
                source_file = os.path.join(root, file)
                image_webp = Image.open(source_file)
                
                #Tüm karelerin PNG olarak kaydedilmesi
                duration = image_webp.info.get('duration', 0)
                loop = image_webp.info.get('loop', 0)
                frames = []
                try:
                    while True:
                        frames.append(image_webp.copy())
                        image_webp.seek(len(frames))
                except EOFError:
                    pass
                
                #PNG dosyalarının GIF formatına dönüştürülmesi
                target_file = source_file[:-4] + ".gif"
                frames[0].save(target_file, save_all=True, append_images=frames[1:], format='GIF', duration=duration, loop=loop, optimize=False)
                


def GifToWebpAll():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".gif"):
                source_file = os.path.join(root, file)
                target_file = source_file[:-4] + ".webp"
                image = Image.open(source_file)
                image.save(target_file, format="webp")


def PathToGIF():
    subdir_path = "PNGtoGIF"
    
    if os.path.exists(subdir_path):
        gif_path = os.path.join(subdir_path, 'MyCreated.gif')
        png_files = [f for f in os.listdir(subdir_path) if f.endswith('.png')]
        png_files.sort()

        frames = []
        for png_file in png_files:
            png_path = os.path.join(subdir_path, png_file)
            im = Image.open(png_path)
            frames.append(im)

        frames[0].save(gif_path, save_all=True, append_images=frames[1:], format='GIF', duration=300, loop=0, optimize=False)


        
    else:
        os.mkdir(subdir_path)
        print('Lütfen PNGtoGIF dosyası içinde png dosyalarını tutunuz.')
        
    
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
WEBP to GIF (Tüm Dizin)[9]
GIF to WEBP (Tüm Dizin)[10] Not work
Path to GIF (Alt Dizin)[11]
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
    elif chose == 9: WebpToGifAll(), print('\nWebpToGifAll')
    elif chose == 10: GifToWebpAll(), print('\nGifToWebpAll')
    elif chose == 11: PathToGIF(), print('\nPathToGif')
    else:
        print('\nLütfen 1den 10a kadar giriniz.')

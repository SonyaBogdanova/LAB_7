"LAB_7"

def p1():

    from PIL import Image

    filename = "capybara.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def p2():

    from PIL import Image, ImageOps

    filename = "capybara.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((980, 852))
    new_img.show()
    new_img.save('C:/LAB_7/pythonProject/7_2/capybara_resize.jpg')

    second_img = ImageOps.mirror(new_img)
    second_img.show()
    second_img.save('C:/LAB_7/pythonProject/7_2/capybara_mirror_gor.jpg')

    third_img = ImageOps.flip(new_img)
    third_img.show()
    third_img.save('C:/LAB_7/pythonProject/7_2/capybara_mirror_ver.jpg')

def p3():

    import torchvision.transforms.functional as F
    import PIL
    from PIL import Image, ImageFilter, ImageEnhance

    filename = "capybara.jpg"
    with Image.open(filename) as img:
        img.load()

    Filter_1 = img.filter(ImageFilter.FIND_EDGES)
    Filter_1.show()
    Filter_1.save('C:/LAB_7/pythonProject/5_Filters/1.jpg')

    Filter_2 = img.crop((900, 200, 2000, 1600))
    Filter_2.show()
    Filter_2.save('C:/LAB_7/pythonProject/5_Filters/2.jpg')

    convert = PIL.ImageEnhance.Color(img)
    Filter_3 = convert.enhance(2.5)
    Filter_3.show()
    Filter_3.save('C:/LAB_7/pythonProject/5_Filters/3.jpg')


    Filter_4 = F.adjust_hue(img, 0.3)
    Filter_4.show()
    Filter_4.save('C:/LAB_7/pythonProject/5_Filters/4.jpg')

    Filter_5 = F.rgb_to_grayscale(img, 1)
    Filter_5.show()
    Filter_5.save('C:/LAB_7/pythonProject/5_Filters/5.jpg')

def p4():

    from PIL import Image
    import torchvision.transforms.functional as F

    filename = "capybara.jpg"
    with Image.open(filename) as img:
        img.load()

    water = "apple.png"
    with Image.open(water) as img_2:
        img_2.load()

    img_2.thumbnail((700, 700))
    img_2_mask = img_2.convert("RGBA")
    img_2 = img_2.convert("RGBA")
    img.paste(img_2, (1100, 230), mask=img_2_mask)
    img = F.adjust_contrast(img, 1.3)
    img.save('C:/LAB_7/pythonProject/7_4/Merged_Image.jpg')
    img.show()

p1(), p2(), p3(), p4()



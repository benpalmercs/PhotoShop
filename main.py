from random import *

from PIL import Image, ImageDraw
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen


class PhotoShopApp(App):
    pass


class Display(Screen):
    # def on_touch_down(self,touch):
    #     x,y = touch.x,touch.y
    #     self.coordinates.append(int(x))
    #     self.coordinates.append(int(y))
    #     if len(self.coordinates)>4:
    #         self.coordinates = self.coordinates[2:]
    #     print(self.coordinates)s
    #     print(self.count)
    #     touch.push()
    #     touch.apply_transform_2d(self.to_local)
    #     ret = super(RelativeLayout, self).on_touch_down(touch)
    #     touch.pop()
    #     return ret
    # def on_touch_up(self,touch):
    #     x,y = touch.x,touch.y
    #     self.coordinates.append(int(x))
    #     self.coordinates.append(int(y))
    #     if len(self.coordinates)>4:
    #         self.coordinates = self.coordinates[2:]
    #     print(self.coordinates)
    #     print(self.count)
    #     touch.push()
    #     touch.apply_transform_2d(self.to_local)
    #     ret = super(RelativeLayout, self).on_touch_up(touch)
    #     touch.pop()
    #     return ret
    def load_image(self, image):
        self.ids.image.source = image

    def sepia(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                red = int(red * .393 + green * 0.769 + blue * 0.189)
                green = int(red * .349 + green * 0.686 + blue * 0.168)
                blue = int(red * .272 + green * 0.534 + blue * 0.131)
                pixels[x, y] = (red, green, blue)
        img.save(name + "sepia.png")
        self.ids.image_file.text = self.ids.image_name.text + "sepia.png"
        self.ids.image_name.text += "sepia"
        self.ids.image.source = name + "sepia.png"

    def invert(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(name + "inverted.png")
        self.ids.image_file.text = self.ids.image_name.text + "inverted.png"
        self.ids.image_name.text += "inverted"
        self.ids.image.source = name + "inverted.png"

    def line_drawing(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if x < img.size[0] - 1:
                    if (pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) > (
                            pixels[x + 1, y][0] + pixels[x + 1, y][1] + pixels[x + 1, y][2]):
                        red = pixels[x, y][0] - 300
                        green = pixels[x, y][1] - 300
                        blue = pixels[x, y][2] - 300
                    else:
                        red = pixels[x, y][0] + 300
                        green = pixels[x, y][1] + 300
                        blue = pixels[x, y][2] + 300
                    pixels[x, y] = (red, green, blue)
        img.save(name + "line.png")
        self.ids.image_file.text = self.ids.image_name.text + "line.png"
        self.ids.image_name.text += "line"
        self.ids.image.source = name + "line.png"

    def mirror(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if x < img.size[0] / 2:
                    swap1 = pixels[x * (-1), y]
                    swap2 = pixels[x, y]
                    pixels[x * (-1), y] = swap2
                    pixels[x, y] = swap1
        img.save(name + "mirror.png")
        self.ids.image_file.text = self.ids.image_name.text + "mirror.png"
        self.ids.image_name.text += "mirror"
        self.ids.image.source = name + "mirror.png"

    def mirror2(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if y < img.size[1] / 2:
                    swap1 = pixels[x, y * (-1)]
                    swap2 = pixels[x, y]
                    pixels[x, y * (-1)] = swap2
                    pixels[x, y] = swap1
        img.save(name + "mirror2.png")
        self.ids.image_file.text = self.ids.image_name.text + "mirror2.png"
        self.ids.image_name.text += "mirror2"
        self.ids.image.source = name + "mirror2.png"


PhotoShopApp().run()

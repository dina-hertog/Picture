"""
picture.py
Author: Dina
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

lips= Color(0xff90d0, 1.0)
pink = Color(0xff55f0, 1.0)
blue = Color(0x1090ff, 1.0)
skin = Color(0xffffee,1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
hair1 = Color(0x551000, 1.0)
hair2 = Color(0x5512020, 1.0)
shadowedSkin = Color(0xeeeedd, 1.0)

thinline = LineStyle(1, black)
thickline = LineStyle(2, black)
noline = LineStyle(0, white)

rectangle1 = RectangleAsset(600, 400, thinline, skin)
rectangle2 = RectangleAsset(210, 50, noline, skin)
ellipse1 = EllipseAsset(200, 250, thinline, skin)
triangle1 = PolygonAsset([(430, 250), (460, 230), (460, 270)], thickline, white)
triangle2 = PolygonAsset([(650, 250), (620, 230), (620, 270)], thickline, white)
triangle3 = PolygonAsset([(520, 250), (480, 230), (480, 270)], thickline, white)
triangle4 = PolygonAsset([(560, 250), (600, 230), (600, 270)], thickline, white)
triangle5 = PolygonAsset([(540, 250), (520, 375), (600, 375)], thickline, shadowedSkin) 
circle1 = CircleAsset(50, thinline, hair1)
circle2 = CircleAsset(55, thinline, hair2)
circle3 = CircleAsset(22, thinline, blue)
ellipse2 = EllipseAsset(100, 50, thinline, lips)

#head
Sprite(ellipse1, (550,300))
#level 2 light hair
Sprite(circle2, (390, 80)) #2left3
Sprite(circle2, (500, 20)) #2left1
Sprite(circle2, (600, 25)) #2right1
Sprite(circle2, (720, 90)) #2right3
#level 2 dark hair
Sprite(circle1, (350, 130)) #2left4
Sprite(circle1, (420, 40)) #2left2
Sprite(circle1, (550, 10)) #2top
Sprite(circle1, (670, 50)) #2right2
Sprite(circle1, (760, 150)) #2right4
#level 1 lighthair
Sprite(circle2, (490, 100)) #left1
Sprite(circle2, (620, 95)) #right1
Sprite(circle2, (390, 170)) #left3
Sprite(circle2, (715, 180)) #right3
#level 1 dark hair
Sprite(circle1, (550, 90)) #top
Sprite(circle1, (440, 130)) #left2
Sprite(circle1, (680, 130)) #right2
Sprite(circle1, (350, 220)) #left4
Sprite(circle1, (750, 230)) #right4
#left eye
Sprite(triangle1)
Sprite(triangle3)
Sprite(circle3, (470, 250))
#right eye
Sprite(triangle2)
Sprite(triangle4)
Sprite(circle3, (610, 250))
#nose
Sprite(triangle5)
#mouth
Sprite(ellipse2,(550, 450))
#half mouth cover
Sprite(rectangle2, (450, 400))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
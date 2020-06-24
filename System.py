import pygame
import time, time, copy, random, math
import sqlite3


pygame.init()

WHITE = (255, 255, 255)  # установка цветов
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (27, 65, 16)
LIGHT_GREEN_2 = (227, 254, 228)
DARK_ORANGE = (177, 167, 92)
BROWN = (74, 47, 4)
GRAY = (128, 128, 128)
PINK = (255, 0, 255)
VIOLET = (150, 99, 254)
defold_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 20)
level_3_maps = []
is_click = False


width, height = 0, 0


def get_maps():
    map = [
        [(ps_width(4.895522388059701), ps_height(7.36318407960199), ps_width(0.0), ps_height(0.0), True), (ps_width(0.7761194029850746), ps_height(10.945273631840797), ps_width(0.6567164179104478), ps_height(87.46268656716418), True), (ps_width(0.7761194029850746), ps_height(96.71641791044776), ps_width(98.44776119402985), ps_height(1.691542288557214), True), (ps_width(98.32835820895522), ps_height(10.447761194029852), ps_width(0.9552238805970149), ps_height(86.26865671641791), True), (ps_width(0.7761194029850746), ps_height(10.447761194029852), ps_width(97.55223880597015), ps_height(1.492537313432836), True), (ps_width(3.462686567164179), ps_height(46.169154228855724), ps_width(4.2388059701492535), ps_height(1.9900497512437811), True), (ps_width(6.8059701492537314), ps_height(48.059701492537314), ps_width(0.7761194029850746), ps_height(4.278606965174129), False), (ps_width(4.119402985074627), ps_height(56.71641791044776), ps_width(3.462686567164179), ps_height(3.18407960199005), True), (ps_width(7.641791044776119), ps_height(46.26865671641791), ps_width(0.6567164179104478), ps_height(6.268656716417911), True), (ps_width(4.119402985074627), ps_height(60.0), ps_width(0.9552238805970149), ps_height(28.1592039800995), True), (ps_width(4.119402985074627), ps_height(59.701492537313435), ps_width(0.8955223880597015), ps_height(1.492537313432836), True), (ps_width(1.5522388059701493), ps_height(87.16417910447761), ps_width(0.7761194029850746), ps_height(2.7860696517412937), False), (ps_width(4.358208955223881), ps_height(45.27363184079602), ps_width(1.6119402985074627), ps_height(0.6965174129353234), False), (ps_width(76.53731343283582), ps_height(12.039800995024876), ps_width(6.08955223880597), ps_height(70.74626865671642), True), (ps_width(82.50746268656717), ps_height(77.01492537313433), ps_width(12.776119402985074), ps_height(5.6716417910447765), True), (ps_width(85.25373134328358), ps_height(30.945273631840795), ps_width(11.402985074626866), ps_height(2.5870646766169156), False), (ps_width(83.46268656716418), ps_height(19.203980099502488), ps_width(4.0), ps_height(1.492537313432836), True), (ps_width(86.14925373134328), ps_height(20.597014925373134), ps_width(0.7761194029850746), ps_height(0.8955223880597015), True), (ps_width(85.19402985074628), ps_height(20.597014925373134), ps_width(1.0746268656716418), ps_height(1.691542288557214), True), (ps_width(87.34328358208955), ps_height(19.601990049751244), ps_width(0.47761194029850745), ps_height(0.4975124378109453), True), (ps_width(86.92537313432835), ps_height(18.80597014925373), ps_width(0.5373134328358209), ps_height(0.7960199004975125), True), (ps_width(86.44776119402985), ps_height(18.109452736318406), ps_width(0.5373134328358209), ps_height(1.492537313432836), True), (ps_width(85.31343283582089), ps_height(17.213930348258707), ps_width(1.0149253731343284), ps_height(1.9900497512437811), True), (ps_width(1.7313432835820894), ps_height(33.73134328358209), ps_width(15.343283582089553), ps_height(5.6716417910447765), False), (ps_width(14.746268656716419), ps_height(43.582089552238806), ps_width(1.6119402985074627), ps_height(45.472636815920396), True), (ps_width(33.37313432835821), ps_height(83.88059701492537), ps_width(8.298507462686567), ps_height(12.7363184079602), False), (ps_width(41.014925373134325), ps_height(53.43283582089552), ps_width(9.194029850746269), ps_height(15.721393034825871), True), (ps_width(53.014925373134325), ps_height(31.243781094527364), ps_width(9.253731343283581), ps_height(14.72636815920398), False), (ps_width(28.238805970149254), ps_height(32.53731343283582), ps_width(9.014925373134329), ps_height(16.019900497512438), False), (ps_width(16.597014925373134), ps_height(15.82089552238806), ps_width(9.014925373134329), ps_height(15.422885572139304), True), (ps_width(17.791044776119403), ps_height(49.45273631840796), ps_width(9.492537313432836), ps_height(17.213930348258707), True), (ps_width(52.656716417910445), ps_height(65.4726368159204), ps_width(9.73134328358209), ps_height(15.721393034825871), False), (ps_width(64.35820895522389), ps_height(81.8905472636816), ps_width(9.134328358208956), ps_height(15.124378109452737), True), (ps_width(48.71641791044776), ps_height(14.129353233830846), ps_width(8.895522388059701), ps_height(15.323383084577115), True), (ps_width(85.91044776119404), ps_height(18.208955223880597), ps_width(0.835820895522388), ps_height(1.492537313432836), True)],
        [(ps_width(0.8955223880597015), ps_height(10.945273631840797), ps_width(1.0746268656716418), ps_height(86.96517412935323), True), (ps_width(1.0746268656716418), ps_height(95.42288557213931), ps_width(97.91044776119404), ps_height(2.189054726368159), False), (ps_width(97.31343283582089), ps_height(9.054726368159203), ps_width(1.671641791044776), ps_height(86.3681592039801), True), (ps_width(0.5970149253731343), ps_height(9.253731343283581), ps_width(98.50746268656717), ps_height(1.592039800995025), False), (ps_width(24.417910447761194), ps_height(22.08955223880597), ps_width(20.597014925373134), ps_height(18.507462686567163), True), (ps_width(56.417910447761194), ps_height(46.069651741293534), ps_width(24.29850746268657), ps_height(25.970149253731343), True), (ps_width(45.492537313432834), ps_height(69.55223880597015), ps_width(8.955223880597014), ps_height(7.562189054726368), False), (ps_width(27.46268656716418), ps_height(55.32338308457712), ps_width(4.358208955223881), ps_height(16.218905472636816), True), (ps_width(22.686567164179106), ps_height(60.0), ps_width(17.134328358208954), ps_height(16.51741293532338), False), (ps_width(70.44776119402985), ps_height(24.577114427860696), ps_width(3.2238805970149254), ps_height(4.17910447761194), False), (ps_width(73.01492537313433), ps_height(27.46268656716418), ps_width(3.8208955223880596), ps_height(4.676616915422885), True)],
        [(ps_width(0.5373134328358209), ps_height(10.348258706467663), ps_width(1.2537313432835822), ps_height(87.06467661691542), True), (ps_width(0.5373134328358209), ps_height(95.32338308457712), ps_width(98.68656716417911), ps_height(2.08955223880597), True), (ps_width(97.97014925373135), ps_height(10.64676616915423), ps_width(1.2537313432835822), ps_height(86.86567164179104), True), (ps_width(0.5970149253731343), ps_height(9.751243781094526), ps_width(98.74626865671642), ps_height(1.890547263681592), True), (ps_width(1.8507462686567164), ps_height(39.601990049751244), ps_width(6.626865671641791), ps_height(2.388059701492537), False), (ps_width(7.402985074626866), ps_height(45.57213930348259), ps_width(1.1343283582089552), ps_height(7.7611940298507465), True), (ps_width(1.791044776119403), ps_height(57.114427860696516), ps_width(6.626865671641791), ps_height(2.5870646766169156), False), (ps_width(26.08955223880597), ps_height(26.567164179104477), ps_width(2.4477611940298507), ps_height(53.134328358208954), True), (ps_width(6.149253731343284), ps_height(70.34825870646766), ps_width(11.64179104477612), ps_height(17.81094527363184), True), (ps_width(6.865671641791045), ps_height(15.124378109452737), ps_width(11.462686567164178), ps_height(16.81592039800995), False), (ps_width(28.597014925373134), ps_height(30.945273631840795), ps_width(66.74626865671642), ps_height(2.8855721393034828), False), (ps_width(83.5223880597015), ps_height(11.343283582089553), ps_width(1.7313432835820894), ps_height(16.71641791044776), True), (ps_width(32.53731343283582), ps_height(51.940298507462686), ps_width(2.388059701492537), ps_height(43.582089552238806), False), (ps_width(46.149253731343286), ps_height(64.4776119402985), ps_width(37.97014925373134), ps_height(7.064676616915423), True), (ps_width(35.940298507462686), ps_height(41.592039800995025), ps_width(59.40298507462686), ps_height(2.8855721393034828), False), (ps_width(91.70149253731343), ps_height(36.11940298507463), ps_width(3.044776119402985), ps_height(3.482587064676617), True), (ps_width(86.26865671641791), ps_height(52.13930348258707), ps_width(11.582089552238806), ps_height(9.850746268656716), True), (ps_width(41.014925373134325), ps_height(46.26865671641791), ps_width(8.716417910447761), ps_height(15.621890547263682), True), (ps_width(44.59701492537314), ps_height(88.55721393034825), ps_width(34.92537313432836), ps_height(2.985074626865672), False), (ps_width(44.59701492537314), ps_height(83.68159203980099), ps_width(34.74626865671642), ps_height(2.8855721393034828), False), (ps_width(44.656716417910445), ps_height(78.70646766169155), ps_width(34.62686567164179), ps_height(3.084577114427861), False)]

    ]
    return map


def get_maps_5_level():
    maps = [[(ps_width(3.044776119402985), ps_height(12.437810945273633), ps_width(20.83582089552239), ps_height(23.48258706467662), True), (ps_width(3.8208955223880596), ps_height(13.83084577114428), ps_width(19.223880597014926), ps_height(20.497512437810947), False), (ps_width(4.597014925373134), ps_height(15.223880597014926), ps_width(17.611940298507463), ps_height(17.81094527363184), True), (ps_width(5.373134328358209), ps_height(16.119402985074625), ps_width(16.238805970149254), ps_height(15.721393034825871), False), (ps_width(6.149253731343284), ps_height(17.213930348258707), ps_width(14.746268656716419), ps_height(13.432835820895523), True), (ps_width(6.865671641791045), ps_height(18.208955223880597), ps_width(13.313432835820896), ps_height(11.044776119402986), False), (ps_width(7.582089552238806), ps_height(19.203980099502488), ps_width(11.940298507462687), ps_height(9.054726368159203), True), (ps_width(8.17910447761194), ps_height(20.0), ps_width(10.805970149253731), ps_height(7.36318407960199), False), (ps_width(8.835820895522389), ps_height(20.99502487562189), ps_width(9.492537313432836), ps_height(5.373134328358209), True), (ps_width(9.611940298507463), ps_height(21.791044776119403), ps_width(8.059701492537313), ps_height(3.781094527363184), False), (ps_width(10.388059701492537), ps_height(22.388059701492537), ps_width(6.746268656716418), ps_height(2.6865671641791047), True), (ps_width(11.104477611940299), ps_height(22.98507462686567), ps_width(5.432835820895522), ps_height(1.592039800995025), False), (ps_width(11.701492537313433), ps_height(23.48258706467662), ps_width(4.2388059701492535), ps_height(0.4975124378109453), True), (ps_width(3.4029850746268657), ps_height(5.870646766169155), ps_width(0.0), ps_height(0.0), True)]

            ]
    return random.choice(maps)

def install_size(size):  # инициализация
    global width, height
    width, height = size


def ps_height(percent):  # возрощает число процентов от высоты
    percent = percent / 100
    return int(height * percent)


def ps_width(percent):  # возрощает число процентов от ширены
    percent = percent / 100
    return int(width * percent)


def get_point(cx, cy, r, percent):
    dx = int(math.sin(percent * math.pi / 180) * r)
    dy = int(math.sin((90 - percent) * math.pi / 180) * r)
    x = cx + dx
    y = cy + dy
    return x, y


def draw_0(canvas, complexity, x, y, color=RED):
    draw_symbol(canvas, complexity, x, y, '0', color)


def draw_8(canvas, complexity, x, y, color=RED):
    draw_symbol(canvas, complexity, x, y, '8', color)


def draw_symbol(canvas, complexity, x, y, symbol, color):
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', int(ps_height(14) * complexity))
    txt = Text(canvas, x, y, symbol, font, color)
    txt.show()


def draw_square(canvas, complexity, x, y, color=RED):
    pygame.draw.rect(canvas, color, (x, y, int(ps_width(7) * complexity), int(ps_width(7) * complexity)), 0)



def draw_circle(canvas, complexity, x, y, color=RED):
    pygame.draw.ellipse(canvas, color, (x, y, int(ps_width(7) * complexity), int(ps_width(7) * complexity)))


def draw_circle2(canvas, complexity, x, y, color=RED):
    pygame.draw.ellipse(canvas, color, (x, y, int(ps_width(7) * complexity), int(ps_width(7) * complexity)))
    pygame.draw.ellipse(canvas, BLACK, (x + int(ps_width(2.5) * complexity), y + int(ps_width(2.5) * complexity), int(ps_width(2) * complexity), int(ps_width(2) * complexity)))


def draw_triangle(canvas, complexity, x, y, color=RED):
    pygame.draw.polygon(canvas, color, ((x, y + int(ps_width(7) * complexity)), (x + int(ps_width(7) * complexity) // 2, y), (x + int(ps_width(7) * complexity), y + int(ps_width(7) * complexity))))


def draw_octagon(canvas, complexity, x, y, color=RED):
    complexity /= 1.7
    pygame.draw.polygon(canvas, color, ((x + int(ps_width(7) * complexity / 3 * 2), y), (x + int(ps_width(7) * complexity / 3 * 4), y), (x + int(ps_width(14) * complexity), y + int(ps_width(7) * complexity / 3 * 2)), (x + int(ps_width(14) * complexity), y + int(ps_width(7) * complexity / 3 * 4)), (x + int(ps_width(7) * complexity / 3 * 4), y + int(ps_width(14) * complexity)), (x + int(ps_width(7) * complexity / 3 * 2), y + int(ps_width(14) * complexity)), (x, y + int(ps_width(7) * complexity / 3 * 4)), (x, y + int(ps_width(7) * complexity / 3 * 2))  ))



class Object:  # любой граффический объект
    def __init__(self, canvas, image, x, y, width, height):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visibility = True

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def change_image(self, image):
        self.image = image

    def check_tip(self, x, y):  # проверка на принодлежность х и у в объекте
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self):  # отобразить
        if self.visibility:
            self.canvas.blit(self.image, (self.x, self.y))


class Text(Object):  # объект текст
    def __init__(self, canvas, x, y, text, font=defold_font, color=WHITE):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = str(text)
        self.font = font
        self.visibility = True
        self.color = color
        self.height = len(str(self.text).split('\n')) * ps_height(2)

    def change_text(self, new_text):
        self.text = str(new_text)

    def show(self):  # отобразить построчно
        if not self.visibility and self.image is not None:
            return
        texts = str(self.text).split('\n')
        for i in range(len(texts)):
            text = self.font.render(texts[i], 1, self.color)
            self.canvas.blit(text, (self.x, int(self.y + i * ps_height(2))))


class Button(Object):  # кнопка
    def __init__(self, canvas, image, x, y, width, height, function=None, image_animation=None):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = [function]
        self.image_animation = image_animation
        self.visibility = True
        self.status = False

    def add_function(self, function):  # добовляет функцию
        if self.function == [None]:
            self.function = [function]
        else:
            self.function.append(function)

    def get_function(self, function):  # устонавливает одну функцию
        self.function = [function]

    def del_function(self):  # удоляет все функции
        self.function = [None]

    def get_image_animation(self, image):  # установка анимации при нажатии
        self.image_animation = image

    def show_animation(self):  # отобразить анимацию
        if self.image_animation is not None:
            self.canvas.blit(self.image_animation, (self.x, self.y))
        else:
            self.canvas.blit(self.image, (self.x, self.y))

    def click(self, *args):  # запустить все функции
        if self.function == [None] or not self.visibility:
            return False
        for function in self.function:
            try:
                return function(args)
            except:
                print('не удалось запустить функцию')
                return False

    def show(self):  # отобразить
        if self.visibility and self.image is not None:
            if self.status:
                self.show_animation()
                return
            self.canvas.blit(self.image, (self.x, self.y))


class Window(Object):  # пролистывающиеся окно
    def __init__(self, canvas, image, x, y, width, height, column_count):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.column_count = column_count
        self.visibility = True
        self.paging = False
        self.mod = True
        self.objects = []
        self.shift_y = y
        self.width_object = 70
        self.last_x, self.last_y = 0, 0

    def show_all(self):
        for object in self.objects:
            object.visibility = True

    def hide_all(self):
        for object in self.objects:
            object.visibility = False

    def delete_all_objects(self):
        self.objects = []

    def add_object(self, object):  # добавляет объект и меняет его позицию
        object.visibility = self.visibility

        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (
                self.width // self.column_count) + self.x
        if self.column_count != 1:
            y = (len(self.objects) // self.column_count) * object.height + self.shift_y
        else:
            y = sum(map(lambda x: x.height, self.objects)) + self.shift_y + (ps_height(2) * len(self.objects))
        object.move_to(x, y)
        self.objects.append(object)

    def check(self, event):  # проверка событий
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def pag(self, y):
        self.shift_y = y
        if self.mod:  # следующие действия делают так,
            # чтоб объекты не выходили за границы экрана
            if self.shift_y > self.y:
                self.shift_y = self.y
            if ((len(self.objects) // self.column_count) + 1) >= (
                    self.height // self.width_object):

                if self.shift_y < -((((len(self.objects) // self.column_count)) - (
                        self.height // self.width_object))) * self.width_object:
                    self.shift_y = -((((len(self.objects) // self.column_count)) - (
                            self.height // self.width_object))) * self.width_object
            else:
                self.shift_y = self.y

        for i in range(len(self.objects)):
            object = self.objects[i]
            if self.column_count != 1:
                y = (i // self.column_count) * self.objects[i].height + self.shift_y
            else:
                y = sum(map(lambda x: x.height, self.objects[:i])) + self.shift_y + (ps_height(2) * i)
            object.move_to(object.x, y)

    def render(self):
        if not self.visibility:
            return
        if self.image is not None:
            self.show()
        for object in self.objects:
            object.show()


class Group:  # группа
    def __init__(self):
        self.all_objects = []
        self.last_x, self.last_y = 0, 0
        self.visibility = True
        self.container = []

    def add_objects(self, *objects):
        for object in objects:
            self.all_objects.append(object)

    def delete(self, *objects):
        if len(objects) == 0:
            self.all_objects = []
        for object in objects:
            del self.all_objects[self.all_objects.index(object)]

    def off_all(self):
        for object in self.all_objects:
            object.visibility = False

    def on_all(self):
        for object in self.all_objects:
            object.visibility = True

    def check(self, event):  # проверка событий
        if not self.visibility:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.check_tip(x, y):
                        object.status = True

                if isinstance(object, Window):
                    if event.button == 5:  # скрол вниз
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y - 50)
                    if event.button == 4:  # скрол вверх
                        if object.check_tip(x, y) and object.visibility:
                            object.pag(object.shift_y + 50)
                    if event.button == 1:  # левое нажатие мыши
                        if object.check_tip(x, y) and object.visibility:
                            object.paging = True

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for object in self.all_objects:
                if isinstance(object, Button):
                    if object.status and object.check_tip(x, y):
                        object.click()
                    object.status = False

                if isinstance(object, Window):
                    object.paging = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = self.last_x - x
            shift_y = self.last_y - y
            self.last_x, self.last_y = x, y
            for object in self.all_objects:
                if isinstance(object, Window):
                    if object.paging:
                        object.pag(object.shift_y - shift_y)

    def show(self):  # отображение
        for object in self.all_objects:
            object.show()

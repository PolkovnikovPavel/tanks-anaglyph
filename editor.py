import os, random, random, time
from System import *
from images.images import *


def exit(*args):  # завершает программу
    global running
    save()
    running = False


def convert(i):
    x, y, w, h, c = i

    if w < 0:
        x += w
        w *= -1
    if h < 0:
        y += h
        h *= -1

    x = x * 100 / width
    y = y * 100 / height
    w = w * 100 / width
    h = h * 100 / height
    if c:
        c = 'True'
    else:
        c = 'False'
    return f'(ps_width({x}), ps_height({y}), ps_width({w}), ps_height({h}), {c})'



def save():  # сохраняет текущии данные
    o = []
    for i in member:
        o.append(convert(i))
    print('[' + ', '.join(o) + ']')


def loud(*args):
    global member
    x = [(ps_width(3.044776119402985), ps_height(12.437810945273633), ps_width(20.83582089552239), ps_height(23.48258706467662), True), (ps_width(3.8208955223880596), ps_height(13.83084577114428), ps_width(19.223880597014926), ps_height(20.497512437810947), False), (ps_width(4.597014925373134), ps_height(15.223880597014926), ps_width(17.611940298507463), ps_height(17.81094527363184), True), (ps_width(5.373134328358209), ps_height(16.119402985074625), ps_width(16.238805970149254), ps_height(15.721393034825871), False), (ps_width(6.149253731343284), ps_height(17.213930348258707), ps_width(14.746268656716419), ps_height(13.432835820895523), True), (ps_width(6.865671641791045), ps_height(18.208955223880597), ps_width(13.313432835820896), ps_height(11.044776119402986), False), (ps_width(7.582089552238806), ps_height(19.203980099502488), ps_width(11.940298507462687), ps_height(9.054726368159203), True), (ps_width(8.17910447761194), ps_height(20.0), ps_width(10.805970149253731), ps_height(7.36318407960199), False), (ps_width(8.835820895522389), ps_height(20.99502487562189), ps_width(9.552238805970148), ps_height(5.373134328358209), True), (ps_width(9.611940298507463), ps_height(21.791044776119403), ps_width(8.059701492537313), ps_height(3.781094527363184), False), (ps_width(10.388059701492537), ps_height(22.388059701492537), ps_width(6.746268656716418), ps_height(2.6865671641791047), True), (ps_width(11.104477611940299), ps_height(22.98507462686567), ps_width(5.492537313432836), ps_height(1.592039800995025), False), (ps_width(11.761194029850746), ps_height(23.48258706467662), ps_width(4.2388059701492535), ps_height(0.5970149253731343), True)]

    if len(x) == 0:
        return
    member = x



def create_all_objects():  # определяет все объекты
    image = get_free_image('images/circle.png', (ps_width(2), ps_width(2)))
    img = Object(screen, image, ps_width(3), ps_height(50), ps_width(2),
                 ps_width(2))
    always_on_display.add_objects(img)

    image = get_free_image('images/square_blue.png', (ps_width(3), ps_width(3)))
    img = Object(screen, image, ps_width(90), ps_height(18), ps_width(3), ps_width(3))
    always_on_display.add_objects(img)

    image = get_free_image('images/setings.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(95), ps_height(2), ps_width(4),
                 ps_width(4))
    always_on_display.add_objects(btn)

    image = get_free_image('images/home.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(2), ps_height(2), ps_width(4),
                 ps_width(4))
    btn.add_function(loud)
    always_on_display.add_objects(btn)



FPS = 100
ratio = 3 / 5  # отношение сторон окна приложения

type_window = 'main_window'  # опредиление типа окна

display = pygame.display.Info()  # установка окна прриложения в нужном месте под
# любой физический размер экрана
width, height = display.current_w - 75, display.current_h - 75
if width * ratio <= height:
    height = int(width * ratio)
else:
    width = int(height / ratio)
size = width, height
print(size)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)
install_size(size)  # инсталяция итоговых размеров окна для дальнейшей работы

objects_main = Group()
always_on_display = Group()
last_x = 0
last_y = 0
pos_x = 0
pos_y = 0
is_click = False
is_color = True
member = []

create_all_objects()

running = True
bg = BLACK
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)  # поддержка фпс
    screen.fill(bg)

    for event in pygame.event.get():
        always_on_display.check(event)

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_color = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_color = False
            else:
                del member[-1]

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            is_click = True
            last_x = x
            last_y = y

        if event.type == pygame.MOUSEBUTTONUP:
            is_click = False
            x = last_x
            y = last_y
            w = pos_x - last_x
            h = pos_y - last_y
            c = is_color
            member.append((x, y, w, h, c))

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            pos_x = x
            pos_y = y

    if is_click:
        if is_color:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)

        pygame.draw.rect(screen, color, (last_x, last_y, pos_x - last_x, pos_y - last_y), 1)

    for i in member:
        x, y, w, h, c = i
        if c:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h), 0)
        else:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, w, h), 0)

    always_on_display.show()
    pygame.display.flip()  # обновление экрана

pygame.quit()

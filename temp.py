import os, random, random, time
from System import *
from images.images import *


def exit(*args):  # завершает программу
    global running
    save()
    running = False


def save():  # сохраняет текущии данные
    pass


def start_1_level(*args):
    global type_window, complexity, timer
    type_window = '1_level'
    level_1_group.delete()
    complexity = 1.9
    timer = time.time()
    u = random.choices(range(2))[0]

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 40)
    txt = Text(screen, ps_width(30), ps_height(3), 'Попадайте в танки другого цвета', font)
    level_1_group.add_objects(txt)

    xy = [(i + random.choice(range(ps_width(3))), j + random.choice(range(ps_width(3)))) for j in
          range(ps_height(60) - int(ps_width(5 * complexity)) * 2,
                ps_height(60) + int(ps_width(5 * complexity)),
                int(ps_width(5 * complexity)))
          for i in
          range(ps_width(50) - int(ps_width(5 * complexity)) * 3,
                ps_width(50) + int(ps_width(5 * complexity)) * 3,
                int(ps_width(5 * complexity)))]

    if u == 0:
        image = get_free_image('images/tank_red.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
        x, y = random.choice(xy)
        del xy[xy.index((x, y))]
        two_tank = Button(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
        two_tank.add_function(continue_level_1)
        level_1_group.add_objects(two_tank)
        for i in range(17):
            image = get_free_image('images/tank_blue.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
            x, y = random.choice(xy)
            del xy[xy.index((x, y))]
            tank = Object(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
            level_1_group.add_objects(tank)
    else:
        image = get_free_image('images/tank_blue.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
        x, y = random.choice(xy)
        del xy[xy.index((x, y))]
        two_tank = Button(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
        two_tank.add_function(continue_level_1)
        level_1_group.add_objects(two_tank)
        for i in range(17):
            image = get_free_image('images/tank_red.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
            x, y = random.choice(xy)
            del xy[xy.index((x, y))]
            tank = Object(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
            level_1_group.add_objects(tank)


def continue_level_1(*args):
    global type_window, complexity, timer
    level_1_group.delete()
    complexity -= 0.1
    timer = time.time()
    if complexity < 0.2:
        start_2_level()
        return
    u = random.choices(range(2))[0]

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 40)
    txt = Text(screen, ps_width(30), ps_height(3), 'Попадайте в танки другого цвета', font)
    level_1_group.add_objects(txt)

    xy = [(i + random.choice(range(ps_width(3))),
           j + random.choice(range(ps_width(3)))) for j in
          range(ps_height(60) - int(ps_width(5 * complexity)) * 2,
                ps_height(60) + int(ps_width(5 * complexity)),
                int(ps_width(5 * complexity)))
          for i in
          range(ps_width(50) - int(ps_width(5 * complexity)) * 3,
                ps_width(50) + int(ps_width(5 * complexity)) * 3,
                int(ps_width(5 * complexity)))]

    if u == 0:
        image = get_free_image('images/tank_red.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
        x, y = random.choice(xy)
        del xy[xy.index((x, y))]
        two_tank = Button(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
        two_tank.add_function(continue_level_1)
        level_1_group.add_objects(two_tank)
        for i in range(17):
            image = get_free_image('images/tank_blue.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
            x, y = random.choice(xy)
            del xy[xy.index((x, y))]
            tank = Object(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
            level_1_group.add_objects(tank)
    else:
        image = get_free_image('images/tank_blue.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
        x, y = random.choice(xy)
        del xy[xy.index((x, y))]
        two_tank = Button(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
        two_tank.add_function(continue_level_1)
        level_1_group.add_objects(two_tank)
        for i in range(17):
            image = get_free_image('images/tank_red.png', (ps_width(5 * complexity), ps_width(5 * complexity)))
            x, y = random.choice(xy)
            del xy[xy.index((x, y))]
            tank = Object(screen, image, x, y, ps_width(5 * complexity), ps_width(5 * complexity))
            level_1_group.add_objects(tank)


def start_2_level(*args):
    global type_window, complexity, timer, platform, losing_level_2, animation_group_level_2
    type_window = '2_level'
    level_2_group.delete()
    complexity = 1.5
    losing_level_2 = 0
    timer = time.time()
    aim.visibility = False

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 40)
    txt = Text(screen, ps_width(30), ps_height(3), 'Уворачивайтесь от летящих блоков', font)
    level_2_group.add_objects(txt)

    if num_colour:
        image = get_free_image('images/platform_blue.png', (ps_width(11.94 / complexity), ps_height(6.69 / complexity)))
    else:
        image = get_free_image('images/platform_red.png', (ps_width(11.94 / complexity), ps_height(6.69 / complexity)))
    platform = Object(screen, image, 0, ps_height(93), ps_width(11.94 / complexity), ps_height(6.69 / complexity))
    level_2_group.add_objects(platform)

    animation_group_level_2 = []
    for i in range(12):
        w, h = random.choices(range(ps_width(1), ps_width(2)))[0], random.choices(range(ps_width(3), ps_width(4)))[0]
        surf = pygame.Surface((w, h))
        if num_colour:
            surf.fill((255, 0, 0))
        else:
            surf.fill((0, 0, 255))
        animation_group_level_2.append((surf, [random.choices(range(0, width))[0],
                    random.choices(range(-20, height))[0],
                    random.choices(range(int(4 / complexity), int(11 / complexity)))[0], w, h]
                                        ))


def continue_level_2(*args):
    global complexity, timer, losing_level_2, bg
    for i in animation_group_level_2:
        x, y = i[1][:2]
        if y > 0:
            rect = pygame.Rect((x, y, 0, 0))
            screen.blit(i[0], rect)
        i[1][1] += i[1][2]
        if i[1][1] > height:
            i[1][0] = random.choices(range(0, width))[0]
            i[1][1] = -80
            i[1][2] = random.choices(range(int(4 / complexity), int(11 / complexity)))[0]

        if platform.check_tip(i[1][3] + i[1][0], i[1][4] + i[1][1]):
            losing_level_2 = 1

    if time.time() - timer > 4:
        w, h = random.choices(range(ps_width(1), ps_width(2)))[0], \
               random.choices(range(ps_width(3), ps_width(4)))[0]
        surf = pygame.Surface((w, h))
        if num_colour:
            surf.fill((255, 0, 0))
        else:
            surf.fill((0, 0, 255))
        animation_group_level_2.append(
            (surf, [random.choices(range(0, width))[0],
                    random.choices(range(-20, height))[0],
                    random.choices(range(int(4 / complexity), int(11 / complexity)))[0], w, h]
             ))

        complexity -= 0.1
        timer = time.time()
    if complexity < 0.4:
        start_3_level()
        return

    if losing_level_2 > 28:
        losing_level_2 = 0
        bg = BLACK

    if losing_level_2 > 0:
        if losing_level_2 % 2 == 0:
            losing_level_2 += 1
            if bg == BLACK:
                bg = WHITE
            else:
                bg = BLACK
        else:
            losing_level_2 += 1


def start_3_level(*args):
    global type_window, complexity, timer, moving_level_3, walls_level_3, losing_level_3

    type_window = '3_level'
    moving_level_3 = [0, 0]
    walls_level_3 = Group()
    losing_level_3 = 0
    aim.visibility = True
    timer = time.time()

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 40)
    txt = Text(screen, ps_width(30), ps_height(3), 'управление: ↓→↑←  Доберитесь до крестика', font)
    level_3_group.add_objects(txt)

    level_3_group.all_objects[0].move_to(ps_width(3), ps_height(50))
    map = level_3_maps[random.choice(range(len(level_3_maps)))]
    del level_3_maps[level_3_maps.index(map)]
    for i in map:
        x, y, w, h, c = i
        surf = pygame.Surface((w, h))
        if num_colour:
            if c:
                surf.fill((255, 0, 0))
            else:
                surf.fill((0, 0, 255))
        else:
            if c:
                surf.fill((0, 0, 255))
            else:
                surf.fill((255, 0, 0))
        obj = Object(screen, surf, x, y, w, h)
        walls_level_3.add_objects(obj)


def continue_level_3(*args):
    global losing_level_3, bg
    level_3_group.all_objects[0].x += moving_level_3[0]
    level_3_group.all_objects[0].y += moving_level_3[1]
    x = level_3_group.all_objects[0].x
    y = level_3_group.all_objects[0].y
    w = level_3_group.all_objects[0].width
    h = level_3_group.all_objects[0].height
    for i in walls_level_3.all_objects:
        if i.check_tip(x, y) or i.check_tip(x + w, y) or i.check_tip(x + w, y + h) or i.check_tip(x, y + h) or i.check_tip(x + w // 2, y + h // 2):
            level_3_group.all_objects[0].x -= moving_level_3[0]
            level_3_group.all_objects[0].y -= moving_level_3[1]
            if losing_level_3 == 0:
                losing_level_3 = 1
            break

    if level_3_group.all_objects[0].check_tip(ps_width(91.5), ps_height(19.5)) or time.time() - timer > 35:
        start_4_level()
        return

    if losing_level_3 > 0:
        if losing_level_3 % 2 == 0:
            losing_level_3 += 1
            if bg == BLACK:
                bg = WHITE
            else:
                bg = BLACK
        else:
            losing_level_3 += 1
    if losing_level_3 > 28:
        losing_level_3 = 0
        bg = BLACK


def start_4_level(*args):
    global type_window, complexity, timer, moving_level_3, walls_level_3, losing_level_3

    type_window = '4_level'
    moving_level_3 = [0, 0]
    walls_level_3 = Group()
    losing_level_3 = 0
    aim.visibility = True
    timer = time.time()

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 40)
    txt = Text(screen, ps_width(30), ps_height(3), 'управление: ↓→↑←  Доберитесь до крестика', font)
    level_3_group.add_objects(txt)

    level_3_group.all_objects[0].move_to(ps_width(3), ps_height(50))
    map = level_3_maps[random.choice(range(len(level_3_maps)))]
    del level_3_maps[level_3_maps.index(map)]
    for i in map:
        x, y, w, h, c = i
        surf = pygame.Surface((w, h))
        if c:
            surf.fill((255, 0, 0))
        else:
            surf.fill((0, 0, 255))
        obj = Object(screen, surf, x, y, w, h)
        walls_level_3.add_objects(obj)


def continue_level_4(*args):
    global losing_level_3, bg
    level_3_group.all_objects[0].x += moving_level_3[0]
    level_3_group.all_objects[0].y += moving_level_3[1]
    x = level_3_group.all_objects[0].x
    y = level_3_group.all_objects[0].y
    w = level_3_group.all_objects[0].width
    h = level_3_group.all_objects[0].height
    for i in walls_level_3.all_objects:
        if i.check_tip(x, y) or i.check_tip(x + w, y) or i.check_tip(x + w, y + h) or i.check_tip(x, y + h) or i.check_tip(x + w // 2, y + h // 2):
            level_3_group.all_objects[0].x -= moving_level_3[0]
            level_3_group.all_objects[0].y -= moving_level_3[1]
            if losing_level_3 == 0:
                losing_level_3 = 1
            break

    if level_3_group.all_objects[0].check_tip(ps_width(91.5), ps_height(19.5)) or time.time() - timer > 35:
        go_to_main()
        return

    if losing_level_3 > 0:
        if losing_level_3 % 2 == 0:
            losing_level_3 += 1
            if bg == BLACK:
                bg = WHITE
            else:
                bg = BLACK
        else:
            losing_level_3 += 1
    if losing_level_3 > 28:
        losing_level_3 = 0
        bg = BLACK


def start_5_level(*args):
    global type_window
    type_window = '5_level'
    aim.visibility = True
    timer = time.time()


def continue_level_5(*args):
    pass

def go_to_main(*args):
    global type_window, bg, level_3_maps
    aim.visibility = True
    bg = BLACK
    level_3_maps = get_maps()
    type_window = 'main_window'


def create_all_objects():  # определяет все объекты
    global animation_group, aim, num_colour, level_3_maps, level_3_maps_temp
    num_colour = False
    animation_group = []
    for i in range(39):
        line = random.choices(range(ps_height(1), ps_width(5)))
        surf = pygame.Surface((line[0], line[0]))
        surf.fill((0, 0, 255))
        animation_group.append((surf, [random.choices(range(0, width))[0], random.choices(range(-20, height))[0], random.choices(range(3, 13))[0]]))

    image = get_free_image('images/setings.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(95), ps_height(2), ps_width(4), ps_width(4))
    always_on_display.add_objects(btn)

    image = get_free_image('images/home.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(2), ps_height(2), ps_width(4), ps_width(4))
    btn.add_function(go_to_main)
    always_on_display.add_objects(btn)

    image = get_free_image('images/start_a_game.png', (ps_width(17.91), ps_height(9.8505)))
    btn = Button(screen, image, ps_width(41.045), ps_height(45.07475), ps_width(17.91), ps_height(9.8505))
    btn.add_function(start_3_level)
    objects_main.add_objects(btn)
t
    image = get_free_image('images/aim.png', (ps_width(5), ps_width(5)))
    aim = Object(screen, image, 0, 0, ps_width(5), ps_width(5))

    image = get_free_image('images/circle.png', (ps_width(2), ps_width(2)))
    img = Object(screen, image, ps_width(3), ps_height(50), ps_width(2), ps_width(2))
    level_3_group.add_objects(img)

    if num_colour:
        image = get_free_image('images/square_blue.png', (ps_width(3), ps_width(3)))
    else:
        image = get_free_image('images/square_red.png', (ps_width(3), ps_width(3)))
    img = Object(screen, image, ps_width(90), ps_height(18), ps_width(3), ps_width(3))
    level_3_group.add_objects(img)


    level_3_maps = get_maps()


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

pygame.mouse.set_visible(False)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)
install_size(size)  # инсталяция итоговых размеров окна для дальнейшей работы

objects_main = Group()
always_on_display = Group()
level_1_group = Group()
level_2_group = Group()
level_3_group = Group()
level_5_group = Group()
animation_group_level_2 = []
create_all_objects()

running = True
bg = BLACK
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)  # поддержка фпс
    screen.fill(bg)

    for event in pygame.event.get():
        always_on_display.check(event)
        if type_window == 'main_window':
            objects_main.check(event)
        if type_window == '1_level':
            level_1_group.check(event)
        if type_window == '3_level' or type_window == '4_level':
            level_3_group.check(event)

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYUP:
            if type_window == '3_level' or type_window == '4_level':
                if event.key == pygame.K_LEFT and moving_level_3[0] == -2:
                    moving_level_3[0] = 0
                elif event.key == pygame.K_RIGHT and moving_level_3[0] == 2:
                    moving_level_3[0] = 0
                elif event.key == pygame.K_UP and moving_level_3[1] == -2:
                    moving_level_3[1] = 0
                elif event.key == pygame.K_DOWN and moving_level_3[1] == 2:
                    moving_level_3[1] = 0

        if event.type == pygame.KEYDOWN:
            if type_window == '3_level' or type_window == '4_level':
                if event.key == pygame.K_LEFT:
                    moving_level_3[0] = -2
                elif event.key == pygame.K_RIGHT:
                    moving_level_3[0] = 2
                elif event.key == pygame.K_UP:
                    moving_level_3[1] = -2
                elif event.key == pygame.K_DOWN:
                    moving_level_3[1] = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.MOUSEBUTTONUP:
            pass

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            aim.move_to(x - ps_width(3), y - ps_width(3))
            if type_window == '2_level':
                platform.move_to(x - ps_width(5.97), ps_height(93))


    always_on_display.show()
    if type_window == 'main_window':
        for i in animation_group:
            x, y = i[1][:2]
            if y > 0:
                rect = pygame.Rect((x, y, 0, 0))
                screen.blit(i[0], rect)
            i[1][1] += i[1][2]
            if i[1][1] > height:
                i[1][0] = random.choices(range(0, width))[0]
                i[1][1] = -80
                i[1][2] = random.choices(range(3, 13))[0]
        objects_main.show()
    if type_window == '1_level':
        level_1_group.show()
        if time.time() - timer > 10:
            continue_level_1()
    if type_window == '2_level':
        level_2_group.show()
        continue_level_2()
    if type_window == '3_level':
        level_3_group.show()
        walls_level_3.show()
        continue_level_3()
    if type_window == '4_level':
        level_3_group.show()
        walls_level_3.show()
        continue_level_4()

    aim.show()
    pygame.display.flip()  # обновление экрана

pygame.quit()

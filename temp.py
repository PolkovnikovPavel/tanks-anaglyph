import os, random, random, time
from System import *
from images.images import *


def exit(*args):  # завершает программу
    global running
    save()
    running = False


def save():  # сохраняет текущии данные
    pass


def change_color(*args):
    global num_colour
    if num_colour:
        num_colour = False
        image = get_free_image('images/square_blue.png', (ps_width(3), ps_width(3)))
    else:
        num_colour = True
        image = get_free_image('images/square_red.png', (ps_width(3), ps_width(3)))
    settings_group.all_objects[1].change_image(image)


def start_settings(*args):
    global type_window, bg
    aim.visibility = True
    bg = BLACK
    type_window = 'settings'


def start_all_levels(*args):
    global type_launch
    type_launch = True
    start_1_level()


def start_all_levels_2(*args):
    global type_launch
    type_launch = True
    start_10_level()


def start_1_level(*args):
    global type_window, complexity, timer
    type_window = '1_level'
    level_1_group.delete()
    complexity = 1.9
    timer = time.time()
    u = random.choices(range(2))[0]

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
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
        if type_launch:
            start_2_level()
        else:
            go_to_mode_1()
        return
    u = random.choices(range(2))[0]

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
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

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
    txt = Text(screen, ps_width(30), ps_height(3), 'Уворачивайтесь от летящих блоков', font)
    level_2_group.add_objects(txt)

    if num_colour:
        image = get_free_image('images/platform_blue.png', (ps_width(11.94 / 1.5), ps_height(6.69 / 1.5)))
    else:
        image = get_free_image('images/platform_red.png', (ps_width(11.94 / 1.5), ps_height(6.69 / 1.5)))
    platform = Object(screen, image, 0, ps_height(93), ps_width(11.94 / 1.5), ps_height(6.69 / 1.5))
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

    pygame.draw.rect(screen, (255, 255, 255, 50), (0, 0, int((width / 4) * (time.time() - timer)), 13), 0)

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
                    random.choices(range(-20, height - ps_height(80)))[0],
                    random.choices(range(int(4 / complexity), int(11 / complexity)))[0], w, h]
             ))

        complexity -= 0.1
        timer = time.time()
    if complexity < 0.4:
        if type_launch:
            start_3_level()
        else:
            go_to_mode_1()
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

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
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

    if level_3_group.all_objects[0].check_tip(ps_width(91.5), ps_height(19.5)) or time.time() - timer > 62:
        if type_launch:
            start_4_level()
        else:
            go_to_mode_1()
        return
    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 62) * (time.time() - timer)), 13), 0)

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

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
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

    if level_3_group.all_objects[0].check_tip(ps_width(91.5), ps_height(19.5)) or time.time() - timer > 62:
        if type_launch:
            start_5_level()
        else:
            go_to_mode_1()
        return
    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 62) * (time.time() - timer)), 13), 0)

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
    global type_window, level_5_map, timer
    type_window = '5_level'
    aim.visibility = True
    timer = time.time()
    level_5_map = []

    for i in get_maps_5_level():
        x, y, w, h, c = i
        f = True
        surf = pygame.Surface((w, h))
        if f:
            if c:
                surf.fill((255, 0, 0))
            else:
                surf.fill((0, 0, 255))
        else:
            pass
        obj = Object(screen, surf, x, y, w, h)
        level_5_group.add_objects(obj)


def continue_level_5(*args):
    if time.time() - timer > 150:
        if type_launch:
            start_6_level()
        else:
            go_to_mode_1()
        return

    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 150) * (time.time() - timer)), 13), 0)


    for i in level_5_map:
        x, y, w, h, c, f = i
        if not f:
            if c:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h), 0)
            else:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, w, h), 0)
        else:
            if w < 0:
                w = -w
                x -= w
            if h < 0:
                h = -h
                y -= h
            if c:
                pygame.draw.ellipse(screen, (255, 0, 0), (x, y, w, h))
            else:
                pygame.draw.ellipse(screen, (0, 0, 255), (x, y, w, h))

    if is_click:
        x, y, w, h, c, f = old_x, old_y, pos_x - old_x, pos_y - old_y, is_color, is_circle
        if not f:
            if c:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h), 2)
            else:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, w, h), 2)
        else:
            if w < 0:
                w = -w
                x -= w
            if h < 0:
                h = -h
                y -= h
            if c:
                pygame.draw.ellipse(screen, (255, 0, 0), (x, y, w, h))
            else:
                pygame.draw.ellipse(screen, (0, 0, 255), (x, y, w, h))


def appdate_6_level():
    if time.time() - timer > 15:
        continue_level_6()

    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 15) * (time.time() - timer)), 13), 0)

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
    txt = Text(screen, ps_width(29), ps_height(2.5), 'Найдите такую же фигуру как в центре', font)
    txt.show()

    if num_colour:
        color = RED
    else:
        color = BLUE

    pygame.draw.rect(screen, color, (ps_width(29), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, PINK, (ps_width(43), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))

    for i in range(len(functions)):
        args = arguments[i]
        functions[i](*args)


def start_6_level(*args):
    global type_window, timer, complexity, arguments, functions
    type_window = '6_level'
    aim.visibility = True
    complexity = 1
    level_6_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14), ps_width(14))
    right_call.add_function(continue_level_6)
    level_6_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))


def continue_level_6(*args):
    global type_window, timer, complexity, arguments, functions
    complexity -= 0.1
    if complexity < 0.2:
        if type_launch:
            start_9_level()
        else:
            go_to_mode_1()
        return

    level_6_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14),
                        ps_width(14))
    right_call.add_function(continue_level_6)
    level_6_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

# доделать 7 и 8 уровни(это тоже самое что и 6 уровень)
def appdate_7_level():
    if time.time() - timer > 15:
        continue_level_6()

    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 15) * (time.time() - timer)), 13), 0)

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
    txt = Text(screen, ps_width(29), ps_height(2.5), 'Найдите такую же фигуру как в центре', font)
    txt.show()

    if num_colour:
        color = RED
    else:
        color = BLUE

    pygame.draw.rect(screen, color, (ps_width(29), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, PINK, (ps_width(43), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))

    for i in range(len(functions)):
        args = arguments[i]
        functions[i](*args)


def start_7_level(*args):
    global type_window, level_5_map, timer, complexity, arguments, functions
    type_window = '7_level'
    aim.visibility = True
    complexity = 1
    level_7_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    variants_of_departure = [(0, 0), (ps_width(7), 0), (ps_width(7), ps_width(7)), (0, ps_width(7))]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    departure = random
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14), ps_width(14))
    right_call.add_function(continue_level_7)
    level_7_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))


def continue_level_7(*args):
    global type_window, level_5_map, timer, complexity, arguments, functions
    complexity -= 0.1
    if complexity < 0.2:
        go_to_mode_1()

    level_6_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14),
                        ps_width(14))
    right_call.add_function(continue_level_6)
    level_6_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))


def appdate_8_level():
    if time.time() - timer > 15:
        continue_level_6()

    pygame.draw.rect(screen, WHITE, (0, 0, int((width / 15) * (time.time() - timer)), 13), 0)

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4))
    txt = Text(screen, ps_width(29), ps_height(2.5), 'Найдите такую же фигуру как в центре', font)
    txt.show()

    if num_colour:
        color = RED
    else:
        color = BLUE

    pygame.draw.rect(screen, color, (ps_width(29), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(5), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(29), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(43), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, color, (ps_width(57), ps_width(33), ps_width(14), ps_width(14)), ps_width(0.5))
    pygame.draw.rect(screen, PINK, (ps_width(43), ps_width(19), ps_width(14), ps_width(14)), ps_width(0.5))

    for i in range(len(functions)):
        args = arguments[i]
        functions[i](*args)


def start_8_level(*args):
    global type_window, level_5_map, timer, complexity, arguments, functions
    type_window = '7_level'
    aim.visibility = True
    complexity = 1
    level_6_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14), ps_width(14))
    right_call.add_function(continue_level_6)
    level_6_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))


def continue_level_8(*args):
    global type_window, level_5_map, timer, complexity, arguments, functions
    complexity -= 0.1
    if complexity < 0.2:
        go_to_mode_1()

    level_6_group.delete()
    timer = time.time()
    surf = pygame.Surface((ps_width(14), ps_width(14)))

    obj1 = Object(screen, surf, ps_width(29), ps_width(5), ps_width(14), ps_width(14))
    obj2 = Object(screen, surf, ps_width(43), ps_width(5), ps_width(14), ps_width(14))
    obj3 = Object(screen, surf, ps_width(57), ps_width(5), ps_width(14), ps_width(14))
    obj4 = Object(screen, surf, ps_width(29), ps_width(19), ps_width(14), ps_width(14))
    obj5 = Object(screen, surf, ps_width(43), ps_width(19), ps_width(14), ps_width(14))
    obj6 = Object(screen, surf, ps_width(57), ps_width(19), ps_width(14), ps_width(14))
    obj7 = Object(screen, surf, ps_width(29), ps_width(33), ps_width(14), ps_width(14))
    obj8 = Object(screen, surf, ps_width(43), ps_width(33), ps_width(14), ps_width(14))
    obj9 = Object(screen, surf, ps_width(57), ps_width(33), ps_width(14), ps_width(14))

    arguments = []
    functions = []

    options = [draw_circle, draw_square, draw_triangle, draw_octagon, draw_circle2]
    right = random.choice(options)
    del options[options.index(right)]
    calls = [obj1, obj2, obj3, obj4, obj6, obj7, obj8, obj9]

    right_call = random.choice(calls)
    del calls[calls.index(right_call)]
    right_call = Button(screen, surf, right_call.x, right_call.y, ps_width(14),
                        ps_width(14))
    right_call.add_function(continue_level_6)
    level_6_group.add_objects(right_call)

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, right_call.x + int(ps_width(7) - ps_width(7) * complexity / 2), right_call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    if random.choice(range(2)) == 1:
        color = RED
    else:
        color = BLUE
    functions.append(right)
    arguments.append((screen, complexity, obj5.x + int(ps_width(7) - ps_width(7) * complexity / 2), obj5.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))

    for call in calls:
        if random.choice(range(2)) == 1:
            color = RED
        else:
            color = BLUE
        functions.append(random.choice(options))
        arguments.append((screen, complexity, call.x + int(ps_width(7) - ps_width(7) * complexity / 2), call.y + int(ps_width(7) - ps_width(7) * complexity / 2), color))


def appdate_9_level():
    if int(time.time() * 10) % 2 == 0:
        if num_colour:
            color = BLUE
        else:
            color = RED
        if figure == 0 or figure == 3 or figure == 6:
            pygame.draw.circle(screen, color, (x, y), ps_width(15))
        elif figure == 1 or figure == 5:
            pygame.draw.rect(screen, color, (x - ps_width(15), y - ps_width(15), ps_width(30), ps_width(30)), 0)
        elif figure == 2 or figure == 4:
            pygame.draw.polygon(screen, color, (
            (x, y - ps_width(15)),
            (x + ps_width(15), y + ps_width(15)),
            (x - ps_width(15), y + ps_width(15))
                                                ))

    else:
        if num_colour:
            color = RED
        else:
            color = BLUE
        if figure == 0 or figure == 3 or figure == 6:
            pygame.draw.circle(screen, color, (level_9_group.container[0][0], level_9_group.container[0][1]), ps_width(15))
        elif figure == 1 or figure == 5:
            pygame.draw.rect(screen, color, (level_9_group.container[0][0] - ps_width(15), level_9_group.container[0][1] - ps_width(15), ps_width(30), ps_width(30)), 0)
        elif figure == 2 or figure == 4:
            pygame.draw.polygon(screen, color, (
            (level_9_group.container[0][0], level_9_group.container[0][1] - ps_width(15)),
            (level_9_group.container[0][0] + ps_width(15), level_9_group.container[0][1] + ps_width(15)),
            (level_9_group.container[0][0] - ps_width(15), level_9_group.container[0][1] + ps_width(15))
                                                ))


def start_9_level(*args):
    global type_window, figure
    type_window = '9_level'
    aim.visibility = False
    figure = 0

    level_9_group.container = [[ps_width(50), ps_height(40)], []]
    level_9_group.delete()
    btn = Button(screen, None, ps_width(10), ps_height(10), ps_width(80), ps_width(90), continue_level_9)
    level_9_group.add_objects(btn)


def continue_level_9(*args):
    global figure
    if len(level_9_group.all_objects) > 1:
        level_9_group.delete()
        btn = Button(screen, None, ps_width(10), ps_height(10), ps_width(80), ps_width(90), continue_level_9)
        level_9_group.add_objects(btn)
    delte_x = abs(level_9_group.container[0][0] - x)
    delte_y = abs(level_9_group.container[0][1] - y)
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3.2))
    txt = Text(screen, ps_width(45), ps_height(5), f'Сдвиг на: {int(((delte_x ** 2 + delte_y ** 2) ** 0.5) * 100) / 100} ед.', font)
    level_9_group.add_objects(txt)
    level_9_group.container[1].append((delte_x ** 2 + delte_y ** 2) ** 0.5)
    level_9_group.container[0] = [random.choice(range(ps_width(20), ps_width(80))), random.choice(range(ps_height(34), ps_height(66)))]

    figure += 1
    if figure == 8:
        go_to_mode_1()
    elif figure == 7:
        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3.2))
        middle = int(sum(level_9_group.container[1]) / len(
            level_9_group.container[1]) * 100) / 100
        minn = int(min(level_9_group.container[1]) * 100) / 100
        maxx = int(max(level_9_group.container[1]) * 100) / 100
        t = f'''    Средний сдвиг: {middle} ед.\n
    Минимальный сдвиг: {minn} ед.\n
    Максимальный сдвиг: {maxx} ед.'''
        txt = Text(screen, ps_width(45), ps_height(15), t, font)
        level_9_group.add_objects(txt)


def appdate_10_level():
    global animation_group_level_10
    animation_group_level_10[1] -= level_10_group.container[1]
    percent = animation_group_level_10[1]
    delte = 360 // (level_10_group.container[0] * 2)
    for i in range(level_10_group.container[0]):
        pygame.draw.polygon(screen, animation_group_level_10[6], (
            (ps_width(50), ps_height(50)),
            get_point(ps_width(50), ps_height(50), ps_width(250), percent),
            get_point(ps_width(50), ps_height(50), ps_width(250), delte + percent)
        ))

        percent += delte * 2

    animation_group_level_10[0] += level_10_group.container[1]
    percent = animation_group_level_10[0]
    delte = 360 // (level_10_group.container[0] * 2)
    animation_group_level_10[2] += animation_group_level_10[4]
    animation_group_level_10[3] += animation_group_level_10[5]
    x, y = animation_group_level_10[2], animation_group_level_10[3]
    for i in range(level_10_group.container[0]):
        pygame.draw.polygon(screen, animation_group_level_10[7], (
            (x, y),
            get_point(x, y, ps_width(250), percent),
            get_point(x, y, ps_width(250),
                      delte + percent)
        ))

        percent += delte * 2

    if x > ps_width(49.5) and x < ps_width(50.5) and y > ps_height(49.5) and y < ps_height(50.5):
        continue_level_10()


def start_10_level(*args):
    global type_window, bg, animation_group_level_10
    type_window = '10_level'
    aim.visibility = False
    animation_group_level_10 = [0, 0, random.choice(range(ps_width(22), ps_width(78))),
                                random.choice(range(ps_height(22), ps_height(78))),
                                0, 0, WHITE, BLACK]
    bg = animation_group_level_10[7]
    level_10_group.container = [20, 0.5, 1]


def continue_level_10(*args):
    global bg, animation_group_level_10
    color_1 = WHITE
    color_2 = BLACK
    level_10_group.container[0] = 20
    level_10_group.container[1] = 0.5

    if level_10_group.container[2] == 1:
        level_10_group.container[0] = 20
        level_10_group.container[1] = 0.4
        color_1 = RED
        color_2 = GREEN
    elif level_10_group.container[2] == 2:
        level_10_group.container[0] = 20
        level_10_group.container[1] = 0.6
        color_1 = BLACK
        color_2 = DARK_ORANGE
    elif level_10_group.container[2] == 3:
        level_10_group.container[0] = 36
        level_10_group.container[1] = 0.3
        color_1 = WHITE
        color_2 = GREEN
    elif level_10_group.container[2] == 4:
        level_10_group.container[0] = 20
        level_10_group.container[1] = 0.7
        color_1 = WHITE
        color_2 = RED
    elif level_10_group.container[2] == 5:
        level_10_group.container[0] = 20
        level_10_group.container[1] = 0.5
        color_1 = WHITE
        color_2 = GRAY
    elif level_10_group.container[2] == 6:
        level_10_group.container[0] = 18
        level_10_group.container[1] = 0.72
        color_1 = VIOLET
        color_2 = BLUE
    elif level_10_group.container[2] == 7:
        level_10_group.container[0] = 20
        level_10_group.container[1] = 0.58
        color_1 = PINK
        color_2 = RED
    elif level_10_group.container[2] == 8:
        if not type_launch:
            go_to_mode_2()
        else:
            start_1_level()
        return

    animation_group_level_10 = [0, 0, random.choice(range(ps_width(22), ps_width(78))),
                                random.choice(range(ps_height(22), ps_height(78))),
                                0, 0, color_1, color_2]
    bg = color_2
    level_10_group.container[2] += 1



def appdate_11_level():
    pass


def start_11_level(*args):
    global type_window, bg
    type_window = '11_level'
    aim.visibility = False


def continue_level_11(*args):
    pass


def go_to_main(*args):
    global type_window, bg, level_3_maps, type_launch
    aim.visibility = True
    type_launch = False
    bg = BLACK
    level_3_maps = get_maps()
    type_window = 'modes'


def go_to_mode_1(*args):
    global type_window, bg, level_3_maps, type_launch
    aim.visibility = True
    type_launch = False
    bg = BLACK
    level_3_maps = get_maps()
    type_window = 'mode_1'


def go_to_mode_2(*args):
    global type_window, bg, type_launch
    aim.visibility = True
    type_launch = False
    bg = LIGHT_GREEN_2
    type_window = 'mode_2'


def create_all_objects():  # определяет все объекты
    global animation_group, aim, num_colour, level_3_maps, is_color, is_circle, type_launch, animation_group_2, animation_group_level_10
    is_color = False
    is_circle = False
    num_colour = False
    type_launch = False
    animation_group = []
    animation_group_2 = []
    animation_group_level_10 = [0, 0, random.choice(
        range(ps_width(22), ps_width(78))), random.choice(
        range(ps_height(22), ps_height(78))), 0, 0]

    for i in range(42):
        line = random.choices(range(ps_height(1), ps_width(5)))
        surf = pygame.Surface((line[0], line[0]))
        surf.fill((0, 0, 255))
        animation_group.append((surf, [random.choices(range(0, width))[0], random.choices(range(-20, height))[0], random.choices(range(3, 13))[0]]))

    image = get_free_image('images/setings.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(95), ps_height(2), ps_width(4), ps_width(4))
    btn.add_function(start_settings)
    image = get_free_image('images/setings_2.png', (ps_width(4), ps_width(4)))
    btn.get_image_animation(image)
    always_on_display.add_objects(btn)

    image = get_free_image('images/home.png', (ps_width(4), ps_width(4)))
    btn = Button(screen, image, ps_width(2), ps_height(2), ps_width(4), ps_width(4))
    btn.add_function(go_to_main)
    always_on_display.add_objects(btn)

    image = get_free_image('images/start_a_game.png', (ps_width(17.91), ps_height(9.8505)))
    btn = Button(screen, image, ps_width(41.045), ps_height(45.07475), ps_width(17.91), ps_height(9.8505))
    btn.add_function(go_to_mode_1)
    objects_main.add_objects(btn)

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

    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(4.5))
    txt = Text(screen, ps_width(10), ps_height(30), 'Инверсия цвета для 3D очков', font)
    settings_group.add_objects(txt)

    image = get_free_image('images/square_blue.png', (ps_width(3), ps_width(3)))
    btn = Button(screen, image, ps_width(65), ps_height(30), ps_width(3), ps_width(3))
    btn.add_function(change_color)
    settings_group.add_objects(btn)

    image = get_free_image('images/start_a_mode_1.png', (ps_width(15), ps_width(19.5)))
    btn = Button(screen, image, ps_width(33), ps_height(30), ps_width(15), ps_width(19.5))
    btn.add_function(go_to_mode_1)
    modes_group.add_objects(btn)

    image = get_free_image('images/start_a_mode_2.png', (ps_width(15), ps_width(19.5)))
    btn = Button(screen, image, ps_width(52), ps_height(30), ps_width(15), ps_width(19.5))
    btn.add_function(go_to_mode_2)
    modes_group.add_objects(btn)

    surf = pygame.Surface((1, 1))
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3))

    btn = Button(screen, surf, ps_width(10), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_all_levels)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(12), ps_height(13), 'Играть\n\nвсе', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(25), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_1_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(27), ps_height(13), 'Найди\n\nдругой\n\nтанк', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(40), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_2_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(41), ps_height(13), 'Увернись\n\nот пуль', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(55), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_3_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(56), ps_height(13), 'Лабиринт', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(70), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_5_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(71), ps_height(13), 'Рисовалка', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(10), ps_height(32), ps_width(10), ps_width(10))
    btn.add_function(start_6_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(12), ps_height(35), 'Поиски', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(25), ps_height(32), ps_width(10), ps_width(10))
    btn.add_function(start_9_level)
    mode_1_group.add_objects(btn)
    txt = Text(screen, ps_width(28), ps_height(35), 'Тест', font)
    mode_1_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(10), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_all_levels_2)
    mode_2_group.add_objects(btn)
    txt = Text(screen, ps_width(12), ps_height(13), 'Играть\n\nвсе', font, BROWN)
    mode_2_group.add_objects(txt)

    btn = Button(screen, surf, ps_width(25), ps_height(10), ps_width(10), ps_width(10))
    btn.add_function(start_10_level)
    mode_2_group.add_objects(btn)
    txt = Text(screen, ps_width(27), ps_height(13), 'Паучок', font, BROWN)
    mode_2_group.add_objects(txt)


FPS = 100
ratio = 3 / 5  # отношение сторон окна приложения

type_window = 'modes'  # опредиление типа окна

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

old_x = 0
old_y = 0
pos_x = 0
pos_y = 0

objects_main = Group()
always_on_display = Group()
settings_group = Group()
modes_group = Group()
mode_1_group = Group()
mode_2_group = Group()
level_1_group = Group()
level_2_group = Group()
level_3_group = Group()
level_5_group = Group()
level_6_group = Group()
level_7_group = Group()
level_8_group = Group()
level_9_group = Group()
level_10_group = Group()
animation_group_level_2 = []
create_all_objects()

running = True
is_click = False
x, y = 0, 0
bg = BLACK
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)  # поддержка фпс
    screen.fill(bg)
    # print(old_x, old_y, pos_x, pos_y)


    for event in pygame.event.get():
        always_on_display.check(event)
        if type_window == 'main_window':
            objects_main.check(event)
        elif type_window == '1_level':
            level_1_group.check(event)
        elif type_window == '3_level' or type_window == '4_level':
            level_3_group.check(event)
        elif type_window == '6_level':
            level_6_group.check(event)
        elif type_window == '9_level':
            level_9_group.check(event)
        elif type_window == 'settings':
            settings_group.check(event)
        elif type_window == 'modes':
            modes_group.check(event)
        elif type_window == 'mode_1':
            mode_1_group.check(event)
        elif type_window == 'mode_2':
            mode_2_group.check(event)

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYUP:
            if type_window == '3_level' or type_window == '4_level':
                if event.key == pygame.K_LEFT and moving_level_3[0] == -ps_width(0.13):
                    moving_level_3[0] = 0
                elif event.key == pygame.K_RIGHT and moving_level_3[0] == ps_width(0.13):
                    moving_level_3[0] = 0
                elif event.key == pygame.K_UP and moving_level_3[1] == -ps_width(0.13):
                    moving_level_3[1] = 0
                elif event.key == pygame.K_DOWN and moving_level_3[1] == ps_width(0.13):
                    moving_level_3[1] = 0
            elif type_window == '5_level':
                if event.key == pygame.K_SPACE:
                    is_circle = False
            elif type_window == '10_level':
                if event.key == pygame.K_LEFT and animation_group_level_10[4] == -ps_height(0.13):
                    animation_group_level_10[4] = 0
                elif event.key == pygame.K_RIGHT and animation_group_level_10[4] == ps_height(0.13):
                    animation_group_level_10[4] = 0
                elif event.key == pygame.K_UP and animation_group_level_10[5] == -ps_height(0.13):
                    animation_group_level_10[5] = 0
                elif event.key == pygame.K_DOWN and animation_group_level_10[5] == ps_height(0.13):
                    animation_group_level_10[5] = 0

        if event.type == pygame.KEYDOWN:
            if type_window == '3_level' or type_window == '4_level':
                if event.key == pygame.K_LEFT:
                    moving_level_3[0] = -ps_width(0.13)
                elif event.key == pygame.K_RIGHT:
                    moving_level_3[0] = ps_width(0.13)
                elif event.key == pygame.K_UP:
                    moving_level_3[1] = -ps_width(0.13)
                elif event.key == pygame.K_DOWN:
                    moving_level_3[1] = ps_width(0.13)
            elif type_window == '5_level':
                if event.key == pygame.K_SPACE:
                    is_circle = True
                else:
                    if len(level_5_map) > 0:
                        del level_5_map[-1]
            elif type_window == '10_level':
                if event.key == pygame.K_LEFT:
                    animation_group_level_10[4] = -ps_height(0.13)
                elif event.key == pygame.K_RIGHT:
                    animation_group_level_10[4] = ps_height(0.13)
                elif event.key == pygame.K_UP:
                    animation_group_level_10[5] = -ps_height(0.13)
                elif event.key == pygame.K_DOWN:
                    animation_group_level_10[5] = ps_height(0.13)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            old_x = x
            old_y = y
            is_click = True
            if type_window == '5_level':
                if event.button == 3:
                    is_color = True
                else:
                    is_color = False


        if event.type == pygame.MOUSEBUTTONUP:
            is_click = False
            if type_window == '5_level':
                level_5_map.append((old_x, old_y, pos_x - old_x, pos_y - old_y, is_color, is_circle))


        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            pos_x = x
            pos_y = y
            aim.move_to(x - ps_width(3), y - ps_width(3))
            if type_window == '2_level':
                platform.move_to(x - ps_width(11.94 / 3), ps_height(93))



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
    elif type_window == '1_level':
        level_1_group.show()
        if time.time() - timer > 10:
            continue_level_1()
    elif type_window == '2_level':
        level_2_group.show()
        continue_level_2()
    elif type_window == '3_level':
        level_3_group.show()
        walls_level_3.show()
        continue_level_3()
    elif type_window == '4_level':
        level_3_group.show()
        walls_level_3.show()
        continue_level_4()
    elif type_window == '5_level':
        continue_level_5()
        level_5_group.show()
    elif type_window == '6_level':
        appdate_6_level()
    elif type_window == '9_level':
        appdate_9_level()
        level_9_group.show()
    elif type_window == '10_level':
        appdate_10_level()
    elif type_window == 'settings':
        settings_group.show()
    elif type_window == 'modes':
        for i in animation_group:
            sx, sy = i[1][:2]
            if y > 0:
                rect = pygame.Rect((sx, sy, 0, 0))
                screen.blit(i[0], rect)
            i[1][1] += i[1][2]
            if is_click:
                i[1][1] += int(i[1][2] * 1.3)
            if x - ps_width(7) < sx and x + ps_width(7) > sx and y - ps_height(10) < sy and y + ps_height(10) > sy:
                i[1][1] += int(i[1][2] * 4)
            if i[1][1] > height:
                i[1][0] = random.choices(range(0, width))[0]
                i[1][1] = -80
                i[1][2] = random.choices(range(3, 13))[0]
        modes_group.show()

    elif type_window == 'mode_1':
        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3))
        for object in mode_1_group.all_objects:
            if isinstance(object, Button):
                x, y, w, h = object.x, object.y, object.width, object.height
                pygame.draw.rect(screen, PINK, (x, y, w, h), ps_width(0.7))
            elif isinstance(object, Text):
                object.show()

    elif type_window == 'mode_2':
        font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', ps_height(3))
        for object in mode_2_group.all_objects:
            if isinstance(object, Button):
                x, y, w, h = object.x, object.y, object.width, object.height
                pygame.draw.rect(screen, DARK_ORANGE, (x, y, w, h), ps_width(0.7))
            elif isinstance(object, Text):
                object.show()

    aim.show()
    if not aim.visibility:
        pygame.draw.ellipse(screen, (255, 0, 255), (x, y, ps_width(0.7), ps_width(0.7)))
    pygame.display.flip()  # обновление экрана

pygame.quit()

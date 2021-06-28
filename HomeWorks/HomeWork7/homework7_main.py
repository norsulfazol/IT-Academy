#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############
# Main module #
###############

import random
from turtle import *
from time import sleep
from homework7_obj import Room, Strength, PositiveHero, NegativeHero

_DEFAULTS = {'room_side_len': 40,
             'rooms_num_x': 10,
             'rooms_num_y': 10,
             'room_walls_num_min': 1,
             'room_walls_num_max': 2,
             'artifacts_strength_num': 0,
             'artifact_strength_shape': 1,
             'artifact_strength_color': 2,
             'artifact_strength_val': 0,
             'p_hero_shape': 1,
             'p_hero_color': 1,
             'p_hero_num_moves_at_time': 1,
             'p_hero_strength': 0,
             'n_heroes_num': 10,
             'n_hero_shape': 1,
             'n_hero_color': 1,
             'n_hero_num_moves_at_time': 1,
             'n_hero_strength': 0}

_FONTS = {'main': ('Arial', 18, 'bold'), 'hint': ('Arial', 10, 'bold')}

get_sequence_str = lambda sequence: ''.join([f'\n{i} - {e}' for i, e in enumerate(sequence)])


def get_obj_info(obj):
    obj[1].write(f'{obj[0]}\n', align='center', font=_FONTS['hint'])
    sleep(1)
    obj[1].undo()


if __name__ == '__main__':
    title = '!!! BASTARDS [v.1.2-alpha] !!!'
    window = Screen()
    window.title(f'{title} (Initializing the maze ...)')
    params = {'room_side_len': ('Room side length in pixels', 40, 100),
              'rooms_num_x': ('Number of rooms horizontally', 2, 100),
              'rooms_num_y': ('Number of rooms vertically', 2, 100),
              'room_walls_num_min': ('Minimum number of walls in the room', 0, 3),
              'room_walls_num_max': ('Maximum number of walls in the room', 0, 3)}
    for k in params:
        i = numinput('Maze parameters', f'{params[k][0]} (int, {params[k][1]}-{params[k][2]})',
                     _DEFAULTS[k], params[k][1], params[k][2])
        params[k] = _DEFAULTS[k] if i is None else int(i)
    if params['room_walls_num_max'] < params['room_walls_num_min']:
        params['room_walls_num_max'] = params['room_walls_num_min']
    window.screensize(canvwidth=params['rooms_num_x'] * params['room_side_len'],
                      canvheight=params['rooms_num_y'] * params['room_side_len'],
                      bg='black')
    window.setup(width=params['rooms_num_x'] * params['room_side_len'] + 100,
                 height=params['rooms_num_y'] * params['room_side_len'] + 100,
                 startx=None, starty=None)
    title = f'{title} [{params["rooms_num_x"]}x{params["rooms_num_y"]}, {params["room_side_len"]}px]'
    #
    window.title(f'{title} (Building a maze ...)')
    rooms = []
    maze = Turtle()
    maze.pen(shown=False,
             pendown=False,
             pencolor='white',
             pensize=1,
             speed=10)
    maze.goto(window.screensize()[0] / -2, window.screensize()[1] / 2)
    for y in range(params['rooms_num_y']):
        for x in range(params['rooms_num_x']):
            # creating a new room object
            rooms.append(Room(side_lenght=params['room_side_len'],
                              coords=(int(maze.xcor() + params['room_side_len'] // 2),
                                      int(maze.ycor() - params['room_side_len'] // 2))))
            for i in ((1, 'right', 'left'), (params["rooms_num_x"], 'bottom', 'top')):
                if len(rooms) > i[0] and not rooms[-i[0] - 1].side_is_wall(i[1]):
                    rooms[-i[0] - 1].available_rooms(available_rooms={i[1]: rooms[-1]})
                    rooms[-1].available_rooms(available_rooms={i[2]: rooms[-i[0] - 1]})
                    rooms[-1].side_is_wall(location=i[2], is_wall=False)
            # room walls
            room_walls_num = random.randint(params['room_walls_num_min'], params['room_walls_num_max'])
            # generating a list of room walls that can be removed
            room_walls_to_remove = [i[1] for i in ((int(maze.xcor()) != int(window.screensize()[0] / 2) -
                                                    params['room_side_len'], 'right'),
                                                   (int(maze.ycor()) != int(window.screensize()[1] / -2) +
                                                    params['room_side_len'], 'bottom'))
                                    if i[0] and i[1] in rooms[-1].get_walls_locations()]
            # adjusting the number of walls in the room
            while len(rooms[-1].get_walls_locations()) > room_walls_num and room_walls_to_remove:
                rooms[-1].side_is_wall(location=room_walls_to_remove.pop(random.randrange(len(room_walls_to_remove))),
                                       is_wall=False)
            # drawing a new room
            for i in (('top', maze.setx, maze.xcor, 1),
                      ('right', maze.sety, maze.ycor, -1),
                      ('bottom', maze.setx, maze.xcor, -1),
                      ('left', maze.sety, maze.ycor, 1)):
                if rooms[-1].side_is_wall(location=i[0]):
                    maze.pd()
                else:
                    maze.pu()
                i[1](i[2]() + params['room_side_len'] * i[3])
            maze.pu()
            maze.setx(window.screensize()[0] / -2 if x == params['rooms_num_x'] - 1
                      else maze.xcor() + params['room_side_len'])
        maze.sety(window.screensize()[1] / 2 if y == params['rooms_num_y'] - 1
                  else maze.ycor() - params['room_side_len'])
    maze.goto(0, 0)
    maze.color('blue')
    maze.write('This is such a maze ...', align='center', font=_FONTS['main'])
    sleep(1.5)
    maze.undo()
    #
    window.title(f'{title} (Initializing artifacts ...)')
    shapes_num, colors_num = len(Strength.shapes), len(Strength.colors)
    params = {'artifacts_strength_num': ('Number of "strength" artifacts (int, 1-10, 0-random)', 0, 10),
              'artifact_strength_shape': (
                  f'"Strength" artifact shape (int, 0-{shapes_num - 1}): {get_sequence_str(Strength.shapes)}',
                  0, shapes_num - 1),
              'artifact_strength_color': (
                  f'"Strength" artifact color (int, 0-{colors_num - 1}): {get_sequence_str(Strength.colors)}',
                  0, colors_num - 1),
              'artifact_strength_val': ('Value of "strength" artifact (int, -10-10, 0-random)', -10, 10)}
    for k in params:
        i = numinput('Artifacts parameters', params[k][0], _DEFAULTS[k], params[k][1], params[k][2])
        params[k] = _DEFAULTS[k] if i is None else int(i)
    if not params['artifact_strength_shape']:
        params['artifact_strength_shape'] = random.randrange(1, shapes_num)
    if not params['artifact_strength_color']:
        params['artifact_strength_color'] = random.randrange(1, colors_num)
    #
    window.title(f'{title} (Building artifacts ...)')
    artifacts = []
    for _ in range(params['artifacts_strength_num'] if params['artifacts_strength_num'] else random.randint(1, 10)):
        artifacts.append((Strength(current_room=random.choice(rooms),
                                   value=params['artifact_strength_val'] if params['artifact_strength_val']
                                   else random.randint(1, 10) * random.choice((-1, 1))),
                          Turtle()))
        artifacts[-1][1].pen(shown=False,
                             pendown=False,
                             pencolor=Strength.colors[params['artifact_strength_color']],
                             pensize=1,
                             speed=1)
        artifacts[-1][1].shape(Strength.shapes[params['artifact_strength_shape']])
        artifacts[-1][1].color(Strength.colors[params['artifact_strength_color']])
        artifacts[-1][1].goto(*artifacts[-1][0].current_room().coords())
        artifacts[-1][1].st()
        artifacts[-1][1].write(f'{artifacts[-1][0]}\n', align='center', font=_FONTS['hint'])
        sleep(1)
        artifacts[-1][1].undo()
    #
    window.title(f'{title} (Initializing positive hero ...)')
    shapes_num, colors_num = len(PositiveHero.shapes), len(PositiveHero.colors)
    params = {
        'p_hero_shape': (f'Positive hero shape (int, 0-{shapes_num - 1}): {get_sequence_str(PositiveHero.shapes)}',
                         0, shapes_num - 1),
        'p_hero_color': (f'Positive hero color (int, 0-{colors_num - 1}): {get_sequence_str(PositiveHero.colors)}',
                         0, colors_num - 1),
        'p_hero_num_moves_at_time': ('Number of positive hero moves at a time (int, 1-10, 0-random)', 0, 10),
        'p_hero_strength': ('Value of positive hero strength (int, 1-20, 0-random)', 0, 20)}
    for k in params:
        i = numinput('Positive hero parameters', params[k][0], _DEFAULTS[k], params[k][1], params[k][2])
        params[k] = _DEFAULTS[k] if i is None else int(i)
    if not params['p_hero_shape']:
        params['p_hero_shape'] = random.randrange(1, shapes_num)
    if not params['p_hero_color']:
        params['p_hero_color'] = random.randrange(1, colors_num)
    #
    window.title(f'{title} (Building positive hero ...)')
    heroes = [(PositiveHero(current_room=random.choice(rooms),
                            num_moves_at_time=params['p_hero_num_moves_at_time']
                            if params['p_hero_num_moves_at_time'] else random.randint(1, 10),
                            strength=params['p_hero_strength']
                            if params['p_hero_strength'] else random.randint(1, 20)),
               Turtle())]
    heroes[0][1].pen(shown=False,
                     pendown=False,
                     pencolor=PositiveHero.colors[params['p_hero_color']],
                     pensize=1,
                     speed=1)
    heroes[0][1].shape(PositiveHero.shapes[params['p_hero_shape']])
    heroes[0][1].color(PositiveHero.colors[params['p_hero_color']])
    heroes[0][1].onclick(lambda x, y: get_obj_info(heroes[0]))
    heroes[0][1].goto(*heroes[0][0].current_room().coords())
    heroes[0][1].settiltangle(270)
    heroes[0][1].st()
    heroes[0][1].write(f'{heroes[0][0]}\n', align='center', font=_FONTS['hint'])
    sleep(1)
    heroes[0][1].undo()
    #
    window.title(f'{title} (Initializing negative heroes ...)')
    shapes_num = len(NegativeHero.shapes)
    colors = [i for i in NegativeHero.colors if i != PositiveHero.colors[params['p_hero_color']]]
    colors_num = len(colors)
    params = {'n_heroes_num': ('Number of negative heroes (int, 1-50, 0-random):', 0, 50),
              'n_hero_shape': (
                  f'Negative hero shape (int, 0-{shapes_num - 1}): {get_sequence_str(NegativeHero.shapes)}',
                  0, shapes_num - 1),
              'n_hero_color': (f'Negative hero color (int, 0-{colors_num - 1}): {get_sequence_str(colors)}',
                               0, colors_num - 1),
              'n_hero_num_moves_at_time': ('Number of negative hero moves at a time (int, 1-10, 0-random)', 0, 10),
              'n_hero_strength': ('Value of negative hero strength (int, 1-10, 0-random)', 0, 10)}
    for k in params:
        i = numinput('Negative heroes parameters', params[k][0], _DEFAULTS[k], params[k][1], params[k][2])
        params[k] = _DEFAULTS[k] if i is None else int(i)
    #
    window.title(f'{title} (Building negative heroes ...)')
    for _ in range(params['n_heroes_num'] if params['n_heroes_num'] else random.randint(1, 50)):
        hero_shape = NegativeHero.shapes[
            params['n_hero_shape'] if params['n_hero_shape'] else random.randrange(1, shapes_num)]
        hero_color = colors[params['n_hero_color'] if params['n_hero_color'] else random.randrange(1, colors_num)]
        heroes.append((NegativeHero(current_room=random.choice(rooms),
                                    num_moves_at_time=params['n_hero_num_moves_at_time']
                                    if params['n_hero_num_moves_at_time'] else random.randint(1, 10),
                                    strength=params['n_hero_strength']
                                    if params['n_hero_strength'] else random.randint(1, 10)),
                       Turtle()))
        while heroes[-1][0].current_room() is heroes[0][0].current_room():
            heroes[-1][0].current_room(random.choice(rooms))
        heroes[-1][1].pen(shown=False,
                          pendown=False,
                          pencolor=hero_color,
                          pensize=1,
                          speed=1)
        heroes[-1][1].shape(hero_shape)
        heroes[-1][1].color(hero_color)
        heroes[-1][1].goto(*heroes[-1][0].current_room().coords())
        heroes[-1][1].settiltangle(90)
        heroes[-1][1].st()
        heroes[-1][1].write(f'{heroes[-1][0]}\n', align='center', font=_FONTS['hint'])
        sleep(1)
        heroes[-1][1].undo()
    #
    maze.write("Let's start the battle ...", align='center', font=_FONTS['main'])
    sleep(1.5)
    maze.undo()
    window.title(f'{title} (Battle ...)')
    while heroes[0][0].strength() > 0 and heroes[1:]:
        # heroes movements
        for h in range(2):
            if heroes[0][0].strength() < 1 or not heroes[1:]:
                break
            hero = (heroes[0], random.choice(heroes[1:]))[h]
            for _ in range(hero[0].num_moves_at_time()):
                if heroes[0][0].strength() < 1 or not heroes[1:]:
                    break
                available_rooms = list(hero[0].current_room().available_rooms().values())
                if available_rooms:
                    random_room = random.choice(available_rooms)
                    hero[1].settiltangle((0, 90, 180, 270)[('right', 'top', 'left', 'bottom').index(
                        hero[0].current_room().get_available_room_location(random_room))])
                    hero[1].goto(*random_room.coords())
                    hero[0].current_room(random_room)
                    # eating artifacts
                    contacts = [i for i in artifacts if i[0].current_room() is hero[0].current_room()]
                    while contacts:
                        contact = contacts.pop()
                        hero[1].resizemode('user')
                        hero[1].shapesize(2, 2)
                        sleep(.2)
                        contact[1].ht()
                        hero[1].undo()
                        hero[0].strength(hero[0].strength() + contact[0].value())
                        if hero[0].strength() < 1:
                            hero[0].strength(1)
                        hero[1].write(f'+{contact[0].value()} strength\n'.replace('+-', '-'),
                                      align='center', font=_FONTS['hint'])
                        sleep(1)
                        hero[1].undo()
                        artifacts.remove(contact)
                    # fight
                    contacts = [i for i in heroes[1:] if i[0].current_room() is heroes[0][0].current_room()]
                    while contacts:
                        contact = contacts.pop()
                        contact[1].resizemode('user')
                        heroes[0][1].resizemode('user')
                        for i in range(3):
                            for j in (contact[1], heroes[0][1]):
                                j.shapesize(2, 2)
                                sleep(.2)
                                j.undo()
                                sleep(.2)
                        heroes[0][0].strength(heroes[0][0].strength() - contact[0].strength())
                        heroes[0][1].write(f'{"losing" if heroes[0][0].strength() < 1 else "winning"}\n',
                                           align='center', font=_FONTS['hint'])
                        sleep(1)
                        heroes[0][1].undo()
                        if heroes[0][0].strength() < 1:
                            heroes[0][1].ht()
                            break
                        contact[1].ht()
                        heroes.remove(contact)
    maze.write(f'Positive hero {"lost" if heroes[0][0].strength() < 1 else "won"}!', align='center',
               font=_FONTS['main'])
    sleep(1.5)
    maze.undo()
    maze.write('GAME OVER', align='center', font=_FONTS['main'])
    window.title(f'{title} GAME OVER')
    sleep(1.5)
    window.bye()

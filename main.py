def on_up_pressed():
    global up_chek
    up_chek = 1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global b_chek
    b_chek = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_set_enter_handler():
    global a_chek, b_chek, left_chek, right_chek, up_chek, down_chek, runtime_chek, menu_check
    a_chek = 0
    b_chek = 0
    left_chek = 0
    right_chek = 0
    up_chek = 0
    down_chek = 0
    runtime_chek = 0
    menu_check = 0
states.set_enter_handler("boot", on_set_enter_handler)

def on_a_pressed():
    global a_chek
    a_chek = 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    global down_chek
    down_chek = 0
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    global left_chek
    left_chek = 1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_menu_released():
    global menu_check
    menu_check = 0
controller.menu.on_event(ControllerButtonEvent.RELEASED, on_menu_released)

def on_right_released():
    global right_chek
    right_chek = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global left_chek
    left_chek = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    global right_chek
    right_chek = 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_a_released():
    global a_chek
    a_chek = 0
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_up_released():
    global up_chek
    up_chek = 0
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    global down_chek
    down_chek = 1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_menu_pressed():
    global menu_check
    menu_check = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_b_released():
    global b_chek
    b_chek = 0
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_add_loop_handler():
    if boot_chek == 1:
        pass
    else:
        control.reset()
states.add_loop_handler("runtime", on_add_loop_handler)

def on_set_exit_handler():
    basic.show_leds("""
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
states.set_exit_handler("boot", on_set_exit_handler)

def on_set_enter_handler2():
    global runtime_chek
    screen().fill(8)
    runtime_chek = 1
states.set_enter_handler("runtime", on_set_enter_handler2)

menu_check = 0
runtime_chek = 0
down_chek = 0
right_chek = 0
left_chek = 0
a_chek = 0
b_chek = 0
up_chek = 0
hash2 = 0
boot_chek = 0
temporany_temperature = input.temperature()
temporany_buss = input.compass_heading()
temporany_light = input.light_level()
random = randint(0, 65535)
temp_hash = random + temporany_temperature * (temporany_buss * temporany_light)
random += 1
boot_chek = 0
states.set_state("boot")
if temp_hash == random + temporany_temperature * (temporany_buss * temporany_light) - 1:
    hash2 = temp_hash - 12347
    temp_hash = hash2 - 4517
    temporany_buss = 0
    temporany_light = 0
    temporany_temperature = 0
    random = randint(0, 65535)
    boot_chek = temp_hash + 12347 + (hash2 + 4517) - (temp_hash + 12347 + (hash2 + 4517)) + 1
    if boot_chek == 1:
        states.set_state("runtime")
    else:
        control.reset()
else:
    control.reset()

def on_every_interval():
    if runtime_chek == 1:
        if boot_chek == 1:
            screen().fill(8)
            screen().print("hash", 0, 0, 1)
            screen().print(convert_to_text(hash2), 100, 0, 1)
            screen().print("a_check", 0, 8, 1)
            screen().print(convert_to_text(a_chek), 100, 8, 1)
            screen().print("b_check", 0, 16, 1)
            screen().print(convert_to_text(b_chek), 100, 16, 1)
            screen().print("up_check", 0, 24, 1)
            screen().print(convert_to_text(up_chek), 100, 24, 1)
            screen().print("down_check", 0, 32, 1)
            screen().print(convert_to_text(down_chek), 100, 32, 1)
            screen().print("left_check", 0, 40, 1)
            screen().print(convert_to_text(left_chek), 100, 40, 1)
            screen().print("right_check", 0, 48, 1)
            screen().print(convert_to_text(right_chek), 100, 48, 1)
            screen().print("menu_check", 0, 56, 1)
            screen().print(convert_to_text(menu_check), 100, 56, 1)
        else:
            control.reset()
    else:
        control.reset()
loops.every_interval(34, on_every_interval)

def on_every_interval2():
    global boot_chek
    if temp_hash == hash2 - 4517:
        boot_chek = 1
    else:
        boot_chek = 0
loops.every_interval(10000, on_every_interval2)

def on_every_interval3():
    global a_chek, b_chek, left_chek, right_chek, up_chek, down_chek
    if a_chek == 1:
        a_chek = 0
    if (0) == (1):
        b_chek = 0
    if left_chek == 1:
        left_chek = 0
    if right_chek == 1:
        right_chek = 0
    if up_chek == 1:
        up_chek = 0
    if down_chek == 1:
        down_chek = 0
loops.every_interval(60000, on_every_interval3)

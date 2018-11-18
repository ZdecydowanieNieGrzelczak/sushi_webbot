import win32api
import win32con
import time
import PIL.ImageOps
from numpy import *
import PIL.ImageGrab
import pyautogui

# Globals
# --------------------------------------------
x_pad = 465
y_pad = 229
food_on_hand = {'shrimp': 5, 'rice': 10, 'nori': 10, 'roe': 10, 'salmon': 5, 'unagi': 5}
sushiTypes = {2119: 'onigiri', 2376: 'caliroll', 2046: 'gunkan'}


class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041


class Cord:

    # FOOD
    # ----------------------------------------
    f_shrimp = (43, 334)
    f_rice = (94, 332)
    f_nori = (30, 387)
    f_roe = (92, 386)
    f_salmon = (34, 441)
    f_unagi = (96, 440)

    # TELEPHONE
    # ---------------------------------------
    telephone = (564, 372)
    toppings = (547, 272)
    t_shrimp = (505, 222)
    t_unagi = (580, 228)
    t_nori = (501, 279)
    t_roe = (583, 272)
    t_salmon = (495, 327)
    t_back = (556, 329)
    t_exit = (599, 338)

    menu_rice = (533, 292)
    buy_rice = (553, 295)
    delivery_norm = (496, 291)
    delivery_fast = (571, 294)

    tables = [(80, 206), (187, 208), (281, 205), (390, 213), (490, 209), (591, 208)]

    bad_nori = (33, 30, 11)
    bad_unagi = (94, 49, 8)
    bad_shrimp = (127, 71, 47)
    bad_roe = (101, 13, 13)
    bad_salmon = (127, 71, 47)
    bad_rice = (127, 127, 127)


def screen_grab():
    box = (466, 230, 1105, 709)
    image = PIL.ImageGrab.grab(box)
    # image.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return image
    
    
def left_click():
    pyautogui.click()
    pyautogui.click()
    # x, y = get_cords()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # time.sleep(.1)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print 'left Down'


def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print 'left release'


def mouse_pos(coordinates):
    if coordinates == get_cords():
        print 'twoja stara'
        return
    win32api.SetCursorPos((0, 0))
    win32api.SetCursorPos((coordinates[0] + x_pad, coordinates[1] + y_pad))


def get_cords():
    x, y = win32api.GetCursorPos()
    return x, y


def start_game():
    mouse_pos([100, 100])
    left_click()
    # first menu
    mouse_pos([351, 210])
    time.sleep(.5)
    left_click()


    # second menu
    mouse_pos([310, 387])
    time.sleep(.5)
    left_click()



    # third menu
    mouse_pos([569, 449])
    time.sleep(.5)
    left_click()

    # forth menu
    mouse_pos([304, 375])
    time.sleep(.5)
    left_click()


def clear_tables():
    for i in range(len(Cord.tables)):
        mouse_pos(Cord.tables[i])
        left_click()
        left_click()
    time.sleep(1)
    

def fold_mat():
    mouse_pos((Cord.f_rice[0]+50, Cord.f_rice[1]))
    left_click()
    time.sleep(.1)


def make_food(food):
    food_on_hand['rice'] -= 1
    food_on_hand['nori'] -= 1
    mouse_pos(Cord.f_rice)
    time.sleep(.1)
    left_click()

    mouse_pos(Cord.f_nori)
    time.sleep(.1)
    left_click()

    if food == 'caliroll':
        food_on_hand['roe'] -= 1
        mouse_pos(Cord.f_roe)
        time.sleep(.1)
        left_click()
    elif food == 'onigiri':
        food_on_hand['rice'] -= 1
        mouse_pos(Cord.f_rice)
        time.sleep(.1)
        left_click()
    elif food == 'gunkan':
        food_on_hand['roe'] -= 2
        mouse_pos(Cord.f_roe)
        time.sleep(.1)
        left_click()
        pyautogui.click()

    time.sleep(.1)
    fold_mat()
    time.sleep(1.5)


def buy_food(food):
    mouse_pos(Cord.telephone)
    time.sleep(.1)
    left_click()
    if food == 'rice':
        mouse_pos(Cord.menu_rice)
        time.sleep(.1)
        left_click()
        image = screen_grab()
        if image.getpixel(Cord.buy_rice) != Cord.bad_rice:
            mouse_pos(Cord.buy_rice)
            time.sleep(.1)
            left_click()
            mouse_pos(Cord.delivery_norm)
            time.sleep(.1)
            left_click()
            time.sleep(2.5)
            food_on_hand['rice'] += 10
        else:
            mouse_pos(Cord.t_exit)
            time.sleep(.1)
            left_click()
            time.sleep(1)
            buy_food(food)
    else:
        mouse_pos(Cord.toppings)
        time.sleep(.1)
        left_click()
        image = screen_grab()
        if food == 'shrimp':
            if image.getpixel(Cord.t_shrimp) != Cord.bad_shrimp:
                mouse_pos(Cord.t_shrimp)
                time.sleep(.1)
                left_click()
                mouse_pos(Cord.delivery_norm)
                time.sleep(.1)
                left_click()
                time.sleep(2.5)
                food_on_hand['shrimp'] += 10
            else:
                mouse_pos(Cord.t_exit)
                left_click()
                time.sleep(.1)
                buy_food(food)
        elif food == 'nori':
            if image.getpixel(Cord.t_nori) != Cord.bad_nori:
                mouse_pos(Cord.t_nori)
                time.sleep(.1)
                left_click()
                mouse_pos(Cord.delivery_norm)
                time.sleep(.1)
                left_click()
                time.sleep(2.5)
                food_on_hand['nori'] += 10
            else:
                mouse_pos(Cord.t_exit)
                left_click()
                time.sleep(.1)
                buy_food(food)
        elif food == 'roe':
            if image.getpixel(Cord.t_roe) != Cord.bad_roe:
                mouse_pos(Cord.t_roe)
                time.sleep(.1)
                left_click()
                mouse_pos(Cord.delivery_norm)
                time.sleep(.1)
                left_click()
                time.sleep(2.5)
                food_on_hand['roe'] += 10
            else:
                mouse_pos(Cord.t_exit)
                left_click()
                time.sleep(.1)
                buy_food(food)
        elif food == 'salmon':
            if image.getpixel(Cord.t_salmon) != Cord.bad_salmon:
                mouse_pos(Cord.t_salmon)
                time.sleep(.1)
                left_click()
                mouse_pos(Cord.delivery_norm)
                time.sleep(.1)
                left_click()
                time.sleep(2.5)
                food_on_hand['salmon'] += 10
            else:
                mouse_pos(Cord.t_exit)
                left_click()
                time.sleep(.1)
                buy_food(food)
        elif food == 'unagi':
            if image.getpixel(Cord.t_unagi) != Cord.bad_unagi:
                mouse_pos(Cord.t_unagi)
                time.sleep(.1)
                left_click()
                mouse_pos(Cord.delivery_norm)
                time.sleep(.1)
                left_click()
                time.sleep(2.5)
                food_on_hand['unagi'] += 10
            else:
                mouse_pos(Cord.t_exit)
                left_click()
                time.sleep(.1)
                buy_food(food)


def check_food():
    for item, left in food_on_hand.items():
        if left <= 4:
            print '%s is low and needs to be replenished' % item
            buy_food(item)


def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    return pixel_array


def get_seat_one():
    box = (26 + x_pad, 63 + y_pad, 87 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_seat_two():
    box = (127 + x_pad, 63 + y_pad, 188 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_seat_three():
    box = (228 + x_pad, 63 + y_pad, 289 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_seat_four():
    box = (329 + x_pad, 63 + y_pad, 390 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_seat_five():
    box = (430 + x_pad, 63 + y_pad, 491 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_seat_six():
    box = (531 + x_pad, 63 + y_pad, 592 + x_pad, 75 + y_pad)
    image = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(box))
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    print pixel_array
    # image.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return pixel_array


def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


def check_bubs():
    clear_tables()
    check_food()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes[s1]
            make_food(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1

    else:
        print 'Table 1 unoccupied'

    clear_tables()
    check_food()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes[s2]
            make_food(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2

    else:
        print 'Table 2 unoccupied'

    check_food()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes[s3]
            make_food(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3

    else:
        print 'Table 3 unoccupied'

    check_food()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes[s4]
            make_food(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4

    else:
        print 'Table 4 unoccupied'

    clear_tables()
    check_food()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes[s5]
            make_food(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5

    else:
        print 'Table 5 unoccupied'

    check_food()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 1 is occupied and needs %s' % sushiTypes[s6]
            make_food(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6

    else:
        print 'Table 6 unoccupied'
    clear_tables()


def main():
    time.sleep(10)
    start_game()
    time.sleep(5)
    while True:
        check_bubs()


if __name__ == '__main__':
    pass


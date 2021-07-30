# предварительно установив pygame
import pygame 
import sys 
# мой модуль с функциями
from fmodul import * 

pygame.init() 

list_object = []
# временно тут. Создаем 0-ю запись в списке обьектов и вкладываем туда настройки (настройки описаны в readme.py)
list_object.append([-1, 640, 480, 20, 20, 0, 0, 3, 1, 1, "calibri", (0, 51, 51), (0, 90, 90),(0, 90, 90),
                    (120, 120, 120), (120, 120, 120), (235, 235, 235), (235, 235, 235), (0, 0, 0), (0, 0, 0),
                    (0, 0, 0), (0, 0, 0), (190, 190, 190)]) 

""" Видимое поле состоит из невидимых (виртуальных) квадратиков или прямоугольников (сетки). Подобно листу в клетку.
    Видимые элементы строятся вписываясь в квадратики.
    От величины квадратиков зависит масштаб изображения в окне программы """
# ширина и высота виртуального квадратика (сетки) или подгружаем из файла
x_hidden_grid = list_object[0][3]
y_hidden_grid = list_object[0][4]

""" Количество квадратиков по х и у определяет размер рабочего поля. Меняется динамически.
    Точка отсчета верхний левый угол (координата 0,0).
    Размер всего поля это массив. Список строк (у) в каждой из которых список столбцов (элементов строк, х) """
# кол-во столбцов column_array (координата х) и строк line_array (координата у) 
column_array = list_object[0][5]
line_array = list_object[0][6] 

""" массив для виртуальных квадратиков (создаем и заполняем 0-ми)
    0 - пустое поле
    1 - тень иконки
    2 - тень соединительной линии 
    3 - тень рамки отдельной схемы """
array = [[0]*column_array for i in range(line_array)] 

"""название системного шрифта """
FONT_DISPLAY_MAIN = list_object[0][10]

""" размерность по умолчанию в квадратиках по х,у иконки """
x_icon_default = list_object[0][7]
y_icon_default = list_object[0][8]
""" вылет соединительной линии от иконки вниз или вправо """
len_line_default = list_object[0][9] 

# размеры создаваемого окна 
x_screen = list_object[0][1]
y_screen = list_object[0][2]
# надпись в шапке
pygame.display.set_caption("Редактор блок-схем ДРАКОН") 

# создать окно изменяемого размера
screen = pygame.display.set_mode((x_screen, y_screen), pygame.RESIZABLE) 

# для задержки в цикле while()
clock = pygame.time.Clock() 

""" Cмещение области видимости массива квадратиков относительно видимой части в окне программы 
    (0,0 нет смещения, левый верхний угол)
    Значение может быть отрицательной величиной. Положительное смещение блокируется.
    Используеться для отрисовки только видимой в данный момент части массива квадратиков
    чтобы не бегать лишний раз по "невидимым" на экране элементам массива """
slip_x = 0 
slip_y = 0 

# цвета
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FON = list_object[0][11]
FON_SCHEMS_0 = list_object[0][12]
FON_SCHEMS_1 = list_object[0][13]
RAMKA_0 = list_object[0][14]
RAMKA_1 = list_object[0][15]
FON_ICONS_0 = list_object[0][16]
FON_ICONS_1 = list_object[0][17]
RAMKA_ICONS_0 = list_object[0][18]
RAMKA_ICONS_1 = list_object[0][19]
LINE_ICO_0 = list_object[0][20]
LINE_ICO_1 = list_object[0][21]
VALENT_POINT = list_object[0][22]

GREY = (170, 170, 170)
""" ========================================================================= """

cycle = True
while cycle:
    # получить размеры рабочей области окна 
    x_screen, y_screen = pygame.display.get_surface().get_size() 
    # обновить координаты мыши относительно предыдущего считанного значения (смещение)
    x_presset, y_presset = pygame.mouse.get_rel()

    # обновить текущее значение кол-во столбцов и строк массива array, т. к. его могут менять другие функции
    column_array = list_object[0][5]
    line_array = list_object[0][6] 

    # пробежаться по очереди событий
    for event in pygame.event.get(): 
        # Выход по крестику или Alt+F4 (выход из цикла while)
        if event.type == pygame.QUIT: cycle = False 

        # событие нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # получить координаты клика
            x_mouse, y_mouse = pygame.mouse.get_pos() 
            # вычисляем координаты ячейки в массиве с учетом смещения
            focus_column_array = (x_mouse - slip_x) // x_hidden_grid 
            focus_line_array = (y_mouse - slip_y) // y_hidden_grid 
            # Защита от клика вне квадратика (сетки)
            if (focus_column_array in range(column_array)) and (focus_line_array in range(line_array)):
                # левая кнопка мыши 
                if event.button == 1:
                    pass
                    # array[focus_line_array][focus_column_array] = 1 
                # правая кнопка мыши 
                if event.button == 3:
                    pass
                    # array[focus_line_array][focus_column_array] = 0 
            # колесико ВВЕРХ увеличить сетку
            if event.button == 4:
                x_hidden_grid += 1
                y_hidden_grid += 1
                list_object[0][3] = x_hidden_grid
                list_object[0][4] = y_hidden_grid

            # колесико ВНИЗ уменьшить сетку
            if event.button == 5:
                x_hidden_grid -= 1
                y_hidden_grid -= 1
                # минимальный порог
                if x_hidden_grid < 20: x_hidden_grid = 20
                if y_hidden_grid < 20: y_hidden_grid = 20
                list_object[0][3] = x_hidden_grid
                list_object[0][4] = y_hidden_grid
            
        # событие движения мыши
        if event.type == pygame.MOUSEMOTION:
            # если нажато колесико мыши  
            if event.buttons[1]:
                # получить координаты мыши относительно предыдущего считанного значения
                x_presset, y_presset = pygame.mouse.get_rel() 
                # корректируем смещение
                slip_x += x_presset
                slip_y += y_presset
                """ отключаем положительное смещение. Ячейки [0][0] массива квадратиков при перетягивании вправо или вниз 
                не выходит далее координаты 0,0 поля окна """
                if slip_x > 0: slip_x = 0
                if slip_y > 0: slip_y = 0
                """ отключаем излишнее отрицательное смещение. Ячейки [max][max] массива квадратиков 
                не выходит далее координаты max,max поля окна """
                if  column_array*x_hidden_grid <= x_screen: max_slip_x = 0
                else: max_slip_x = 0 - (column_array*x_hidden_grid - x_screen)
                if line_array*y_hidden_grid <= y_screen: max_slip_y = 0
                else: max_slip_y = 0 - (line_array*y_hidden_grid - y_screen)
                if slip_x < max_slip_x: slip_x = max_slip_x
                if slip_y < max_slip_y: slip_y = max_slip_y

                

        """ нажатие клавиш на клавиатуре """
        if event.type == pygame.KEYDOWN: 
            # нет защиты от отрицательных значений массива
            # клавиша ВВЕРХ удалить последнюю строку массива
            if event.key == pygame.K_UP: 
                del array[-1]
                line_array -= 1
                list_object[0][5] = column_array
                list_object[0][6] = line_array
            # клавиша ВНИЗ добавить в конец массива строку 
            elif event.key == pygame.K_DOWN: 
                array.append([0]*column_array)
                line_array += 1
                list_object[0][5] = column_array
                list_object[0][6] = line_array
            # пробежимся по линиям (строкам) и удалить в каждой последний элемент ( - последний столбец)
            elif event.key == pygame.K_LEFT:
                for y in range(line_array): 
                    array[y].pop()  
                column_array -= 1
                list_object[0][5] = column_array
                list_object[0][6] = line_array
            # пробежимся по линиям (строкам) и добавить в конец каждой элемент ( + последний столбец)
            elif event.key == pygame.K_RIGHT:
                for y in range(line_array): 
                    array[y].append(0) 
                column_array += 1
                list_object[0][5] = column_array
                list_object[0][6] = line_array
            # клавиша 0 распечатать в терминале информацию
            elif event.key == pygame.K_0:
                add_primitive_scheme(array, list_object)
            # косая черта (/) смещение массива квадратиков в точку 0,0 (обнулить смещение)
            elif event.key == pygame.K_KP_DIVIDE: 
                slip_x = 0  
                slip_y = 0  


    # заливка фона
    screen.fill(FON) 

    

    
    
    # получить диапазон отрисовки видимой части массива сетки
    # передадим текущий размер окна х,у смещение по х,у и список объектов 
    home_x_array, end_x_array, home_y_array, end_y_array = range_drawing_screen(x_screen, y_screen, slip_x, slip_y, list_object)

    """
            ИЗМЕНИТЬ!
            Сначала надо отрисовать схемы отдельно.
            Потом выделить иконы и линии и нарисовать их позже, чтобы не было перекрытия иконы фоном схемы

            После измененния вылезла другая проблема в начале отображения иконки


    """
    list_ID_for_drawing = []

    # пробежаться по диапазону и собрать все видимые ID (кроме 0)
    """
    # способ доступа к диапазону с помощью сегмента :
    for line_list_array in array[home_y_array:end_y_array]:
        for cell in line_list_array[home_x_array:end_x_array]:
            if cell != 0:
                list_ID_for_drawing.append(cell)
    """
    
    # способ доступа к диапазону класический
    for line in range(home_y_array, end_y_array):
        for col in range(home_x_array, end_x_array):
            if array[line][col] != 0:
                list_ID_for_drawing.append(array[line][col])

    
    # убрать повторения
    list_ID_for_drawing = list(set(list_ID_for_drawing))


    # создать новый список только со схемами, а в старом оставить все остальные объекты
    list_ID_for_drawing_schems = []

    # переносим ID схем в новый список
    for element_ID in list_ID_for_drawing:
        if list_object[element_ID][0] == 1:
            list_ID_for_drawing_schems.append(element_ID)
    # со старого списка удаляем перенесенные значения
    for element_ID_scheme in list_ID_for_drawing_schems:
        list_ID_for_drawing.remove(element_ID_scheme)

    # прорисовать только схемы
    for schems in list_ID_for_drawing_schems:
        x_0 = list_object[schems][3] * x_hidden_grid + slip_x
        y_0 = list_object[schems][4] * y_hidden_grid + slip_y
        x_n = list_object[schems][5] * x_hidden_grid 
        y_n = list_object[schems][6] * y_hidden_grid 
        FON_SCHEMS_0 = list_object[0][12]
        FON_SCHEMS_1 = list_object[0][13] 
        RAMKA_0 = list_object[0][14]
        RAMKA_1 = list_object[0][15]
        x_0 += x_hidden_grid // 2
        y_0 += y_hidden_grid // 2
        x_n -= x_hidden_grid 
        y_n -= y_hidden_grid
        pygame.draw.rect(screen, FON_SCHEMS_0, (x_0, y_0, x_n, y_n), 0)
        # рамку внутрь на 1 px 
        pygame.draw.rect(screen, RAMKA_0, (x_0, y_0, x_n, y_n), 1) 
    
    # пробежатся по списку и отрисовать объекты в поле зрения
    for id_obj in list_ID_for_drawing:
        type_obj = list_object[id_obj][0]
        
        # иконка
        if type_obj == 2:
            x_0 = list_object[id_obj][3] * x_hidden_grid + slip_x
            y_0 = list_object[id_obj][4] * y_hidden_grid + slip_y
            x_n = list_object[id_obj][5] * x_hidden_grid 
            y_n = list_object[id_obj][6] * y_hidden_grid 
            FON_ICONS_0 = list_object[0][16]
            FON_ICONS_1 = list_object[0][17]
            RAMKA_ICONS_0 = list_object[0][18]
            RAMKA_ICONS_1 = list_object[0][19]
            pygame.draw.rect(screen, FON_ICONS_0, (x_0, y_0, x_n, y_n), 0)
            # рамку внутрь на 1 px 
            pygame.draw.rect(screen, RAMKA_ICONS_0, (x_0, y_0, x_n, y_n), 1) 
            font_default = pygame.font.SysFont(FONT_DISPLAY_MAIN, x_hidden_grid - 2)
            text = str(list_object[id_obj][13])
            tx = font_default.render(text, True, BLACK)
            screen.blit(tx, (x_0+1, y_0+1))

        # линия
        if type_obj == 3:
            x_0 = list_object[id_obj][3] * x_hidden_grid + slip_x
            x_0 += x_hidden_grid // 2
            y_0 = list_object[id_obj][4] * y_hidden_grid + slip_y
            x_n = x_0
            y_n = y_0 + list_object[id_obj][6] * y_hidden_grid 
            LINE_ICO_0 = list_object[0][20]
            LINE_ICO_1 = list_object[0][21]
            pygame.draw.line(screen, LINE_ICO_0, [x_0, y_0], [x_n, y_n], 2)  
    

    """ для отладки (прорисовка ID)
    font_default = pygame.font.SysFont(FONT_DISPLAY_MAIN, 12)
    
    for line in range(home_y_array, end_y_array):
        for col in range(home_x_array, end_x_array):

            x = col*x_hidden_grid + slip_x
            y = line*y_hidden_grid + slip_y

            text = str(array[line][col])
            color_fon = (0, 0, 0)
            id_obj = array[line][col]
            type_obj = list_object[id_obj][0]
            if type_obj == 2 or type_obj == 3:
                color_fon = list_object[id_obj][15]
            else:
                color_fon = FON_SCHEMS_0

            tx = font_default.render(text, True, RED)

            screen.blit(tx, (x, y))
    """

    pygame.display.update( )
    # задержка выраженная в кадр/с 

    clock.tick(25) #FPS

f = open('text_save.txt', 'w')
for index in list_object:
    index = str(index)
    f.write(index + '\n')
f.close()

pygame.quit()
sys.exit(0)


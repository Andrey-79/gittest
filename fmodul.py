""" Модуль fmodul.py содержит функции 
    имена аргументов функций желательно иметь уникальными для легкой замены в пределах функции по Ctrl + H """

def get_number_scheme(x_array_f0: int, y_array_f0: int, list_ob: list) -> int:
    """ Получает координаты x,y в массиве квадратиков и ссылку на список с диапазонами полей
        Возвращает номер схемы на которую ссылается х,у (порядковый номер элемента списка)
        Если совпадений нет то возвращает -1 
        х и у должны иметь тип int, список состоять из координат: [х, у, ширина, высота] (как у класса Rect)
    """
    # enumerate возвращает кортеж (0, [0, 0, 7, 7]) где первое это номер итерации, а второе элемент списка
    for r in enumerate(list_ob):
        # если объект это схема, то
        if r[1][0] == 1:
            # вычисляем диапазоны
            x_range_home = r[1][3]
            x_range_end = r[1][3] + r[1][5]
            y_range_home = r[1][4]
            y_range_end = r[1][4] + r[1][6]
            # входит ли х и у в какой-либо из диапазонов из списка?
            if x_array_f0 in range(x_range_home, x_range_end) and y_array_f0 in range(y_range_home, y_range_end):
                return r[0]
    return -1


def add_primitive_scheme(array_f1: list, list_object_f1: list) ->None:
    """ формирование схемы типа 'Примитив' """
    # размер по умолчанию в квадратиках по х,у иконки 
    x_icon_default = list_object_f1[0][7]
    y_icon_default = list_object_f1[0][8]
    # вылет соединительной линии от иконки вниз или вправо 
    len_line_default = list_object_f1[0][9]
    # цвета
    FONT_DISPLAY_MAIN = list_object_f1[0][10]
    FON_SCHEMS_0 = list_object_f1[0][12]
    FON_SCHEMS_1 = list_object_f1[0][13] 
    RAMKA_0 = list_object_f1[0][14]
    RAMKA_1 = list_object_f1[0][15]
    FON_ICONS_0 = list_object_f1[0][16]
    FON_ICONS_1 = list_object_f1[0][17]
    RAMKA_ICONS_0 = list_object_f1[0][18]
    RAMKA_ICONS_1 = list_object_f1[0][19]
    LINE_ICO_0 = list_object_f1[0][20]
    LINE_ICO_1 = list_object_f1[0][21]
    VALENT_POINT = list_object_f1[0][22]
    # получить из объекта настроек кол-во столбцов (координата х) и строк (координата у) 
    col_array_f1ay = list_object_f1[0][5]
    lin_array_f1ay = list_object_f1[0][6] 

    # каков размер поля необходим чтобы вместить схему, учитывая отступ и рамку?
    x_field = x_icon_default + 4
    y_field = y_icon_default + len_line_default + y_icon_default + 4
    
    """ добавим объект 'схема' """
    list_object_f1.append([1, 0, 0, col_array_f1ay, 0, x_field, y_field, FON_SCHEMS_0, FON_SCHEMS_1, RAMKA_0, RAMKA_1,FONT_DISPLAY_MAIN])

    # узнаем ID обьекта 'схема'
    id_scheme = len(list_object_f1) - 1

    """ Теперь реально добавляем ячеек в массив """
    # добавим строк в массив array_f1[] в случае необходимости
    while(lin_array_f1ay < y_field):
        array_f1.append([0]*col_array_f1ay)
        lin_array_f1ay += 1
    # добавим столбцов 
    for x in range(x_field):
        for y in range(lin_array_f1ay): 
            array_f1[y].append(0) 
        col_array_f1ay += 1

    # сохранить в объекте настроек кол-во столбцов (координата х) и строк (координата у) 
    list_object_f1[0][5] = col_array_f1ay
    list_object_f1[0][6] = lin_array_f1ay

    
    """ определяем диапазоны прохода для созданной выше схемы (адресация: последний объект [-1]) """
    x_diap_home = list_object_f1[-1][3]
    x_diap_end = list_object_f1[-1][3] + list_object_f1[-1][5]
    y_diap_home = list_object_f1[-1][4]
    y_diap_end = list_object_f1[-1][4] + list_object_f1[-1][6]

    """ прорисовка рамки схемы в массив array_f1ay. Вносим на место визуальных рамок ID объекта схемы  """
    for y in range(y_diap_home, y_diap_end):
        for x in range(x_diap_home, x_diap_end):
            if x == x_diap_home or x == x_diap_end-1 or y == y_diap_home or y == y_diap_end-1:
                array_f1[y][x] = id_scheme 

    # переопределяем диаппазон прохода (отбрасываем рамки и один отступ пустого поля)
    x_diap_home = list_object_f1[-1][3] + 2
    x_diap_end = list_object_f1[-1][3] + list_object_f1[-1][5] - 2
    y_diap_home = list_object_f1[-1][4] + 2
    y_diap_end = list_object_f1[-1][4] + list_object_f1[-1][6] - 2

    # добавим обьект 'иконка'
    list_object_f1.append([2, id_scheme, 0, x_diap_home, y_diap_home, x_icon_default, y_icon_default, 0, 0, 0, 0, 0, 0, 'Начало', '', 
                        FON_ICONS_0, FON_ICONS_1, RAMKA_ICONS_0, RAMKA_ICONS_1])

    # прорисовка добавленного обьекта в array_f1[]
    for y in range(list_object_f1[-1][4], list_object_f1[-1][4] + list_object_f1[-1][6]):
        for x in range(list_object_f1[-1][3], list_object_f1[-1][3] + list_object_f1[-1][5]):
            array_f1[y][x] = id_scheme + 1

    # добавим обьект 'линия'
    temp_x = (x_diap_home + (x_diap_end - x_diap_home) // 2)
    y_diap_home += y_icon_default
    list_object_f1.append([3, id_scheme, 0, temp_x, y_diap_home, 1, len_line_default, temp_x, y_diap_home, 0, 0, id_scheme + 1, id_scheme + 3, 0, 0, 
                        LINE_ICO_0, LINE_ICO_1, VALENT_POINT])

    # прорисовка добавленного обьекта
    for y in range(list_object_f1[-1][4], list_object_f1[-1][4] + list_object_f1[-1][6]):
        for x in range(list_object_f1[-1][3], list_object_f1[-1][3] + list_object_f1[-1][5]):
            array_f1[y][x] = id_scheme + 2

    # добавим обьект 'иконка'
    y_diap_home += len_line_default
    list_object_f1.append([2, id_scheme, 0, x_diap_home, y_diap_home, x_icon_default, y_icon_default, 0, 0, 0, 0, 0, 0, 'Конец', '', 
                        FON_ICONS_0, FON_ICONS_1, RAMKA_ICONS_0, RAMKA_ICONS_1])

    # прорисовка добавленного обьекта array_f1[]
    for y in range(list_object_f1[-1][4], list_object_f1[-1][4] + list_object_f1[-1][6]):
        for x in range(list_object_f1[-1][3], list_object_f1[-1][3] + list_object_f1[-1][5]):
            array_f1[y][x] = id_scheme + 3

""" ____________________________________________________________________________________________ """
def range_drawing_screen(x_screen: int, y_screen: int, slip_x: int, slip_y: int, list_object: list) ->list:
    """ БЛОК вычисления диаппазона прорисовки видимой части схемы 
        Возвращает в формате [x_home, x_end, y_home, y_end] """
    # ширина и высота виртуального квадратика (сетки)
    x_hidden_grid = list_object[0][3]
    y_hidden_grid = list_object[0][4]
    # кол-во столбцов column_array_f1ay (координата х) и строк line_array_f1ay (координата у) 
    column_array = list_object[0][5]
    line_array = list_object[0][6] 

    """ определяем диапазон элементов массива видимые в области окна
        по умолчанию от 0-го до элемента который влазит в окно или до максимального """
    home_x_array = 0
    end_x_array = x_screen // x_hidden_grid + 1
    if end_x_array > column_array: end_x_array = column_array
    home_y_array = 0
    end_y_array = y_screen // y_hidden_grid + 1
    if end_y_array > line_array: end_y_array = line_array
    

    """ вычисляем диапазон (для строк и столбцов) для прорисовки видимой в окне части массива 
        если присутствует отрицательное смещение """
    if slip_x < 0: 
        home_x_array = abs(slip_x // x_hidden_grid) - 1
        if home_x_array > column_array: home_x_array = column_array
        end_x_array = home_x_array + (x_screen // x_hidden_grid) + 2
        if end_x_array > column_array: end_x_array = column_array
    if slip_y < 0:
        home_y_array = abs(slip_y // y_hidden_grid) - 1
        if home_y_array > line_array: home_y_array = line_array
        end_y_array = home_y_array + (y_screen // y_hidden_grid) + 2 
        if end_y_array > line_array: end_y_array = line_array
    return [home_x_array, end_x_array, home_y_array, end_y_array]

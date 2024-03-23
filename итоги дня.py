def statistika_za_den():
    son = int(input('Введи баллы за сон>>'))
    print('Подсчет стресса.')
    list3 = []
    summa = 0
    schet = 0
    list1_for_sred = input('Введи список >>')
    list2_for_sred = list1_for_sred.split(' ')
    for i in list2_for_sred:
        i = int(i)
        list3.append(i)
    for i in list3:
        summa += i
        schet += 1
    sred = summa / schet
    print('среднее арифметическое списка = ', round(sred))
    shagi = int(input('Введи шаги за день >>'))
    act1 = int(input('Введи активность в минутах>>'))
    act2 = int(input('Введи активность в часах>>'))

    print('результаты таковы:')
    print(son, ' ', round(sred), ' ', shagi)
    print(act1, ' ', act2)
    stata = [son, round(sred), shagi, act1, act2]
    return stata


def dnevnik():
    print('ДНЕВНИК')

    data_dnevnik = input('Введи дату. Например: 12.10.08' + '\n' + '>>')
    print('\n', 'Часть 1. Напиши все то, что ты делал сегодня подробно. Прибавь к этому описание переживаний и чувств. Можно делать абзацы. Закончить - перейди на новый абзац и введи в конце "0".')
    chast1_final = ''
    chast_final = ''
    chast1 = ''
    while True:
        chast1 = input('>> ')
        if not '0' in chast1:
            chast1_final += chast1 + ' '
        else:
            break
    len1 = len(chast1_final)
    a = 0
    b = 70
    while len1 >= 70:
        chast_final += chast1_final[a:b:1] + '-' + '\n'
        len1 -= 70
        a += 70
        b += 70
    else:
        chast_final += chast1_final[a:b:1]
    chast1_vivod = ''
    chast1_final_vivod = ''
    print('\n', 'Какие выводы у тебя созрели?')
    while True:
        chast1_vivod = input('>> ')
        if not '0' in chast1_vivod:
            chast1_final_vivod += chast1_vivod + '\n'
        else:
            break
    chast_final += '\n' + chast1_final_vivod
    print(chast_final)
    print('Напиши, какие твои поступки заслуживают осуждения?')
    chast4 = input('>> ')
    print('\n', 'Напиши, каким твоим поступкам следует радоваться?')
    chast5 = input('>> ')
    print(''' 
    В дневник будет занесено следующее >''')
    all_day = [data_dnevnik, chast_final]
    return all_day


def PKZSH():
    print(' ПКЖ. Список пунктов')
    print(' ПУНКТ 1. Привычки. За каждую задачу 1 или -1. За первую - 0')
    b1_1 = int(input(' пить 6+ стаканов воды (1,5 л) »'))
    b1_2 = int(input(' утренняя зарядка »'))
    b1_3 = int(input(' чистка зубов утром и вечером, поласкание рта после еды »'))
    b1_4 = int(input(' наличие физической нагрузки »'))
    b1 = b1_1 + b1_2 + b1_3 + b1_4
    print(' баллов за пункт 1 - ', b1)
    print(" ")
    print(' ПУНКТ 2. Выполнение обязательных заданий. За каждое 2 или от -2 до -4')
    b2 = int(input(' введи баллы »'))
    print(' ')
    print(' ПУНКТ 3. Выполнение других заданий. За каждую 2 или от 0 до -2')
    b3 = int(input(' введи баллы »'))
    print(' ')
    print(' ПУНКТ 4. Количество развлечений. За каждые 10 мин сверх лимита -1 б')
    b4 = int(input(' введи баллы »'))
    print(' ')
    print(' ПУНКТ 5. Творчество. За каждый вид от +1 до +5 баллов')
    b5_1 = int(input(' Рисование '))
    b5_2 = int(input(' Поделки '))
    b5_3 = int(input(' Музыка '))
    b5_4 = int(input(' Стихи '))
    b5 = b5_1 + b5_2 + b5_3 + b5_4
    print(' ')
    print(' ПУНКТ 6. Спокойствие. ')
    b6: int = 0
    b6_1 = int(input(' введи уровень стресса »'))
    if b6_1 < 50:
        b6 = 2
    elif 50 <= b6_1 < 55:
        b6 = 1
    elif b6_1 >= 55:
        b6 = 0
    print(' сегодня у тебя', b6, 'баллов')
    print(' ')
    print(' ПУНКТ 7. Развитие спокойствия. от -1 до 2 ')
    b7_1 = int(input('- Медитация»'))
    b7_2 = int(input('- Практика дыхания»'))
    b7_3 = int(input('- Расслабление тела»'))
    b7_4 = int(
        input('- Сохраненение спокойствия вопреки обстоятельствам»'))
    b7 = b7_1 + b7_2 + b7_3 + b7_4
    print(' За развитие спокойствия сегодня', b7, 'баллов')
    print(' ')
    print(' ПУНКТ 8. Развитие внимательности. от -1 до 2')
    b8_1 = int(input('- Медитация »'))
    b8_2 = int(input('- Фокусировка на одной настоящей задаче»'))
    b8_3 = int(input('- Фокусировка и запоминание обстановки вокруг, своих тактильных, вкусовых ощущений, эмоций »'))
    b8 = b8_1 + b8_2 + b8_3
    print(' ')
    print(' ПУНКТ 9. Работа с умом')
    print('Подпункт 1. Знание. От -1 до 2')
    b9_1_1 = int(input('- Чтение »'))
    b9_1_2 = int(input('- Фильмы и ролики »'))
    b9_1_3 = int(input('- Общение с людьми »'))
    b9_1 = b9_1_1 + b9_1_2 + b9_1_3
    print(' За развитие знания сегодня', b9_1, 'баллов')
    print(' ')
    print(' Подпункт 2. Эмоциональный интеллект. От -1 до 2')
    b9_2_1 = int(input('- Дневник эмоций »'))
    b9_2_2 = int(input('- Самосознание »'))
    b9_2_3 = int(input('- Эмпатия к людям »'))
    b9_2_4 = int(input('- Развитие коммуникативных навыков »'))
    b9_2 = b9_2_1 + b9_2_2 + b9_2_3 + b9_2_4
    print(' За развитие EQ сегодня', b9_2, 'баллов')
    print(' ')
    print('Подпункт 3. Логический интеллект. От -1 до 2')
    b9_3_1 = int(input('- Использовать метод Пифагора. Развивать память »'))
    b9_3_2 = int(input('- Решать логические задачи и головоломки »'))
    b9_3_3 = int(input('- Считать числовые последовательности »'))
    b9_3_4 = int(input('- Учить стихи »'))
    b9_3 = b9_3_1 + b9_3_2 + b9_3_3 + b9_3_4
    print(' За развитие IQ сегодня', b9_3, 'баллов')
    b9 = b9_1 + b9_2 + b9_3
    print(' ')
    print(' ПУНКТ 10. Развитие стойкости.От -1 до 2 ')
    b10_1 = int(input('- Поиск и борьба с неправильной гордостью »'))
    b10_2 = int(input('- Делать то, что правильно, но не хочется »'))
    b10_3 = int(input('- В любой ситуации оставаться спокойным »'))
    b10_4 = int(input('- Защищать свое мнение »'))
    b10_5 = int(input('- Выдерживать тяжесть бытия»'))
    b10 = b10_1 + b10_2 + b10_3 + b10_4 + b10_5
    print(' За развитие стойкости сегодня', b10, 'баллов')
    print(' ')
    print(' ПУНКТ 11. Развитие юмора. За каждый пункт 0 или 1')
    b11_1 = int(input('смеяться по-доброму над собрй и другими людьми»'))
    b11_2 = int(input('смотреть на мир несерьезно, искать смешные вещи везде»'))
    b11 = b11_1 + b11_2
    print(' ')
    print('ПУНКТ 12. СЗЧ')
    b12 = float(input("""Соблюдение пунктов из not-to-do листа>>"""))
    B = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12
    print('ПОЗДРАВЛЯЮ! ТЫ ЗАКОНЧИЛ ЕЩЕ ОДИН ДЕНЬ! ТВОИ БАЛЛЫ ЗА СЕГОДНЯ', B)

    print('ПРОВЕРКА УРОВНЯ')
    print(" ")
    point_to_reach = 200
    point_now = int(input('введи кол-во очков на данный момент '))
    point_now = point_now + B
    point = point_to_reach - point_now
    ochki = [B, point_now]
    if point <= 0:
        print('Поздравляю! Ты прошел новый этап! В награду ты можешь потратить деньги только на себя и на что угодно.')
    else:
        print('сейчас у тебя', point_now, 'очков. Нужно еще', point, 'очков')
    return ochki


def vse_itogi():
    send1 = statistika_za_den()
    s1_1, s1_2, s1_3, s1_4, s1_5 = send1
    send2 = dnevnik()
    s2_1, s2_2 = send2
    send_3 = PKZSH()
    send_3_1, send_3_2 = send_3
    send3 = 'Получил баллов:' + str(send_3_1) + '. Прогресс: ' + str(send_3_2) + '/' + str(200)
    all_to_send = str(s2_1) + '\n' + str(s1_1) + ' ' + str(s1_2) + ' ' + str(s1_3) + '\n' + str(s1_4) + ' ' + str(s1_5) + '\n' + s2_2 + '\n' + send3 + '\n' + '\n'
    dnev = open('Дневниковые записи.txt', 'a')
    dnev.write(all_to_send)
    dnev.close()
    all_stat_to_send = str(s2_1) + '\n' + str(s1_1) + ' ' + str(s1_2) + ' ' + str(s1_3) + '\n' + str(s1_4) + ' ' + str(s1_5) + '\n' + send3 + '\n' + '\n'
    all_son = str(s1_1)
    all_stress = str(s1_2)
    all_shagi = str(s1_3)
    all_act1 = str(s1_4)
    all_act2 = str(s1_5)
    with open('файлы с данными/статистика/статистика дней.txt', 'a') as stata:
        stata.write(all_stat_to_send + '\n')
    with open('файлы с данными/статистика/статистика сна.txt', 'a') as stata_son:
        stata_son.write(all_son)
    with open('файлы с данными/статистика/статистика стресса.txt', 'a') as stata_stress:
        stata_stress.write(all_stress)
    with open('файлы с данными/статистика/статистика шагов.txt', 'a') as stata_shagi:
        stata_shagi.write(all_shagi)
    with open('файлы с данными/статистика/статистика актив1.txt', 'a') as stata_act1:
        stata_act1.write(all_act1)
    with open('файлы с данными/статистика/статистика актив2.txt', 'a') as stata_act2:
        stata_act2.write(all_act2)

    all_pkschz = str(s2_1) + '\n' + send3
    with open('файлы с данными/статистика/статистика пкж.txt', 'a') as stata_pkschz:
        stata_pkschz.write(all_pkschz)


vop1 = int(input('''Подведение итогов дня. Выбери часть цифрой:
1. Статистика;
2. Дневник;
3. ПКЖ;
4. Статистика, дневник, ПКЖ
>> '''))
if vop1 == 1:
    vopros = str(input('Нужно вводить в документы? да/нет'))
    if vopros == 'да':
        send1 = statistika_za_den()
        s1_1, s1_2, s1_3, s1_4, s1_5 = send1
        s2_1 = str(input('Введи сегодняшнюю дату'))
        all_son = str(s1_1)
        all_stress = str(s1_2)
        all_shagi = str(s1_3)
        all_act1 = str(s1_4)
        all_act2 = str(s1_5)
        with open('файлы с данными/статистика/статистика сна.txt', 'a') as stata_son:
            stata_son.write(all_son + ',' + ' ')
        with open('файлы с данными/статистика/статистика стресса.txt', 'a') as stata_stress:
            stata_stress.write(all_stress + ',' + ' ')
        with open('файлы с данными/статистика/статистика шагов.txt', 'a') as stata_shagi:
            stata_shagi.write(all_shagi + ',' + ' ')
        with open('файлы с данными/статистика/статистика актив1.txt', 'a') as stata_act1:
            stata_act1.write(all_act1 + ',' + ' ')
        with open('файлы с данными/статистика/статистика актив2.txt', 'a') as stata_act2:
            stata_act2.write(all_act2 + ',' + ' ')
    else:
        print('Введено не будет!')
        statistika_za_den()
elif vop1 == 2:
    vopros = str(input('Нужно вводить в документы? да/нет'))
    if vopros == 'да':
        send2 = dnevnik()
        s2_1, s2_2 = send2
        all_to_send = '\n' + '\n' + str(s2_1) + '\n' + s2_2
        dnev = open('Дневниковые записи.txt', 'a')
        dnev.write(all_to_send)
        dnev.close()
        ozen_disz = str(input('Оцени свою дисциплину за сегодня>>'))
        with open('файлы с данными/файлы: оценка/оценка - дисциплина.txt', 'a') as ozenka_1:
            ozenka_1.write(ozen_disz + ',' + ' ')
        ozen_samoraz = str(input('Оцени свое саморазвитие за сегодня>>'))
        with open('файлы с данными/файлы: оценка/оценка - саморазвитие.txt', 'a') as ozenka_2:
            ozenka_2.write(ozen_samoraz + ',' + ' ')
        ozen_product = str(input('Оцени свою продуктивность за сегодня>>'))
        with open('файлы с данными/файлы: оценка/оценка - продуктивность.txt', 'a') as ozenka_3:
            ozenka_3.write(ozen_product + ',' + ' ')
        ozen_spok = str(input('Оцени свое спокойствие за сегодня>>'))
        with open('файлы с данными/файлы: оценка/оценка - спокойствие.txt', 'a') as ozenka_4:
            ozenka_4.write(ozen_spok + ',' + ' ')
    else:
        print('Введено не будет!')
        dnevnik()

elif vop1 == 3:
    vopros = str(input('Нужно вводить в документы? да/нет'))
    if vopros == 'да':
        send_3 = PKZSH()
        send_3_1, send_3_2 = send_3
        all_to_send = 'Получил баллов:' + str(send_3_1) + '. Прогресс: ' + str(send_3_2) + '/' + str(200)
        dnev = open('Дневниковые записи.txt', 'a')
        dnev.write(all_to_send)
        dnev.close()
        s2_1 = str(input('Введи сегодняшнюю дату >>'))
        send3 = 'Получил баллов:' + str(send_3_1) + '. Прогресс: ' + str(send_3_2) + '/' + str(200)
        all_pkschz = send3
        with open('файлы с данными/статистика/статистика пкж.txt', 'a') as stata_pkschz:
            stata_pkschz.write(str(send_3_1) + '\n')
    else:
        print('Введено не будет!')
        PKZSH()

elif vop1 == 4:
    vse_itogi()
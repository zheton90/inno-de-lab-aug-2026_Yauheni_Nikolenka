raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# 1. Разбил строку на отдельные элементы, используя точку с запятой (;) в качестве разделителя.
list_user_record = raw_user_record.split(";")

# 2. Очистить каждый полученный элемент от ведущих и замыкающих пробельных символов.
clean_list_user_record = [t.strip() for t in list_user_record]

# 3. Применил к идентификатору пользователя (первый элемент) префикс UID-, используя форматирование строк.
clean_list_user_record[0] = 'UID-' + clean_list_user_record[0]

# 4. Преобразовал имя пользователя (второй элемент), заменив символ нижнего подчеркивания ( _ ) на пробел, и привести слова к правильному регистру (каждое слово с заглавной буквы).
clean_list_user_record[1] = clean_list_user_record[1].title().replace("_", " ")

# 5. Привёл название города (третий элемент) к верхнему регистру.
clean_list_user_record[2] = clean_list_user_record[2].upper()

# 6. Статус пользователя (четвертый элемент) переёл в нижний регистр.
clean_list_user_record[3] = clean_list_user_record[3].lower()

# 7. Объединил обработанные элементы в одну строку с разделителем |.
clean_row_user_record = ' | '.join(clean_list_user_record)

# Вывел результат на экран.
print(f'Нормализованная запись: {clean_row_user_record}')

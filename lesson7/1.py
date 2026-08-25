raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

list_user_record = raw_user_record.split(";")
clean_list_user_record = [t.strip() for t in list_user_record]
clean_list_user_record[0] = 'UID-' + clean_list_user_record[0]
clean_list_user_record[1] = clean_list_user_record[1].title().replace("_", " ")
clean_list_user_record[2] = clean_list_user_record[2].upper()
clean_list_user_record[3] = clean_list_user_record[3].lower()
clean_row_user_record = ' | '.join(clean_list_user_record)

print(f'Нормализованная запись: {clean_row_user_record}')

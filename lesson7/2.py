raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# 1. Отсеил все транзакции, не имеющие статус SUCCESS.
# 2. Извлек числовое значение суммы платежа.
# 3. Исключил аномальные транзакции с неположительной суммой (меньше или равной нулю).
# 4. Преобразовал корректные суммы в целочисленный тип данных (int).
clean_transactions = [t[8:] for t in raw_transactions if t.startswith('SUCCESS') and int(t[8:]) > 0]

# clean_price_transactions = [t[8:] for t in clean_success_transactions ]
# clean_positive_transactions = [t for t in clean_price_transactions if int(t) > 0]

# Вывел результат на экран.
print(f"Очищенные транзакции: {clean_transactions}")

db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"    }
}

# Извл вложенный словарь connection
db_connection = db_config.get("connection", {})

# 1. Извлечь значения host и port из вложенного словаря connection.
db_host = db_connection.get("host")
db_port = db_connection.get("connection")

# 2. Безопасно проверил наличие ключа ssl_settings в db_config.
# Если этот ключ или вложенный в него параметр ssl_mode отсутствуют, присвоил переменной дефолтное значение verify-full.
db_config.get("ssl_settings", 'verify-full')

# 3. Изменил значение пользователя (user) во вложенном словаре на admin.
db_config["connection"]['user'] = 'admin'

# 4. Добавил новый параметр max_connections со значением 100 непосредственно во вложенный словарь connection.
db_config["connection"]['max-connection'] = 100

# 5. Вывел обновленное содержимое конфигурации connection как показано в примере, используя итерацию по парам ключ-значение.
print(f"SSL Mode: {db_config.get("ssl_settings", 'verify-full')}")
print("Параметры соединения:")
for k, v in db_config["connection"].items():
    print (f"* {k}: {v}")

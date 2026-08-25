db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"    }
}

db_connection = db_config.get("connection", {})

db_host = db_connection.get("host")
db_port = db_connection.get("connection")

db_config.get("ssl_settings", 'verify-full')

db_config["connection"]['user'] = 'admin'
db_config["connection"]['max-connection'] = 100

print(f"SSL Mode: {db_config.get("ssl_settings", 'verify-full')}")
print("Параметры соединения:")
for k, v in db_config["connection"].items():
    print (f"{k}: {v}")

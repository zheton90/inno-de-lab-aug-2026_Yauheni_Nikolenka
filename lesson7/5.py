system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

# 1. Распаковал элементы кортежей в переменные: node_name, cpu_load,ram_usage, status.
node_name = [n[0] for n in system_telemetry]
cpu_load = [c[1] for c in system_telemetry]
ram_usage = [r[2] for r in system_telemetry]
status = [s[3] for s in system_telemetry]

# 2. Отфильтровал (проигнорировать) серверы, имеющие статус offline.
online_system_telemetry = [k for k in system_telemetry if k[3] == 'online' ]

# 3. Сформировал список имен активных серверов.
name_online_system_telemetry = [n[0] for n in system_telemetry if n[3] == 'online']

# 4. Рассчитал суммарные показатели активной группы:
# sum_online_system_telemetry - общее количество работающих серверов,
# middle_cpu_load - среднюю загрузку CPU (с округлением до двух знаков после запятой) и
# max_ram_usage - пиковое (максимальное) значение использования оперативной памяти RAM.
sum_online_system_telemetry = len(online_system_telemetry)
middle_cpu_load = round(float(sum(cpu_load) / sum_online_system_telemetry ), 2)
max_ram_usage = max(ram_usage)

# Вывел результат на экран как показано в примере.
print(f"""
Активные узлы в сети: {name_online_system_telemetry}
Итоговый отчет телеметрии:
{{
'active_nodes_count': {sum_online_system_telemetry},
'metrics': {{
    'average_cpu': {middle_cpu_load},
    'max_ram': {max_ram_usage}
    }}
}}
""")

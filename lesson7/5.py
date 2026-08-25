system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

node_name = [n[0] for n in system_telemetry]
cpu_load = [c[1] for c in system_telemetry]
ram_usage = [r[2] for r in system_telemetry]
status = [s[3] for s in system_telemetry]

online_system_telemetry = [k for k in system_telemetry if k[3] == 'online' ]
name_online_system_telemetry = [n[0] for n in system_telemetry if n[3] == 'online']

sum_online_system_telemetry = len(online_system_telemetry)
middle_cpu_load = float(sum(cpu_load) / sum_online_system_telemetry )
max_ram_usage = max(ram_usage)

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


# 1. Распаковать элементы кортежей на переменные: node_name, cpu_load,ram_usage, status.
# 2. Отфильтровать (проигнорировать) серверы, имеющие статус offline.
# 3. Сформировать список имен активных серверов.
# 4. Рассчитать суммарные показатели активной группы:
# общее количество работающих серверов,
# среднюю загрузку CPU (с округлением до двух знаков после запятой) и
# пиковое (максимальное) значение использования оперативной памяти RAM.

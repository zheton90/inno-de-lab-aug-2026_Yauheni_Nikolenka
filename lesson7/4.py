requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# 1. Сохранил список запрошенных ролей во множество set_roles для мгновенного удаления дубликатов.
set_roles = set(requested_roles)

# 2. Сохранил в cross_roles роли, которые одновременно присутствуют как в списке уникальных запрошенных,
# так и в списке обязательных административных ролей (пересечение множеств).
cross_roles = set(t for t in set_roles if t in required_admin_roles)

# 3. Сохранил в unrequested_roles недостающие административные роли,
# которые не были запрошены пользователем (разность множеств).
unrequested_roles = set(t for t in required_admin_roles if t not in set_roles)

# 4. Проверил и сохранил наличие роли security_officer в дедуплицированном множестве запрошенных ролей
# с помощью высокопроизводительного оператора членства, выполняющегося за время O(1).
is_security_officer_requested = "security_officer" in requested_roles

# Вывел результат на экран как показано в примере.
print(f'Уникальные запрошенные роли: {set_roles}')
print(f'Общие административные роли: {cross_roles}')
print(f'Недостающие административные роли: {unrequested_roles}')
print(f'Наличие роли security_officer в запросе: {is_security_officer_requested}')

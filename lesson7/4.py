requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}

set_roles = set(requested_roles)
cross_roles = set(t for t in set_roles if t in required_admin_roles)
unrequested_roles = set(t for t in required_admin_roles if t not in set_roles)
is_security_officer_requested = "security_officer" in requested_roles

print(f'Уникальные запрошенные роли: {set_roles}')
print(f'Общие административные роли: {cross_roles}')
print(f'Недостающие административные роли: {unrequested_roles}')
print(f'Наличие роли security_officer в запросе: {is_security_officer_requested}')

ROLE_SCOPES = {
    "ADMIN": [
        "admin:manage",
        "admin:view_reservations"
    ],
    "CLIENT": [
        "client:read_user",
        "client:write_user",
        "client:reserve_table",
        "client:order"
    ]
}

ALL_KNOWN_SCOPES = {}
for scopes_list in ROLE_SCOPES.values():
    for scope in scopes_list:
        ALL_KNOWN_SCOPES[scope] = f"Permission for {scope}"
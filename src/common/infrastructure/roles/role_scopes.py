ROLE_SCOPES = {
    "ADMIN": [
        "admin:gestion",
        "admin:ver_reservas"
    ],
    "CLIENT": [
        "client:crear_perfil",
        "client:mod_perfil",
        "client:reservar_mesa",
        "client:preordenar_menu"
    ]
}

ALL_KNOWN_SCOPES = {}
for scopes_list in ROLE_SCOPES.values():
    for scope in scopes_list:
        ALL_KNOWN_SCOPES[scope] = f"Permission for {scope}"
JAZZMIN_SETTINGS = {
    "site_title": "EZ Study",
    "site_header": "EZ Study",
    "site_brand": "EZ Study",
    "welcome_sign": "Welcome to EZ Study",
    "copyright": "EZ Study",
    "search_model": ["auth.User", "auth.Group"],


    "topmenu_links": [
        {"name": "EZ Study", "url": "home", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    "default_icon_parents": "fas fa-circle",
    "default_icon_children": "fas fa-dot-circle",
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme" : "darkly",
}
users:list=[
    {"name":"Oliwia","location":"Warszawa","posts":420},
    {"name":"Wiktoria","location":"Chelm","posts":120},
    {"name":"Sabina","location":"Opole","posts":345},
    {"name":"Kaja","location":"Tomaszow","posts":235},

]
print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów")









from app.models import db, Category, environment, SCHEMA

all_categories = [
    {"id": 1, "name": "Gear"},
    {"id": 2, "name": "Style"},
    {"id": 3, "name": "Cars"},
    {"id": 4, "name": "Tech"},
    {"id": 5, "name": "Shelter"},
    {"id": 6, "name": "Vices"},
    {"id": 7, "name": "Body"},
    {"id": 8, "name": "Etc"},
]


def seed_categories():
    categories = [
        Category(name=category["name"])
        for category in all_categories
    ]

    [db.session.add(category) for category in categories]

    db.session.commit()


def undo_categories():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM categories")

        db.session.commit()

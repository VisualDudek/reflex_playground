# Your First Database Model
get familiar with: 
- docs-> Learn / State / Database
- ORM

Reflex uses SQLModel to provide a built-in ORM wrapping SQLAlchemy.

Reflex leverages `alembic` to manage db schema changes.

There is `alembic.ini` config file

- add db_url into `rxconfig.py`
- create ContactEntryModel subclass of `rx.Model`
- init db `reflex db init`
- makemigrations
- migrate
- check `alembic/script.py.mako`
- you need to explicite `table=True` for models make effect in SQL
- now `just dbmakeall` will make reference point

# Storing Date with Models and Forms

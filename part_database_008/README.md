# Your First Database Model
get familiar with: 
- docs-> Learn / State / Database
- ORM

Reflex uses SQLModel to provide a built-in ORM wrapping SQLAlchemy.

Reflex leverages `alembic` to manage db schema changes.

- add db_url into `rxconfig.py`
- create ContactEntryModel subclass of `rx.Model`
- init db `reflex db init`
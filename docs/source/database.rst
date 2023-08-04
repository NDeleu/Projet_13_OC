Database
=========

SQLite3
--------

The database we use for this application is SQLite (here SQLite3).

SQLite is a lightweight, self-contained, file-oriented SQL database engine
often used for small to medium-sized applications,
due to its ease of installation and use.


Why use SQLite3 ? :

1/ Easy setup: Django is configured to use SQLite by default when creating a new project.
    In your Django settings file (settings.py) you will find the database configuration as `DATABASE`.

2/ No Server Required: Unlike other database management systems like PostgreSQL or MySQL,
    SQLite does not require a separate server process. All data is stored in a single file,
    which is managed directly by the SQLite engine.

3/ Portability: Since the SQLite database is simply a file,
    it is easy to copy and move to another location or system.


Presentation of objects and ERD
--------------------------------

3 objects are represented in the database : Profile, Letting, Address .

* Profile : Representing a customers. linked to the django User model (django.contrib.auth.models).
                                        Allows the identification of a user.

* Letting : Representing a letting ticket. linked to an Address to identify its object.

* Address : Representing a rental property. The address of the property is provided.


Presentation of the models
---------------------------

Presentation of Model Classes :


Profile : Representing a customers

.. autoclass:: profiles.models.Profile
   :members:


Letting : Representing a letting ticket

.. autoclass:: lettings.models.Letting
   :members:


Address : Representing a rental property

.. autoclass:: lettings.models.Address
   :members:
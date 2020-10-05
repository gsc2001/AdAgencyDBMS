# DnA AdAgency Project (MYSQL THREE OF A KIND)

## `create.py`

This file contains the implementation of the create queries. The user can add new records of Actor, Director, Brands, Products, Ads, Shows, Channels, Preferred Brands of the Actors and Ads displayed in the shows. If the entered data is invalid (by checking in python and in MYSQL) we return and ask the user to enter the data again.

## `read.py`

This file contains the implementation of the read queries and our functional requirements. The user can request all the records of Actor, Director, Brands, Products, Ads, Shows, Channels, Preferred Brands of the Actors and Ads displayed in the shows along with other user specific functional requirements which can be used for analysis.

## `update.py`

This file contains the implementation of the update queries. We allow the user to update product description and price, channel baseprice, show surcharge, account number and name of the person, height and weight of the actor, director salary and supervisor.

## `delete.py`

This file constains the implementation of the delete queries. Deletion of Actor, Director, Brand, Channel, Product, Ad, Show, Guardian are allowed along with deletion of relationship instances in prefers and displayedBetween table.

## `menus.py`

This file constains the implementation of the menu interface through which the user can choose the operation which he/she wishes to perform on the database using the command line interface. Depending on user input it calls the corresponding the functions.

## `app/__init__.py`

This file contains the main function which asks the username and password from the user and connects to the database by calling the function **_connect_to_database_** which is defined in the `app/utils/connect.py` file.

## `AdAgency.sql`

This is the dump file for our AdAgency Database. It contains the queries needed to create all the tables and load them with relevant data with basic checks.

---

## USAGE

### Loading database

-   Create a database 'AdAgency'

```sql
CREATE DATABASE AdAgency;
```

-   Change current database

```sql
USE AdAgency;
```

-   source the dump

```sql
SOURCE AdAgency.sql
```

### CLI

#### Install dependencies

-   Create a venv in python

```bash
    python3 -m venv DnA
```

-   Install dependencies

```bash
    pip install -r requirements.txt # or pip-sync requirements.txt
```

-   Run script

```bash
    ./main.py
```

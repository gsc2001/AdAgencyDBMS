# DnA AdAgency Project (MySQL)

## Setup

### Database

Enter the following commands in **MySQL shell**

1. Create a database 'AdAgency'

```sql
CREATE DATABASE AdAgency;
```

2. Change current database

```sql
USE AdAgency;
```

3. source the dump

```sql
SOURCE AdAgency.sql
```

### CLI

4. Create a venv in python

```bash
    python3 -m venv DnA
```

5. Switch to the virtual environment created

```bash
    source DnA/bin/activate
```

6. Install dependencies

```bash
    pip install -r requirements.txt # or pip-sync requirements.txt
```

7. Run script

```bash
    ./main.py
```

---

## Navigating the CLI (inspired by OS Shell)

### Commands

- `ls`: View options
- `cd [arg]`: Navigate to _arg_ (option name or option number or `..`)
- `[num]`: Navigate to _num_ option number
- `clear`: Clear the output
- `exit`: Close app
- `help`: View these commands anytime!

_Suggestions for new commands are always welcome :stuck_out_tongue_closed_eyes:_

### Menu Structure

```
Main
│
└───Add
│   │   Actor
│   │   Director
│   │   Brand
│   │   Channel
│   │   Show
│   │   Product
│   │   Ad
│   │   Guardian
│
└───Update
│   │
│   └───Actor
│   │   │   Account Number
│   │   │   Name
│   │   │   Height & Weight
│   │   │   Add Preferred Brand
│   │   │   Remove Preferred Brand
│   │
│   └───Director
│   │   │   Account Number
│   │   │   Name
│   │   │   Salary
│   │   │   Supervisor
│   │
│   └───Brand
│   │   │   POC Email
│   │   │   POC Phone
│   │
│   └───Product
│   │   │   Price
│   │   │   Description
│   │
│   └───Channel
│   │   │   Base Price
│   │
│   └───Show
│   │   │   Surcharge
│   │   │   Air an Ad
│   │   │   Remove an Ad
│   │
│   └───Ad
│       │   Air in a show
│       │   Remove from a show
│
└───Delete
│   │   Actor
│   │   Director
│   │   Brand
│   │   Channel
│   │   Show
│   │   Product
│   │   Ad
│   │   Guardian
│
└───Read
    │   Actors
    │   Directors
    │   Brands
    │   Channels
    │   Shows
    │   Products
    │   Ads
    │   Guardians
    │   Ad-Show Relations
    │   Actor's preffered brands
    │   Actors with Physical features
    │   Average Ad Production cost
    │   Maximum preferred brand
    │   Partial text search for shows
    │   Partial text search for actor
    │   Best shows for an ad
    │   Shows with surcharge less than a value
    │   Maximum of sum of contract money of brand
    │   Bill for an Ad
    │   Shows list by amount
```

---

## File Details

### `app/__init__.py`

This file contains the main function which asks the username and password from the user and connects to the database by calling the function **_connect_to_database_** which is defined in the `app/utils/connect.py` file.

### `AdAgency.sql`

This is the dump file for our AdAgency Database. It contains the queries needed to create all the tables and load them with relevant data with basic checks.

### `menus.py`

This file constains the implementation of the menu interface through which the user can choose the operation which he/she wishes to perform on the database using the command line interface. Depending on user input it calls the corresponding the functions.

### `create.py`

This file contains the implementation of the create queries. The user can add new records of Actor, Director, Brands, Products, Ads, Shows, Channels, Preferred Brands of the Actors and Ads displayed in the shows. If the entered data is invalid (by checking in python and in MySQL) we return and ask the user to enter the data again. Also, please add the guardians before adding a junior actor and provide aadhar card of guardians of the actor.

### `read.py`

This file contains the implementation of the read queries and our functional requirements. The user can request all the records of Actor, Director, Brands, Products, Ads, Shows, Channels, Preferred Brands of the Actors and Ads displayed in the shows along with other user specific functional requirements which can be used for analysis.

### `update.py`

This file contains the implementation of the update queries. We allow the user to update product description and price, channel baseprice, show surcharge, account number and name of the person, height and weight of the actor, director salary and supervisor.

### `delete.py`

This file constains the implementation of the delete queries. Deletion of Actor, Director, Brand, Channel, Product, Ad, Show, Guardian are allowed along with deletion of relationship instances in prefers and displayedBetween table.

---

## Contributors

#### Team: _Three Of A Kind_

- Gurkirat Singh (2019101069)
- Shrey Gupta (2019101058)
- Sanchit Arora (2019101047)

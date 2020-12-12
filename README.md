# Database ORM Address Book
A python console application that uses a MySQL database and an ORM to manage a
simple address book.

* [Installation](./README.md#installation)
  * [Requirements](./README.md#requirements)
  * [Setup](./README.md#setup)

-----

# Installation & Setup

## Requirements

It is recommended that you use [PyCharm](https://www.jetbrains.com/pycharm/download/)
as your IDE for this project. This allows you to easily create a virual environment
for loading dependencies.

* [Install MySQL](https://dev.mysql.com/downloads/mysql/)
* [SQL Alchemy](https://www.sqlalchemy.org/download.html#current)
* [Install PyMySQL](https://pymysql.readthedocs.io/en/latest/user/installation.html)
  * Include the dependency for “sha256_password” authentication.

## Setup

Run the seed file to set up your database in MySQL.

* [`MySQL/create.sql`](./MySQL/create.sql)

All that this seed file does is create the schema, `AddressBookORM`.

# Lost and Found Box

Phase 3 CLI project

## Description

A CLI Application that uses **Python, SQLAlchemy, and Alembic** to create User and Item classes, and then to manage the relationship between them. In User table users can add their enteries with basic information like name and email, and can add lost and found item details, and modify the item status accordingly throughout the process. Repository has a built-in seeding file to pre-seed the database with test data to test out the application's features.

## Installation

Fork the repo and clone it locally in the desired destination folder using below command:

```bash
git clone SSH_File
```


## Usage

After cloning, run the following command to install the relavant environment and dependancies to get the application working.

```bash
pipenv install && pipenv shell
```

pipenv shell will navigate us into the virtual environment where the application will run.

To seed the database with intial test or fake data to test out the functioning of the app. We can also hard code the data into the file or we can also use an api to fech initial data as well. For initital data, run the below mentioned command:

```bash
python3 seeds.py
```

Then to start the app run the following command:

```bash
python3 cli.py
```

Have Fun!

## Information

This application while functional, might not include all the functionalities of a Lost and Found application. This project was built with the goal of displaying the ability to create python classes and successfully map them to a database using SQLAlchemy and then to ensure an appropriate handling of database migrations using Alembic when establishing the relationships between these classes.

## Improvements / Roadmap

- Add a method to create new instance of lost and found items.
- Add a method to display list of lost and found items and also list them according to their final_status.
- Add a method to change the final_status when someone claimed any item marking the completion of the process.


## Resources

- https://pypi.org/


<br>

- https://docs.sqlalchemy.org/en/14/index.html

- I express my deep gratitude to the Flatiron instructors. The process of creating this project was quite daunting as I was trying to learn many things all at once. However, by diligently watching and revisiting various demonstrations and lectures, I successfully navigated through this project and developed a decent CLI application. Thank you for your invaluable guidance!

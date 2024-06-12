# Personal Finance Manager

## Date, 2024/06/12

## Description

Personal Finance Manager is a Python CLI application designed to help users manage their income and expenses effectively. The application uses an Object-Relational Mapping (ORM) approach to interact with a SQLite database, allowing users to categorize, add, view, and delete income and expense records.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Classes and Methods](#classes-and-methods)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add, view, and delete categories
- Add, view, and delete income records
- Add, view, and delete expense records
- Store data persistently using SQLite

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/personal-finance-manager.git
    cd personal-finance-manager
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Technologies used

(a) Python
(b) SQLite
(c) Git

## Usage

1. Run the CLI application:

    ```sh
    python lib/modules/cli.py
    ```

2. Follow the on-screen menu to manage categories, incomes, and expenses.

## Project Structure

personal-finance-manager/
│
├── lib/
│ ├── modules/
│ │ ├── init.py
│ │ ├── category.py
│ │ ├── income.py
│ │ ├── expense.py
│ │ └── cli.py
│ ├── connection.py
│ └── setup.py
│
├── requirements.txt
└── README.md

## Classes and Methods

### Category

- `Category.create_table()`: Creates the `categories` table.
- `Category.save()`: Saves a category to the database.
- `Category.get_all()`: Retrieves all categories from the database.
- `Category.find_by_id(id)`: Finds a category by its ID.
- `Category.find_by_name(name)`: Finds a category by its name.
- `Category.delete()`: Deletes a category from the database.

### Income

- `Income.create_table()`: Creates the `incomes` table.
- `Income.save()`: Saves an income record to the database.
- `Income.get_all()`: Retrieves all income records from the database.
- `Income.find_by_id(id)`: Finds an income record by its ID.
- `Income.delete()`: Deletes an income record from the database.

### Expense

- `Expense.create_table()`: Creates the `expenses` table.
- `Expense.save()`: Saves an expense record to the database(db).
- `Expense.get_all()`: Retrieves all expense records from the db.
- `Expense.find_by_id(id)`: Finds an expense record by its ID.
- `Expense.delete()`: Deletes an expense record from the db.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License Copyright (c) 2024.

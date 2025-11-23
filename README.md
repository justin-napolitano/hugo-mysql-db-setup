# hugo-mysql-db-setup

A Python-based project to automate MySQL database setup and management for Hugo blog integration. This repository includes utilities to create, use, and drop MySQL databases and tables via scripts, facilitating streamlined blog content management.

---

## Features

- Python class for MySQL connection and database operations
- Automated execution of SQL scripts to create tables
- Integration with dotenv for environment variable management
- Modular structure supporting submodules for configuration and utility classes

## Tech Stack

- Python 3
- mysql-connector-python
- python-dotenv
- MySQL

## Getting Started

### Prerequisites

- Python 3.x installed
- MySQL server installed and running
- `.env` file with the following variables:
  - `DB_USER`
  - `DB_PASSWORD`
  - `DB_HOST`
  - `DB_NAME`

### Installation

Clone the repository and initialize submodules:

```bash
git clone https://github.com/justin-napolitano/hugo-mysql-db-setup.git
cd hugo-mysql-db-setup
# Add submodules
# If not initialized already

git submodule add https://github.com/justin-napolitano/mysql-config.git mysql-config
git submodule add https://github.com/justin-napolitano/mysql-utility-class.git mysql-utility-class

# Create empty __init__.py files for module setup

touch __init__.py
cd mysql-utility-class
# Add __init__.py with relative imports as needed
```

### Running

Run the main script to perform database operations:

```bash
python main.py
```

This script will:
- Connect to the MySQL server
- Create a test database
- Execute SQL scripts to create tables
- Drop the test database
- Disconnect from MySQL

## Project Structure

```
/
|-- __init__.py          # Empty file to mark root as package
|-- main.py              # Main script to run DB setup and teardown
|-- index.md             # Documentation and blog post content
|-- mysql-config/        # SQL scripts and MySQL configuration
|   |-- authors.sql      # SQL to create authors table
|   |-- posts.sql        # SQL to create posts table
|   |-- mastodon.sql     # SQL to create mastodon_posts table
|   |-- index.md         # MySQL config guide
|-- MySQLConnector/      # Python MySQL connection class
|   |-- __init__.py      # Imports MySQLConnector class
|   |-- MySQLConnector.py# Implementation of MySQLConnector class
|-- test                 # Placeholder or test file
```

## Future Work / Roadmap

- Add error handling and logging improvements
- Support for more complex schema migrations
- Integration with Hugo blog content generation
- Add automated tests
- Enhance configuration management
- Support for additional database engines

---

For detailed usage and configuration, refer to the `index.md` files and source code comments.

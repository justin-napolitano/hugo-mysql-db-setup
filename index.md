+++
title =  "Automate Posting Hugo Blog to Social Sites (with a db) Part 2"
date = "2024-06-15"
description = "How To automate posting to social sites"
author = "Justin Napolitano"
tags = ['python', "hugo","programming","fail"]
images = ["images/feature-image.png"]
+++


## Background



### Previous posts in this series

1. [part 1](https://jnapolitano.com/en/posts/hugo-social-publisher/)
2. [part 2](https://jnapolitano.com/en/posts/python-rss-reader/)
3. [part 3](https://jnapolitano.com/en/posts/mysql-install-buntu/)
4. [part 4](https://jnapolitano.com/en/posts/mysql-config/)
5. [part 5](https://jnapolitano.com/en/posts/hugo-rss-setup/)
6. [part 6](https://jnapolitano.com/en/posts/hugo-rss-mysql-update/)



### Expand a the mysql class

I create a [repo](https://github.com/justin-napolitano/mysql-utility-class.git) at ```https://github.com/justin-napolitano/mysql-utility-class.git``` to enable importing as a submodule the class that i have been workign on. 

### Set up the db

In [another part in this series](https://jnapolitano.com/en/posts/mysql-config/), I detailed setting up the mysql db via the command line. I am going to furher that workflow by modifying the files in that repo and then running thm to generat tables within my instance of mysql.


## Setup you dev environment...again

### Copy the .env file


Copy over the .env files from the previous few steps. 

### Import the Config repo 

```bash

git submodule add https://github.com/justin-napolitano/mysql-config.git mysql-config

```

### Import the utility class repo

```bash

git submodule add https://github.com/justin-napolitano/mysql-utility-class.git mysql-utility-class   

```


### Setup the package as a module 

#### From root drop an empty __init_.py file

```bash 

touch __init__.py
```

#### From the utility class directory drop another __init__.py

This one however will contain a relative import to enable access to the class

##### Touch

```bash 
cd {to the utility class directory} && touch __init__.py

```

##### Echo to file

```bash

echo "from .MySQLConnector import MySQLConnector" > __init__.py

```

#### Check the module hierarchy

We should be looking like this



```markdown
your_project/
|-- __init__.py
|-- main.py
|-- .env
`-- MySQLConnector/
    |-- __init__.py
    `-- MySQLConnector.py
```

## Create the main file

### Touch main.py

```bash

touch main.,py

```


### Modify main.py

My file currently looks like this to test the connect 

```python

from MySQLConnector import MySQLConnector

from dotenv import load_dotenv
import os



if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    connection = MySQLConnector()
    connection.connect()
    connection.disconnect()

```


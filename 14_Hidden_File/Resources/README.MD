# Hidden File

## Issue

The URL and subdirectories at "http://{IP}:{PORT}/.hidden/" reveal sensitive data (flag)


## Attack Vector

1 - Examining the URL "http://{IP}:{PORT}/.hidden/" we find a huge number of subdirectories which makes manual iteration impossible. So we create automation scripts.

2 - Open bash and navigate to script directory. Launch script with `python3 crawler.py` . Make sure to set the base URL!

3 - Once completed navigate to script directory. Launch script with `python3 checkreadme.py` . This will read all README files in the scraped URLs 

4 - Examine the contents of 'ReadMeFileContent.txt' and search for flag.

5 - Flag is `d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466`


## Mitigation

1 - Do not put sensitive files in web root directory

2 - Ensure server does not allow access to locations unless user is properly verified

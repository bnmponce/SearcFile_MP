# Search Files and Folders by Command Line

This tool allows to search files and folders by command line. It has been implemented in Python using the ArgParse library which is useful to handle arguments.
This tool uses a configuration file .INI which store by default the following criteria:
'path: C:/Users/Public'
'name: " "'
'Type: 3 = both files and folder'
'Case Sensitive: n=nonCase sensitive',

### Prerequisites

The following libraries are required to be installed:

```
pip install pypiwin32
pip install PTable
```

### How to use:

You can peform searches by using the following arguments:

```
usage: __main__.py [-h] [-s] [--name NAME] [--path PATH] [--type TYPE]
                   [--size SIZE] [--operator OPERATOR] [--extension EXTENSION]
                   [--date DATE] [--opdate OPDATE] [--controldate CONTROLDATE]
                   [--casesensitive CASESENSITIVE] [--owner OWNER]
                   [--content CONTENT] [--namefind NAMEFIND]
                   [--contentfind CONTENTFIND] [-r]

DEV FUNDAMENTALS II - SEARCH FILES AND FOLDERS.

optional arguments:
  -h, --help            show this help message and exit
  -s                    perform search with criteria given. (default: False)
  --name NAME, -n NAME  Configure the name of the file or folder to search.
                        (default: )
  --path PATH, -p PATH  Configure the path in order to search a file or
                        folder. (default: C:\)
  --type TYPE, -t TYPE  Configure the type of search file or folder to search.
                        (default: 3)
  --size SIZE, -z SIZE  Configure the file size (Mb) to search. If you specify
                        only the size, it will search by default the files
                        size less than the size specified. Otherwise use the
                        following operators: -l, -g or -e (default: None)
  --operator OPERATOR, -o OPERATOR
                        Enter the operator to search by specific size: -l: to
                        search files less than the size specified -g: to
                        search the files greater than the size specified -e:
                        to search the exact match size (default: l)
  --extension EXTENSION, -ext EXTENSION
                        Configure the file extension to search. It will search
                        all file types by default if none is given (default:
                        None)
  --date DATE, -d DATE  Configure the date to search a file (default: None)
  --opdate OPDATE, -od OPDATE
                        Enter the date operator to search by specific date: l:
                        to search files less than the date specified g: to
                        search the files greater than the date specified e: to
                        search the exact match date (default: None)
  --controldate CONTROLDATE, -cd CONTROLDATE
                        Enter the operator to search by control date: created,
                        modified and acceded c: to search files created in the
                        specified date m: to search files modified in the
                        specified date a: to search files acceded in the
                        specified date (default: None)
  --casesensitive CASESENSITIVE, -cs CASESENSITIVE
                        Enter the argument -cs to specify if your search by
                        name will be case sensitive or notBy default it will
                        be case sensitive, other wise use the values: y: you
                        confirm as yes, you want to search by case sensitive
                        name n: you confirm as no, you do not want to search
                        by case sensitive name (default: n)
  --owner OWNER, -ow OWNER
                        Enter the owner name to filter the search by owner.
                        (default: None)
  --content CONTENT, -c CONTENT
                        Enter the operator -c and the content you want to
                        search. It is only supported .txt for the momentIt
                        will search all matches with the text introduced. If
                        you want to search an specific text, use: -f argument
                        followed by e to search the exact match (default:
                        None)
  --namefind NAMEFIND, -nf NAMEFIND
                        Enter the argument find / -f to specify if you want to
                        search by an specific name/textBy default the searches
                        are finding all matches that contains the text
                        introduced. Otherwise use: e: if you want to find an
                        exact name/text (default: None)
  --contentfind CONTENTFIND, -cf CONTENTFIND
                        Enter the argument find / -f to specify if you want to
                        search by an specific name/textBy default the searches
                        are finding all matches that contains the text
                        introduced. Otherwise use: e: if you want to find an
                        exact name/text (default: None)
  -r                    perform a reset of default values of search all in the
                        path C:.path: C:name: " "Type: 3 = both files and
                        folderCase Sensitive: n=nonCase sensitive (default:
                        False)
```

Simple example to execute:
```
python __main__.py -s --name test --path C:\Users\Administrator\Documents
```
Complex example to execute:
```
python __main__.py -s --name test --namefind e --path C:\Users\Administrator\Documents --type 3 --casesensitive n --extension txt --size 0.00 --operator g --date 01-01-2017 --opdate g --controldate c --owner Administrator --content test
```

## Versioning

This is a Beta version.

For the Beta version available, see the [tags on this repository] (https://github.com/bnmponce/SearcFile_MP/tree/develop)

## Authors
* **Ariel Zurita** - *Search* - [Search](https://github.com/bnmponce/SearcFile_MP/tree/develop/search_files_mag/src/com/jalasoft/search_files/search)
* **Gladys Copaga** - *Menu* - [Menu](https://github.com/bnmponce/SearcFile_MP/tree/develop/search_files_mag/src/com/jalasoft/search_files/menu)
* **Magdalena Ponce** - *Validators* - [Validators](https://github.com/bnmponce/SearcFile_MP/tree/develop/search_files_mag/src/com/jalasoft/search_files/utils)

## License

None
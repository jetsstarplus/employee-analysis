# Resume Analysis System

This is a python application that scans uploades Resumes from applicants and and returns the results based on the computer science field

## Getting started
Clone the repository [Resume analysis system](https://github.com/jetsstarplus/employee-analysis.git)<br>
Download [virtualenv](https://pypi.org/project/virtualenv/)
```bash
    pip install -g virtualenv
```
Create a Virtual environment
```bash
    mkvirtualenv [your-env's name]
    workon [your-env's name]
```
Install the dependencies using [pip](https://pip.pypa.io/en/stable/)
```bash
    pip install -r requirements.txt
```
Navigate to in the file to ``Ruth/Ruth/settings/local.py``
<br>
Configure The right database setting for the db you are using. 
<br><br>`sqlite3` is a file database you don't have to download it.
<br>
<br>
`mysql` can work with either [xampp](https://www.apachefriends.org/download.html) or
[mysql](https://www.mysql.com/downloads/) engine installed and with the database created in the engine
<br>
<br>

`postgresql` is another Relational database management system whose configurations and usage can be found at 
[official download page](https://www.postgresql.org/download/)

### Wrapping Up
Fire up your django dev server via the following command
```python
    python manage.py runserver
```

#### Done Happy coding and presentation
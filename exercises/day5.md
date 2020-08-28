### Files exercises

1. Write a Python program that reads file content and displays the number of lines that were read.
1. Write a Python program to append text into a file and display the new content.
1. Write a function `grep` that receives `text` and `file` as parameters and returns a list with all the lines in the file containing `text`. 
1. Write another function `grepinto` that receives `text`, `infile` and `outfile` as parameters and writes to `outfile` the lines in `infile` that contain `text`. Open both files within one `with` statement. 

[!] `file`, `infile` and `outfile` are all file names - not file handlers.

### File system exercises

1. Write a Python program that creates a directory `outdir` at the current location and a directory `innerdir` inside `outdir`.
   Create an empty file inside `innerdir`. Use `os.walk()` to print the directory tree for `outdir`.
   Remove the directories and the file.
1. Write a generator function that yields all the file names with an extension from a directory.
   Give the path and the file extension as parameters. 

### Unittest exercises

1. Write a test case for `Employee.raise_salary()` method. Consider all representative cases.


### Django exercises
1. [optional] Run the interactive Django shell (`python manage.py shell`) and play around with the ORM (create objects, query db).
```python
>>> from university.models import * 
>>> from datetime import date
>>> ase = University.objects.create(name='ASE', city='buc')  # object creation; returns University object
>>> Student.objects.all()  # select * from students
>>> Student.objects.create(first_name='John', last_name='Doe', date_enrolled=date(2019, 10, 1), university=ase)
>>> john = Student.objects.filter(university=ase).first()  # select * from students where condition
>>> john.last_name = 'Popescu'
>>> john.save()  # object update
```
1. Create a view for student details (similar to university details).
1. Create a template for the student details view. Display all student object fields.
1. Create a url to point to the new view.
1. Link the student details page to the university details page (for each student displayed under current university, transform its name into a link to the details page).

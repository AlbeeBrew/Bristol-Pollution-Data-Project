Let's start from the beginning. This is going to be a brief overview of this assignment.
# Task 1
Task 1 is divided into two sub-categories.
In part-a(crop.py). I tried to crop and filter the data without using the **pandas** module to get extra credit and I was successful in doing it. It wasn't an easy task. 
The same goes for the part-b (clean.py). I preferred using the **pandas** module because it is fast and efficient. I encountered a problem but only for the time I was unaware of the fact that I could use the *replace* method on the **Series**object. But when I did, the problem was solved. The replaced method took care of it. I didn't need to replace the 18 stations(monitor) with their responding values. 
# Task 2
Extracting pollution_er.png was quite easy with the GUI tools that come with MySQL. I used **MySQL Workbench** to model the database. And upon the guidance of the instructor, used forward engineer to generate **pollution.sql** file. 
At first, there were some connection issues because I had forgotten that port **3306** was already in use. I needed to connect with port **3307**. Yeah, the latter one was used in **MySQL WorkBench** and the port **3306** was used in **PhpMyAdmin**. Reading an article on google, helped me find my fault and correct it immediately.
# Task 3
This is probably the Task, that took most of my time in this Assignment. Using **pandas** and **mariadb** was very convenient. **mariadb** was my module of choice. I successfully connected to the MySQL server and populated all the relevant data into it. My mistake was that I was inserting the *readings* table before inserting the *stations* table. That caused an error. The error was caused by the foreign-key constraints. Then I realized that the *stations* table is the parent table because of the relationship between these two tables. I realized that I needed to insert data into the *station* table first before adding anything into the *readings* table. One more problem I encountered was that even in the *executemany* method of the MySQL connection cursor I couldn't execute more than one query at a time. I wasn't able to terminate a query by prefixing it with a semicolon';'. I needed to execute all of them separately. Hence, I did. Even if Task2 generated **pollution.sql** file. Unfortunately, I couldn't use that file as a starting point for Task 3.
I hope you will like insert-100.py too. It was a relatively challenging task than others. 
# Task 4
In **query-a.sql**, returned the correct maximum value of the *NOX* of all stations and it was pretty straightforward. 
In **query-b.sql**, I followed the same rule as **query-a.sql**. Here I used *AVG* aggregation. Limited the DateTime to 2019. 
Just a little bit of change in **query-b.sql** made it look like **query-c.sql**. Where instead of limiting the DateTime to 2019. It is ranged between 2010 and 2019 (both included).
# Task 5
Finally, the **MongoDB** modeling, implementation, and query.
As **MongoDB** developers say, modeling a **MongoDB** database is more of an art than a science. With a gut feeling, I began modeling the structure and behavior of the database. Learned a lot of new methods and functionalities of **MongoDB** that I didn't know before. I used **pymongo** with the help to implement and model the database with python functions as well. 
Implementation was quite straightforward. But instead of doing it by hand, I preferred writing a python script to automate it for me. This leads me to use **pymongo** an API to interact with **MongoDB** using **python**. But typecasting was needed. As database itself has a lot of data types built-in which is also an advantage of using MongoDB. 
Querying the same data as **query-c.sql** was done using the *aggregate* method. Yeah, I faced a few errors here and there but eventually solved them. One of them which I think is worthy of talk is that the **aggregate** method takes an expression to work with. I kept passing an array and wondered why it doesn't work. But yeah, I solved it by removing those brackets.
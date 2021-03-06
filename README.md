# COVID-19 cases in Texas daycares

This project helps to present the most recent accumulated COVID cases of the kids and staff in texas childcare centers. The general public can see the cases by City and by zip code. The authorized database manager can edit the cases numbers. This web is hosted in heroku and link is (https://covid-cases-in-tx-daycare.herokuapp.com/).

## 1. Getting started

#### 1.1 Data souces and manipulation:

The data is from texas health and Huamn Service (https://www.hhs.texas.gov/services/health/coronavirus-covid-19/texas-covid-19-case-count-vaccination-data). The raw data is in .xls file, and I modifided it into .csv file. I onload the data to psql with the following step:

    (1) create psql database locally
        (1.1) create a database
            see "/backend/covid_in_tx_daycare.sql"
        (1.2) create a table structure
            see "create_daycare_table.psql"
        (1.3) copy .csv to (2) table
            run 
            '''
                $COPY covid_in_tx_daycare FROM '/YOURPATH/create_daycare_table.psql' DELIMITER ',' CSV HEADER;
        (1.4) Validate the data inserted in table by select query
            * run psql in terminal
            * check with "SELECT * FROM covid_in_tx_daycare LIMIT 5;"
    
    (2) dump the data to heroku-psql
        (2.1) create a the app in heroku, named "covid-cases-in-tx-daycare"
        (2.2) type 'Heroku Postgres' into the Add-ons search field of your app.
            * The link for reference (https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1)
        (2.3) choose "Hobby Dev - Free" and click 'Provision'
        (2.4) access to the database credential by navigating to "Resources tab" in your app's dashboard again and select the Heroku Postgres
        (2.5) go to pgAdmin4 to create a new server with the credentials from (2.4)
            * The link for reference (https://www.jhipster.tech/tips/028_tip_pgadmin_heroku.html)
        (2.6) dump database from (1) to heroku-psql
            * in the local terminal
                ```
                heroku pg:psql --app covid-cases-in-tx-daycare < covid_in_tx_daycare.sql







## 1. 

Install the backend prerequirement dependencies by using this command:

    pip3 install -r requirements.txt

We need then create database and insert all the data in tables
- for database, , cd to '\backend' directory and excute this command:

        psql 
        \i setup.sql

        \q  \\to exit the database before insert data to tables
    
- for tables, cd to '\backend' directory and excute:

        psql trivia < trivia.psql

After install the database and tables, we start the backend and frontend server to play.
- for backend, cd to '\backend' directory:

        export FLASK_APP=flaskr
        export FLASK_ENV=development
        flask run
    
- for frontend, cd to '\frontend' directory:

        npm install
        npm start

So far, we have done the server part, the following section will be focused on the detailed API reference

## 2. API reference

In this project, the API is a REST API. The requests include "GET", "POST", and "DELETE", and the error codes are 400, 404, 422, and 405. Using the API, we can request all the categories and the questions (in pagination, with the specific category for each question on a particular page), we can search questions in a selected category, create questions, delete questions, and find a random question in any chosen category.

#### (1) Base url - get all the categories

This command is expected to fetch json file, including all the categories in a json file, the status of fetch ("success", true or false), and the total number of categories. The category json is a dictionary with a key named as "id", and a description.

    curl http://127.0.0.1:5000/categories

The response is 

    {
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "success": true, 
    "total_categories": 6
    }

#### (2) All questions
This request can render all the questions but in pagination form. The default page = 1 with 8 questions showingup. The categories the response are the categories of the shown 8 questions, other than all the categories in the database:

    curl http://127.0.0.1:5000/questions

the reponse:

    {
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "current_categories": {
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "questions": [
        {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
        "answer": "Maya Angelou", 
        "category": 4, 
        "difficulty": 2, 
        "id": 5, 
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
        "answer": "Brazil", 
        "category": 6, 
        "difficulty": 3, 
        "id": 10, 
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
        "answer": "Uruguay", 
        "category": 6, 
        "difficulty": 4, 
        "id": 11, 
        "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
        "answer": "George Washington Carver", 
        "category": 4, 
        "difficulty": 2, 
        "id": 12, 
        "question": "Who invented Peanut Butter?"
        }, 
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ], 
    "success": true, 
    "total_questions": 19
    }

For questions in other pages, we can use the command: curl http://127.0.0.1:5000/questions?page=${integer}. For example:

    curl http://127.0.0.1:5000/questions?page=2

#### (3) Creating a question
This method will create a new entry of question. A successful create requires all of three: "question", "answer", "category". 

    curl -X POST -H "Content-Type: application/json" -d '{"question": "test question", "answer": "test answer", "category": "1", "difficulty":"1"}' http://127.0.0.1:5000/questions

response:

    {
    "new_question": {
        "answer": "test answer", 
        "category": 1, 
        "difficulty": 1, 
        "id": 28, 
        "question": "test question"
    }, 
    "success": true, 
    "total_questions": 20
    }


#### (4) Deleting a question
We can also delete a question, by using

    curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5000/questions/20

Response:
    {  "deleted_question": {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
    }, 
    "success": true
    }

#### (5) Searching a question
Here, we search any words/letters in a question description, and the reponses will list all the questions that fit the requirement, along with their corresponding categories.

        curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"what"}' -H "Content-Type: application/json" 


-response:
    
    {
    "current_category": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment"
    }, 
    "questions": [
        {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "Mona Lisa", 
        "category": 2, 
        "difficulty": 3, 
        "id": 17, 
        "question": "La Giaconda is better known as what?"
        }, 
        {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
        }, 
        {
        "answer": "Blood", 
        "category": 1, 
        "difficulty": 4, 
        "id": 22, 
        "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ], 
    "success": true, 
    "total_questions": 8
    }

#### (6) listing all question in a category
The command will pull all the questions in the chosen category. `curl http://127.0.0.1:5000/categories/${integer}/questions` It will automatically validate the integer number, and check whether it is in the categories id range. I give an example to fetch questions in category 1:

        curl http://127.0.0.1:5000/categories/1/questions

response:
     
    {
        "current_questions": [
            {
            "answer": "The Liver", 
            "category": 1, 
            "difficulty": 4, 
            "id": 20, 
            "question": "What is the heaviest organ in the human body?"
            }, 
            {
            "answer": "Alexander Fleming", 
            "category": 1, 
            "difficulty": 3, 
            "id": 21, 
            "question": "Who discovered penicillin?"
            }, 
            {
            "answer": "Blood", 
            "category": 1, 
            "difficulty": 4, 
            "id": 22, 
            "question": "Hematology is a branch of medicine involving the study of what?"
            }
        ], 
        "success": true, 
        "total_questions": 3
    }

#### (7) Rendering a random question in a category


        curl -d '{"previous_questions":[17], "quiz_category":{"type": "Art", "id": "2"}}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/quizzes

--response
    
    {
    "question": {
        "answer": "One", 
        "category": 2, 
        "difficulty": 4, 
        "id": 18, 
        "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    "success": true
    }
    

#### (8) error handlers
The error code in our project are 400, 404, 405, and 422. We also render a json file to explain the error. For example, we use:

    curl http://127.0.0.1:5000/categories/100/questions

error 422
response:
``` 
    {
    "error": 422, 
    "message": "can not process the resource", 
    "success": false
    }
```

## 3. Authors
Yan Xu, Udacity Full-stack team

## 4. Acknowledgement
Yan thanks the mentors in Full-stack team. They are patient and resourceful. In particular, Mr. Nitish K offered a huge help on the /quizzs handler.

#### copy from Udacity example
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

- Models:

```
    Movies with attributes title and release date

    Actors with attributes name, age and gender
```

- Endpoints:
```
    GET /actors and /movies
    DELETE /actors/ and /movies/
    POST /actors and /movies and
    PATCH /actors/ and /movies/
```

- Roles:

    -- Casting Assistant
    ```
        Can view actors and movies
    ```

    -- Casting Director

    ```
        All permissions a Casting Assistant has and???
        Add or delete an actor from the database
        Modify actors or movies
    ```

    -- Executive Producer
    ```
        All permissions a Casting Director has and???
        Add or delete a movie from the database
    ```

- Tests:
```
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    At least two tests of RBAC for each role
```

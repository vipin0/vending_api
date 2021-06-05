## VEDING API

#### instruction to run the API
 
###### 1. Make Sure you have python >= 3.8 installed and is in your system PATH
 
###### 2. Find the requirements.txt file and open a terminal in the same directory

###### 3. Run the Following commands
 
 ```
 pip install -r requirements.txt
 
 python manage.py makemigrations

 python manage.py migrate

 python manage.py runserver

 ```

 ###### 4. Now open postman to test the API
    1. To create new order create a POST request at http://127.0.0.1:8000/api/orders/create/and enter the data in the following format
    ```
    {
        'penny':
        'nickel':
        'dime':
        'quarter':
        'coke':
        'pepsi':
        'soda':
    }

    ```
    2. To get all the orders make a GET request at http://127.0.0.1:8000/api/orders/
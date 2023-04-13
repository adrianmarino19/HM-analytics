from flask import Flask, request
from pymysql import connect
from pymysql.cursors import DictCursor
from flask_restx import Api, Resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
api = Api(app)
API_KEY = "secretkey"

# Database connection parameters
db_config = {
    "host": "34.29.76.124",
    "user": "root",
    "password": "capstone123",
    "database": "main",
}

# Initialize the app and create the users table if it doesn't exist
def init_app():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_users_table_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Users table created or already exists.")
    except Exception as e:
        print("Error while creating users table:", e)

# Get a connection to the database
def get_db_connection():
    connection = connect(**db_config)
    return connection

# Fetch data from the database
def fetch_data_from_db(query):
    connection = get_db_connection()
    cursor = connection.cursor(DictCursor)
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    connection.close()
    return {"data": data, "columns": columns}

# Define the Articles resource
class Articles(Resource):
    def get(self):
        # Check if the API key is valid
        api_key = request.headers.get("x_api_key")
        if not api_key or api_key != API_KEY:
            return {"error": "Invalid API key"}, 401

        # Get a connection to the database and execute a query to get the articles
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles LIMIT 10000")
        articles = cursor.fetchall()

        # Get the column names
        column_names = [desc[0] for desc in cursor.description]

        # Close the database connection and return the data and column names as a JSON object
        connection.close()
        return {"data": articles, "columns": column_names}


# Define the Transactions resource
class Transactions(Resource):
    def get(self):
        # Check if the API key is valid
        api_key = request.headers.get("x_api_key")
        if not api_key or api_key != API_KEY:
            return {"error": "Invalid API key"}, 401

        # Get a connection to the database and execute a query to get the transactions
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM transactions LIMIT 100000")
        transactions = cursor.fetchall()

        # Get the column names
        column_names = [desc[0] for desc in cursor.description]

        # Close the database connection and return the data and column names as a JSON object
        connection.close()
        return {"data": transactions, "columns": column_names}


# Define the Customers resource
class Customers(Resource):
    def get(self):
        # Check if the API key is valid
        api_key = request.headers.get("x_api_key")
        if not api_key or api_key != API_KEY:
            return {"error": "Invalid API key"}, 401

        # Get a connection to the database and execute a query to get the customers
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers LIMIT 10000")
        customers = cursor.fetchall()

        # Get the column names
        column_names = [desc[0] for desc in cursor.description]

        # Close the database connection and return the data and column names as a JSON object
        connection.close()
        return {"data": customers, "columns": column_names}


# Define the UsersSignup resource
class UsersSignup(Resource):
    def post(self):
        # Check if the API key is valid
        api_key = request.headers.get("x_api_key")
        if not api_key or api_key != API_KEY:
            return {"error": "Invalid API key"}, 401

        # Get the username and password from the request data
        data = request.get_json()
        new_username = data.get('username')
        new_password = data.get('password')

        # Validation and other operations like hashing the password should be done here

        # Get a connection to the database and execute a query to check if the username already exists
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (new_username,))
        existing_user = cursor.fetchone()

        # If the username does not exist, insert the new user into the database
        if not existing_user:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (new_username, new_password))
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "User created successfully"}
        else:
            cursor.close()
            connection.close()
            return {"error": "Username already exists"}, 409


class UsersLogin(Resource):
    def post(self):
        # Check API key
        api_key = request.headers.get("x_api_key")
        if not api_key or api_key != API_KEY:
            return {"error": "Invalid API key"}, 401

        # Get username and password from request
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Connect to database and execute query to get user with matching username
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        # Check if user exists and password matches
        if user and password == user[2]:
            # Replace this with a proper token generation process
            access_token = "your_access_token_here"
            return {"access_token": access_token}
        else:
            return {"error": "Username/password is incorrect"}, 401

# Define endpoints for the API resources
api.add_resource(UsersSignup, "/api/users/signup")
api.add_resource(UsersLogin, "/api/users/login")
api.add_resource(Articles, "/api/articles")
api.add_resource(Transactions, "/api/transactions")
api.add_resource(Customers, "/api/customers")

# Initialize the Flask application and run it
if __name__ == "__main__":
    init_app() 
    app.run(debug=True, port=3010)
<p align="center">
  <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg", width = "20%">
</p>
<h3 align="center">H&M Analytics</h3>

<p align="center"><b>By:</b> Adrian Marino</p>
<p align="center"><b>Project Supervisors:</b> Gustavo Martín Vela & Pepe García</p>

<h2> Overview </h2>

<p> The H&M KPI Dashboard is a web-based application that presents a comprehensive overview of various Key Performance Indicators (KPIs) using real datasets from H&M. Especifically, the data is based on customers, articles, and transactions data. By employing a cloud-based architecture, the application fetches, filters, and displays KPI data in <b>real-time</b>.<p>

The project is built from four components:

1. A frontend built with Streamlit, which allows users to register and login, but most importantly to view and manipulate data visualizations regarding the customers, articles, and transactions data. Additionally, there is a .streamlit config folder which personalizes the theme of the application.
2. A backend API built with Flask, which handles user authentication and serves data to the frontend from the database in JSON format via HTTP GET requests.
3. Google Cloud SQL-based MySQL database with four tables: customers, articles, transactions, and users (containing the credentials for login information).
4. User authentication and registration, which stores user information in the users table within database and verifies credentials during login.

Both the frontend and backend are hosted on Google App Engine, ensuring a seamless link between the two components. To reduce loading times, the application limits the number of rows retrieved to 1000 rows each. 

<p><b>Please beware</b> that the link doesn't apply the registration and login. However, by running the application locally, the code does include this two features.<p>


<h2>🔗 Project Links and User Credentials </h2>

Links:
- **Analytics Dashboard** - https://frontend-dot-starry-iris-377408.oa.r.appspot.com/
- **API Endpoints** - https://api-dot-starry-iris-377408.oa.r.appspot.com/

In order to access the dashboard, please use one of the profiles below:

| Username  | Password |
| ------------- | ------------- |
| pepegarcia  | python |
| gustavo  | capstone  |
| adrianmarino  | willywonka  |

Keep in mind that locally you can add more profiles to the database.

<h2>💻 Technology Stack </h2>

Python, SQL, Flask, Streamlit, Pandas, Google App Engine, MySQL.


<h2>🏃 How to Run the Project Locally</h2>

1. Clone the repository:

```
git clone https://github.com/sophieschaesberg/HnM-dashboard.git
```

2. Set up a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages for both frontend and backend:

```
cd frontend
pip install -r requirements.txt
cd ../backend
pip install -r requirements.txt
```

4. Run the Flask API:

```
cd backend
python api.py
```

5. In another terminal, run the Streamlit front-end:

```
cd frontend
streamlit run streamlit.py
```

<h2>📊 Datasets </h2>

The datasets consist of data related with Customers, Transactions, and Articles. Each of the datasets contain their own columns, briefly explained below:

- **Customers dataset** featuringcustomer_id, FN, Active, club_member_status, fashion_news_frequency, age, and postal_code.

- **Transactions dataset** featuring t_dat, customer_id, article_id, price, and sales_channel_id.

- **Articles dataset** featuring article_id, product_code, prod_name, product_type_name, colour_group_name, department_name, index_group_name, and section_name.

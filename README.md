***Install Dependencies***

First, you'll need to install the necessary dependencies by running the following command in your terminal:
pip install flask flask-mysql
This will install the Flask web framework and the Flask-MySQL extension for connecting to a MySQL database.


***Create a Database Connection***

Create a connection to your MySQL database using ***db.by***.


***Create the API Endpoints***

Create the API endpoints for retrieving the Bank List and its branch details for a specific branch using ***app.py***.

Two API endpoints are defined in this code: one returns the Bank List, while the other returns branch-specific information. 
The server does a MySQL database query and returns the results in JSON format when the endpoints are reached via a GET request.

***Run the Server***


To start the server, simply run the following command in your terminal: ***python app.py***





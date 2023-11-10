# REST-APIs with Flask, Postman and PostgreSQL
Develop a RESTful API system using Flask, where Postman serves as the client for
conducting CRUD (Create, Read, Update, Delete) operations. The system efficiently
processes HTTP requests from Postman, directs them to Flask API endpoints, and
executes corresponding database queries in PostgreSQL for seamless data management.

# Architecture & Workflow:
1. Postman Request: Postman (Client) sends HTTP requests to the Flask API
(Server) using different HTTP methods (GET, POST, PUT, DELETE)
2. Flask API Processing: The Flask API receives and processes the request
3. Database Interaction: The Flask API interacts with the PostgreSQL database. It
performs CRUD operations (Create, Read, Update, Delete) on the database as
needed
4. No Database Response: In this flow, you don't expect a specific response from
the database
5. Flask API Response: The Flask API sends an HTTP response back to Postman
6. Postman Response: Postman displays the HTTP response received from the
Flask API.

# HTTPS Status Code
200 (OK): The request was successful.  
201 (Created): A new resource was successfully created.  
404 (Not Found): The requested resource was not found.  
400 (Bad Request): The request was malformed or had invalid data.  
500 (Internal Server Error): An unexpected server error occurred.   



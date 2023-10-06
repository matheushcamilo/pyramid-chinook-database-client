# pyramid-chinook-database-client
A client for Chinook demo database to test pyramid's base functionalities

## How to run
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Run `initialize_tutorial_db development.ini` to create and populate a local sqlite database
5. Run `pserve development.ini` to start the server
6. Run `pytest --ini=development.ini` to run the tests
7. Run `pytest --cov=tests --ini=development.ini` to check the coverage
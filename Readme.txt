To run the application go to the project directory and enter:
	docker build -t my-fastapi-app .
Then enter:
	docker run -d -p 8000:8000 my-fastapi-app
You should be able to access the API at http://localhost:8000.
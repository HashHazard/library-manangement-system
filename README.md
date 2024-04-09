# Library Management System Backend API

Welcome to the backend API for the Library Management System built on FastAPI and MongoDB.

## API Documentation

You can find the detailed API documentation [here](https://library-manangement-system.onrender.com/docs) which includes endpoints, request and response formats, and examples.

## Technologies Used

- **FastAPI**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **MongoDB**: MongoDB is a NoSQL database used for storing and managing library data efficiently.
- **Render**: The backend API is hosted on Render at [library-manangement-system.onrender.com](https://library-manangement-system.onrender.com).

## Setup

To set up the backend API locally for development or testing purposes, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/HashHazard/library-management-system-backend.git
   ```

2. Install dependencies:

   ```bash
   cd library-management-system-backend
   pip install -r requirements.txt
   ```

3. Configure environment variables:

   ```bash
   export DB_URL=<your_mongodb_uri>
   export DB_NAME=<your_database_name>
   ```

4. Run the server:

   ```bash
   python3 main.py
   ```

5. The API should now be accessible at `http://0.0.0:8000`.

## Deployment

The backend API is deployed on Render at [library-manangement-system.onrender.com](https://library-manangement-system.onrender.com). You can deploy your own instance of the API by following the Render documentation.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or issues related to the Library Management System backend API. Happy coding! 📚🚀

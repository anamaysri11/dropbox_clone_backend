# Dropbox Clone Backend

Welcome to the backend repository of the Dropbox Clone application! This project is built using Django and Django REST Framework, providing a robust and scalable backend to handle file uploads, downloads, and management. The backend is containerized using Docker and utilizes a MySQL database for data persistence.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

The Dropbox Clone Backend is designed to handle file storage and management functionalities, including:

- **File Upload:** Allows users to upload files to the server.
- **File Listing:** Provides endpoints to list all uploaded files.
- **File Download:** Enables users to download specific files.
- **File Deletion:** Allows deletion of uploaded files.
- **File Categorization:** Organizes files into categories like Photos, Shared, and Documents.

This backend serves as the foundation for the frontend application, ensuring seamless interaction and data management.

---

## Features

- **RESTful API:** Built with Django REST Framework for scalable and maintainable API endpoints.
- **File Management:** Supports uploading, listing, downloading, and deleting files.
- **Content-Type Validation:** Ensures only supported file types are uploaded.
- **Dockerized Setup:** Simplifies deployment and environment setup using Docker and Docker Compose.
- **MySQL Database:** Utilizes MySQL for reliable and efficient data storage.
- **CORS Configured:** Allows cross-origin requests from the frontend application.

---

## Technologies Used

- **Backend Framework:** Django 5.0.6
- **API Framework:** Django REST Framework
- **Database:** MySQL 8.0
- **Containerization:** Docker & Docker Compose
- **Environment Management:** python-decouple
- **Middleware:** django-cors-headers

---

## Prerequisites

Before setting up the backend, ensure you have the following installed on your system:

- **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Git:** [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dropbox_clone_backend.git
   cd dropbox_clone_backend
   ```

2. **Create Environment Variables**

   Create a `.env` file in the root directory to manage sensitive information.

   ```bash
   touch .env
   ```

   Add the following variables to the `.env` file:

   ```env
   DB_NAME=dropbox_clone_db
   DB_USER=dropbox_user
   DB_PASSWORD=securepassword
   DB_HOST=db
   DB_PORT=3306
   ```

   > **Note:** Ensure that `.env` is included in your `.gitignore` to prevent sensitive data from being exposed.

3. **Build and Start Docker Containers**

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers for the web application and MySQL database.

4. **Apply Migrations**

   In a new terminal window, run the following command to apply database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a Superuser (Optional)**

   To access the Django admin interface, create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser account.

---

## Configuration

### Environment Variables

The application uses environment variables for configuration. These variables are managed using `python-decouple` and are defined in the `.env` file.

- **DB_NAME:** Name of the MySQL database.
- **DB_USER:** MySQL database user.
- **DB_PASSWORD:** Password for the MySQL user.
- **DB_HOST:** Hostname for the MySQL database (service name defined in `docker-compose.yml`).
- **DB_PORT:** Port number for the MySQL database.

> **Important:** Do not expose your `.env` file or commit it to version control. Always keep it secure.

### CORS Configuration

The backend is configured to allow cross-origin requests from the frontend application running on `http://localhost:3000`. If your frontend is hosted on a different domain or port, update the `CORS_ALLOWED_ORIGINS` in `settings.py` accordingly.

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## Running the Application

### Starting the Backend

To start the backend application along with the MySQL database, navigate to the project directory and run:

```bash
docker-compose up --build
```

- **Web Service (`web`):** Runs the Django development server on `http://localhost:8000/`.
- **Database Service (`db`):** Runs MySQL server on `localhost:3306`.

### Stopping the Backend

To stop the running containers, press `Ctrl + C` in the terminal where `docker-compose` is running, then execute:

```bash
docker-compose down
```

---

## API Endpoints

The backend exposes the following API endpoints for file management:

### 1. **Upload File**

- **URL:** `/api/upload/`
- **Method:** `POST`
- **Description:** Uploads a new file to the server.
- **Request Body:**
  - `file`: The file to be uploaded (multipart/form-data).
- **Response:**
  - `201 Created` with the uploaded file details.
- **Example:**

  ```bash
  curl -X POST -F 'file=@/path/to/your/file.jpg' http://localhost:8000/api/upload/
  ```

### 2. **List All Files**

- **URL:** `/api/files/`
- **Method:** `GET`
- **Description:** Retrieves a list of all uploaded files.
- **Response:**
  - `200 OK` with an array of file objects.
- **Example:**

  ```bash
  curl http://localhost:8000/api/files/
  ```

### 3. **Retrieve File Details**

- **URL:** `/api/files/<id>/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific file by its ID.
- **Response:**
  - `200 OK` with the file object.
- **Example:**

  ```bash
  curl http://localhost:8000/api/files/1/
  ```

### 4. **Download File**

- **URL:** `/api/download/<id>/`
- **Method:** `GET`
- **Description:** Downloads the specified file by its ID.
- **Response:**
  - `200 OK` with the file content as an attachment.
- **Example:**

  ```bash
  curl -O http://localhost:8000/api/download/1/
  ```

### 5. **Delete File**

- **URL:** `/api/files/<id>/delete/`
- **Method:** `DELETE`
- **Description:** Deletes the specified file by its ID.
- **Response:**
  - `204 No Content` on successful deletion.
- **Example:**

  ```bash
  curl -X DELETE http://localhost:8000/api/files/1/delete/
  ```

---

## Models

### 1. **File**

Represents a file uploaded by the user.

- **Fields:**
  - `file`: `FileField` - The uploaded file.
  - `filename`: `CharField` - The name of the file.
  - `content_type`: `CharField` - The MIME type of the file.
  - `uploaded_at`: `DateTimeField` - Timestamp when the file was uploaded.
  - `shared`: `BooleanField` - Indicates if the file is shared (default: `False`).

- **String Representation:**
  - Returns the `filename`.

### 2. **UploadedFile**

Represents a file upload instance.

- **Fields:**
  - `filename`: `CharField` - The name of the file.
  - `content_type`: `CharField` - The MIME type of the file.
  - `uploaded_at`: `DateTimeField` - Timestamp when the file was uploaded.
  - `file`: `FileField` - The uploaded file.

- **String Representation:**
  - Returns the `filename`.

> **Note:** The `File` and `UploadedFile` models appear to have overlapping functionalities. Consider consolidating them into a single model to avoid redundancy unless they serve distinct purposes in your application.

---

## Usage

### Uploading a File

1. **Access the Upload Endpoint:**

   Navigate to `http://localhost:8000/api/upload/` using a tool like Postman or via frontend integration.

2. **Send a POST Request:**

   - **Method:** `POST`
   - **Headers:**
     - `Content-Type: multipart/form-data`
   - **Body:**
     - `file`: Select the file to upload.

3. **Receive Response:**

   On successful upload, you will receive a `201 Created` response with the file details.

### Listing All Files

1. **Access the List Endpoint:**

   Navigate to `http://localhost:8000/api/files/`.

2. **Send a GET Request:**

   - **Method:** `GET`

3. **Receive Response:**

   You will receive a `200 OK` response with an array of all uploaded files.

### Downloading a File

1. **Access the Download Endpoint:**

   Navigate to `http://localhost:8000/api/download/<id>/` where `<id>` is the ID of the file you wish to download.

2. **Send a GET Request:**

   - **Method:** `GET`

3. **Receive Response:**

   The file will be downloaded as an attachment.

### Deleting a File

1. **Access the Delete Endpoint:**

   Navigate to `http://localhost:8000/api/files/<id>/delete/` where `<id>` is the ID of the file you wish to delete.

2. **Send a DELETE Request:**

   - **Method:** `DELETE`

3. **Receive Response:**

   On successful deletion, you will receive a `204 No Content` response.

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the Repository**

   Click on the "Fork" button at the top-right corner of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/dropbox_clone_backend.git
   cd dropbox_clone_backend
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Changes**

   Implement your feature or bug fix.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add feature XYZ"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request**

   Navigate to the original repository and click on "Compare & pull request" to submit your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or support, please contact:

- **Name:** Your Name
- **Email:** your.email@example.com
- **GitHub:** [yourusername](https://github.com/yourusername)

---

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Heroicons](https://heroicons.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [react-tooltip](https://www.npmjs.com/package/react-tooltip)

---

**Thank you for using the Dropbox Clone Backend!**

---

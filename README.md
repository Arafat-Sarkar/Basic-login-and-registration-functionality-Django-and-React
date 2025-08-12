# Project: Basic User Authentication System

This project is a full-stack user authentication system with a **Django REST Framework** backend and a **React** frontend. It provides essential features like user registration, login, and logout.

---

## 1. Backend: Django REST Framework

The backend handles all user data management, authentication logic, and API endpoints.

### **Technologies Used**

* **Django**: The primary web framework.
* **Django REST Framework**: For building the RESTful API.
* **MySQL**: The database used to store user information.
* **`django-rest-framework-simplejwt`**: Provides JSON Web Tokens (JWTs) for secure, token-based authentication.

### **Key Features**

* **Registration**: A `UserSerializer` validates user data, and a `ViewSet` handles user creation, including password hashing.
* **Login & Token Management**:
    * The system uses `simplejwt`'s `TokenObtainPairView` to handle user login.
    * On successful login, it issues an access token and a refresh token.
* **Logout**: Logout functionality is handled on the client side by deleting the stored tokens.

---

## 2. Frontend: React

The frontend is a single-page application (SPA) that provides the user interface and interacts with the backend API.

### **Technologies Used**

* **React**: For building the user interface.
* **React Router**: Manages client-side navigation and protected routes.
* **Axios**: A library for making API requests to the backend.
* **Material-UI**: A component library for creating a modern and responsive design.

### **Authentication Flow**

1.  **Forms**: Material-UI is used to create user-friendly forms for registration and login.
2.  **API Communication**: **Axios** sends data to the Django API endpoints.
3.  **Token Storage**: Upon successful login, the received access and refresh tokens are stored in the browser's `localStorage`.
4.  **Protected Routes**: **React Router** checks for the presence of a token to protect certain routes, redirecting unauthenticated users to the login page.
5.  **Logout**: The logout function simply clears the tokens from `localStorage`, effectively logging the user out.

---

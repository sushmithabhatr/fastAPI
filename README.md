# FastAPI User Authentication API

A production-ready REST API built with **FastAPI**, featuring user registration, login, JWT-based authentication, and protected routes.

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Key Learnings](#key-learnings)

---

## Project Overview
This project demonstrates a secure user authentication system with token-based authorization. Users can register, log in, and access protected endpoints only if authenticated. The project includes input validation, password hashing, and error handling.

---

## Tech Stack
- **Backend:** Python 3.9, FastAPI  
- **Database:** SQLite (SQLAlchemy ORM)  
- **Authentication:** JWT tokens, OAuth2 password flow  
- **Password Security:** bcrypt via Passlib  
- **API Documentation:** Swagger UI (FastAPI built-in)  
- **Version Control:** Git & GitHub  
- **Optional Deployment:** Docker

---

## Features
1. **User Registration**
   - Endpoint: `POST /users/`
   - Accepts email and password
   - Hashes password and stores user in database

2. **User Login**
   - Endpoint: `POST /auth/login`
   - Verifies credentials
   - Returns JWT access token

3. **Protected Routes**
   - Endpoint: `GET /users/me`
   - Requires JWT token
   - Returns current user info

4. **Get All Users**
   - Endpoint: `GET /users/`
   - Requires JWT token
   - Returns list of all users

5. **Input Validation & Error Handling**
   - Uses Pydantic schemas
   - Returns proper HTTP status codes (`401`, `422`, `500`)

---
## Key Learnings

- Building APIs with **FastAPI** and async endpoints
- User authentication with **JWT** and OAuth2 password flow
- Password hashing using **bcrypt** with Passlib
- Database management with **SQLAlchemy ORM**
- Input validation and error handling using **Pydantic schemas**
- Dependency management, debugging, and version control with **Git/GitHub**

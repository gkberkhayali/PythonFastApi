### Backend
- Python
- FastAPI
- SQLAlchemy
- Uvicorn

### Frontend
- React
- JavaScript/TypeScript
- HTML/CSS
- REST API communication

### Database 
- PostgreSQL

# PythonFastApi

PythonFastApi is a full-stack web application built with a FastAPI backend and a React frontend. The project combines a modern Python API layer with a responsive client-side interface, creating a solid foundation for building and showcasing modern web applications.

## Overview

This project was developed to demonstrate how to build a modern full-stack application using Python on the backend and React on the frontend. The backend handles API logic, database access, and business rules, while the frontend provides an interactive user experience for working with the application.

## What I Built

In this project, I focused on creating a complete application foundation by:

- building a FastAPI-based backend
- configuring database connectivity with PostgreSQL and SQLAlchemy
- creating a React frontend for interacting with the application
- structuring the project in a way that can be extended with more features over time

## Project Purpose

The purpose of this project is to provide a practical example of a full-stack application where:

- the backend exposes API endpoints
- the frontend communicates with the backend
- data is stored and managed using a relational database
- the project can be expanded with additional features and functionality

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or newer installed
- Node.js and npm installed
- PostgreSQL installed and running locally

## Backend Setup

Clone the repository and install the Python dependencies:

```bash 
git clone https://github.com/gkberkhayali/PythonFastApi
cd PythonFastApi
python -m venv .myenv
.\.myenv\Scripts\Activate.ps1
pip install fastapi uvicorn sqlalchemy psycopg2-binary


## Frontend  Setup
cd frontend
npm install
npm start

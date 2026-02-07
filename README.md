# Car Dealership Review System (Full Stack Capstone)

A robust, full-stack web application for browsing car dealerships and posting reviews. Originally a microservice architecture, this project has been refactored into a streamlined **Django + React** monolith for improved performance, security, and ease of deployment.

## 🚀 Features

-   **Dealerships**: Browse a list of car dealerships with filtering by state.
-   **Details**: View detailed information about each dealership and read customer reviews.
-   **Reviews**: Authenticated users can post reviews with sentiment analysis (integrated or simulated).
-   **Authentication**: Secure Login and Registration system.
-   **Responsive Design**: Built with React for a dynamic and responsive user interface.

## 🛠️ Tech Stack

-   **Backend**: Django (Python)
    -   Django REST Framework (JSON responses)
    -   SQLite Database (Migrated from MongoDB)
-   **Frontend**: React.js
    -   Create React App
    -   React Router v6
-   **Styling**: CSS / Bootstrap (via class names)

## 📦 Installation & Setup

### Prerequisites
-   Python 3.8+
-   Node.js & npm

### 1. Clone the Repository
```bash
git clone https://github.com/Yaswanth1832K/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Backend Setup
Navigate to the server directory and install Python dependencies.
```bash
cd server
pip install -r requirements.txt
pip install Django Pillow requests python-dotenv
```

Run database migrations and seed initial data (Dealerships & Reviews).
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```

Start the Django server.
```bash
python manage.py runserver
```
The backend will run at `http://127.0.0.1:8000`.

### 3. Frontend Setup
Open a new terminal, navigate to the frontend directory, and install dependencies.
```bash
cd server/frontend
npm install
```

Start the React development server.
```bash
npm start
```
The app will open at `http://localhost:3000`.

## 📂 Project Structure

-   `server/djangoapp`: Core Django app containing Models, Views, and URLs.
-   `server/djangoapp/models.py`: Database models for `Dealership` and `Review`.
-   `server/djangoapp/management/commands/seed_data.py`: Script to populate DB from JSON.
-   `server/frontend/src/components`: React components (`Dealers`, `Dealer`, `PostReview`, `Login`, `Register`).

## 🛡️ Security Improvements
-   **Secrets Management**: `SECRET_KEY` and debug settings moved to `.env` file (not committed).
-   **Data Integrity**: Migrated raw JSON data into a relational SQLite database with proper foreign keys.
-   **API Security**: Backend serves as the single source of truth, removing fragile external microservice calls.

## 🤝 Contributing
1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

# Steady Course Fitness

Steady Course Fitness is a Flask-based web application designed to help users track their weight loss journey and build custom exercise plans. With a clean, navy-themed interface inspired by maritime navigation, users can register, set weight goals, and explore a database of exercises to add to their personal training regimen.

## Features

* **User Authentication**: Securely register and login to manage personal fitness data.
* **Goal Tracking**: Set a goal weight and update your current weight to see exactly how many "pounds to go" remain on your journey.
* **Exercise Database**: Browse a library of foundational exercises across categories like Lower-Body, Upper-Body, Cardio, and Full-Body.
* **Custom Training Plans**: Select specific exercises from the database to build a personalized workout list.
* **Responsive Design**: A mobile-friendly interface styled with a custom theme using modern CSS grid and flexbox layouts.

## Project Structure

The application is built with a modular Python backend and a template-driven frontend:

* **`main.py`**: The core Flask application containing all route definitions and business logic.
* **`auth_handler.py`**: Manages user registration, authentication, and local data persistence in `users.json`.
* **`data.py`**: Serves as the exercise database, providing details and categorized information for each movement.
* **`templates/`**: HTML templates using Jinja2 inheritance for a consistent layout.
* **`static/`**: Contains the custom CSS stylesheet and high-quality exercise imagery.

## Technical Requirements

* **Python 3.x**
* **Flask**: The primary web framework.

## Getting Started

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the application**:
    ```bash
    python main.py
    ```
3.  **Access the app**: Open your browser and navigate to `http://127.0.0.1:5000/`.

## Credits

Exercise imagery is sourced from Unsplash contributors. All icons and logos were custom-created using Inkscape.
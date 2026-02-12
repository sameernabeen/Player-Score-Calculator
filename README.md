# Game Score Calculator

A Python project demonstrating fundamental programming concepts and simple web application development using Flask. This project includes both a command-line interface (CLI) script and a web-based calculator.

## Features

- **CLI Version**: Run a script in your terminal to input player details and calculate the average score.
- **Web App Version**: A user-friendly web interface built with Flask to perform the same calculations in a browser.
- **Input Handling**: Accepts player name, games played, and total score.
- **Error Handling**: Validates numeric inputs to prevent crashes.

## Prerequisites

- Python 3.x
- Flask (for the web application)

## Installation

1.  Clone the repository or download the source code.
2.  Navigate to the project directory:
    ```bash
    cd game_score_project
    ```
3.  Install the required dependencies:
    ```bash
    pip install flask
    ```

## Usage

### Command Line Interface (CLI)

Run the standalone script:

```bash
python game_score.py
```

Follow the prompts to enter the player's name, games played, and total score.

### Web Application

1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```
3.  Fill out the form and click "Calculate Average".

## Example Output

**Input:**
- Player: Alice
- Games Played: 10
- Total Score: 500

**Output:**
```
Player: Alice
Games Played: 10
Total Score: 500
Average Score: 50.0
```

## Project Structure

- `game_score.py`: Standalone CLI script.
- `app.py`: Flask application entry point.
- `templates/index.html`: HTML template for the web interface.

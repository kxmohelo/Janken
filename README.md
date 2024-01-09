# Janken Game

This is a simple Rock-Paper-Scissors game with a web interface using Python and Flask.

## How to Run the Game

1. Make sure you have Python installed on your machine. See [www.python.org](https://www.python.org).

2. Install the required packages:

    ```bash
    pip install Flask
    ```

3. Make sure the three hand images (`rock.png`, `paper.png`, and `scissors.png`) are in the `static` folder found in the project root directory.

4. Run the Flask app:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## How to Play

- Choose your hand by clicking on the respective hand image, then the game result will be displayed after the hand shake countdown.
- A **play again** button will show when the results are displayed - *to continue playing*.

## File Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: HTML template for the game interface.
- `static/`: Folder containing static files (hand images).

## Dependencies

- Flask: [https://pypi.org/project/Flask/](https://pypi.org/project/Flask/)

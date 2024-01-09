# Janken Game

This is a simple Rock-Paper-Scissors game with a web interface using Python and Flask.

## How to Run the Game

1. Make sure you have Python installed on your machine.

2. Install the required packages:

    ```bash
    pip install Flask
    ```

3. Save three hand images (`rock.png`, `paper.png`, and `scissors.png`) in a folder named `static` in the same directory as `app.py`.

4. Run the Flask app:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

6. Choose your hand by clicking on the respective image.

7. Two rock images will shake during the countdown, and then the game result will be displayed.

## File Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: HTML template for the game interface.
- `static/`: Folder containing static files (hand images).

## Dependencies

- Flask: [https://pypi.org/project/Flask/](https://pypi.org/project/Flask/)

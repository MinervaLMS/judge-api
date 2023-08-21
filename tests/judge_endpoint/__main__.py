"""Run flask app for testing."""

from . import create_app

app = create_app()

if __name__ == "__main__":  # Only in dev
    app.run(host="0.0.0.0", port=8080, debug=True)  # nosec

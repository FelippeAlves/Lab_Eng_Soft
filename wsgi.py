import sys 

from src.main import app, init_db

if __name__ == "__main__":
    if 'init_db' in sys.argv:
        init_db(app)
    app.run(debug=False)
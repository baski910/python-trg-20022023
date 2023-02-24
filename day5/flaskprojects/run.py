from app import db,create_app

from app.resources import BookListResource

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
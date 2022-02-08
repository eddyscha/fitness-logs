from api.api import create_app

from db.base import Session, engine, Base


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()

    app = create_app()

    app.run(debug=True)

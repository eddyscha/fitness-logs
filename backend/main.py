from api.api import create_app

from db.base import Session, engine, Base
from db.activity import Activity
from db.logs import Logs

Base.metadata.create_all(engine)
session = Session()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

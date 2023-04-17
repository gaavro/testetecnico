import json
import pytest
from app import create_app, db
from models import Expression


@pytest.fixture
def client():
    app = create_app("testing")
    app_context = app.app_context()
    app_context.push()

    with app.test_client() as client:
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_avaliar_expression(client):
    expression = Expression(expression="(x OR y) AND z")
    db.session.add(expression)
    db.session.commit()

    response = client.get("/avaliar/1?x=1,y=0,z=1")
    assert response.status_code == 200
    assert json.loads(response.data) == {"result": True}


def test_listar_expression(client):
    expression1 = Expression(expression="(x OR y) AND z")
    expression2 = Expression(expression="(x OR y) OR z")
    db.session.add_all([expression1, expression2])
    db.session.commit()

    response = client.get("/expressoes")
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "expressoes": [
            {"id": 1, "expression": "(x OR y) AND z"},
            {"id": 2, "expression": "(x OR y) OR z"}
        ]
    }








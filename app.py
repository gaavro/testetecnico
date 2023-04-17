from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from .models import Expression

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/expressoes', methods=['GET'])
def listar_expressoes():
    expressoes = Expression.query.all()
    return jsonify([{'id': e.id, 'expressao': e.expression} for e in expressoes])

@app.route('/expressoes', methods=['POST'])
def criar_atualizar_expressao():
    if not request.json or 'expressao' not in request.json:
        abort(400)
    expressao = request.json['expressao']
    e = Expression.query.filter_by(expression=expressao).first()
    if e:
        e.expression = expressao
        db.session.commit()
        return jsonify({'id': e.id, 'expressao': e.expression})
    else:
        nova_expressao = Expression(expression=expressao)
        db.session.add(nova_expressao)
        db.session.commit()
        return jsonify({'id': nova_expressao.id, 'expressao': nova_expressao.expression})

@app.route('/expressoes/<int:expression_id>', methods=['DELETE'])
def excluir_expressao(expression_id):
    e = Expression.query.get(expression_id)
    if e:
        db.session.delete(e)
        db.session.commit()
        return jsonify({'mensagem': 'Expressão excluída com sucesso'})
    else:
        abort(404)

@app.route('/avaliar/<int:expression_id>', methods=['GET'])
def avaliar_expressao(expression_id):
    e = Expression.query.get(expression_id)
    if e:
        x = request.args.get('x')
        y = request.args.get('y')
        z = request.args.get('z')
        try:
            resultado = eval(e.expression, {'x': int(x), 'y': int(y), 'z': int(z)})
        except:
            abort(400)
        return jsonify({'resultado': resultado})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

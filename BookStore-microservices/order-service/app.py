from flask import Flask
from extensions import db
from controllers.order_controller import order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bookstore_user:bookstore_pass@<DB_HOST>:3306/bookstore'

db.init_app(app)
app.register_blueprint(order, url_prefix='/order')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5003, debug=True)

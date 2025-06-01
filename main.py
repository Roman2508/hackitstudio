from flask import Flask, request, session, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()


db = SQLAlchemy(app)


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    photo = db.Column(db.String(), nullable=False)
    mileage = db.Column(db.Integer(), nullable=False)
    engine = db.Column(db.Integer(), nullable=False)
    color = db.Column(db.String(), nullable=False)
    transmission = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.Date(), default=datetime.utcnow)

    def __init__(self, title, description, price, photo, mileage, engine, color, transmission):
        self.title = title
        self.description = description
        self.price = price
        self.photo = photo
        self.mileage = mileage
        self.engine = engine
        self.color = color
        self.transmission = transmission


# db.create_all()


@app.route('/', methods=["GET"])
def get_home():
    return render_template('index.html')


@app.route('/catalog', methods=["GET"])
def get_catalog():
    return render_template('catalog.html')


@app.route('/create-ad', methods=["GET"])
def get_create_ad():
    return render_template('create-ad.html')


@app.route('/create-ad', methods=["POST"])
def create_ad():
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    photo = request.form['photo']
    mileage = request.form['mileage']
    engine = request.form['engine']
    color = request.form['color']
    transmission = request.form['transmission']

    row = Car(title, description, price, photo,
              mileage, engine, color, transmission)
    db.session.add(row)
    db.session.commit()

    return render_template('create-ad.html')


if __name__ == "__main__":
    app.run()

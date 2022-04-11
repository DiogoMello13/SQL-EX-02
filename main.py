
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(30))
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(100))
  image = db.Column(db.String(100)) 
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

contatos=[
  {'name': 'João da Silva' , 'email': 'joao@gmail.com', 'phone': '(16) 99922-1122'},
  {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16) 99922-3333'},
]


@app.route('/')
def index():
  user = User.query.all()
  contacts = Contacts.query.all()
  return render_template('index.html', user=user, contacts=contacts, contatos=contatos)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contatos.append({
    'name': name, 'email': email, 'phone': phone
  })
  new_user = User(name=name, email=email)
  new_contacts = Contacts(name=name, email=email, phone=phone)
  db.session.add(new_user)
  db.session.add(new_contacts)
  db.session.commit()
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  contatos.pop(id)

  return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
  user = User.query.filter_by(id=id).first()
  user.complete = True
  db.session.commit()
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contatos[index]['name'] = name
  contatos[index]['email'] = email
  contatos[index]['phone'] = phone
  return redirect('/')
  user = User.query.filter_by(id=id).first()
  user.title = name
  db.session.commit()



if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)
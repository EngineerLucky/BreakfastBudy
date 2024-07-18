from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    menu_items = [
        {'name': 'Pancakes', 'price': 5.99},
        {'name': 'Waffles', 'price': 6.99},
        {'name': 'Omelette', 'price': 7.99}
    ]
    return jsonify(menu_items)

if __name__ == '__main__':
    app.run(debug=True)


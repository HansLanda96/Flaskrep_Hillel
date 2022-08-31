from flask import Flask
from utils import current_time, average_height_weight, show_requirements
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route('/')
@app.route('/index.html')
def hello():
    return f'<h1>Hello World!</h1><br>{current_time()} '


@app.route('/get_name')
def get_name():
    name = fake.first_name()
    last_name = fake.last_name()
    return f'Person: {name} {last_name}'


@app.route('/avg_data')
def average():
    avg_height = average_height_weight()[0]
    avg_weight = average_height_weight()[1]
    return f'<h2>Average height of all students: <tt>{avg_height}cm</tt>' \
           f'<br><br>Average weight of all students: <tt>{avg_weight}kg</tt></h2>'


@app.route('/requirements')
def requirements():
    return f'<head><h2>Requirements for project:</h2></head>' \
           f'<br><br><h3><cite>{show_requirements()}</cite></h3>'


if __name__ == '__main__':
    app.run(debug=True, port=5050)

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/student/')
def student():
    students = [
        {'name': 'Антон', 'surname': 'Кабаков', 'age': 30, 'grade': 5},
        {'name': 'Алексей', 'surname': 'Федорин', 'age': 34, 'grade': 4},
        {'name': 'Игорь', 'surname': 'Леонтьев', 'age': 20, 'grade': 3}
    ]
    context= {'students': students}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
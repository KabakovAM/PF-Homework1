from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context= {'title': 'Домашняя'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes():
    context= {'title': 'Одежда'}
    return render_template('clothes.html', **context)

@app.route('/footwear/')
def footwear():
    context= {'title': 'Обувь'}
    return render_template('footwear.html', **context)

@app.route('/jacket/')
def jacket():
    context= {'title': 'Куртка'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
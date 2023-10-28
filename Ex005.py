from flask import Flask

app = Flask(__name__)

@app.route('/get-html/')
def get_html():
    return """
    <h1>Моя первая HTML страница</h1>
    <p>Привет, мир!</p>
    """

if __name__=='__main__':
    app.run(debug=True)
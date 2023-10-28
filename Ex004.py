from flask import Flask

app = Flask(__name__)

@app.route('/<string:row>/')
def row_length(row):
    return str(len(row))

if __name__=='__main__':
    app.run(debug=True)
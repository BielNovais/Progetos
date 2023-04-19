from flask import Flask, jsonify

app = Flask(__name__)

@app.router('/api/get_data', methods=['GET'])
def get_data():
    data = ('Boa noite, professor')
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
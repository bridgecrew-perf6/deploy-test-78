import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    datapath = os.environ.get("DATA_PATH")
    with open(datapath) as f:
        data = f.readlines()
        return f"""
        <p>Read data:</p>
        <p>{data}</p>
        """


if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

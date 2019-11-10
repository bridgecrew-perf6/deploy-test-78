import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    datapath = os.environ.get("DATA_PATH")
    with open(datapath) as f:
        data = f.readlines()

        result = "<table border='1px solid black'><tr>"
        for col in data[0].split(","):
            result += f"<th>{col}</th>"
        result += "</tr>"

        for row in data[1:]:
            result += "<tr>"
            for cell in row.split(","):
                result += f"<td>{cell}</td>"
            result += "</tr>"
        return result


if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

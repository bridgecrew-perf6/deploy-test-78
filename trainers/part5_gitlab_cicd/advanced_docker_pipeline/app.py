from flask import Flask, render_template, request
import datetime
from tools import calculator

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    today = datetime.date.today()
    return render_template(
        template_name_or_list="hello.html",
        name=request.args.get("name"),
        value=calculator.sum(today.year, today.month),
    )


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

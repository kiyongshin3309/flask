from flask import Flask, render_template, request, redirect, url_for
import hgtk
import time
from word_list import get_word_list

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_level = request.form.get("student_level")
        month = request.form.get("month")
        language = request.form.get("language")

        return redirect(url_for("typing", student_level=student_level, month=month, language=language))

    return render_template("index.html")

@app.route("/typing")
def typing():
    student_level = request.args.get("student_level", "초등학생")
    month = request.args.get("month", "1월")
    language = request.args.get("language", "한글")

    word_list = get_word_list(student_level, month, language)

    return render_template("typing.html", word_list=word_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

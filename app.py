from flask import Flask, request, redirect, render_template

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos, enumerate=enumerate)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo")
    todos.append(todo)
    return redirect("/")

@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    del todos[index]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

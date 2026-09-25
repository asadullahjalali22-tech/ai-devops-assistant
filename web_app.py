from flask import Flask, request, render_template_string
from agents.planner import create_plan

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>AI DevOps Assistant</title>
</head>
<body>

<h1>AI DevOps Assistant</h1>

<form method="POST">
    <label>DevOps Task:</label><br><br>

    <input
        type="text"
        name="task"
        style="width: 400px;"
        placeholder="Create a simple S3 static website"
        required
    >

    <button type="submit">
        Create Plan
    </button>
</form>

{% if plan %}
<hr>

<h2>Planner Agent</h2>

<ol>
{% for step in plan %}
    <li>{{ step }}</li>
{% endfor %}
</ol>

{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    plan = None

    if request.method == "POST":
        task = request.form["task"]
        plan = create_plan(task)

    return render_template_string(
        HTML,
        plan=plan
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

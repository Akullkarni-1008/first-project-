from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Echo</title>
<p>{{ user_input }}</p>  {# Auto-escaped by Jinja2 #}
"""

@app.route("/echo")
def echo():
    user_input = request.args.get("q", "")
    return render_template_string(TEMPLATE, user_input=user_input)

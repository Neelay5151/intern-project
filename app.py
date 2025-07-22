from flask import Flask, request, render_template_string
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>Bengaluru House Data Viewer</title>
<h2>Upload the Bengaluru_House_Data.csv file</h2>
<form action="/" method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if tables %}
  <h3>Preview of Dataset</h3>
  {{ tables|safe }}
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    tables = None
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith(".csv"):
            df = pd.read_csv(file)
            tables = df.head().to_html(classes='data', header="true", index=False)
    return render_template_string(HTML_TEMPLATE, tables=tables)

if __name__ == "__main__":
    app.run(debug=True)

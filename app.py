from flask import Flask, render_template, send_from_directory
from student_analysis import load_and_analyze, make_charts, save_report

app = Flask(__name__)

# Load student data
df = load_and_analyze()

# Generate charts and Excel report
make_charts(df)
save_report(df)


@app.route("/")
def home():
    return render_template(
        "index.html",
        students=df.to_dict(orient="records")
    )


@app.route("/download-report")
def download_report():
    report_path = save_report(df)

    return send_from_directory(
        report_path.parent,
        report_path.name,
        as_attachment=True
    )


@app.route("/refresh")
def refresh():
    global df

    df = load_and_analyze()
    make_charts(df)
    save_report(df)

    return render_template(
        "index.html",
        students=df.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)
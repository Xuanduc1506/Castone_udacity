from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<h2>Hello my name is Nguyễn Xuân Đức. This is my capstone project about Uda_devops</h2>"
    return html.format(format)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

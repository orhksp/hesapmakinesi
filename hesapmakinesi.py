from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            expression = request.form["expression"]
            # Güvenlik için eval yerine safer eval kullanılabilir
            result = eval(expression)
        except Exception:
            result = "Hata: Geçerli bir ifade giriniz!"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

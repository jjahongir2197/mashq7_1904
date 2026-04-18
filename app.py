from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():

    result = ""

    if request.method == "POST":

        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "Underweight"

        elif bmi < 25:
            status = "Normal"

        else:
            status = "Overweight"

        result = f"BMI: {round(bmi,2)} ({status})"

    return render_template(
        "bmi.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)

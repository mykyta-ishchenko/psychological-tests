from flask import Blueprint, redirect, render_template, request

from forms.emotional_burnout_boyko.form import Form as FormEBB
from forms.ost_rusalov.form import Form as FormOSTR
from wokrer import Worker

routes = Blueprint("route", __name__)

worker = Worker(
    FormEBB(),
    FormOSTR(),
)


@routes.route("/test/<test_name>", methods=["POST", "GET"])
def test(test_name: str):
    form = worker.get(test_name)

    if not form:
        return redirect("/")

    if request.method == "POST":
        result = form.process_result(request.form.to_dict())
        return render_template("result.html",
                               label=form.display_name,
                               response=result,
                               info=form.info
                               )

    return render_template("test.html",
                           form=form,
                           )


@routes.route("/")
def home():
    return render_template("home.html", label="Psychological tests", forms=worker.forms)

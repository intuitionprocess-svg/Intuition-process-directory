from flask import Flask, render_template, abort
import requests
import re

app = Flask(__name__)

API_URL = "https://ip-course-finder.onrender.com/api/courses"


def slug_to_name(slug):
    """aparna-atmaram → Aparna Atmaram"""
    return " ".join(part.capitalize() for part in slug.split("-"))


def fetch_teacher_courses(teacher_name):
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    courses = resp.json().get("courses", [])
    name_lower = teacher_name.lower()
    return [
        c for c in courses
        if any(t.lower() == name_lower for t in (c.get("teachers") or []))
    ]


@app.route("/<slug>")
def teacher_page(slug):
    if not re.match(r"^[a-z0-9-]+$", slug):
        abort(404)
    teacher_name = slug_to_name(slug)
    try:
        courses = fetch_teacher_courses(teacher_name)
    except Exception as e:
        return render_template("teacher.html", teacher=teacher_name, courses=[], error=str(e))
    if not courses and not any(True for _ in []):
        # Still render the page — teacher may exist but have no upcoming courses
        pass
    return render_template("teacher.html", teacher=teacher_name, courses=courses, error=None)


@app.route("/")
def index():
    abort(404)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5051))
    app.run(debug=False, host="0.0.0.0", port=port)

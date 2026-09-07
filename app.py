import  requests

from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


student = {
    "name": "",
    "grade": "",
    "section": "",
    "adviser": "",
    "profile_picture": ""
}

teacher = {
    "name": "",
    "subject": "",
    "grade": "",
    "section": ""
}

assignments = []
announcements =[]
materials =[]

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/role")
def role():
  return render_template("role.html")


@app.route("/student", methods=["GET", "POST"])
def student_page():

    if request.method == "POST":

        student["name"] = request.form.get("name")
        student["grade"] = request.form.get("grade")
        student["section"] = request.form.get("section")
        student["adviser"] = request.form.get("adviser")

        picture = request.files.get("profile_picture")

        if picture and picture.filename:

            filename = secure_filename(picture.filename)

            picture.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            student["profile_picture"] = filename

        return redirect(url_for("dashboard"))

    return render_template(
        "student.html",
        student=student
    )


@app.route("/dashboard")
def dashboard():
    total_assignments = len(assignments)

    completed_assignments = sum(
        1 for assignment in assignments
        if assignment.get("completed", False)
    )

    pending_assignments = total_assignments - completed_assignments

    if total_assignments > 0:
        progress = round((completed_assignments / total_assignments) * 100)
    else:
        progress = 0

    upcoming_assignments = sorted(
        assignments,
        key=lambda assignment: assignment.get("due_date", "")
    )

    return render_template(
        "dashboard.html",
        student=student,
        assignments=assignments,
        upcoming_assignments=upcoming_assignments,
        total_assignments=total_assignments,
        completed_assignments=completed_assignments,
        pending_assignments=pending_assignments,
        progress=progress,
        announcements=announcements
    )


@app.route("/complete-assignment/<int:assignment_id>", methods=["POST"])
def complete_assignment(assignment_id):
    if 0 <= assignment_id < len(assignments):
        assignments[assignment_id]["completed"] = not assignments[assignment_id].get("completed", False)

    return redirect(url_for("dashboard"))


@app.route("/materials", methods=["GET", "POST"])
def materials_page():
    if request.method == "POST":
        title = request.form.get("title")
        subject = request.form.get("subject")
        description = request.form.get("description")

        if title and subject and description:
            materials.append({
                "title": title,
                "subject": subject,
                "description": description
            })

        return redirect(url_for("materials_page"))

    return render_template(
        "materials.html",
        materials=materials
    )



@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    if request.method == "POST":
        title = request.form.get("title")
        subject = request.form.get("subject")
        due_date = request.form.get("due_date")
        description = request.form.get("description")

        assignment = {
            "title": title,
            "subject": subject,
            "due_date": due_date,
            "description": description,
            "completed": False
        }

        assignments.append(assignment)

        return redirect(url_for("calendar"))

    return render_template("calendar.html", assignments=assignments)

      



@app.route("/progress")
def progress_page():

    total_assignments = len(assignments)

    completed_assignments = sum(
        1 for assignment in assignments
        if assignment.get("completed", False)
    )

    pending_assignments = total_assignments - completed_assignments

    if total_assignments > 0:
        progress = round(
            (completed_assignments / total_assignments) * 100
        )
    else:
        progress = 0

    return render_template(
        "progress.html",
        total_assignments=total_assignments,
        completed_assignments=completed_assignments,
        pending_assignments=pending_assignments,
        progress=progress
    )
   




@app.route("/weather")
def weather():

    city = "Manila"

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 14.5995,
        "longitude": 120.9842,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "timezone": "Asia/Manila"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        data = response.json()

        current = data["current"]

        weather_data = {
            "city": city,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "code": current["weather_code"]
        }

    except Exception:

        weather_data = None

    return render_template(
        "weather.html",
        weather=weather_data
    )



@app.route("/games")
def games():

    
    return render_template("games.html")
@app.route("/teacher-profile", methods=["GET", "POST"])
def teacher_profile():

    if request.method == "POST":

        teacher["name"] = request.form.get("name")
        teacher["subject"] = request.form.get("subject")
        teacher["grade"] = request.form.get("grade")
        teacher["section"] = request.form.get("section")

        return redirect(url_for("teacher_page"))

    return render_template(
        "teacher_profile.html",
        teacher=teacher
    )

@app.route("/teacher")
def teacher_page():

    total_assignments = len(assignments)

    completed_assignments = sum(
        1 for assignment in assignments
        if assignment.get("completed", False)
    )

    pending_assignments = total_assignments - completed_assignments

    return render_template(
        "teacher.html",
        total_assignments=total_assignments,
        completed_assignments=completed_assignments,
        pending_assignments=pending_assignments
    )
@app.route("/class-info")
def class_info():
    return render_template("class_info.html")
@app.route("/schedule")
def schedule():
    return render_template("schedule.html")
@app.route("/announcements", methods=["GET", "POST"])
def announcements_page():
    if request.method == "POST":
        title = request.form.get("title")
        message = request.form.get("message")

        if title and message:
            announcements.append({
                "title": title,
                "message": message
            })

        return redirect(url_for("announcements_page"))

    return render_template(
        "announcements.html",
        announcements=announcements
    )

@app.route("/task-tracker")
def task_tracker():
    total = len(assignments)

    completed = sum(
        1 for assignment in assignments
        if assignment.get("completed", False)
    )

    pending = total - completed

    return render_template(
        "task_tracker.html",
        assignments=assignments,
        total=total,
        completed=completed,
        pending=pending
    )

if __name__ == "__main__":
    app.run(debug=True)



    

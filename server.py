from flask import Flask


app = Flask(__name__) #insance of Flask called Dunder method


@app.route("/", methods=["GET"])
def index():
    return "Welcome to FLASK framework!"


@app.route("/cohort61", methods=["GET"])
def cohort61():
    students_list = [
        "Micah", 
        "Jeuan", 
        "Brant", 
        "Mat", 
        "Leo", 
        "Eric"
    ]
    return students_list


@app.route("/cohort100", methods=["GET"])
def cohort100():
    students_list = [
        "Bob", 
        "Brandon", 
        "Eve", 
        "Grace"
    ]
    return students_list


@app.route("/contact", methods=["GET"])
def contact():
    information = {
        "email": "Janedoe929@email.com", 
        "phone": "555-525-5555"
    }
    return information


@app.route("/course", methods=["GET"])
def course():
    course_information = {
        "title": "Intro with API Flask", 
        "duration": "4 Sessions", 
        "level": "Beginner"
    }
    return course_information


@app.route("/user", methods=["GET"])
def user():
    user_info = {
        "name": "Micah", 
        "role": "Fullstack developer",
        "is_active": True,
        "favorite_technologies": ["React", "JavaScript", "Python"]
    }
    return user_info


#--------Coupons----------


coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


@app.route("/api/coupons", methods=["GET"])
def coupon_list():

    return coupons


@app.route("/api/coupons/count", methods=["GET"])
def coupon_count():

    return {"count": len(coupons)}


if __name__ == "__main__":
    app.run(debug=True)
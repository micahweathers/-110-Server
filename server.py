from flask import Flask, jsonify, request
from http import HTTPStatus


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


#Session3
#Path paramters

@app.route("/greet/<string:name>")
def greet(name):
    return f"Hiya {name}"


student_names = ["Micah", "Jeuan", "Brant", "Mat"]


@app.route("/students", methods=["POST"])
def add_student():
    student_names.append("Eric")
    return student_names


products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 299.00,
        "category": "entertainment",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.00,
        "category": "kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 99.00,
        "category": "electronics",
        "image": "https://picsum.photos/seed/3/300/300"
    }
]
#GET api/products endpoint returns list of products


@app.route("/api/products", methods=["GET"])
def product_list():

    return jsonify({
        "success": True,
        "message": "Products retrieved",
        "data": products
        }), HTTPStatus.OK #200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):

    print(product_id)
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product Retrieved",
                "data": product
            })

    return jsonify({
        "success": False,
        "message": "Not a valid ID number."
    }), HTTPStatus.NOT_FOUND


#POST /api/products


@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    new_product["_id"] = len(products) + 1
    products.append(new_product)

    return jsonify({
        "success": True,
        "message": "Product Created",
        "data": new_product
    }), HTTPStatus.CREATED

#--------Coupons----------


coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


@app.route("/api/coupons", methods=["GET"])
def coupon_list():

    return jsonify({"coupons": coupons})


@app.route("/api/coupons/count", methods=["GET"])
def coupon_count():

    return jsonify({"count": len(coupons)})
#Assignment 3 get coupon by id, create coupon


@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):

    print(coupon_id)
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "Coupon Retrieved",
                "data": coupon
            })

    return jsonify({
        "success": False,
        "message": "Not a valid ID number."
    }), HTTPStatus.NOT_FOUND


@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    new_coupon["_id"] = len(coupons) + 1
    coupons.append(new_coupon)

    return jsonify({
        "success": True,
        "message": "Coupon Created",
        "data": new_coupon
    }), HTTPStatus.CREATED


if __name__ == "__main__":
    app.run(debug=True)
import os
from flask import Flask, render_template, request, redirect, url_for, make_response
from datetime import datetime
from functools import wraps, update_wrapper
from shutil import copyfile
from hand_gesture_control import hand_gesture_control_bp
import image_processing

app = Flask(__name__)
app.register_blueprint(hand_gesture_control_bp, url_prefix='/hand_gesture_control')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

@app.route("/index")
@app.route("/")
@nocache
def index():
    return render_template("uploaded.html", file_path="img/image_here.jpg")

@app.route("/about")
@nocache
def about():
    return render_template('about.html')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/upload", methods=["POST"])
@nocache
def upload():
    target = os.path.join(APP_ROOT, "static/img")
    if not os.path.isdir(target):
        os.makedirs(target)
    for file in request.files.getlist("file"):
        file.save("static/img/img_now.jpg")
    copyfile("static/img/img_now.jpg", "static/img/img_normal.jpg")
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/normal", methods=["POST"])
@nocache
def normal():
    copyfile("static/img/img_normal.jpg", "static/img/img_now.jpg")
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/grayscale", methods=["POST"])
@nocache
def grayscale():
    image_processing.grayscale()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/zoomin", methods=["POST"])
@nocache
def zoomin():
    image_processing.zoomin()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/zoomout", methods=["POST"])
@nocache
def zoomout():
    image_processing.zoomout()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/move_left", methods=["POST"])
@nocache
def move_left():
    image_processing.move_left()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/move_right", methods=["POST"])
@nocache
def move_right():
    image_processing.move_right()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/move_up", methods=["POST"])
@nocache
def move_up():
    image_processing.move_up()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/move_down", methods=["POST"])
@nocache
def move_down():
    image_processing.move_down()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/brightness_addition", methods=["POST"])
@nocache
def brightness_addition():
    image_processing.brightness_addition()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/brightness_substraction", methods=["POST"])
@nocache
def brightness_substraction():
    image_processing.brightness_substraction()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/brightness_multiplication", methods=["POST"])
@nocache
def brightness_multiplication():
    image_processing.brightness_multiplication()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/brightness_division", methods=["POST"])
@nocache
def brightness_division():
    image_processing.brightness_division()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/histogram_equalizer", methods=["POST"])
@nocache
def histogram_equalizer():
    image_processing.histogram_equalizer()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/edge_detection", methods=["POST"])
@nocache
def edge_detection():
    image_processing.edge_detection()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/blur", methods=["POST"])
@nocache
def blur():
    image_processing.blur()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/sharpening", methods=["POST"])
@nocache
def sharpening():
    image_processing.sharpening()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/histogram_rgb", methods=["POST"])
@nocache
def histogram_rgb():
    image_processing.histogram_rgb()
    if image_processing.is_grey_scale("static/img/img_now.jpg"):
        return render_template("histogram.html", file_paths=["img/grey_histogram.jpg"])
    else:
        return render_template("histogram.html", file_paths=["img/red_histogram.jpg", "img/green_histogram.jpg", "img/blue_histogram.jpg"])
    
@app.route("/dilasi", methods=["POST"])
@nocache
def dilasi():
    image_processing.dilasi()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/erosi", methods=["POST"])
@nocache
def erosi():
    image_processing.erosi()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/opening", methods=["POST"])
@nocache
def opening():
    image_processing.Opening()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/closing", methods=["POST"])
@nocache
def closing():
    image_processing.Closing()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/count_white_objects", methods=["POST"])
@nocache
def count_white_objects():
    num_object = image_processing.count_white_objects()
    return render_template("uploaded.html", file_path="img/img_now.jpg", num_object=num_object)

@app.route("/identifikasi_number", methods=["POST"])
@nocache
def indent_citra():
    num_object = image_processing.indent_citra()
    return render_template("uploaded.html", file_path="img/img_now.jpg", num_object=num_object)

@app.route("/training_data", methods=["POST"])
@nocache
def training_data():
    image_processing.training_data()
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route("/deteksi_emoji", methods=["POST"])
@nocache
def deteksi_emoji():
    num_object = image_processing.deteksi_emoji()
    return render_template("uploaded.html", file_path="img/img_now.jpg", num_object=num_object)

@app.route("/thresholding", methods=["POST"])
@nocache
def thresholding():
    lower_thres = int(request.form['lower_thres'])
    upper_thres = int(request.form['upper_thres'])
    image_processing.threshold(lower_thres, upper_thres)
    return render_template("uploaded.html", file_path="img/img_now.jpg")

@app.route('/hand_gesture_page')
def hand_gesture_page():
    return render_template('hand_gesture_page.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, render_template

import map

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('finder_main.html')

@app.route('/find/<category>')
def potatoes(category):
    map_html = map.district_marker(category)

    return render_template('find_winterSnack.html', map_html=map_html)

@app.route('/find/<category>/<district>')
def potatoes_district(category, district):
    map_html = map.detail_marker(category, district)

    return render_template('find_winterSnack.html', map_html=map_html)

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == '__main__':
    app.run(debug=True)
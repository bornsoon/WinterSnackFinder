from flask import Flask, render_template, jsonify

import map
import urllib.parse

app = Flask(__name__)

name = {'bungeoppang': '붕어빵 찾기', 'sweetpotato': '고구마 찾기' }

@app.route('/')
def home():
    return render_template('finder_main.html')

@app.route('/find/<category>')
def potatoes(category):
    return render_template('find_winterSnack.html', title=name[category])

@app.route('/find/<category>/<district>')
def potatoes_district(category, district):
    district = urllib.parse.unquote(district)
    return render_template('find_winterSnack.html', title=district + '에서 '+ name[category])

@app.route('/api/<category>')
def api_potatoes(category):
    map_html = map.district_marker(category)

    return jsonify({"map_html": map_html})

@app.route('/api/<category>/<district>')
def api_potatoes_district(category, district):
    district = urllib.parse.unquote(district)
    map_html = map.detail_marker(category, district)

    return jsonify({"map_html": map_html})


if __name__ == '__main__':
    app.run()
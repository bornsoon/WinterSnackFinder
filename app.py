from flask import Flask, render_template, jsonify

import map
# import urllib.parse

app = Flask(__name__)

name = {'bungeoppang': '붕어빵 찾기', 'sweetpotato': '고구마 찾기' }

@app.route('/')
def home():
    return render_template('finder_main.html')

@app.route('/find/<category>')
def snacks(category):
    return render_template('find_winterSnack.html', title=name[category])

@app.route('/find/<category>/<dist_code>')
def snacks_district(category, dist_code):
    # district = urllib.parse.unquote(district)
    return render_template('find_winterSnack.html', title=name[category])

@app.route('/api/<category>')
def api_snacks(category):
    map_html = map.district_marker(category)

    return jsonify({"map_html": map_html})

@app.route('/api/<category>/<dist_code>')
def api_snacks_district(category, dist_code):
    # district = urllib.parse.unquote(district)
    map_html = map.detail_marker(category, dist_code)

    return jsonify({"map_html": map_html})


if __name__ == '__main__':
    app.run()
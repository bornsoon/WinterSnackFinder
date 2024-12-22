from flask import Flask, render_template

import map

app = Flask(__name__)

name = {'bungeoppang': '붕어빵 찾기', 'sweetpotato': '고구마 찾기' }

@app.route('/')
def home():
    return render_template('finder_main.html')

@app.route('/find/<category>')
def potatoes(category):
    map_html = map.district_marker(category)

    return render_template('find_winterSnack.html', map_html=map_html, title=name[category])

@app.route('/find/<category>/<district>')
def potatoes_district(category, district):
    map_html = map.detail_marker(category, district)

    return render_template('find__winterSnack.html', map_html=map_html, title=name[category])


if __name__ == '__main__':
    app.run()
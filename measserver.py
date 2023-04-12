import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

# Lista mittauksia varten
measurements = []

# Avaa sivun result.html ja näyttää mittaukset siinä taulukkomuodossa
@app.route('/')
def get_all_measurements_page():
    return render_template('result.html', result = measurements)

# Näytä mittaukset Google Chart -kaavion avulla
@app.route('/line')
def get_line():
    return render_template('linechart.html', result = measurements)

# Otetaan vastaan HTTP POSTilla lähetty mittaus ja laitetaan se listaan
@app.route('/uusimittaus', methods=['POST'])
def new_meas():
    # luetaan data viestistä ja deserialisoidaan JSON-data
    m = request.get_json(force=True)
    # muutetaan mittaus Google Chartille sopivaan muotoon (sanakirja -> lista)
    mg = [m['alfa'], m['x'], m['y'], m['z']]
    # laitetaan listamuotoinen mittaus taulukkoon
    measurements.append(mg)
    # palautetaan vastaanotettu tieto
    return json.dumps(m, indent=True)

if __name__ == '__main__':
   app.run(debug = True)
   
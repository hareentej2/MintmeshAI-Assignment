from flask import Flask, request, jsonify
from covid import Covid
from flask_cors import CORS
import json
c = Covid(source="worldometers")
# print(c.get_status_by_country_name('India'))
# w = Worldometer()
# print(w.categories())
# print(w.what_is_here())
# print(w.)
app = Flask(__name__)

@app.route('/')
def get_status():
    data = c.get_data()
    
    data = [{'country': d['country'], 
    'confirmed': d['confirmed'], 
    'active': d['active'], 
    'deaths': d['deaths'], 
    'Recovery Rate': round(d['recovered']/d['confirmed'],4), 
    'Percentage of Population Infected': round(d['confirmed']/int(d['population']),4)
    } for d in data if int(d['population']) > 0 ]
    return jsonify(data)

@app.route('/country')
def get_country_status():
    countries = request.args
    print(countries)
    summary = []
    for k,v in countries.items():
        data = c.get_status_by_country_name(v)
        summary.append({'country': data['country'], 
            'confirmed': data['confirmed'], 
            'active': data['active'], 
            'deaths': data['deaths'],
            'Recovery Rate': round(data['recovered']/data['confirmed'],4), 
            'Percentage of Population Infected': round(data['confirmed']/int(data['population']),4)
            })
    return jsonify(summary)

if __name__ == '__main__':
    app.run()
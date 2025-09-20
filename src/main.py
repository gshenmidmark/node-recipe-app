from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data: countries and their cities
country_cities = {
    "usa": ["New York", "Los Angeles", "Chicago"],
    "spain": ["Madrid", "Barcelona", "Valencia"],
    "japan": ["Tokyo", "Osaka", "Kyoto"]
}

@app.route('/countries/<country>/cities', methods=['GET'])
def get_cities(country):
    country = country.lower()
    cities = country_cities.get(country)
    if cities is None:
        return jsonify({"error": "Country not found"}), 404
    return jsonify({"country": country, "cities": cities})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
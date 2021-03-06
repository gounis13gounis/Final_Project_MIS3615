# from flask import Flask, render_template, request
#
# from mbta_helper import find_stop_near
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def calculate():
#    if request.method == 'POST':
#        Location = request.form['location']
#        Near_stop,wheelchair = find_stop_near(Location)
#        # Country Code = float(request.form['country code'])
#        # we want results from api
#        if Near_stop and wheelchair:
#            return render_template('mbta_result.html',location=Location,near_stop=Near_stop,wheelchair=wheelchair)
#        else:
#            return render_template('mbta_form.html',error=True)
#    return render_template('mbta_form.html', error=None)
# names = ['Bailey', 'Valerie', 'Penny', 'Devan']
#
# print(names[-1][-2])
#
print(weather_forecast["name":"Wellesley"])
weather_forecast["list"][1]["weather"]
weather_forecast = {'city': {'coord': {'lat': 42.2965, 'lon': -71.2926},
          'country': 'US',
          'id': 4954738,
          'name': 'Wellesley',
          'population': 27982},
 'cnt': 40,
 'cod': '200',
 'list': [{'clouds': {'all': 0},
           'dt': 1553104800,
           'dt_txt': '2019-03-20 18:00:00',
           'main': {'grnd_level': 1016.75,
                    'humidity': 43,
                    'pressure': 1027.1,
                    'sea_level': 1027.1,
                    'temp': 286.04,
                    'temp_kf': 3.11,
                    'temp_max': 286.04,
                    'temp_min': 282.931},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 218.501, 'speed': 2.97}},
          {'clouds': {'all': 48},
           'dt': 1553115600,
           'dt_txt': '2019-03-20 21:00:00',
           'main': {'grnd_level': 1014.81,
                    'humidity': 42,
                    'pressure': 1025.26,
                    'sea_level': 1025.26,
                    'temp': 285.21,
                    'temp_kf': 2.33,
                    'temp_max': 285.21,
                    'temp_min': 282.879},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'scattered clouds',
                        'icon': '03d',
                        'id': 802,
                        'main': 'Clouds'}],
           'wind': {'deg': 236.002, 'speed': 2.57}},
          {'clouds': {'all': 0},
           'dt': 1553126400,
           'dt_txt': '2019-03-21 00:00:00',
           'main': {'grnd_level': 1015.59,
                    'humidity': 50,
                    'pressure': 1026.13,
                    'sea_level': 1026.13,
                    'temp': 279.85,
                    'temp_kf': 1.56,
                    'temp_max': 279.85,
                    'temp_min': 278.291},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 202.503, 'speed': 2.77}},
          {'clouds': {'all': 0},
           'dt': 1553137200,
           'dt_txt': '2019-03-21 03:00:00',
           'main': {'grnd_level': 1016.59,
                    'humidity': 54,
                    'pressure': 1027.17,
                    'sea_level': 1027.17,
                    'temp': 276.38,
                    'temp_kf': 0.78,
                    'temp_max': 276.38,
                    'temp_min': 275.598},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 203.003, 'speed': 3.01}},
          {'clouds': {'all': 0},
           'dt': 1553148000,
           'dt_txt': '2019-03-21 06:00:00',
           'main': {'grnd_level': 1016.13,
                    'humidity': 63,
                    'pressure': 1026.72,
                    'sea_level': 1026.72,
                    'temp': 273.26,
                    'temp_kf': 0,
                    'temp_max': 273.26,
                    'temp_min': 273.26},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 203.503, 'speed': 2.3}},
          {'clouds': {'all': 8},
           'dt': 1553158800,
           'dt_txt': '2019-03-21 09:00:00',
           'main': {'grnd_level': 1015.41,
                    'humidity': 86,
                    'pressure': 1026.12,
                    'sea_level': 1026.12,
                    'temp': 269.073,
                    'temp_kf': 0,
                    'temp_max': 269.073,
                    'temp_min': 269.073},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '02n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 174.501, 'speed': 1.06}},
          {'clouds': {'all': 76},
           'dt': 1553169600,
           'dt_txt': '2019-03-21 12:00:00',
           'main': {'grnd_level': 1015.37,
                    'humidity': 79,
                    'pressure': 1025.95,
                    'sea_level': 1025.95,
                    'temp': 271.828,
                    'temp_kf': 0,
                    'temp_max': 271.828,
                    'temp_min': 271.828},
           'snow': {'3h': 0.002},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 159.003, 'speed': 1.62}},
          {'clouds': {'all': 92},
           'dt': 1553180400,
           'dt_txt': '2019-03-21 15:00:00',
           'main': {'grnd_level': 1013.3,
                    'humidity': 64,
                    'pressure': 1023.77,
                    'sea_level': 1023.77,
                    'temp': 277.474,
                    'temp_kf': 0,
                    'temp_max': 277.474,
                    'temp_min': 277.474},
           'snow': {'3h': 0.0055},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 140.502, 'speed': 2.11}},
          {'clouds': {'all': 36},
           'dt': 1553191200,
           'dt_txt': '2019-03-21 18:00:00',
           'main': {'grnd_level': 1010.08,
                    'humidity': 53,
                    'pressure': 1020.48,
                    'sea_level': 1020.48,
                    'temp': 282.388,
                    'temp_kf': 0,
                    'temp_max': 282.388,
                    'temp_min': 282.388},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'scattered clouds',
                        'icon': '03d',
                        'id': 802,
                        'main': 'Clouds'}],
           'wind': {'deg': 143.003, 'speed': 2.86}},
          {'clouds': {'all': 68},
           'dt': 1553202000,
           'dt_txt': '2019-03-21 21:00:00',
           'main': {'grnd_level': 1007.07,
                    'humidity': 51,
                    'pressure': 1017.51,
                    'sea_level': 1017.51,
                    'temp': 281.986,
                    'temp_kf': 0,
                    'temp_max': 281.986,
                    'temp_min': 281.986},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'broken clouds',
                        'icon': '04d',
                        'id': 803,
                        'main': 'Clouds'}],
           'wind': {'deg': 139.501, 'speed': 3.02}},
          {'clouds': {'all': 68},
           'dt': 1553212800,
           'dt_txt': '2019-03-22 00:00:00',
           'main': {'grnd_level': 1004.83,
                    'humidity': 63,
                    'pressure': 1015.08,
                    'sea_level': 1015.08,
                    'temp': 278.116,
                    'temp_kf': 0,
                    'temp_max': 278.116,
                    'temp_min': 278.116},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'broken clouds',
                        'icon': '04n',
                        'id': 803,
                        'main': 'Clouds'}],
           'wind': {'deg': 104.507, 'speed': 2.97}},
          {'clouds': {'all': 92},
           'dt': 1553223600,
           'dt_txt': '2019-03-22 03:00:00',
           'main': {'grnd_level': 1000.72,
                    'humidity': 82,
                    'pressure': 1010.92,
                    'sea_level': 1010.92,
                    'temp': 277.167,
                    'temp_kf': 0,
                    'temp_max': 277.167,
                    'temp_min': 277.167},
           'rain': {'3h': 0.02},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'light rain',
                        'icon': '10n',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 95.5005, 'speed': 3.21}},
          {'clouds': {'all': 92},
           'dt': 1553234400,
           'dt_txt': '2019-03-22 06:00:00',
           'main': {'grnd_level': 993.39,
                    'humidity': 95,
                    'pressure': 1003.76,
                    'sea_level': 1003.76,
                    'temp': 278.042,
                    'temp_kf': 0,
                    'temp_max': 278.042,
                    'temp_min': 278.042},
           'rain': {'3h': 2.52},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'light rain',
                        'icon': '10n',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 77.0036, 'speed': 3.87}},
          {'clouds': {'all': 92},
           'dt': 1553245200,
           'dt_txt': '2019-03-22 09:00:00',
           'main': {'grnd_level': 984.09,
                    'humidity': 99,
                    'pressure': 994.15,
                    'sea_level': 994.15,
                    'temp': 278.667,
                    'temp_kf': 0,
                    'temp_max': 278.667,
                    'temp_min': 278.667},
           'rain': {'3h': 12.74},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'heavy intensity rain',
                        'icon': '10n',
                        'id': 502,
                        'main': 'Rain'}],
           'wind': {'deg': 55.5009, 'speed': 5.66}},
          {'clouds': {'all': 92},
           'dt': 1553256000,
           'dt_txt': '2019-03-22 12:00:00',
           'main': {'grnd_level': 974.46,
                    'humidity': 96,
                    'pressure': 984.37,
                    'sea_level': 984.37,
                    'temp': 280.079,
                    'temp_kf': 0,
                    'temp_max': 280.079,
                    'temp_min': 280.079},
           'rain': {'3h': 15.82},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'heavy intensity rain',
                        'icon': '10d',
                        'id': 502,
                        'main': 'Rain'}],
           'wind': {'deg': 63.5034, 'speed': 7.77}},
          {'clouds': {'all': 92},
           'dt': 1553266800,
           'dt_txt': '2019-03-22 15:00:00',
           'main': {'grnd_level': 968.91,
                    'humidity': 98,
                    'pressure': 978.89,
                    'sea_level': 978.89,
                    'temp': 281.759,
                    'temp_kf': 0,
                    'temp_max': 281.759,
                    'temp_min': 281.759},
           'rain': {'3h': 6.27},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'moderate rain',
                        'icon': '10d',
                        'id': 501,
                        'main': 'Rain'}],
           'wind': {'deg': 70.5024, 'speed': 5.47}},
          {'clouds': {'all': 92},
           'dt': 1553277600,
           'dt_txt': '2019-03-22 18:00:00',
           'main': {'grnd_level': 964.65,
                    'humidity': 100,
                    'pressure': 974.8,
                    'sea_level': 974.8,
                    'temp': 282.014,
                    'temp_kf': 0,
                    'temp_max': 282.014,
                    'temp_min': 282.014},
           'rain': {'3h': 1.78},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'light rain',
                        'icon': '10d',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 44.5018, 'speed': 3.87}},
          {'clouds': {'all': 92},
           'dt': 1553288400,
           'dt_txt': '2019-03-22 21:00:00',
           'main': {'grnd_level': 965.65,
                    'humidity': 97,
                    'pressure': 975.87,
                    'sea_level': 975.87,
                    'temp': 281.23,
                    'temp_kf': 0,
                    'temp_max': 281.23,
                    'temp_min': 281.23},
           'rain': {'3h': 1.93},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'light rain',
                        'icon': '10d',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 344.505, 'speed': 4.02}},
          {'clouds': {'all': 92},
           'dt': 1553299200,
           'dt_txt': '2019-03-23 00:00:00',
           'main': {'grnd_level': 970.1,
                    'humidity': 100,
                    'pressure': 980.35,
                    'sea_level': 980.35,
                    'temp': 279.426,
                    'temp_kf': 0,
                    'temp_max': 279.426,
                    'temp_min': 279.426},
           'rain': {'3h': 5.58},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'moderate rain',
                        'icon': '10n',
                        'id': 501,
                        'main': 'Rain'}],
           'wind': {'deg': 308.501, 'speed': 4.3}},
          {'clouds': {'all': 92},
           'dt': 1553310000,
           'dt_txt': '2019-03-23 03:00:00',
           'main': {'grnd_level': 974.29,
                    'humidity': 98,
                    'pressure': 984.42,
                    'sea_level': 984.42,
                    'temp': 277.405,
                    'temp_kf': 0,
                    'temp_max': 277.405,
                    'temp_min': 277.405},
           'rain': {'3h': 6.62},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'moderate rain',
                        'icon': '10n',
                        'id': 501,
                        'main': 'Rain'}],
           'wind': {'deg': 312.002, 'speed': 3.75}},
          {'clouds': {'all': 92},
           'dt': 1553320800,
           'dt_txt': '2019-03-23 06:00:00',
           'main': {'grnd_level': 977.58,
                    'humidity': 98,
                    'pressure': 987.78,
                    'sea_level': 987.78,
                    'temp': 276.791,
                    'temp_kf': 0,
                    'temp_max': 276.791,
                    'temp_min': 276.791},
           'rain': {'3h': 4.31},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'moderate rain',
                        'icon': '10n',
                        'id': 501,
                        'main': 'Rain'}],
           'wind': {'deg': 317.003, 'speed': 4.11}},
          {'clouds': {'all': 92},
           'dt': 1553331600,
           'dt_txt': '2019-03-23 09:00:00',
           'main': {'grnd_level': 981.91,
                    'humidity': 93,
                    'pressure': 992.03,
                    'sea_level': 992.03,
                    'temp': 276.141,
                    'temp_kf': 0,
                    'temp_max': 276.141,
                    'temp_min': 276.141},
           'rain': {'3h': 0.62},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'light rain',
                        'icon': '10n',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 318.008, 'speed': 4.52}},
          {'clouds': {'all': 92},
           'dt': 1553342400,
           'dt_txt': '2019-03-23 12:00:00',
           'main': {'grnd_level': 986.99,
                    'humidity': 78,
                    'pressure': 997.21,
                    'sea_level': 997.21,
                    'temp': 276.725,
                    'temp_kf': 0,
                    'temp_max': 276.725,
                    'temp_min': 276.725},
           'rain': {'3h': 0.049999999999997},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'light rain',
                        'icon': '10d',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 318.504, 'speed': 4.47}},
          {'clouds': {'all': 80},
           'dt': 1553353200,
           'dt_txt': '2019-03-23 15:00:00',
           'main': {'grnd_level': 991.26,
                    'humidity': 74,
                    'pressure': 1001.6,
                    'sea_level': 1001.6,
                    'temp': 278.598,
                    'temp_kf': 0,
                    'temp_max': 278.598,
                    'temp_min': 278.598},
           'rain': {'3h': 0.039999999999999},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'light rain',
                        'icon': '10d',
                        'id': 500,
                        'main': 'Rain'}],
           'wind': {'deg': 316.505, 'speed': 5.2}},
          {'clouds': {'all': 12},
           'dt': 1553364000,
           'dt_txt': '2019-03-23 18:00:00',
           'main': {'grnd_level': 994.33,
                    'humidity': 64,
                    'pressure': 1004.52,
                    'sea_level': 1004.52,
                    'temp': 280.789,
                    'temp_kf': 0,
                    'temp_max': 280.789,
                    'temp_min': 280.789},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'few clouds',
                        'icon': '02d',
                        'id': 801,
                        'main': 'Clouds'}],
           'wind': {'deg': 314.003, 'speed': 5.36}},
          {'clouds': {'all': 64},
           'dt': 1553374800,
           'dt_txt': '2019-03-23 21:00:00',
           'main': {'grnd_level': 997.46,
                    'humidity': 65,
                    'pressure': 1007.67,
                    'sea_level': 1007.67,
                    'temp': 279.064,
                    'temp_kf': 0,
                    'temp_max': 279.064,
                    'temp_min': 279.064},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'broken clouds',
                        'icon': '04d',
                        'id': 803,
                        'main': 'Clouds'}],
           'wind': {'deg': 306.004, 'speed': 5.07}},
          {'clouds': {'all': 0},
           'dt': 1553385600,
           'dt_txt': '2019-03-24 00:00:00',
           'main': {'grnd_level': 1001.66,
                    'humidity': 68,
                    'pressure': 1012.06,
                    'sea_level': 1012.06,
                    'temp': 275.709,
                    'temp_kf': 0,
                    'temp_max': 275.709,
                    'temp_min': 275.709},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 311.001, 'speed': 4.25}},
          {'clouds': {'all': 0},
           'dt': 1553396400,
           'dt_txt': '2019-03-24 03:00:00',
           'main': {'grnd_level': 1005.05,
                    'humidity': 61,
                    'pressure': 1015.56,
                    'sea_level': 1015.56,
                    'temp': 273.598,
                    'temp_kf': 0,
                    'temp_max': 273.598,
                    'temp_min': 273.598},
           'rain': {},
           'snow': {'3h': 0.0025},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 314.004, 'speed': 3.71}},
          {'clouds': {'all': 0},
           'dt': 1553407200,
           'dt_txt': '2019-03-24 06:00:00',
           'main': {'grnd_level': 1007.13,
                    'humidity': 60,
                    'pressure': 1017.7,
                    'sea_level': 1017.7,
                    'temp': 272.035,
                    'temp_kf': 0,
                    'temp_max': 272.035,
                    'temp_min': 272.035},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 310.002, 'speed': 3.23}},
          {'clouds': {'all': 0},
           'dt': 1553418000,
           'dt_txt': '2019-03-24 09:00:00',
           'main': {'grnd_level': 1008.7,
                    'humidity': 61,
                    'pressure': 1019.34,
                    'sea_level': 1019.34,
                    'temp': 271.164,
                    'temp_kf': 0,
                    'temp_max': 271.164,
                    'temp_min': 271.164},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 302.013, 'speed': 2.76}},
          {'clouds': {'all': 0},
           'dt': 1553428800,
           'dt_txt': '2019-03-24 12:00:00',
           'main': {'grnd_level': 1010.35,
                    'humidity': 56,
                    'pressure': 1021,
                    'sea_level': 1021,
                    'temp': 272.298,
                    'temp_kf': 0,
                    'temp_max': 272.298,
                    'temp_min': 272.298},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 285, 'speed': 2.52}},
          {'clouds': {'all': 0},
           'dt': 1553439600,
           'dt_txt': '2019-03-24 15:00:00',
           'main': {'grnd_level': 1010.48,
                    'humidity': 55,
                    'pressure': 1020.93,
                    'sea_level': 1020.93,
                    'temp': 278.895,
                    'temp_kf': 0,
                    'temp_max': 278.895,
                    'temp_min': 278.895},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 282.504, 'speed': 2.81}},
          {'clouds': {'all': 0},
           'dt': 1553450400,
           'dt_txt': '2019-03-24 18:00:00',
           'main': {'grnd_level': 1009.35,
                    'humidity': 43,
                    'pressure': 1019.69,
                    'sea_level': 1019.69,
                    'temp': 282.993,
                    'temp_kf': 0,
                    'temp_max': 282.993,
                    'temp_min': 282.993},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 277.001, 'speed': 3.56}},
          {'clouds': {'all': 0},
           'dt': 1553461200,
           'dt_txt': '2019-03-24 21:00:00',
           'main': {'grnd_level': 1008.5,
                    'humidity': 41,
                    'pressure': 1018.8,
                    'sea_level': 1018.8,
                    'temp': 283.418,
                    'temp_kf': 0,
                    'temp_max': 283.418,
                    'temp_min': 283.418},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'clear sky',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 281.5, 'speed': 3.76}},
          {'clouds': {'all': 0},
           'dt': 1553472000,
           'dt_txt': '2019-03-25 00:00:00',
           'main': {'grnd_level': 1009.97,
                    'humidity': 45,
                    'pressure': 1020.32,
                    'sea_level': 1020.32,
                    'temp': 279.606,
                    'temp_kf': 0,
                    'temp_max': 279.606,
                    'temp_min': 279.606},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 273.509, 'speed': 3.32}},
          {'clouds': {'all': 0},
           'dt': 1553482800,
           'dt_txt': '2019-03-25 03:00:00',
           'main': {'grnd_level': 1011.3,
                    'humidity': 52,
                    'pressure': 1021.8,
                    'sea_level': 1021.8,
                    'temp': 277.191,
                    'temp_kf': 0,
                    'temp_max': 277.191,
                    'temp_min': 277.191},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '01n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 281.501, 'speed': 2.96}},
          {'clouds': {'all': 8},
           'dt': 1553493600,
           'dt_txt': '2019-03-25 06:00:00',
           'main': {'grnd_level': 1011.68,
                    'humidity': 58,
                    'pressure': 1022.29,
                    'sea_level': 1022.29,
                    'temp': 274.899,
                    'temp_kf': 0,
                    'temp_max': 274.899,
                    'temp_min': 274.899},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'clear sky',
                        'icon': '02n',
                        'id': 800,
                        'main': 'Clear'}],
           'wind': {'deg': 285, 'speed': 2.43}},
          {'clouds': {'all': 24},
           'dt': 1553504400,
           'dt_txt': '2019-03-25 09:00:00',
           'main': {'grnd_level': 1011.63,
                    'humidity': 67,
                    'pressure': 1022.25,
                    'sea_level': 1022.25,
                    'temp': 272.429,
                    'temp_kf': 0,
                    'temp_max': 272.429,
                    'temp_min': 272.429},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'n'},
           'weather': [{'description': 'few clouds',
                        'icon': '02n',
                        'id': 801,
                        'main': 'Clouds'}],
           'wind': {'deg': 265.001, 'speed': 1.61}},
          {'clouds': {'all': 36},
           'dt': 1553515200,
           'dt_txt': '2019-03-25 12:00:00',
           'main': {'grnd_level': 1012.42,
                    'humidity': 75,
                    'pressure': 1022.94,
                    'sea_level': 1022.94,
                    'temp': 273.444,
                    'temp_kf': 0,
                    'temp_max': 273.444,
                    'temp_min': 273.444},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'scattered clouds',
                        'icon': '03d',
                        'id': 802,
                        'main': 'Clouds'}],
           'wind': {'deg': 228.505, 'speed': 1.06}},
          {'clouds': {'all': 36},
           'dt': 1553526000,
           'dt_txt': '2019-03-25 15:00:00',
           'main': {'grnd_level': 1011.36,
                    'humidity': 62,
                    'pressure': 1021.74,
                    'sea_level': 1021.74,
                    'temp': 280.705,
                    'temp_kf': 0,
                    'temp_max': 280.705,
                    'temp_min': 280.705},
           'rain': {},
           'snow': {},
           'sys': {'pod': 'd'},
           'weather': [{'description': 'scattered clouds',
                        'icon': '03d',
                        'id': 802,
                        'main': 'Clouds'}],
           'wind': {'deg': 252.001, 'speed': 1.56}}],
 'message': 0.0087}

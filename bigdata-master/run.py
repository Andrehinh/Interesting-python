# encoding: utf-8

from flask import Flask, render_template, jsonify
from redis_conn import redis_conn_pool
import json


app = Flask(__name__)
rd = redis_conn_pool()


@app.route('/')
def index():
    return render_template('bigdata.html')


def get_chart1_data():
    chart1_data_list = []
    chart1_city_list = []
    chart1_info = {}
    city_data = json.loads(rd.get('ncovcity_data'))
    for city in city_data['newslist'][:5]:
        chart1_dict = {}
        chart1_dict['name'] = city['provinceShortName']
        chart1_dict['value'] = city['confirmedCount']
        chart1_data_list.append(chart1_dict)
        chart1_city_list.append(city['provinceShortName'])
    chart1_info['x_name'] = chart1_city_list
    chart1_info['data'] = chart1_data_list
    return chart1_info


def get_chart2_data():
    chart2_info = {}
    chart2_dict = {}
    city_data = json.loads(rd.get('ncovcity_data'))
    for city in city_data['newslist']:
        chart2_dict[city['provinceShortName']] = city['deadCount']

    chart2_data_list = sorted(chart2_dict.items(), key=lambda x: x[1], reverse=True)
    chart2_city_list = [x[0] for x in chart2_data_list[:5]]
    chart2_info['x_name'] = chart2_city_list
    chart2_info['data'] = chart2_data_list[:5]
    return chart2_info


def get_chart3_1_data():
    chart3_1_list = []
    ncov_data = json.loads(rd.get('ncov_data'))
    ncov = ncov_data['newslist'][0]['desc']
    confirm = {'value': ncov['confirmedCount'], 'name': '确诊'}
    dead = {'value': ncov['deadCount'], 'name': '死亡'}
    chart3_1_list.append(confirm)
    chart3_1_list.append(dead)
    return chart3_1_list


def get_chart3_2_data():
    chart3_2_list = []
    ncov_data = json.loads(rd.get('ncov_data'))
    ncov = ncov_data['newslist'][0]['desc']
    confirm = {'value': ncov['confirmedCount'], 'name': '确诊'}
    cured = {'value': ncov['curedCount'], 'name': '治愈'}
    chart3_2_list.append(confirm)
    chart3_2_list.append(cured)
    return chart3_2_list


def get_chart3_3_data():
    chart3_3_list = []
    ncov_data = json.loads(rd.get('ncov_data'))
    ncov = ncov_data['newslist'][0]['desc']
    cured = {'value': ncov['curedCount'], 'name': '治愈'}
    dead = {'value': ncov['deadCount'], 'name': '死亡'}
    chart3_3_list.append(cured)
    chart3_3_list.append(dead)
    return chart3_3_list


def get_chart4_data():
    chart4_info = {}
    chart4_date_list = []
    chart4_confirm_list = []
    chart4_suspect_list = []
    chart4_heal_list = []
    chart4_dead_list = []
    trend_data = json.loads(rd.get('trend'))
    for data in trend_data['data']['chinaDayList']:
        chart4_date_list.append(data['date'].split('2020-')[1])
        chart4_confirm_list.append(data['total']['confirm'])
        chart4_suspect_list.append(data['total']['suspect'])
        chart4_heal_list.append(data['total']['heal'])
        chart4_dead_list.append(data['total']['dead'])
    chart4_info['x_name'] = chart4_date_list[-20:]
    chart4_info['confirm'] = chart4_confirm_list[-20:]
    chart4_info['suspect'] = chart4_suspect_list[-20:]
    chart4_info['heal'] = chart4_heal_list[-20:]
    chart4_info['dead'] = chart4_dead_list[-20:]
    return chart4_info


def get_chart5_data():
    chart5_info = {}
    chart5_dict = {}
    city_data = json.loads(rd.get('ncovcity_data'))
    for city in city_data['newslist']:
        chart5_dict[city['provinceShortName']] = city['curedCount']

    chart5_data_list = sorted(chart5_dict.items(), key=lambda x: x[1], reverse=True)
    chart5_city_list = [x[0] for x in chart5_data_list[:5]]
    chart5_info['x_name'] = chart5_city_list
    chart5_info['data'] = chart5_data_list[:5]
    return chart5_info


def get_chart5_1_data():
    chart5_1_info = {}
    chart5_1_dict = {}
    trend_data = json.loads(rd.get('trend'))
    for data in trend_data['data']['areaTree'][1:]:
        chart5_1_dict[data['name']] = data['total']['confirm']
    chart5_1_data_list = sorted(chart5_1_dict.items(), key=lambda x: x[1], reverse=True)
    chart5_1_country_list = [x[0] for x in chart5_1_data_list[:5]]
    chart5_1_info['x_name'] = chart5_1_country_list
    chart5_1_info['data'] = chart5_1_data_list[:5]
    return chart5_1_info


def get_chart_map_data():
    map_chart_list = []
    map_data = json.loads(rd.get('ncovcity_data'))
    for data in map_data['newslist']:
        map_chart_dict = {}
        map_chart_dict['name'] = data['provinceShortName']
        map_chart_dict['value'] = data['confirmedCount']
        map_chart_list.append(map_chart_dict)
    return map_chart_list


@app.route('/get_ncov_totalcount')
def ncov_totalcount():
    ncov_data = rd.get('ncov_data')
    result_ncov = json.loads(ncov_data)
    confirmedCount = result_ncov['newslist'][0]['desc']['confirmedCount']
    suspectedCount = result_ncov['newslist'][0]['desc']['suspectedCount']
    return jsonify({'confirmedCount': confirmedCount, 'suspectedCount': suspectedCount})


@app.route('/get_chart_data')
def get_chart_data():
    chart_info = {}
    chart1_data = get_chart1_data()
    chart2_data = get_chart2_data()
    chart4_data = get_chart4_data()
    chart5_data = get_chart5_data()
    chart5_1_data = get_chart5_1_data()
    chart3_1_data = get_chart3_1_data()
    chart3_2_data = get_chart3_2_data()
    chart3_3_data = get_chart3_3_data()
    chart_info['chart1'] = chart1_data
    chart_info['chart2'] = chart2_data
    chart_info['chart5'] = chart5_data
    chart_info['chart4'] = chart4_data
    chart_info['chart5_1'] = chart5_1_data
    chart_info['chart3_1'] = chart3_1_data
    chart_info['chart3_2'] = chart3_2_data
    chart_info['chart3_3'] = chart3_3_data
    return jsonify(chart_info)


@app.route('/get_map_data')
def get_map_data():
    map_data = get_chart_map_data()
    return jsonify(map_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


from flask import Flask, request,jsonify
from flask_cors import CORS

app =Flask(__name__)

@app.route('/')
def hello_flask():
    return "<h1>hello, Flask!</h1>"


@app.route('/create-stage', methods=['POST'])
def create_stage():
    print(dict(request.values))

    return {'status': 200, 'message': '', 'data': {'id': '123'}}


@app.route('/get-stage', methods=['GET'])
def get_stage():
    print(dict(request.args))
    return {'status': 200, 'message': '', 'data': {
        'name': '***',
        'company': '国防大学',
        'benchmarkDate': "2021-01-01",
        "startTime": '2025 - 01 - 01 00:00:00' ,
        'endTime': '2025 - 01 - 01 00:10:00',
        'stageData': [
            {
                "stageIndex": 1,
                "stageName": "第一阶段",
                "target": "第一阶段目的",
                "condition":"第一阶段转换条件",
                "startTime": "",
                "endTime": "",
                "timeRange": ['D0', 'D1', 'D2']
    }

        ]
    }}


@app.route('/resources', methods=['post'])
def resources():
    return {}


@app.route('/policy_list', methods=['get'])
def policy_list():
    return [
        {'key': 'OP大类', 'title': 'OP大类',
         'children': [
             {'key': '2-option1', 'title': '2-option1',}
         ]
         }
    ]


@app.route('/save-option', methods=['POST'])
def save_option():
    print(dict(request.values))

    return {'status': 200, 'message': '', 'data': {'id': '123'}}



@app.route('/get-option', methods=['GET'])
def get_option():
    print(dict(request.args))
    res = {
        "taskName": "名称",
        "taskModel": "12",
        "startTime": "2020 - 01 - 0100: 00:00",
        "endTime": "2020 - 01 - 01 10: 00:00",
        "tartget": ["雷达1", "雷达2"],
        # "resource": {"歼击机": 10,  "轰炸机": 20},
        "resource": [{"id": 1, "name": "歼击机", "values": 10}, {"id": 2, "name": "轰炸机", "values": 20}],
        "expectResult": [{"id": 2, "name": "红方力量", "values": 20}]

    }

    return {'status': 200,'message': '', 'data': res}



@app.route('/resources-type')
def resources_type():
    return jsonify(
        [{"name": "机型1", "id": "123"}]
    )


@app.route('/expect-result-type')
def expect_type():
    return jsonify(
        [{"name": "地方损毁程度1", "id": "13"}]
    )


@app.route('/target-type')
def target_type():
    return jsonify(
        [{"name": "雷达", "id": "13"}]
    )


@app.route('/stage-data')
def stage_data():
    res = {
        "taskName": "名称",
        "taskModel": "12",
        "startTime": "2020 - 01 - 0100: 00:00",
        "endTime": "2020 - 01 - 01 10: 00:00",
        "tartget": ["雷达1", "雷达2"],
        # "resource": {"歼击机": 10,  "轰炸机": 20},
        "resource": [{"id": 1, "name": "歼击机", "values": 10}, {"id": 2, "name": "轰炸机", "values": 20}],
        "expectResult": [{"id": 2, "name": "红方力量", "values": 20}]

    }

    return {'status': 200, 'message': '', 'data': [res]}



if __name__=='__main__':

    app.run(host='127.0.0.1' ,port=5000)


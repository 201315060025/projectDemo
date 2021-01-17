from flask import render_template
import pickle
import os
from flask import Flask,request,redirect,url_for

app = Flask(__name__)


res_dict = {
  "blx": [{"ip": "60", "port": "200-300"}, {"ip": "60", "port": "200-300"}],
  "blx2": [{"ip": "60", "port": "200-300"}, {"ip": "60", "port": "200-300"}]
}


def get_data():
  if os.path.exists("res.pkl"):
    with open("res.pkl", "rb") as f:
      name_detail = pickle.load(f)
  else:
    name_detail = {}
  return name_detail


def save_data_handle(data):
  with open("res.pkl", "wb") as f:
    pickle.dump(data, f)


@app.route('/', methods=['GET', 'POST'])
def index():
 name_detail = get_data()
 name_list = list(name_detail.keys())
 color_map = {name: name_detail[name][0].get("color", "#EEE0E5") for name in name_list}
 return render_template('index.html', name_list=name_list, name_detail=name_detail, color_map=color_map)


@app.route('/save_data', methods=['GET', 'POST'])
def save_data():
  ip, port, name, category = request.args["ip"].strip(), request.args["port"].strip(), request.args["name"].strip(), request.args["catgory"].strip()
  name_detail = get_data()
  color = "#EEE0E5" if category == "red" else "#99ccff"

  if not name:
    pass
  else:
    if name not in name_detail:
      name_detail[name] = []

    name_detail[name].append({"ip": ip, "port": port, "color": color})
  save_data_handle(name_detail)
  return redirect(url_for('index'), code=302)



@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete_data(name):
  name_detail = get_data()
  if name in name_detail:
    name_detail.pop(name)
  save_data_handle(name_detail)
  return redirect(url_for('index'), code=302)

app.run(debug=True, host="0.0.0.0", port=8000)

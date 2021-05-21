from flask import Flask,jsonify
import mysql.connector as mysql

# conn = mysql.connect(
#     host="localhost",
#     user="root",
#     password="pi",
#     database="smartfarming"
# )

# cursor = conn.cursor()

app = Flask(__name__)

@app.route('/getValues',methods=['GET'])
def hello():
    dataToSend = {}
    try:
    #    result = cursor.execute("select * from values")
    #    moisture_value = result.moisture_value
    #    ldr_value = result.ldr_value
    #    temp_value = result.temp_value
    #    motar_state = result.motarState
    #    light_state = result.light_state
    #    fan_state = result.fan_state
       dataToSend['moisture_value'] = 100
       dataToSend['ldr_value'] = 50
       dataToSend['temp_value'] = 44
       dataToSend['motar_state'] = "ON"
       dataToSend['light_state'] = "OFF"
       dataToSend['fan_state'] = "ON"
       return jsonify({"result":dataToSend,"status":1})
    except:
       return jsonify({"result":{},"status":0})




if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    
    


"""This script wraps the client into a Flask server. It receives POST request with                        
prediction data, and forward the data to tensorflow server for inference.                                 

Modified to accommedate multiple serving models.
"""                                                                                                       
                                                                                                          
from flask import Flask, render_template, request, url_for, jsonify                                       
import json                                                                                               
import tensorflow as tf                                                                                   
import numpy as np                                                                                        
import os                                                                                                 
import argparse                                                                                           
import sys                                                                                                
from datetime import datetime                                                                             
                                                                                                          
from grpc.beta import implementations                                                                     
from tensorflow_serving.apis import predict_pb2                                                           
from tensorflow_serving.apis import prediction_service_pb2                                                
                                                                                                          

app = Flask(__name__)                                                                                     
                                                                                                          

class ClientChannels():                                                                                  

    channel_map = {
        'rt': {
            'neur': {
                'aaba': implementations.insecure_channel('localhost', 9000),
                'aapl': implementations.insecure_channel('localhost', 9001),
                'amd': implementations.insecure_channel('localhost', 9002),
                'amzn': implementations.insecure_channel('localhost', 9003),
                'c': implementations.insecure_channel('localhost', 9004),
                'goog': implementations.insecure_channel('localhost', 9005),
                'googl': implementations.insecure_channel('localhost', 9006),
                'intc': implementations.insecure_channel('localhost', 9007),
                'msft': implementations.insecure_channel('localhost', 9008),
                'vz': implementations.insecure_channel('localhost', 9009)
            }, 'svm': {
                'aaba': implementations.insecure_channel('localhost', 9020),
                'aapl': implementations.insecure_channel('localhost', 9021),
                'amd': implementations.insecure_channel('localhost', 9022),
                'amzn': implementations.insecure_channel('localhost', 9023),
                'c': implementations.insecure_channel('localhost', 9024),
                'goog': implementations.insecure_channel('localhost', 9025),
                'googl': implementations.insecure_channel('localhost', 9026),
                'intc': implementations.insecure_channel('localhost', 9027),
                'msft': implementations.insecure_channel('localhost', 9028),
                'vz': implementations.insecure_channel('localhost', 9029)
            }
        }, 'hist': {
            'neur': {
                'aaba': implementations.insecure_channel('localhost', 9010),
                'aapl': implementations.insecure_channel('localhost', 9011),
                'amd': implementations.insecure_channel('localhost', 9012),
                'amzn': implementations.insecure_channel('localhost', 9013),
                'c': implementations.insecure_channel('localhost', 9014),
                'goog': implementations.insecure_channel('localhost', 9015),
                'googl': implementations.insecure_channel('localhost', 9016),
                'intc': implementations.insecure_channel('localhost', 9017),
                'msft': implementations.insecure_channel('localhost', 9018),
                'vz': implementations.insecure_channel('localhost', 9019),
            }, 'svm': {
                'aaba': implementations.insecure_channel('localhost', 9030),
                'aapl': implementations.insecure_channel('localhost', 9031),
                'amd': implementations.insecure_channel('localhost', 9032),
                'amzn': implementations.insecure_channel('localhost', 9033),
                'c': implementations.insecure_channel('localhost', 9034),
                'goog': implementations.insecure_channel('localhost', 9035),
                'googl': implementations.insecure_channel('localhost', 9036),
                'intc': implementations.insecure_channel('localhost', 9037),
                'msft': implementations.insecure_channel('localhost', 9038),
                'vz': implementations.insecure_channel('localhost', 9039)
            }
        }
    }
                                                                                                          
    def inference(self, freq, ml_type, sym, val_x):                                                                           
        if ml_type == 'neur': model_name = 'NNModel'                                                           
        elif ml_type == 'svm': model_name = 'SVMMODEL'                                                           
        elif ml_type == 'bay': model_name = 'BayesianModel'                                                           
        else: return {}

        try:                                                                                               
            request = predict_pb2.PredictRequest()                                                         
            request.model_spec.name = model_name                                                           
            request.model_spec.signature_name = 'prediction'                                               
            channel = self.channel_map[freq][ml_type][sym]                                                 
        except:                                                                                            
            return {}                                                                                      
                                                                                                           
        stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)                     
        temp_data = val_x.astype(np.float32)                                                              
        data, label = temp_data, np.sum(temp_data * np.array([1,2,3]).astype(np.float32), 1)              
        request.inputs['input'].CopyFrom(tf.contrib.util.make_tensor_proto(data))                    
        result = stub.Predict(request, 5.0)                                                     
        return result, label                                                                              
                                                                                                          

run = ClientChannels()                                                                                   
print("Initialization done. ")                                                                            
                                                                                                          

# Define a route for the default URL, which loads the form                                                
@app.route('/inference/<freq>/<ml_type>/<sym>', methods=['POST'])                                                                
def inference(freq, ml_type, sym):                                                                                          
    request_data = request.json                                                                           
    input_data = np.expand_dims(np.array(request_data), 0)                                                
    result, label = run.inference(freq, ml_type, sym, input_data)                                                             
    floats = result.outputs['output'].float_val                                                           
    return jsonify({'ScaledPrediction': floats[0]})                                                       
                                                                                                          
                                                                                                          
if __name__ == "__main__":                                                                                
    app.run(host= '0.0.0.0')                                                                              

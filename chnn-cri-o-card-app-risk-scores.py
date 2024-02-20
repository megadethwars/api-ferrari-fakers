from flask import Flask, request, jsonify

app = Flask(__name__)

  
@app.route('/process_request/2', methods=['POST'])
def process_request3():
    if request.method == 'POST':
        request_data = request.json
      
        response = {
            "customerId": "104",
            "applicationId": "116626283",
            "scoresPerModel": 
                {
                    "scoreModelName": "Plan-A",         
                    "responseDate": "2024-02-08T19:21:10Z"
                },
            "lastUpdatedDate":"2020-05-15"
        }
        response_data = request_data
        return jsonify(response)
    
@app.route('/process_request/3', methods=['POST'])
def process_request4():
    if request.method == 'POST':
        request_data = request.json
        
        response = {
            "customerId": "104",
            "applicationId": "116626283",
            "scoresPerModel": [
                {
                    "scoreModelName": "Plan-A",
                    "scores": [
                        {
                            "scoreId": "Credit-Bureau-Model-Score",
                            "score": -1.0
                        },
                        {
                            "scoreId": "Channels-Model-Score",
                            "score": -1.0
                        },
                        {
                            "scoreId": "Credit-Card-Behavior-Model-Score",
                            "score": -1.0
                        },
                        {
                            "scoreId": "Liabilities-Model-Score",
                            "score": -1.0
                        },
                        {
                            "scoreId": "Product-Holding-Model-Score",
                            "score": -1.0
                        },
                        {
                            "scoreId": "Application-Model-Score",
                            "score": 0.916764
                        },
                        {
                            "scoreId": "Bureau-Model-Score",
                            "score": 0.939243
                        },
                        {
                            "scoreId": "Assembly-Model-Score",
                            "score": 0.961911
                        },
                        {
                            "scoreId": "Customer-Final-Score",
                            "score": 69.0
                        }
                    ],
                    "responseDate": "2024-02-08T19:21:10Z"
                },
                {
                    "scoreModelName": "Plan-B",
                    "responseDate": "2024-02-08T19:21:10Z"
                }
            ],
            "lastUpdatedDate":"2020-05-15"
        }

        response_data = response
        return jsonify(response_data)
    return "ok"


    
@app.route('/api/v1/channels/credit-initiation/customers/scores/retrieve', methods=['POST'])
def process_requestplanA():
    if request.method == 'POST':
        response=None
        request_data = request.json
        if request_data['scoreModelName']=='Plan-A':
            response = {
                "customerId": "104",
                "applicationId": "116626283",
                "scoresPerModel": [
                    {
                        "scoreModelName": "Plan-A",
                        "scores": [
                            {
                                "scoreId": "Credit-Bureau-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Channels-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Credit-Card-Behavior-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Liabilities-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Product-Holding-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Application-Model-Score",
                                "score": 0.916764
                            },
                            {
                                "scoreId": "Bureau-Model-Score",
                                "score": 0.939243
                            },
                            {
                                "scoreId": "Assembly-Model-Score",
                                "score": 0.961911
                            },
                            {
                                "scoreId": "Customer-Final-Score",
                                "score": 69.0
                            }
                        ],
                        "responseDate": "2024-02-08T19:21:10Z"
                    }
                ],
                "lastUpdatedDate":"2020-05-15"
            }
        
        elif request_data['scoreModelName']=='Plan-B':
            response = {
            "customerId": "32111647",
            "applicationId": "2021062300065",
            "scoresPerModel": [
                {
                    "scoreModelName": "Plan-B",
                    "scores": [
                        {
                            "scoreId": "New-To-Revolving-Model-Score",
                            "score": 170.0
                        },
                        {
                            "scoreId": "Cobranded-Costco-Model-Score",
                            "score": 168.0
                        },
                        {
                            "scoreId": "Cobranded-Home-Depot-Model-Score",
                            "score": 173.0
                        },
                        {
                            "scoreId": "Cobranded-Others-Model-Score",
                            "score": 172.0
                        },
                        {
                            "scoreId": "Brands-On-Us-Model-Score",
                            "score": 141.0
                        },
                        {
                            "scoreId": "Brands-Off-Us-Model-Score",
                            "score": 157.0
                        },
                        {
                            "scoreId": "ThinHit&Communications-Model-Score",
                            "score": 117.0
                        },
                        {
                            "scoreId": "Inquiriesand-Pure-Model-Score",
                            "score": 142.0
                        }
                        ],
                    "responseDate": "2024-02-08T19:23:02Z"
                    }
                ],
                "lastUpdatedDate": None
            }

        else:
            response = {
            "customerId": "32111647",
            "applicationId": "2021062300065",
            "scoresPerModel": [
                {
                        "scoreModelName": "Plan-A",
                        "scores": [
                            {
                                "scoreId": "Credit-Bureau-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Channels-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Credit-Card-Behavior-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Liabilities-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Product-Holding-Model-Score",
                                "score": -1.0
                            },
                            {
                                "scoreId": "Application-Model-Score",
                                "score": 0.916764
                            },
                            {
                                "scoreId": "Bureau-Model-Score",
                                "score": 0.939243
                            },
                            {
                                "scoreId": "Assembly-Model-Score",
                                "score": 0.961911
                            },
                            {
                                "scoreId": "Customer-Final-Score",
                                "score": 69.0
                            }
                        ],
                        "responseDate": "2024-02-08T19:21:10Z"
                    }
                ,
                {
                    "scoreModelName": "Plan-B",
                    "scores": [
                        {
                            "scoreId": "New-To-Revolving-Model-Score",
                            "score": 170.0
                        },
                        {
                            "scoreId": "Cobranded-Costco-Model-Score",
                            "score": 168.0
                        },
                        {
                            "scoreId": "Cobranded-Home-Depot-Model-Score",
                            "score": 173.0
                        },
                        {
                            "scoreId": "Cobranded-Others-Model-Score",
                            "score": 172.0
                        },
                        {
                            "scoreId": "Brands-On-Us-Model-Score",
                            "score": 141.0
                        },
                        {
                            "scoreId": "Brands-Off-Us-Model-Score",
                            "score": 157.0
                        },
                        {
                            "scoreId": "ThinHit&Communications-Model-Score",
                            "score": 117.0
                        },
                        {
                            "scoreId": "Inquiriesand-Pure-Model-Score",
                            "score": 142.0
                        }
                        ],
                    "responseDate": "2024-02-08T19:23:02Z"
                    }
                ],
                "lastUpdatedDate": None
            }

        response_data = response
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

    

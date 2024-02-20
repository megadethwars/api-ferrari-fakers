from flask import Flask, request, jsonify

app = Flask(__name__)

  

@app.route('/api/v1/channels/credit-initiation/customers/risk-scores/retrieve', methods=['POST'])
def process_bigCollections():
    if request.method == 'POST':
        
        
        response = {
            "customer":{
                "customerId":"11053457",
                "customerSegments":[
                    {
                        "customerSegment":"Blue Basico",
                        "customerSegmentDate":"2021-05-12"
                    }
                ]
            },
            "scoreModelId":"216424",
            "scoreModelTypeCode":"1",
            "modelScores":[
                {
                    "scoreName":"Camelot",
                    "lastUpdatedDate":"2022-12-20",
                    "scoreDate":"2022-11-30",
                    "score":"0.752584765",
                    "creditAprrovedFlag":"true",
                    "creditAprrovedDate": "2022-12-01",
                    "creditScoreDecile":0.3,
                    "creditScoreQuartile":0.75
                }
            ]
        }
        
        

        response_data = response
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

    

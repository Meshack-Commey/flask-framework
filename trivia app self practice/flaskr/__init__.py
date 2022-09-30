import os
from flask import Flask, jsonify
from flask_cors import CORS 


#define the create app function
def create_app(test_config=True):
    app = Flask(__name__)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origin": "*"}})
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Conrol-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response
        
    @app.route('/messages')
    @cross_origin
    def get_message():
        return 'GETTING MESSAGES'
    
    return app




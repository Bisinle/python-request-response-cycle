#!/usr/bin/env python3
import os
from flask import Flask,request,current_app,g, make_response
from flask import redirect

app = Flask(__name__)



@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    # return f'''<h4>host for this page is <h1>{host}</h1></h4>
    #             <h4>the name of this application is  <h1>{appname}</h1></h4>
    #             <h4>the name of this application is  <h1>{g.path}</h1></h4>
            
    #         ''',\
    #         202
    response_body = f'''<h4>host for this page is <h1>{host}</h1></h4>
               <h4>the name of this application is  <h1>{appname}</h1></h4>
               <h4>the name of this application is  <h1>{g.path}</h1></h4>
            
            '''
    status_code = 200
    headers = {}
    return make_response(response_body,status_code,headers)

@app.route('/about')
def about():
    
    return   redirect('https://twitter.com')

# request_context = app.test_request_context()
# request_context.push()

if __name__ == '__main__':
    app.run(port=5555, debug=True)

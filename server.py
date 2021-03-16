from flask import Flask, request, jsonify
app = Flask(__name__, static_url_path='')


@app.route('/', methods = ['GET'])
def root():
    print('Loading Index page')
    return app.send_static_file('index.html')

@app.route('/main.js', methods = ['GET'])
def js():
    return app.send_static_file('main.js')

@app.route('/style.css', methods = ['GET'])
def css():
    return app.send_static_file('style.css')

@app.route('/person', methods = ['POST'])
def person():
    print(request.form['fname'])
    print(request.form['lname'])
    #save_in_database(first, lat)
    return jsonify({'status': 'Thank you for your data'})

if __name__ == '__main__':
    app.run()

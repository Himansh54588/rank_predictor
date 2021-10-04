
from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_category')
def get_category():
    response=jsonify({
        'category': util.get_category()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/get_rank',methods=['GET','POST'])
def get_rank():
    category=request.form['category']
    marks=int(request.form['marks'])

    response=jsonify({
        'rank': util.get_rank(category,marks)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response




if __name__ == '__main__':
    app.debug = True
    app.run()

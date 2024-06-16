from flask import Flask, request, jsonify
import backend_dao
import umo_dao
from sql_connection import sql_connection

connection = sql_connection()
app = Flask(__name__)


@app.route('/getproducts',methods = ['GET'])
def get_products():
    products= backend_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route('deleteProduct', methods = ['POST'])
def delete_product():
    return_id = backend_dao.delete_from_products(connection,request.form['product_id'])
    response= jsonify({
        'product_id' : return_id
    })

    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

if __name__ == "__main__":
    print('Starting Python Flask Server For Grocery Store Management system')
    app.run(port=5000)
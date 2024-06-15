from sql_connection import sql_connection


def get_all_products(connection):

    cursor = connection.cursor()
    query= ("select products.product_id, products.name, products.price_per_unit, products.umo_id, umo.umocol from products inner join umo on products.umo_id=umo.um_id"
            )

    cursor.execute(query)

    response = []

    for (product_id , name, price_per_unit,umo_id,umocol) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name' : name,
                'umo_id' : umo_id,
                'price_per_unit' : price_per_unit,
                'umo_name' : umocol
            }
        )
    cursor= connection.close()
    return response



if __name__ == '__main__':
    connection = sql_connection()
    print(get_all_products(connection))
from sql_connection import sql_connection

def get_um0(connection):
    cursor = connection.cursor()

    query = ("select * from umo")

    cursor.execute(query)
    response = []
    for um_id, umocol in cursor:
        response.append({
            'umo_id' : um_id,
            'um_col' : umocol
        })
    return response

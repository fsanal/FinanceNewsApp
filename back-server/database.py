import pymysql


def get_session():
    return pymysql.connect(host='cis450.czwf6yzxfpm1.us-east-1.rds.amazonaws.com', port=3306, user='admin', password='BoombaZombie', db='data', cursorclass=pymysql.cursors.DictCursor)


def scan_headline():
    items = None
    connection = get_session()

    try:
        with connection.cursor() as cursor:
            sql = '''
                    SELECT *
                    FROM Headline
                    ORDER BY date ASC
                    LIMIT 27;     
                  '''
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        print('Success!')

    return items


def search_headlines_database(searchQuery, startdate, enddate):
    items = None
    connection = get_session()

    try:
        with connection.cursor() as cursor:
            sql = '''
                    SELECT *
                    FROM Headline
                    WHERE MATCH(headline) AGAINST ('{}' IN NATURAL LANGUAGE MODE)
                  '''.format(searchQuery)
            if startdate:
                sql = sql + " AND DATE(date) > '{}'".format(startdate)
            if enddate:
                sql = sql + " AND DATE(date) < '{}'".format(enddate)
            sql = sql + " LIMIT 27;"
            print(sql)
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        print('Success!')
    print(items)
    return items


def scan_events():
    items = None
    connection = get_session()

    try:
        with connection.cursor() as cursor:
            sql = f'''
                    SELECT *
                    FROM Economic_Event    
                  '''
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        print('Success!')

    return items


def get_headlines_for_event(event):
    items = None
    connection = get_session()

    try:
        with connection.cursor() as cursor:
            sql = f'''
                    SELECT date, headline, sentiment_score
                    FROM Event_Association e JOIN Headline h
                    ON e.headline_id = h.id
                    WHERE event_id = {event}
                  '''
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        print('Success!')

    return items


def get_ids_with_term_year(term, year):
    items = None
    connection = get_session()

    try:
        with connection.cursor() as cursor:
            sql = f'''
                    SELECT id
                    FROM Headline
                    WHERE headline LIKE "%{term}%"
                    AND YEAR(date) = "{year}"
                  '''
            cursor.execute(sql)
            items = cursor.fetchall()
    finally:
        print('Success!')

    ids = []
    for item in items:
        ids.append(item['id'])

    return ids


def create_associations(event_id, headline_ids):
    connection = get_session()

    for headline_id in headline_ids:
        try:
            with connection.cursor() as cursor:
                sql = f'''
                        INSERT INTO Event_Association (event_id, headline_id)
                        VALUES ("{event_id}", "{headline_id}")
                      '''
                cursor.execute(sql)
                connection.commit()
        finally:
            print('Success!')

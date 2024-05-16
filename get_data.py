from fastapi import FastAPI
from utils.sqlutil import SqlConn
from utils.config_connect_db import config_sql
from datetime import datetime
import json

# Create an instance of the FastAPI class
app = FastAPI()


def api_getdata(user):
    server, database, username, password, driver = config_sql()
    with SqlConn(server, username, password, driver) as _sql:
        # values = (input_product)
        sp_query_data= f"""\
                       SELECT * FROM public.tweets t
                        JOIN public.users u ON t.tweet_user_id = u.user_id
                        WHERE t.tweet_user_id = '@{user}'
                        """
        print(sp_query_data)
        result = _sql._yeild_execute(database, sp_query_data)
        dict_data = {'User':        [getattr(item, 'tweet_user_id') for item in result],
                    'Username':     [getattr(item, 'user_name') for item in result],
                    'Tweet':        [getattr(item, 'tweet_detail') for item in result],
                    'Date':         [getattr(item, 'tweet_date_created') for item in result],
                    'Link':         [getattr(item, 'tweet_link') for item in result],
                    'Date':         [getattr(item, 'tweet_date_created').strftime('%Y-%m-%d %H:%M:%S') for item in result],
        }

        return json.dumps(dict_data)

# Define a route using a decorator
@app.get("/api/user={user}")
def read_root(user):
    # return {'user':user, 'tag':tag}
    return api_getdata(user)

# Define another route
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

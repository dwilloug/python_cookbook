from pandas import DataFrame
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL

import settings

def db_connect():
    return create_engine(URL(**settings.DATABASE))

def build_connection(engine):
    return engine.connect()

engine = db_connect()
con = build_connection(engine)

def get_profiles_data_frame(team, agent_level):
    select_inc = text(
        'SELECT * FROM public."' + team + '_profiles" WHERE profiles = :agent_level'
    )
    prof = conn.execute(select_inc, agent_level=str(agent_level))
    profile_df = DataFrame(prof.fetchall())
    profile_df.columns = prof.keys()
    return profile_df
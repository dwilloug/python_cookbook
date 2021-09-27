import re

import pandas as pd
from sqlalchemy import text

import common.db as db
import common.error as error_common

def generate_agent_sql_configuration(agent_name, agent_level, profile_df):
    if agent_name == "":
        raise ValueError
    if agent_level == "":
        raise ValueError
    profile_df.drop(["profile"], axis=1, inplace=True)
    maximum_load = profile_df["maximum_load"]
    profile_df.drop(["maximum_load"], axis=1, inplace=True)
    skills_list = profile_df.columns.tolist()
    if skills_list == []:
        raise ValueError
    skills = profile_df.to_dict(orient="records")[0]
    column_string = "( {}, {}, {}, {}, {}, {} ".format(
        "agent_name",
        "agent_level",
        "last_leveled",
        "availability",
        "load_points",
        "maximum_load",
    )
    for skill in skills_list:
        if re.match("^[a-zA-Z0-9_]*$", skill):
            column_string = column_string + ", {}, {}_last_worked".format(skill, skill)
        else:
            raise ValueError
    column_string = column_string + " )"
    value_string = "( {}, {}, {}, {}, {}, {} ".format(
        agent_name, agent_level, "now()", "False", 0, maximum_load[0]
    )
    for skill in skills_list:
        value_string = value_string + ", {}, now()".format(skills[skill])
    value_string = value_string + " )"
    string_map = {"column_string": column_string, "value_string": value_string}
    return string_map

def add_agent_sql_configuration(agent, team):
    try:
        agent_name = agent["name"]
        agent_level = agent["level"]
    except KeyError as e:
        error = error_common.build_error(True, e, 400)
        return error
    profile_df = db.get_profiles_data_frame(team, agent_level)
    sql_configuration = generate_agent_sql_configuration(
        agent_name, agent_level, profile_df
    )
    return sql_configuration

def add_profile_sql_configuration(profile, load_points, skills):
    column_string = "( {}, {} ".format("profile", "maximum_load")
    for skill in skills:
        if re.match("^[a-zA-Z0-9_]*$", skill):
            column_string = column_string + ", {}".format(skill)
        else:
            raise ValueError
    column_string = column_string + " )"
    value_string = "( '{}', {}".format(profile, load_points)
    for skill in skills:
        value_string = value_string + ", {}".format(skills[skill] * 1000)
    value_string = value_string + " )"
    string_map = {"column_string": column_string, "value_string": value_string}
    return string_map
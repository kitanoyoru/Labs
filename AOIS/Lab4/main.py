import os

import orjson as json

from typing import Optional

from lab4.formulas import SKNF, SDNF
from lab4.operations import get_minimized, irredudant_calculated_tabular


# Load data

data_path = os.path.join(os.getcwd(), "data", "data.json")

data: Optional[dict] = None

with open(data_path, "r") as f:
    data = json.loads(f.read())

if data is None:
    raise Exception("failed to load data")


# Minimized

table_p = SKNF.create_sknf_table(data["P"])
table_s = SKNF.create_sknf_table(data["S"])

short_form_p = get_minimized(table_p, SKNF.create_short_sknf_form)
short_form_s = get_minimized(table_s, SKNF.create_short_sknf_form)

print("Min P:", irredudant_calculated_tabular(SKNF.create_sknf(data["P"]), short_form_p, '*'))
print("Min S:", irredudant_calculated_tabular(SKNF.create_sknf(data["S"]), short_form_s, '*'))

table_y1 = SDNF.create_sdnf_table(data["Y1"])
short_form_y1 = get_minimized(table_y1, SDNF.create_short_sdnf_form)

table_y2 = SDNF.create_sdnf_table(data["Y2"])
short_form_y2 = get_minimized(table_y2, SDNF.create_short_sdnf_form)

table_y3 = SDNF.create_sdnf_table(data["Y3"])
short_form_y3 = get_minimized(table_y3, SDNF.create_short_sdnf_form)

table_y4 = SDNF.create_sdnf_table(data["Y4"])
short_form_y4 = get_minimized(table_y4, SDNF.create_short_sdnf_form)

print("Min Y1:", irredudant_calculated_tabular(SDNF.create_sdnf(data["Y1"]), short_form_y1, '+'))
print("Min Y2:", irredudant_calculated_tabular(SDNF.create_sdnf(data["Y2"]), short_form_y2, '+'))
print("Min Y3:", irredudant_calculated_tabular(SDNF.create_sdnf(data["Y3"]), short_form_y3, '+'))
print("Min Y4:", irredudant_calculated_tabular(SDNF.create_sdnf(data["Y4"]), short_form_y4, '+'))

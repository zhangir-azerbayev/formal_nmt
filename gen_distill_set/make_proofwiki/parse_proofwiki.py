import os 
import sys
import json
import ndjson 
import re

with open("raw_proofwiki.json") as f:
    struct = json.load(f)

data = []

for thm in struct["dataset"]["theorems"]:
    if thm["contents"]:
        statement = re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1", " ".join(thm["contents"]))
        statement = re.sub(r":\$", r"$", statement)
        statement = re.sub(r"\{\{begin-eqn\}\}\s*", r"$$", statement)
        statement = re.sub(r"\s*\{\{end-eqn\}\}", r"$$", statement)
        statement = re.sub(r"\{\{\s*eqn\s*\|\s*l\s*=\s*(.*?)\s*\|\s*r\s*=\s*(.*?)\s*\}\}", r"\1 = \2,", statement)
        statement = re.sub(r",\$\$$", r".$$", statement)
        print("THEOREM: ", statement)
        data.append({"nl_statement": statement, "id": thm["id"]})

with open("proofwiki.jsonl", "w") as f: 
    ndjson.dump(data, f)

from app import *
import os
import json

db.create_all()

def declare_chal(data):
    chal = Challenges.query.filter_by(name=data["name"]).first()
    if chal is not None:
        for n in data:
            if n == "name": continue
            setattr(chal, n, data[n])
    else:
        data["solves"] = "0"
        data["score"] = str(MAX_SCORE)
        db.session.add(Challenges(**data))
    db.session.commit()

for file in os.listdir("./chals"):
    if file.endswith(".json"):
        with open(os.path.join("./chals", file)) as fd:
            chal = json.load(fd)
        declare_chal(chal)

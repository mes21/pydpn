from pydpn import DeeperNetwork
import json

login = json.load(open(f"c://temp/deepercred.json", "r"))

p = DeeperNetwork(**login)
p

import sys
from pathlib import Path
from ruamel.yaml import YAML

val = 'my-image:version'
subst = sys.argv[1]
file_name = Path(sys.argv[2])

def update(d, val, sub):
    if isinstance(d, dict):
        for k in d:
            v = d[k]
            if v == val:
                d[k] = sub
            else:
                update(v, val, sub)
    elif isinstance(d, list):
        for item in d:
            update(item, val, sub)

yaml = YAML()
yaml.preserve_quotes = True  # to preserve superfluous quotes in the input
data = yaml.load(file_name)
update(data, val, subst)
yaml.dump(data, file_name)
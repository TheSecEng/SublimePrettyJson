from collections import defaultdict
from xml.etree import cElementTree as ET


def xml_to_etree(xml_data: str):
    return ET.XML(xml_data)


# Description: Thanks StackOverflow
# - https://stackoverflow.com/a/10077069/1998673
def etree_to_dict(etree):
    d = {etree.tag: {} if etree.attrib else None}
    children = list(etree)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {etree.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if etree.attrib:
        d[etree.tag].update(('@' + k, v) for k, v in etree.attrib.items())
    if etree.text:
        text = etree.text.strip()
        if children or etree.attrib:
            if text:
                d[etree.tag]['#text'] = text
        else:
            d[etree.tag] = text
    return d

import xml.etree.ElementTree as ET

def xmlek(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    dane = {root.tag: {}}

    def pars_element(element, parent):
        for child in element:
            if len(child) > 0:
                parent[child.tag] = {}
                pars_element(child, parent[child.tag])
            else:
                parent[child.tag] = child.text
    pars_element(root, dane[root.tag])
    return dane

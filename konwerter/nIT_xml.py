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


def save_xmlek(dane, xml_file):
    def d_t_e(tag, d):
        elem = ET.element(tag)
        for key, val in d.items():
            child = d_t_e(key, val) if isinstance(val,dict) else ET.element(key)
            child.text = str(val)
            elem.append(child)
        return elem
    root_tag = list(dane.keys())[0]
    root_elem = d_t_e(root_tag, dane[root_tag])
    tree = ET.ElementTree(root_elem)
    tree.write(xml_file)
def build_xml_elements(parent_element, data):
    for key, value in data.items():
        if isinstance(value, dict):
            element = ET.SubElement(parent_element, key)
            build_xml_elements(element, value)
        elif isinstance(value, list):
            for item in value:
                element = ET.SubElement(parent_element, key)
                if isinstance(item, dict):
                    build_xml_elements(element, item)
                else:
                    element.text = str(item)
        else:
            if key.startswith('@'):
                parent_element.set(key[1:], str(value))
            else:
                element = ET.SubElement(parent_element, key)
                element.text = str(value)

def build_xml_element(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key.startswith("@"):
                    attribute_name = key[1:]
                    parent.set(attribute_name, str(value))
                elif isinstance(value, dict):
                    element = ET.SubElement(parent, key.replace(" ", "_"))
                    build_xml_element(element, value)
                elif isinstance(value, list):
                    for item in value:
                        subelement = ET.SubElement(parent, key.replace(" ", "_"))
                        build_xml_element(subelement, item)
                else:
                    element = ET.SubElement(parent, key.replace(" ", "_"))
                    element.text = str(value)
        else:
            parent.text = str(data)

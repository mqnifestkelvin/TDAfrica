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

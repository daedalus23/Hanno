import xml.etree.ElementTree as ET


class LoadXML:
    def __init__(self, xmlPath, serviceName):
        with open(xmlPath, "r") as xmlfile:
            self.tree = ET.ElementTree(ET.fromstring(xmlfile.read()))
            self.root = self.tree.getroot()
            self.name = serviceName
            self.service = self.find_service(serviceName)
            self.configuration = {}
            self.attributes = {}
            self.actions = {}
            for child in self.service:
                if child.tag == 'configuration':
                    for attr in child:
                        self.configuration[attr.tag] = self.type_check(attr)
                elif child.tag == 'attributes':
                    for attr in child:
                        self.attributes[attr.tag] = self.type_check(attr)
                elif child.tag == 'actions':
                    for command in child.iter('command'):
                        self.actions[command.attrib['id']] = {
                            'commandCall': command.attrib['id'],
                            'continuous': command.find('continuous').text.lower() == 'true'
                        }

    @staticmethod
    def type_check(arg):
        if arg.attrib['type'] == 'float':
            return float(arg.text)
        elif arg.attrib['type'] == "int":
            return int(arg.text)
        elif arg.attrib['type'] == "bool":
            return bool(arg.text)
        else:
            return str(arg.text)

    def find_service(self, name):
        for service in self.root.findall('service'):
            if service.attrib['name'] == name:
                return service
        raise ValueError(f"No service with name '{name}' found in the XML file.")

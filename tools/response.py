import re
import json
from tools import all_tools


class Response:
    def __init__(self, data):
        self.action = None
        if type(data) == 'dict':
            self._parse_json(data)
        else:
            self._parse_text(data)

    def _parse_json(self, data):
        if "action" in data:
            self.action = data["action"]
        elif "final_answer" in data:
            self.action = search_tool_name(data["final_answer"])

    def _parse_text(self, text):
        is_json = False
        json_data = None
        try:
            json_data = json.loads(text)
            is_json = True
            self._parse_json(json_data)
        except:
            print("failed text:")
            print(text)

        if not is_json:
            left = text.find("{")
            right = text.find("}")
            if left != -1 and right != -1 and left < right:
                text = text[left: right+1]
                data = json.loads(text)
                self._parse_json(data)
            else:
                self.action = search_tool_name(text)


def search_tool_name(text):
    tool_names = [tool._name for tool in all_tools]
    ret = re.search("|".join(tool_names), text)
    if ret:
        return ret.group(0)
    return None

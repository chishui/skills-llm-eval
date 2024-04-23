import re
import json
from tools import all_tools


class Response:
    def __init__(self, text):
        self.action = None
        self._parse(text)

    def _parse(self, text):
        left = text.find("{")
        right = text.find("}")
        if left != -1 and right != -1 and left < right:
            text = text[left: right+1]
            data = json.loads(text)
            if "action" in data:
                self.action = data["action"]
            elif "final_answer" in data:
                self.action = search_tool_name(data["final_answer"])
        else:
            self.action = search_tool_name(text)


def search_tool_name(text):
    tool_names = [tool._name for tool in all_tools]
    ret = re.search("|".join(tool_names), text)
    if ret:
        return ret.group(0)
    return None

from tools import all_tools


def load_basic_prompt(yaml_file):
    from yaml import load, dump
    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    with open(yaml_file, "r") as f:
        data = load(f, Loader=Loader)
        return data


def generate_prompt(user_input, basic_prompt):
    prompt = [basic_prompt["INTRODUCTION"], basic_prompt["TOOLS_INTRODUCTION"], "<tools>"]

    for tool in all_tools:
        prompt.append("<tool>")
        prompt.append(tool.generate_prompt())
        prompt.append("</tool>")
    prompt.append("</tools>")

    prompt.append(basic_prompt["RESPONSE_FORMAT_INSTRUCTION"])
    prompt.append(basic_prompt["USER_INPUT"].replace("[user_input]", user_input))

    return "\n".join(prompt)

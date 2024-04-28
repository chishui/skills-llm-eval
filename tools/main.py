import json
import traceback
from clients.client import Claude1, Claude3Haiku
from prompt import generate_prompt, load_basic_prompt
from response import Response
from progress.bar import Bar

claude_client = Claude1()


def evaluate(data_file, yaml_file):
    results = []
    success_count = 0
    basic_prompt = load_basic_prompt(yaml_file)
    index = 0
    with open(data_file, "r") as f:
        lines = f.readlines()
        bar = Bar('Processing', max=len(lines))
        for line in lines:
            index = index + 1
            data = json.loads(line)
            question = data["question"]
            expected_tool = data["tool"]
            try:
                prompt = generate_prompt(question, basic_prompt)
                llm_response = claude_client.run(prompt)
                response = Response(llm_response)
                if response.action == expected_tool:
                    results.append({"id": index, "result": True})
                    success_count = success_count + 1
                else:
                    results.append({"id": index, "result": False, "expected": expected_tool,
                                    "llm_selected": response.action, "question": question, "llm_response": llm_response})
            except Exception:
                print(traceback.format_exc())
                print(f"exception: id: {index}, line: {line}")
            finally:
                bar.next()
    bar.finish()
    print(results)
    print(f"success rate %: {100 * success_count/index}")


if __name__=="__main__":
    evaluate("/Users/xiliyun/Downloads/data_within_tool_subset.json", "prompts/basic.yml")





import json
from client import Claude
from prompt import generate_prompt
from response import Response

claude_client = Claude()


def evaluate(data_file):
    results = []
    success_count = 0
    with open(data_file, "r") as f:
        lines = f.readlines()
        index = 0
        for line in lines:
            index = index + 1
            data = json.loads(line)
            question = data["question"]
            expected_tool = data["tool"]
            try:
                prompt = generate_prompt(question)
                llm_response = claude_client.run(prompt)
                response = Response(llm_response)
                if response.action == expected_tool:
                    results.append({"id": index, "result": True})
                    success_count = success_count + 1
                else:
                    results.append({"id": index, "result": False, "expected": expected_tool,
                                    "llm_selected": response.action, "llm_response": llm_response})
            except Exception as e:
                print(e)
                print(f"exception: id: {index}, line: {line}")
    print(results)
    print(f"success rate %: {100 * success_count/len(results)}")


if __name__=="__main__":
    evaluate("/Users/xiliyun/Downloads/data_within_tool_subset.json")





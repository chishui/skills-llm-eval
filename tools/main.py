import json
import argparse
import traceback
from clients.client import Claude1, Claude3Haiku
from prompt import generate_prompt, load_basic_prompt
from response import Response
from progress.bar import Bar
from utils.log import logger, DEBUG_INFO


def evaluate(client, data_file, yaml_file, data_size):
    results = []
    success_count = 0
    basic_prompt = load_basic_prompt(yaml_file)
    index = 0
    with open(data_file, "r") as f:
        lines = f.readlines()
        if data_size > 0:
            lines = lines[:data_size]
        bar = Bar('Processing', max=len(lines))
        for line in lines:
            index = index + 1
            data = json.loads(line)
            question = data["question"]
            expected_tool = data["tool"]
            try:
                prompt = generate_prompt(question, basic_prompt)
                llm_response = client.run(prompt)
                response = Response(llm_response)
                if response.action == expected_tool:
                    results.append({"id": index, "result": True})
                    success_count = success_count + 1
                else:
                    results.append({"id": index, "result": False, "expected": expected_tool,
                                    "llm_selected": response.action, "question": question, "llm_response": llm_response})
            except Exception:
                logger.error(traceback.format_exc())
                logger.error(f"exception: id: {index}, line: {line}")
            finally:
                bar.next()
    bar.finish()
    logger.info(results)
    logger.info(f"success rate %: {100 * success_count/index}")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-file", required=True)
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--llm-name", choices=["claude1", "claude3-haiku"], required=True)
    parser.add_argument("--data-size", type=int, default=1, required=True)
    parser.add_argument("--verbose", action='store_true')

    return parser.parse_args()


def get_client(llm_name):
    if llm_name == "claude1":
        return Claude1()
    elif llm_name == "claude3-haiku":
        return Claude3Haiku()


if __name__=="__main__":
    args = get_args()
    if args.verbose:
        logger.setLevel(DEBUG_INFO)
    client = get_client(args.llm_name)
    evaluate(client, args.data_file, args.prompt_file, data_size=args.data_size)





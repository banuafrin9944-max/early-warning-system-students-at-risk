import argparse
import json
from agent.core import AgentExecutor
from agent.llm import LLM
from tools import build_tools

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    agent = AgentExecutor(LLM(), build_tools())
    answer, trace = agent.run(args.query)

    if args.json:
        print(json.dumps({
            "answer": answer,
            "trace": trace
        }))
    else:
        print(answer)

if __name__ == "__main__":
    main()



   

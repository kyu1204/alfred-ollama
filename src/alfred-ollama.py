import sys

import requests
from workflow import Workflow


def main(wf):
    args = wf.args[0]
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama2",
        "prompt": args,
        "stream": False,
    }
    response = requests.post(url, json=data)
    response.raise_for_status()

    result = response.json()
    wf.add_item(
        title=args,
        subtitle=result["response"],
        valid=True,
        arg=result["response"],
    )
    wf.send_feedback()


if __name__ == "__main__":
    workflow = Workflow()
    sys.exit(workflow.run(main))

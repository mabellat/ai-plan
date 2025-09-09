from __future__ import annotations
import json, time, os
from typing import Any, Dict, List, Callable, Tuple, Optional

# Skeleton ReAct-style agent. Plug in your LLM and tools.
# For production: add tracing, budgets, safety filters, and eval hooks.

class Tool:
    def __init__(self, name: str, desc: str, fn: Callable[[str], str]):
        self.name, self.desc, self.fn = name, desc, fn

class ReActAgent:
    def __init__(self, llm_call: Callable[[str], str], tools: List[Tool], max_steps: int = 8):
        self.llm_call = llm_call
        self.tools = {t.name: t for t in tools}
        self.max_steps = max_steps

    def run(self, task: str) -> str:
        scratch = []
        for step in range(self.max_steps):
            prompt = self._format_prompt(task, scratch)
            thought = self.llm_call(prompt)
            if thought.startswith("FINAL:" ):
                return thought[len("FINAL:"):].strip()
            # expected format: TOOL[tool_name]: input
            if thought.startswith("TOOL[") and "]:" in thought:
                tool_name = thought.split("TOOL[")[1].split("]:")[0].strip()
                tool_input = thought.split("]:",1)[1].strip()
                if tool_name not in self.tools:
                    scratch.append({"error": f"Unknown tool {tool_name}"})
                    continue
                out = self.tools[tool_name].fn(tool_input)
                scratch.append({"tool": tool_name, "input": tool_input, "output": out})
            else:
                scratch.append({"thought": thought})
        return "FINAL: (max steps reached)"

    def _format_prompt(self, task: str, scratch: List[Dict[str, str]]) -> str:
        prefix = (
            "You are a helpful agent. Think step by step.\n"
            "When you need a tool, respond as 'TOOL[tool_name]: <input>'.\n"
            "When done, respond as 'FINAL: <answer>'.\n"
            "Available tools: " + ", ".join(f"{n}" for n in self.tools) + "\n\n"
        )
        transcript = "\n".join(json.dumps(s) for s in scratch[-6:])
        return f"{prefix}TASK: {task}\nSCRATCH:\n{transcript}\nNEXT:"

# Example tools
def calculator(inp: str) -> str:
    try:
        return str(eval(inp, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"error: {e}"

def echo(inp: str) -> str:
    return inp

def dummy_llm(prompt: str) -> str:
    # Placeholder. Replace with real LLM call.
    if "2+2" in prompt:
        return "TOOL[calculator]: 2+2"
    return "FINAL: Hello from dummy LLM."

if __name__ == "__main__":
    agent = ReActAgent(dummy_llm, [Tool("calculator","safe arithmetic", calculator), Tool("echo","echo text", echo)])
    print(agent.run("Compute 2+2 then say hi"))

import json
import os
import time


class ReflectionAgent:
    """
    A deterministic CLI agent that walks an employee through the
    Daily Reflection Tree — no LLM calls at runtime.
    """

    # Human-readable labels for state values shown in the summary
    STATE_LABELS = {
        "locus": {
            "victim": "reactive, externally-driven",
            "victor": "proactive, agency-led"
        },
        "orientation": {
            "entitled": "receiving-focused",
            "contributor": "contribution-focused"
        },
        "radius": {
            "self": "personally-centered",
            "altro": "outward-looking"
        }
    }

    def __init__(self, tree_path):
        self.tree_path = tree_path
        self.tree = self._load_tree()

        # Axis state — set by decision nodes
        self.state = {
            "locus": "unknown",
            "orientation": "unknown",
            "radius": "unknown"
        }

        # Answer store — records the text of every answer chosen
        # Used for {node_id} interpolation in questions and reflections
        self.answers = {}

    # ─────────────────────────────────────────────
    # Setup
    # ─────────────────────────────────────────────

    def _load_tree(self):
        """Load and return the nodes dict from the JSON tree file."""
        try:
            with open(self.tree_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['nodes']
        except FileNotFoundError:
            print(f"\n  Error: Tree file not found at '{self.tree_path}'")
            print("  Make sure you're running this from the project root.\n")
            exit(1)
        except json.JSONDecodeError as e:
            print(f"\n  Error: Invalid JSON in tree file — {e}\n")
            exit(1)

    # ─────────────────────────────────────────────
    # Display helpers
    # ─────────────────────────────────────────────

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _print(self, text, prefix="  ", delay=0.4):
        """Print text with a short pause for a conversational feel."""
        print(f"\n{prefix}{text}")
        time.sleep(delay)

    def _divider(self, char="─", width=50):
        print(f"\n  {char * width}")

    def _interpolate(self, text):
        """
        Replace {node_id} placeholders with the user's actual answer
        for that node. Also replaces {locus}, {orientation}, {radius}
        with human-readable state labels for the summary node.
        """
        # Replace answer placeholders
        for node_id, answer_text in self.answers.items():
            text = text.replace(f"{{{node_id}}}", answer_text)

        # Replace state placeholders with readable labels
        for key, mapping in self.STATE_LABELS.items():
            raw_value = self.state.get(key, "unknown")
            readable = mapping.get(raw_value, raw_value)
            text = text.replace(f"{{{key}}}", readable)

        return text

    # ─────────────────────────────────────────────
    # Input handling
    # ─────────────────────────────────────────────

    def _get_choice(self, max_options):
        """Prompt until the user enters a valid number."""
        while True:
            try:
                raw = input("\n  Your choice (enter a number): ").strip()
                idx = int(raw)
                if 1 <= idx <= max_options:
                    return idx
                print(f"  Please enter a number between 1 and {max_options}.")
            except ValueError:
                print("  Please enter a number.")

    # ─────────────────────────────────────────────
    # Node handlers
    # ─────────────────────────────────────────────

    def _handle_start(self, node):
        self._clear()
        self._divider("═")
        self._print(node["text"], prefix="  ✨  ", delay=0.6)
        self._divider("═")
        input("\n  [Press Enter to begin your reflection]")
        return node["next"]

    def _handle_question(self, node):
        text = self._interpolate(node["text"])
        self._print(text, prefix="  ❓  ")
        options = node["options"]
        print()
        for i, opt in enumerate(options, 1):
            print(f"     {i}.  {opt['text']}")

        choice_idx = self._get_choice(len(options))
        selected = options[choice_idx - 1]

        # Store the chosen answer text for later interpolation
        self.answers[node["id"]] = selected["text"]

        return selected["next"]

    def _handle_decision(self, node):
        """
        Parse the logic field (e.g. 'set locus=victim') and
        update state. Invisible to the user — auto-advances.
        """
        logic = node.get("logic", "")
        if logic.startswith("set "):
            parts = logic.replace("set ", "").split("=")
            if len(parts) == 2:
                self.state[parts[0].strip()] = parts[1].strip()
        return node["next"]

    def _handle_reflection(self, node):
        text = self._interpolate(node["text"])
        self._divider()
        self._print(text, prefix="  💡  ", delay=0.6)
        self._divider()
        input("\n  [Press Enter to continue]")
        return node["next"]

    def _handle_bridge(self, node):
        text = self._interpolate(node["text"])
        self._divider("·")
        self._print(text, prefix="  🌉  ", delay=0.5)
        self._divider("·")
        time.sleep(0.8)
        return node["next"]

    def _handle_summary(self, node):
        text = self._interpolate(node["text"])
        self._divider("═")
        self._print("YOUR REFLECTION SUMMARY", prefix="  📊  ", delay=0.3)
        self._divider("═")
        self._print(text, delay=0.6)
        self._divider("═")
        return node["next"]

    def _handle_end(self, node):
        self._print(node["text"], prefix="  🏁  ", delay=0.5)
        print()
        return None

    # ─────────────────────────────────────────────
    # Main loop
    # ─────────────────────────────────────────────

    def run(self):
        """Traverse the tree from start to end."""
        current_id = "start"

        handlers = {
            "start":      self._handle_start,
            "question":   self._handle_question,
            "decision":   self._handle_decision,
            "reflection": self._handle_reflection,
            "bridge":     self._handle_bridge,
            "summary":    self._handle_summary,
            "end":        self._handle_end,
        }

        while current_id:
            node = self.tree.get(current_id)
            if not node:
                print(f"\n  Error: Node '{current_id}' not found in tree.")
                break

            node_type = node.get("type")
            handler = handlers.get(node_type)

            if handler:
                current_id = handler(node)
            else:
                print(f"\n  Warning: Unknown node type '{node_type}'. Skipping.")
                current_id = node.get("next")


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Resolve tree path relative to project root
    # Works whether you run from /agent/ or from project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "tree", "reflection-tree.json")

    agent = ReflectionAgent(json_path)
    agent.run()
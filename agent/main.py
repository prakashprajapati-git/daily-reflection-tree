import json
import os
import time

class ReflectionAgent:
    def __init__(self, tree_path):
        self.tree_path = tree_path
        self.tree = self.load_tree()
        self.state = {
            "locus": "unknown",
            "orientation": "unknown",
            "radius": "unknown"
        }

    def load_tree(self):
        """Loads the JSON tree from the specified path."""
        try:
            with open(self.tree_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['nodes']
        except FileNotFoundError:
            print(f"Error: Could not find tree at {self.tree_path}")
            exit(1)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_wrapped(self, text, prefix=""):
        """Prints text with a slight delay for a conversational feel."""
        print(f"\n{prefix}{text}")
        time.sleep(0.5)

    def run(self):
        """Main loop to traverse the tree."""
        current_node_id = "start"
        
        while current_node_id:
            node = self.tree.get(current_node_id)
            if not node:
                break

            node_type = node.get("type")

            if node_type == "start":
                self.clear_screen()
                self.print_wrapped(node["text"], "✨ ")
                current_node_id = node["next"]

            elif node_type == "question":
                self.print_wrapped(node["text"], "❓ ")
                options = node["options"]
                for i, opt in enumerate(options, 1):
                    print(f"   {i}. {opt['text']}")
                
                choice = self.get_user_input(len(options))
                current_node_id = options[choice - 1]["next"]

            elif node_type == "decision":
                # Process logic (e.g., "set locus=victim")
                logic = node.get("logic", "")
                if "set " in logic:
                    key_val = logic.replace("set ", "").split("=")
                    if len(key_val) == 2:
                        self.state[key_val[0]] = key_val[1]
                current_node_id = node["next"]

            elif node_type == "reflection":
                self.print_wrapped(node["text"], "💡 ")
                input("\n[Press Enter to continue]")
                current_node_id = node["next"]

            elif node_type == "bridge":
                print("\n" + "-"*40)
                self.print_wrapped(node["text"], "🌉 ")
                print("-"*40)
                current_node_id = node["next"]

            elif node_type == "summary":
                # Interpolate placeholders with state
                summary_text = node["text"].format(
                    locus=self.state["locus"],
                    orientation=self.state["orientation"],
                    radius=self.state["radius"]
                )
                self.print_wrapped("FINAL REFLECTION", "📊 ")
                self.print_wrapped(summary_text)
                current_node_id = node["next"]

            elif node_type == "end":
                self.print_wrapped(node["text"], "🏁 ")
                current_node_id = None

    def get_user_input(self, max_options):
        """Ensures valid numeric input from the user."""
        while True:
            try:
                val = input("\nSelect an option (number): ")
                idx = int(val)
                if 1 <= idx <= max_options:
                    return idx
                print(f"Please choose a number between 1 and {max_options}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Path relative to the root of the project
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "tree", "reflection-tree.json")
    
    agent = ReflectionAgent(json_path)
    agent.run()
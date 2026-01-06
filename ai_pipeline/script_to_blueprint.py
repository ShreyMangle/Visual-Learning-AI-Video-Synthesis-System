import json
import os
from topic_to_script import generate_script

script = generate_script("Load Balancing")

blueprint = []
for s in script:
    blueprint.append({
        "scene": s["scene"],
        "elements": ["boxes", "arrows", "text"],
        "animation": "fade_in",
        "duration": 4,
        "narration": s["narration"]
    })

base_dir = os.path.dirname(__file__)
output_path = os.path.join(base_dir, "blueprint.json")

with open(output_path, "w") as f:
    json.dump(blueprint, f, indent=2)

print("Blueprint generated successfully inside ai_pipeline.")

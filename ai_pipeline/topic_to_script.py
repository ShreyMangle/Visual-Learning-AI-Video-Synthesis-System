def generate_script(topic):
    return [
        {
            "scene": 1,
            "visual": "Users sending requests",
            "narration": "Multiple users send requests at the same time."
        },
        {
            "scene": 2,
            "visual": "Server overload",
            "narration": "A single server cannot handle all requests."
        },
        {
            "scene": 3,
            "visual": "Load balancer distributes traffic",
            "narration": "A load balancer distributes traffic evenly."
        }
    ]
    
if __name__ == "__main__":
    script = generate_script("Load Balancing")
    for s in script:
        print(f"Scene {s['scene']}: {s['narration']}")


import os
import json

def generate_main_json(input_dir, output_file):
    main_json = {
        "Free": {
            "description": "Completely free, long-term usable Jupyter notebook environments without hidden costs or mandatory subscription."
        },
        "Cloud": {
            "description": "Notebook services provided by major cloud platforms, usually tied to existing cloud accounts or limited-time trials."
        },
        "Subscription": {
            "description": "Platforms offering Jupyter notebooks primarily through paid subscription models, typically with limited or no free tier."
        }
    }

    for category in ["free", "cloud", "subscription"]:
        category_dir = os.path.join(input_dir, category)
        if os.path.exists(category_dir):
            for filename in os.listdir(category_dir):
                if filename.endswith(".json"):
                    filepath = os.path.join(category_dir, filename)
                    with open(filepath, "r", encoding="utf-8") as f:
                        provider_data = json.load(f)
                        provider_name, provider_content = next(iter(provider_data.items()))
                        # Kategorie im Main-JSON schreiben (Großschreibung!)
                        main_json[category.capitalize()][provider_name] = provider_content

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(main_json, out, indent=4, ensure_ascii=False)

# Nutzung:
generate_main_json("providers", "main.json")

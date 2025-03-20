# jupyter-provider
All about Jupyter-Labs and Books in SaaS. 

This repository provides a structured JSON dataset containing comprehensive information about public and commercial Jupyter notebook providers. It serves as a reference, decision-making aid, and systematic evaluation resource for selecting suitable providers.  
  
🇩🇪 german -> liesmich.md  

## 1. Introduction & Purpose

This dataset helps users, researchers, and teams find, compare, and make informed decisions about suitable Jupyter notebook environments. Emphasis is placed on transparency, data quality assurance, and collaborative maintenance (open-research approach).

## 2. Provider Categories

Providers are clearly divided into three main groups:

- **Free**: Completely free notebook environments without long-term costs.
- **Cloud**: Notebook services from major cloud platforms (AWS, Azure, GCP, etc.), usually linked to existing cloud accounts.
- **Subscription**: Commercial providers mainly via subscription with limited or no free options.

## 3. Attributes and Attribute Groups

Each provider is characterized in detail by the following groups:

- **Basics**: General information like description, URL, provider name.
- **Access**: Access options, registration requirements, OAuth logins, session durations, import/export capabilities.
- **Functionality**: Functional capabilities (GPU/TPU availability, JupyterLab support).
- **Scalability**: Resource limits (RAM, CPU, storage).
- **Integrations**: Integration with external services (e.g., Git or cloud storage).
- **Security**: Data protection, encryption, authentication methods.
- **Community**: Documentation availability, support channels, community size.
- **SWOT**: Strengths and weaknesses of each platform.

## 4. JSON Schema & Quality Control

To ensure data quality and transparency, each attribute includes:

- `lastCheck`: Date of last verification (group level).
- `confidence`: Quality indicator:
  - `["high"]`: Verified information with optional source URL.
  - `["medium"]`: Plausible information without explicit source.
  - `["low"]`: Uncertain or estimated.

Confidence for each attribute group and the entire provider is automatically aggregated:

- **All attributes high** → group confidence = `high`
- **At least one medium, no low** → group = `medium`
- **At least one attribute low** → group = `low`

Attributes marked as uncertain (`"available": "unsure"`) also include:

- `reasoning`: Explanation for uncertainty.
- `lastCheck`: Date of last check.

## 5. Maintenance, Community & Open Research

This dataset thrives on shared knowledge. Please help by:

- Checking and correcting existing data.
- Adding missing details and sources.
- Regularly updating information.

Pull requests, issues, and discussions are warmly welcome!

## 6. Technical Merging (CI/CD)

JSON data is maintained per provider in individual files and merged automatically:

```bash
providers/
├── free/
│   ├── kaggle-kernels.json
│   └── google-colab.json
├── cloud/
└── subscription/
```

Use the provided Python script to merge data:

```python
import os, json

def generate_main_json(input_dir, output_file):
    main_json = {"Free":{}, "Cloud":{}, "Subscription":{}}
    for category in ["free", "cloud", "subscription"]:
        category_path = os.path.join(input_dir, category)
        for provider_json in os.listdir(category_path):
            with open(os.path.join(category_path, provider_json), "r") as f:
                data = json.load(f)
                main_key, main_value = next(iter(data.items()))
                main_json[category.capitalize()][main_key] = main_value

    with open(output_file, "w") as out:
        json.dump(main_json, out, indent=4, ensure_ascii=False)

# Example call:
generate_main_json("providers", "main.json")
```

Feel free to use issues and pull requests for continuous improvement!

## 🚀 Call to Action

- Actively use the dataset and share your feedback!
- Contribute enhancements and corrections.
- Help make knowledge open and accessible for everyone!


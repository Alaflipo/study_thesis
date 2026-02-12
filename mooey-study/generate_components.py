for i in range(1,11):

    example = f"""
    "ex{i}": {{
        "type": "image",
        "path": "mooey-study/assets/ex{i}/ex{i}.png",
        "instruction": "Look at the image carefully, then answer the questions below.",
        "instructionLocation": "sidebar",
        "style": {{ "maxWidth": "900px", "width": "100%" }},
        "nextButtonLocation": "sidebar",
        "response": [
            {{
            "id": "difference",
            "type": "longText",
            "prompt": "Describe the difference between the second image compared to the first image.",
            "location": "sidebar",
            "placeholder": "Describe the difference...",
            "required": true
            }},
            {{
                "id": "transform_1",
                "prompt": "Desribe how you would transform the first image into the second image in three or less steps",
                "type": "shortText", 
                "location": "sidebar", 
                "placeholder": "First step...",
                "required": true
            }},
            {{
                "id": "transform_2",
                "prompt": "",
                "type": "shortText", 
                "location": "sidebar", 
                "placeholder": "Second step...",
                "required": false
            }},
            {{
                "id": "transform_3",
                "prompt": "",
                "type": "shortText", 
                "location": "sidebar", 
                "placeholder": "Third step...",
                "required": false
            }}
        ]
    }},
    """
    print(example)

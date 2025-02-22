import gradio as gr

custom_css = """
/* Container that holds the button + tooltip */
.hover-container {
    position: relative;
    display: inline-block;
    margin: 1rem;
    overflow: visible;
}

/* The tooltip, initially hidden */
.hover-tooltip {
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s ease;
    width: 240px;
    background-color: #333;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 8px;
    position: absolute;
    z-index: 999;
}

/* Tooltip arrow pointing upward */
.hover-tooltip::after {
    content: "";
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    border-width: 5px;
    border-style: solid;
    border-color: transparent transparent #333 transparent;
}

/* Show the tooltip on hover */
.hover-container:hover .hover-tooltip {
    visibility: visible;
    opacity: 1;
}

/* Override overflow for Gradio’s html container */
.html-container {
    overflow: visible !important;
}

/* Override overflow for additional Gradio containers */
.hide-container,
.block {
    overflow: visible !important;
}
"""

models_data = [
    {
        "Rank": 1,
        "Model": "Maziyar/PaLM2Alpha",
        "Score": 60.12,
        "Params": "7B",
        "Architecture": "Transformer",
        "License": "Apache-2.0"
    },
    {
        "Rank": 2,
        "Model": "Maziyar/PantheraLlama",
        "Score": 59.85,
        "Params": "13B",
        "Architecture": "Transformer",
        "License": "MIT"
    },
    {
        "Rank": 3,
        "Model": "open-llm/falcon-7b",
        "Score": 59.73,
        "Params": "7B",
        "Architecture": "Transformer",
        "License": "Apache-2.0"
    },
]

def filter_models(search_query, min_score, max_score):
    filtered = []
    for item in models_data:
        if (search_query.lower() in item["Model"].lower()) and (min_score <= item["Score"] <= max_score):
            filtered.append(item)
    return filtered

def display_leaderboard(search_query, min_score, max_score):
    filtered = filter_models(search_query, min_score, max_score)
    return [
        [m["Rank"], m["Model"], m["Score"], m["Params"], m["Architecture"], m["License"]]
        for m in filtered
    ]

# Prepare initial data to display when the app loads
initial_data = [
    [m["Rank"], m["Model"], m["Score"], m["Params"], m["Architecture"], m["License"]]
    for m in models_data
]

with gr.Blocks(css=custom_css) as demo:
    tooltip_html = """
            <div class="hover-container">
                <!-- This is the element that triggers the tooltip on hover -->
                <button style="cursor: pointer;">ⓘ</button>
                
                <!-- The tooltip content -->
                <div class="hover-tooltip">
                    <strong>Name Search:</strong> Search directly by model name<br>
                    <strong>Field Search:</strong> Use field:value syntax<br>
                    <strong>Multiple Searches:</strong> Combine multiple criteria
                </div>
            </div>
            """
    gr.HTML(tooltip_html)
    

demo.launch()

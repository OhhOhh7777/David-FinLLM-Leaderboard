import gradio as gr

# Sample data for our "leaderboard"
# You can customize this with real data
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
    # Filter the models by query and score range
    filtered = []
    for item in models_data:
        if (search_query.lower() in item["Model"].lower()) and (min_score <= item["Score"] <= max_score):
            filtered.append(item)
    return filtered

def display_leaderboard(search_query, min_score, max_score):
    # Return filtered data in a 2D list for gr.DataFrame
    filtered = filter_models(search_query, min_score, max_score)
    return [
        [m["Rank"], m["Model"], m["Score"], m["Params"], m["Architecture"], m["License"]]
        for m in filtered
    ]

with gr.Blocks() as demo:
    gr.Markdown(
        """
        <h1 style="text-align:center;">Open LLM Leaderboard</h1>
        <p style="text-align:center;">
            Comparing Large Language Models in an open and reproducible way
        </p>
        """
    )
    
    with gr.Row():
        search_box = gr.Textbox(label="Search by model name", placeholder="Enter a model name...")
        min_score = gr.Slider(label="Min Score", minimum=0, maximum=100, value=0, step=0.01)
        max_score = gr.Slider(label="Max Score", minimum=0, maximum=100, value=100, step=0.01)
    
    update_button = gr.Button("Update Results")
    
    with gr.Box():
        gr.Markdown("## Leaderboard Results")
        results_table = gr.Dataframe(
            headers=["Rank", "Model", "Score", "Params", "Architecture", "License"],
            datatype=["number", "str", "number", "str", "str", "str"],
            interactive=False
        )
    
    update_button.click(
        fn=display_leaderboard,
        inputs=[search_box, min_score, max_score],
        outputs=results_table
    )

    # Show initial data on load
    results_table.update(
        [
            [m["Rank"], m["Model"], m["Score"], m["Params"], m["Architecture"], m["License"]]
            for m in models_data
        ]
    )

demo.launch()

# run_conversation.py
from cellchat_pipeline import host_workflow

def run_conversation(user_prompt):
    print(f"📝 Received Prompt: {user_prompt}")
    input_file = "data_input.csv"
    meta_file = "meta.csv"
    result = host_workflow(input_file, meta_file)
    return "✅ CellChat analysis completed successfully with selected steps."

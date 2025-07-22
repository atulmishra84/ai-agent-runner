
import gradio as gr
from rpa_logic import launch_rpa_agent

iface = gr.Interface(
    fn=launch_rpa_agent,
    inputs=[
        gr.Textbox(label="User Principal Name (UPN)", placeholder="e.g. john.doe@contoso.com"),
        gr.Textbox(label="Display Name", placeholder="e.g. John Doe"),
        gr.Textbox(label="Password", type="password")
    ],
    outputs=[
        gr.Textbox(label="Result Message"),
        gr.Image(label="Screenshot Preview")
    ],
    title="Entra RPA Bot with Screenshot",
    description="Trigger RPA to create a new user via Microsoft Entra portal and see a visual preview."
)

if __name__ == "__main__":
    iface.launch()

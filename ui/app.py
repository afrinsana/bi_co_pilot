import streamlit as st
from human_copilot import HumanCoPilot
from machine_copilot import FeedbackLoop

# Initialize components
hcp = HumanCoPilot()
feedback = FeedbackLoop()

# UI Layout
st.title("Bi-Co-Pilot Dashboard")
tab1, tab2, tab3 = st.tabs(["Chat", "Model Monitoring", "Feedback"])

with tab1:
    user_input = st.text_input("Ask HCP:")
    if user_input:
        response = hcp.run(mode="text", task=user_input)
        st.markdown(f"**HCP:** {response}")

with tab2:
    def get_performance_metrics():
        import plotly.graph_objects as go
        fig = go.Figure(data=[go.Bar(x=["Metric1", "Metric2"], y=[10, 20])])
        return fig

    st.plotly_chart(get_performance_metrics())  # Mock visualization

with tab3:
    feedback_text = st.text_area("Send feedback to MCP:")
    if st.button("Submit"):
        feedback.send_to_mcp(feedback_text)
        st.success("Feedback sent!")
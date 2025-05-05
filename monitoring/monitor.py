import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prometheus_client import start_http_server, Gauge, Counter
import time
from human_copilot.chat_interface import HumanCoPilot
from machine_copilot.model_optimizer import ModelOptimizer
import psutil

# Initialize metrics
LATENCY = Gauge('hcp_latency_ms', 'Latency of HCP responses in milliseconds')
ACCURACY = Gauge('mcp_accuracy_percent', 'Accuracy of MCP predictions in percent')
ERRORS = Counter('hcp_errors_total', 'Total errors encountered by HCP')
# Add to monitor.py
INFERENCE_TIME = Gauge('mcp_inference_time_ms', 'Time taken for MCP to process a request')
CPU_USAGE = Gauge('system_cpu_percent', 'Current CPU usage')

# Inside track_metrics():
CPU_USAGE.set(psutil.cpu_percent())  # Requires `pip install psutil`
def track_metrics():
    INFERENCE_TIME.set(mcp.get_inference_time())
    start_http_server(8000)  # Expose metrics on port 8000
    
    hcp = HumanCoPilot()  # Initialize your HCP
    mcp = ModelOptimizer()  # Initialize your MCP
    # Inside track_metrics():
    INFERENCE_TIME.set(mcp.get_inference_time())
    CPU_USAGE.set(psutil.cpu_percent())  
    INFERENCE_TIME.set(mcp.get_inference_time())
    while True:
        # 1. Measure HCP latency (real-world example)
        start_time = time.time()
        hcp_response = hcp.process_query("test query")  # Replace with actual HCP call
        LATENCY.set((time.time() - start_time) * 1000)  # Convert to ms
        
        # 2. Measure MCP accuracy (real-world example)
        accuracy = mcp.evaluate_accuracy()  # Replace with actual MCP call
        ACCURACY.set(accuracy)
        
        # 3. Track errors (if any)
        if hcp_response.get("error"):
            ERRORS.inc()
        
        time.sleep(5)  # Adjust interval as needed

if __name__ == "__main__":
    track_metrics()
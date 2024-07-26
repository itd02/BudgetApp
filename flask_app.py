from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the path where the images are saved
IMAGE_DIR = 'images'


@app.route('/')
def index():
    return '''
    <h1>Welcome to the Plot Viewer</h1>
    <ul>
        <li><a href="/plot/imports_exports">Imports and Exports 2023 vs 2024</a></li>
        <li><a href="/plot/imports_comparison">Imports Comparison 2023 vs 2024</a></li>
        <li><a href="/plot/exports_comparison">Exports Comparison 2023 vs 2024</a></li>
        <li><a href="/plot/heatmap">Heatmap of Service Values</a></li>
    </ul>
    '''


@app.route('/plot/<plot_name>')
def plot(plot_name):
    # Ensure that the plot_name is sanitized to prevent directory traversal attacks
    allowed_plots = {
        'imports_exports': 'imports_exports_2023_2024.png',
        'imports_comparison': 'imports_comparison_2023_2024.png',
        'exports_comparison': 'exports_comparison_2023_2024.png',
        'heatmap': 'heatmap_service_values.png'
    }

    if plot_name not in allowed_plots:
        return "Plot not found!", 404

    filename = allowed_plots[plot_name]
    return send_from_directory(IMAGE_DIR, filename)



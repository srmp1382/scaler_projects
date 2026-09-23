import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr
import re

def histogram(data, inp_columns):
    fig, ax=plt.subplots()
    ax.hist(data[inp_columns])
    return fig
def describe(data, inp_column):
    return data[inp_column].describe()
def outliers_plot(data, inp_column):
    fig, ax=plt.subplots()
    ax.boxplot(data[inp_column])
    return fig
def load_file(filename):
    data=pd.read_csv(filename, encoding='utf-8', encoding_errors='replace')
    numerical_cols=data.select_dtypes(include=['int64','float64']).columns.to_list()
    return data, gr.Dropdown(choices=numerical_cols, multiselect=False, value=None, label='Select your column')

with gr.Blocks() as demo:
    
    gr.Textbox("Upload your file here")
    filename=gr.UploadButton("Select your file to upload",file_types=['.csv'])
    
    with gr.Column():
        df_state=gr.State()
        selected_col=gr.Dropdown(choices=[], multiselect=False, value=None, label='Select your column')
    with gr.Column():
        hist_button=gr.Button('Plot histogram')
        hist_output=gr.Plot()

        describe_button=gr.Button('Describe your column')
        desc_output=gr.Textbox()
        outliers_button=gr.Button('Plot outliers')
        outliers_output=gr.Plot()
    filename.upload(inputs=filename, fn=load_file, outputs=[df_state, selected_col])    
    hist_button.click(inputs=[df_state, selected_col], fn=histogram, outputs=[hist_output])
    describe_button.click(inputs=[df_state, selected_col], fn=describe, outputs=[desc_output])
    outliers_button.click(inputs=[df_state, selected_col], fn=outliers_plot, outputs=[outliers_output])
demo.launch(share=True)

    
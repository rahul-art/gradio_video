import gradio as gr

def face_segmentation(img):
    # ... implement face segmentation model on input 200x200 numpy array
    # ... return segmentation mask as numpy array
    return img

webcam = gr.inputs.Image(shape=(200, 200), source="webcam")
gr.Interface(fn=face_segmentation, inputs=webcam, outputs="image").launch()

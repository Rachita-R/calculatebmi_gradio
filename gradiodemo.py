import gradio as gr

def greet_user(name, mood, color):
    return f"👋 Hello **{name}**, you seem *{mood.lower()}*! Your favorite color is {color}."

def calculate_bmi(weight, height):
    try:
        bmi = round(weight / (height/100)**2, 2)
        if bmi < 18.5:
            status = "Underweight 🥗"
        elif 18.5 <= bmi < 25:
            status = "Normal ✅"
        elif 25 <= bmi < 30:
            status = "Overweight ⚠️"
        else:
            status = "Obese 🚨"
        return f"Your BMI is {bmi} → {status}"
    except:
        return "Please enter valid numbers!"

def analyze_image(image):
    if image is None:
        return "⚠️ No image uploaded!"
    return "✅ Image received! Imagine I did some AI magic here 😉"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🌈 My Creative Dashboard  
        Welcome! Explore the tabs below.  
        This demo combines **text, forms, and image tools** in a fun way 🎉
        """
    )

    with gr.Tab("👤 About You"):
        with gr.Row():
            with gr.Column():
                name = gr.Textbox(label="Enter your Name")
                mood = gr.Radio(["Happy", "Sad", "Excited", "Calm"], label="Your Mood")
                color = gr.ColorPicker(label="Favorite Color")
                greet_btn = gr.Button("Say Hello 🎤")
            with gr.Column():
                greet_output = gr.Markdown("👈 Fill the form to see a greeting!")

        greet_btn.click(greet_user, inputs=[name, mood, color], outputs=greet_output)

    with gr.Tab("⚖️ BMI Calculator"):
        with gr.Row():
            weight = gr.Number(label="Weight (kg)")
            height = gr.Number(label="Height (cm)")
            bmi_btn = gr.Button("Calculate BMI 📊")
            bmi_output = gr.Textbox(label="Result")
        bmi_btn.click(calculate_bmi, inputs=[weight, height], outputs=bmi_output)

    with gr.Tab("🖼️ Image Fun"):
        with gr.Row():
            image_input = gr.Image(type="filepath", label="Upload your Image")
            analyze_btn = gr.Button("Analyze Image 🔍")
            image_output = gr.Label(label="Analysis Result")
        analyze_btn.click(analyze_image, inputs=image_input, outputs=image_output)

    with gr.Accordion("ℹ️ Info & Credits", open=False):
        gr.Markdown("This creative demo is powered by **Gradio** 🚀. Built to showcase interactivity.")

demo.launch()

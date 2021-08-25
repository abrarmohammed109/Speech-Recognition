from flask import Flask, render_template, request, redirect
import speech_recognition as sr
# from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)
        
        if file: 
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            text = recognizer.recognize_google(data,key=None)
            print(text)
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

from flask import Flask, request, render_template
import spacy
from spacy import displacy

# Load model outside of route for efficiency
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/entity', methods=['POST'])  # Specify only POST for clarity
def entity():
    if request.method == 'POST':
        try:
            file = request.files['file']
            readable_file = file.read().decode('utf-8', errors='ignore')
            docs = nlp(readable_file)
            html = displacy.render(docs, style='ent', jupyter=False)
            return render_template('index.html', html=html, text=readable_file)
        except Exception as e:  # Handle potential errors gracefully
            return render_template('index.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)

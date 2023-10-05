from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pass the Cloudinary video URL to the template
    cloudinary_url = "https://res.cloudinary.com/douekreel/video/upload/v1696489890/Home_Video_No_Text__9_secs_1_o9nrrb.mp4"
    return render_template('index.html', cloudinary_url=cloudinary_url)

if __name__ == '__main__':
    app.run(debug=True)
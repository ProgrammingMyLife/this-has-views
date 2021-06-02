from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    file = open("views.txt", "r+")
    views = int(open("views.txt", "r+").read())
    views += 1
    file.write(str(views))
    return f'''<center>This page has {views} views </center>'''

if __name__ == "__main__":
    app.run()
    

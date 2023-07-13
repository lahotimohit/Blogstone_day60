from flask import Flask, render_template, request
import requests
import smtplib

my_email = "engtesting23@gmail.com"
password = "szubriqmfovretnz"

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="engtechno25@gmail.com",
                msg=f"Subject: Message come from Blog Website \n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



if __name__ == "__main__":
    app.run(debug=True, port=5001)

from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from functools import wraps
  

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = "Secret key"

db = SQLAlchemy(app)


bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



class User(db.Model, UserMixin):


    __tablename__ = "user"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(250), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")


    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')


    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Web_Dev(db.Model):
    __tablename__ = "web_dev"

    course_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    rating = db.Column(db.Float)
    image = db.Column(db.String(500))
    teacher = db.Column(db.String(500))
    language = db.Column(db.String(50))
    description= db.Column(db.String(500))
    link = db.Column(db.String(500))


    def __repr__(self):
        return f"course_id:{self.course_id} title:{self.title} rating: {self.rating} image: {self.image} teacher: {self.teacher} language: {self.language}  description: {self.description} link: {self.link}"


class Design(db.Model):
    __tablename__ = "design"

    course_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    rating = db.Column(db.Float)
    image = db.Column(db.String(500))
    teacher = db.Column(db.String(500))
    language = db.Column(db.String(50))
    description= db.Column(db.String(500))
    link = db.Column(db.String(500))


    def __repr__(self):
        return f"course_id:{self.course_id} title:{self.title} rating: {self.rating} image: {self.image} teacher: {self.teacher} language: {self.language}  description: {self.description} link: {self.link}"


class Data_Science(db.Model):
    __tablename__ = "data_science"

    course_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    rating = db.Column(db.Float)
    image = db.Column(db.String(500))
    teacher = db.Column(db.String(500))
    language = db.Column(db.String(50))
    description= db.Column(db.String(500))
    link = db.Column(db.String(500))


    def __repr__(self):
        return f"course_id:{self.course_id} title:{self.title} rating: {self.rating} image: {self.image} teacher: {self.teacher} language: {self.language}  description: {self.description} link: {self.link}"


class Marketing(db.Model):
    __tablename__ = "marketing"

    course_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    rating = db.Column(db.Float)
    image = db.Column(db.String(500))
    teacher = db.Column(db.String(500))
    language = db.Column(db.String(50))
    description= db.Column(db.String(500))
    link = db.Column(db.String(500))


    def __repr__(self):
        return f"course_id:{self.course_id} title:{self.title} rating: {self.rating} image: {self.image} teacher: {self.teacher} language: {self.language}  description: {self.description} link: {self.link}"



class Finance(db.Model):
    __tablename__ = "finance"

    course_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    rating = db.Column(db.Float)
    image = db.Column(db.String(500))
    teacher = db.Column(db.String(500))
    language = db.Column(db.String(50))
    description= db.Column(db.String(500))
    link = db.Column(db.String(500))


    def __repr__(self):
        return f"course_id:{self.course_id} title:{self.title} rating: {self.rating} image: {self.image} teacher: {self.teacher} language: {self.language}  description: {self.description} link: {self.link}"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
def setup_db():
    with app.app_context():  # Ensures Flask application context is active
        db.create_all()  

        if not Web_Dev.query.first():
            Web_Dev1 =  Web_Dev(
    title="HTML CSS Basics",
    rating=8.6,
    teacher="Code With Harry",
    language="English",
    image="https://media.licdn.com/dms/image/v2/D5612AQFjHt4B6KrXaQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1681327776406?e=2147483647&v=beta&t=-ftOHvaveyQh1tGJ9_KDMKJBnvhneYu_pkZRYaWmyJw",
    link="https://www.youtube.com/watch?v=G3e-cpL7ofc"
)
            Web_Dev2 =Web_Dev(
    title="Full-Stack Web Development",
    rating=9.5,
    teacher="The Net Ninja",
    language="English",
    image="https://www.infyways.com/_next/image/?url=https%3A%2F%2Fdata.infyways.com%2Fwp-content%2Fuploads%2F2024%2F09%2Ffull-stack-development-guide.png&w=1920&q=75",
    link="https://www.youtube.com/watch?v=nu_pCVPKzTk"
)
            Web_Dev3 = Web_Dev(
    title="JavaScript Mastery",
    rating=8.9,
    teacher="Traversy Media",
    language="English",
    image="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/65ed3e0e175d4779a639f49621f65ae1/22f982bc56c541e8b487e9b6c230cab3",
    link="https://www.youtube.com/watch?v=EerdGm-ehJQ&t=666s"
)
            Web_Dev4 =Web_Dev(
    title="Responsive Web Design",
    rating=9.0,
    teacher="FreeCodeCamp",
    language="English",
    image="https://cc-dev.ccdevprojects.com/blog/wp-content/uploads/2016/10/responsive-web-design-company-India.jpg",
    link="https://www.youtube.com/watch?v=srvUrASNj0s"
)


            db.session.add_all([Web_Dev1,Web_Dev2,Web_Dev3,Web_Dev4])
            db.session.commit()

        if not Design.query.first():
            Design1 = Design(
    title="UI/UX Design Fundamentals",
    rating=9.1,
    teacher="DesignCourse",
    language="English",
    image="https://www.sottacademy.com/storage/app/public/courses/1d1gGJWsYdBOFLGfcR41EbavpPr9dkIPqOKDVxii.jpg",
    link="https://www.youtube.com/watch?v=DwmoLIAwf7Q&list=PLd-qLJXOeZDOgJuYpYrRxaYtyai2GTyQl"
)
            Design2 = Design(
    title="Graphic Design Mastery",
    rating=8.8,
    teacher="Chris Do",
    language="English",
    image="https://courses.iid.org.in/public//uploads/media_manager/621.jpg",
    link="https://www.youtube.com/watch?v=e_dv7GBHka8"
)
            Design3 = Design(
    title="Adobe Photoshop for Beginners",
    rating=9.3,
    teacher="PiXimperfect",
    language="English",
    image="https://i.ytimg.com/vi/H5sQNu6D8KE/maxresdefault.jpg",
    link="https://www.youtube.com/watch?v=IyR_uYsRdPs"
)
            Design4 =  Design(
    title="Canva Design Essentials",
    rating=8.7,
    teacher="Ronny Hermosa",
    language="English",
    image="https://instructorhq.sfo2.cdn.digitaloceanspaces.com/3/course/thumbnail/homepage-tile-canva-ess-live.jpg",
    link="https://www.youtube.com/watch?v=aYhNTZIzDf4&list=PL2jU5A3fxwC8kvuc_zB0FPzAiXwmRAoFQ"
)
            db.session.add_all([Design1, Design2,Design3, Design4])
            db.session.commit()

        if not Data_Science.query.first():
            Data_science1 = Data_Science(
    title="Data Science for Beginners",
    rating=9.0,
    teacher="Krish Naik",
    language="English",
    image="https://takeoffupskill.com/assets/images/blogs/Data-Science-Course-for-Beginers.webp",
    link="https://krishnaik.com/courses/data-science-beginners"
)
            Data_science2 = Data_Science(
    title="Python for Data Science",
    rating=9.2,
    teacher="Jose Portilla",
    language="English",
    image="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230318230239/Python-Data-Science-Tutorial.jpg",
    link="https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/"
)
            Data_science3=Data_Science(
    title="Machine Learning A-Z",
    rating=9.4,
    teacher="Kirill Eremenko",
    language="English",
    image="https://online.fliphtml5.com/grdgl/hfrm/files/large/36a1b98f33ae60c35dada8127cbeb8fe.webp?1721989493&1721989493",
    link="https://www.udemy.com/course/machinelearning/"
)
            Data_science4=Data_Science(
    title="Deep Learning with TensorFlow",
    rating=8.9,
    teacher="Andrew Ng",
    language="English",
    image="https://cdn.educba.com/academy/wp-content/uploads/2020/02/Deep-Learning-with-TensorFlow.jpg",
    link="https://www.coursera.org/specializations/tensorflow-advanced-techniques"
)
            db.session.add_all([Data_science1,Data_science2,Data_science3,Data_science4])
            db.session.commit()
        

        if not Marketing.query.first():
            marketing1 = Marketing(
    title="Digital Marketing Mastery",
    rating=9.1,
    teacher="Neil Patel",
    language="English",
    image="https://learndigitalskill.in/wp-content/uploads/2021/02/cover-2.jpg",
    link="https://neilpatel.com/training/digital-marketing/"
)
            marketing2 =  Marketing(
    title="Social Media Marketing",
    rating=8.8,
    teacher="Gary Vaynerchuk",
    language="English",
    image="https://www.netleafinfosoft.com/our-blog/wp-content/uploads/2020/11/Social-Media-Marketing.jpg",
    link="https://www.garyvaynerchuk.com/social-media-marketing-course/"
)
            marketing3 = Marketing(
    title="SEO & Google Ads",
    rating=9.3,
    teacher="Brian Dean",
    language="English",
    image="https://cdn.prod.website-files.com/65dfb932d2fac52442a131e0/66912efcc2f1057276f52edc_SEO%20vs%20Google%20Ads%205%20Key%20Differences%20You%20Should%20Know.webp",
    link="https://backlinko.com/seo-training"
)
            marketing4 =  Marketing(
    title="Content Marketing Strategies",
    rating=8.9,
    teacher="HubSpot Academy",
    language="English",
    image="https://www.ecommerce-nation.com/wp-content/uploads/2023/06/content-marketing.webp",
    link="https://academy.hubspot.com/courses/content-marketing"
)
            db.session.add_all([marketing1, marketing2, marketing3, marketing4])
            db.session.commit()


        if not Finance.query.first():
            finance1 = Finance(
    title="Personal Finance 101",
    rating=9.0,
    teacher="Ramsey Solutions",
    language="English",
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIVXllo5slsPUVY7JmiNk6s1lxfo2p8bRbUw&s",
    link="https://www.ramseysolutions.com/personal-finance-101"
)
            finance2 =  Finance(
    title="Investing in Stock Market",
    rating=9.2,
    teacher="Warren Buffett's Teachings",
    language="English",
    image="https://univest.in/_next/image?url=https%3A%2F%2Funivest-blog.storage.googleapis.com%2Fblogs%2Fwp-content%2Fuploads%2F2025%2F01%2F30182806%2Fstock-market-investment-main-image-.jpg&w=1080&q=75",
    link="https://www.berkshirehathaway.com/invest"
)       
            finance3 =  Finance(
    title="Cryptocurrency & Blockchain",
    rating=8.8,
    teacher="Andreas M. Antonopoulos",
    language="English",
    image="https://bombaychamber.com/wp-content/uploads/2024/04/Online-Blockchain-Cryptocurrency-Certification-Course-scaled-1.jpg",
    link="https://aantonop.com/cryptocurrency-course"
)
            finance4 = Finance(
    title="Financial Modeling & Valuation",
    rating=9.4,
    teacher="Corporate Finance Institute",
    language="English",
    image="https://img1.wsimg.com/isteam/ip/ecfafad7-7a90-4e7f-be37-51fdaf35ba5a/advance-financial-modeling.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:1240,cg:true",
    link="https://corporatefinanceinstitute.com/financial-modeling-valuation"
)
            db.session.add_all([finance1, finance2, finance3, finance4])
            db.session.commit()
    


            new_user = User(
            name="Admin",
            email="admin@gmail.com",
            mobile=1234567890,
            role="admin"
    )
            new_user.set_password("Admin1234")
            db.session.add(new_user)
            db.session.commit()
setup_db()





def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.role != 'admin':
            flash("Access denied!", "danger")
            return redirect(url_for('dashboard'))
        return func(*args, **kwargs)
    return wrapper



@app.route('/')
def index():
    courses = [
        {
            'title': 'Introduction to Python',
            'description': 'Learn the basics of Python programming, including syntax, data structures, and fundamental concepts.',
            'year': 2024,
            'rating': 4.8,
            'image': 'https://www.aalpha.net/wp-content/uploads/2019/10/Python-programming-india.jpg'
        },
        {
            'title': 'Advanced Machine Learning',
            'description': 'Dive deep into advanced machine learning concepts, including deep learning, reinforcement learning, and neural networks.',
            'year': 2024,
            'rating': 4.9,
            'image': 'https://nanoschool.in/wp-content/uploads/2024/08/ML5-600x400.jpg'
        },
        {
            'title': 'Web Development with Flask',
            'description': 'Build web applications using Flask, a micro-framework for Python, and learn about routing, templates, and databases.',
            'year': 2024,
            'rating': 4.7,
            'image': 'https://static.wixstatic.com/media/b2dfda_1c51fe6397954d13a39841c7f66f4a7d~mv2.png/v1/fill/w_480,h_302,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/b2dfda_1c51fe6397954d13a39841c7f66f4a7d~mv2.png'
        },
        {
            'title': 'Data Science and Analytics',
            'description': 'Learn how to analyze and interpret complex data using Python, Pandas, NumPy, and visualization techniques.',
            'year': 2024,
            'rating': 4.6,
            'image': 'https://imageio.forbes.com/specials-images/imageserve/635f79fbf214917bd2876e03/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds'
        },
        {
            'title': 'Cloud Computing with AWS',
            'description': 'Discover the basics of cloud computing, AWS services, and how to deploy scalable applications in the cloud.',
            'year': 2024,
            'rating': 4.6,
            'image': 'https://images.squarespace-cdn.com/content/v1/60cfd646701da4034512a1c5/ca3d678a-cbfc-4c9c-bc79-9d3be9fb907e/AWS-Cloud.png'
        },

        {
            'title': 'Introduction to Artificial Intelligence',
            'description': 'Explore the foundations of artificial intelligence, including search algorithms, problem-solving techniques, and AI applications.',
            'year': 2024,
            'rating': 4.8,
            'image': 'https://360digit.b-cdn.net/assets/admin/ckfinder/userfiles/images/blog/04-08-2023/04-08-2023-f/29%20-%20An%20Introduction%20to%20Artificial%20Intelligence-01-min.png'
        }
    ]
    return render_template('index.html',courses=courses)

@app.route("/login", methods=["GET", "POST"])
def login():


    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")


        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials!", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():


    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        mobile = request.form.get("mobile")


        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register"))

        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters long!", "danger")
            return redirect(url_for("register"))
        
        if not any(char.isupper() for char in password):
            flash("Password must contain at least one uppercase letter!", "danger")
            return redirect(url_for("register"))


        new_user = User(name=name, email=email, mobile=mobile)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()


        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))


    return render_template("register.html")


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()  # Log the user out
        flash("Logged out successfully!", "info")
        return redirect(url_for('login'))  # Redirect to login page
    return redirect(url_for('login'))



@app.route("/add_courses", methods=["POST"])
@login_required
@admin_required
def add_courses():
    title = request.form.get("title")
    rating = request.form.get("rating")
    image_url = request.form.get("image")
    courses = request.form.get("courses").lower()
    teacher = request.form.get("teacher")
    link = request.form.get("link")  # Get the link from the form

    if not (title and rating and image_url and courses and teacher and link):
        return "Missing required fields"

    try:
        rating = float(rating)
    except ValueError:
        return "Invalid rating"

    courses_map = {
        "web_dev": Web_Dev,
        "design": Design,
        "data_science": Data_Science,
        "marketing": Marketing,
        "finance": Finance,
    }

    if courses in courses_map:
        new_course = courses_map[courses](
            title=title, 
            rating=rating, 
            image=image_url,
            teacher=teacher,
            link=link  # Add the link to the new course
        )
        db.session.add(new_course)
        db.session.commit()
        flash("Course added successfully!", "success")
    else:
        return "Invalid courses"

    return redirect(url_for("courses"))


@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/courses")
def courses():
    web_dev_courses = Web_Dev.query.all()  
    design_courses = Design.query.all()  
    data_science_courses = Data_Science.query.all()
    marketing_courses = Marketing.query.all()
    finance_courses = Finance.query.all()
    return render_template("courses.html", web_dev_courses=web_dev_courses, design_courses=design_courses,data_science_courses=data_science_courses,marketing_courses=marketing_courses,finance_courses=finance_courses)


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    return render_template("profile.html") 


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')

        current_user.name = name
        current_user.email = email
        current_user.mobile = mobile

        db.session.commit()
        flash("Profile updated successfully!", "success")
        
        return redirect(url_for('profile'))  # Redirect to profile page

    return render_template('edit_profile.html')

@app.route("/success")
def success():
    return redirect(url_for('success'))

@app.route("/delete_course/<course_type>/<int:course_id>", methods=["POST"])
@login_required
@admin_required
def delete_course(course_type, course_id):
    course_models = {
        'Web_Dev': Web_Dev,
        'Design': Design,
        'Data_Science': Data_Science,
        'Marketing': Marketing,
        'Finance': Finance
    }
    
    if course_type in course_models:
        course = course_models[course_type].query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            flash("Course deleted successfully!", "success")
        else:
            flash("Course not found!", "error")
    else:
        flash("Invalid course type!", "error")
    
    return redirect(url_for('courses'))

if __name__ == "__main__":
    with app.app_context():  
        setup_db()
    app.run(debug=True)


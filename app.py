# --------------------------
# BASIC FLASK IMPORTS
# --------------------------
from flask import Flask, render_template, request, redirect  # Core Flask modules
from flask_sqlalchemy import SQLAlchemy  # Database ORM
from datetime import datetime  # For timestamp handling

# --------------------------
# FLASK APPLICATION SETUP
# --------------------------
app = Flask(__name__)
# Database Configuration:
# - Using SQLite (file-based database)
# - Database file will be created as 'todo.db' in instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# Disable modification tracking (performance optimization)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)  # Initialize database

# --------------------------
# DATABASE MODEL DEFINITION
# --------------------------
class Todo(db.Model):
    # Unique ID (Primary Key) - हर record का unique identifier
    sno = db.Column(db.Integer, primary_key=True)
    
    # Todo Title - ये field mandatory है (nullable=False)
    title = db.Column(db.String(200), nullable=False)
    
    # Todo Description - 'disc' likely means description
    disc = db.Column(db.String(200), nullable=False)
    
    # Auto-populated Creation Timestamp - अपने आप current time set होगा
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Debugging के लिए useful string representation
    def __repr__(self):
        return f"{self.sno} - {self.title}"

# --------------------------
# ROUTE: HOME PAGE (+ Todo Creation)
# --------------------------
@app.route("/", methods=['GET', 'POST'])
def post_funtion():
    # POST Request Handling (Form Submit)
    if request.method == 'POST':
        # Form data extract करना
        title = request.form['title']  # Todo का title
        disc = request.form['disc']    # Todo का description
        
        # नया Todo Object बनाना
        todo = Todo(title=title, disc=disc)
        
        # Database Operations
        db.session.add(todo)  # Session में temporary add
        db.session.commit()   # Permanent save to database
        
        # PRG Pattern (Post-Redirect-Get) - Prevents form resubmission
        return redirect("/")
    
    # GET Request Handling (Page Load)
    allTodo = Todo.query.all()  # सभी todos डेटाबेस से fetch करना
    return render_template('index.html', allTodo=allTodo)  # Template render with data

# --------------------------
# ROUTE: TODO DELETION
# --------------------------
@app.route("/delete/<int:sno>")
def delete_funtion(sno):
    # Find todo by ID (sno = serial number)
    todo = Todo.query.filter_by(sno=sno).first()
    
    # Database Delete Operations
    db.session.delete(todo)  # Mark for deletion
    db.session.commit()      # Confirm deletion
    
    return redirect("/")  # वापस homepage पर redirect

# --------------------------
# ROUTE: TODO UPDATE
# --------------------------
@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update_function(sno):
    # Find the todo to be updated
    todo = Todo.query.filter_by(sno=sno).first()
    
    # POST = Update Submission
    if request.method == 'POST':
        # Update the fields
        todo.title = request.form['title']  # नया title
        todo.disc = request.form['disc']    # नया description
        db.session.commit()  # Save changes
        return redirect("/")  # Homepage redirect
    
    # GET = Show Update Form
    return render_template('update.html', todo=todo)

# --------------------------
# APPLICATION ENTRY POINT
# --------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)  # Run with:
                         # - Debug mode ON (auto-reload)
                         # - Detailed error pages
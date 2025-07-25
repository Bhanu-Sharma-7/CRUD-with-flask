# 🔥 Flask CRUD App

Yeh ek simple sa CRUD (Create, Read, Update, Delete) web app hai jo **Flask** use karke banaya gaya hai. Isme tum tasks ko add, update, delete aur view kar sakte ho — basic but solid concept ke sath.

---

## 🚀 Features

- ✅ Add / Update / Delete / View tasks
- 🧠 Flask routing + Jinja2 templating
- 🗃️ SQLite database for data storage
- 🎨 Basic clean UI (HTML + CSS)
- 💡 Easy to understand code — perfect for beginners

---

## 🧱 Folder Structure

```
project/
│
├── app.py              # Main Flask app
├── todo.db             # SQLite DB
├── instance/           # Flask instance folder
├── templates/
│   ├── index.html      # Home page
│   └── update.html     # Task update page
├── static/
│   └── style.css       # (agar CSS file banayi ho)
├── env/                # Virtual environment (ignored in git)
└── README.md
```

---

## 🛠️ How to Run

```bash
# Step 1: Virtual environment setup
python -m venv env

# Step 2: Activate env
# For Windows
env\Scripts\activate

# Step 3: Install Flask
pip install flask

# Step 4: Run the app
python app.py
```

👉 Open browser and go to: `http://localhost:5000`

---

## 🌍 App Routes

| URL Route           | Kya karta hai?              |
|---------------------|-----------------------------|
| `/`                 | Sabhi tasks dikhata hai     |
| `/add`              | Naya task add karta hai     |
| `/update/<id>`      | Existing task update karta hai |
| `/delete/<id>`      | Task delete karta hai       |

---

## 📦 Requirements

- Python 3.x
- Flask

Install Flask:

```bash
pip install flask
```

---

## 🧾 .gitignore (suggestion)

```gitignore
__pycache__/
.env
*.db
instance/
env/
.vscode/
```

---

## 🤝 Contribute Karna Hai?

Bindaas pull request bhejo. Koi improvement ka idea ho to pehle ek issue open kar lena.

---

## 📄 License

MIT License 📄  
Use it, modify it, share it ❤️

---

> Banaya gaya with 💻, ☕ and a bit of Python magic by Bhanu Sharma.
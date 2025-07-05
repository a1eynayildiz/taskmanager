# ✅ TaskManager

A role-based task assignment system built with Django. Users can log in and view tasks based on their role (superuser, admin, or standard user).

🌐 Live Demo: [taskmanager on PythonAnywhere](https://a1eynayildiz.pythonanywhere.com/login/)

---

## 🚀 Features

- 🔐 Login system with user roles
- 👑 Superuser: Can create and assign tasks to others
- 🛠 Admin: Can view tasks assigned to them and assign tasks to users
- 🙋‍♀️ Regular users: Can view only the tasks assigned to them
- 📅 Task due dates and tracking
- 📋 Clean interface for viewing assigned and created tasks

---

## 🎯 How it Works

- When you first open the app, you're greeted with a login page:  
  _`https://a1eynayildiz.pythonanywhere.com/login/`_

- After logging in:
  - **Superuser** sees all tasks and can assign new ones
  - **Admin** sees their tasks and can assign to users
  - **User** sees only their own assigned tasks

---

## 🧪 Project Setup

1. **Clone the repository**

```bash
git clone https://github.com/a1eynayildiz/taskmanager.git
cd taskmanager
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations and create superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Run the development server**

```bash
python manage.py runserver
```

Then go to: `http://127.0.0.1:8000/login/`

---

## 📂 Project Structure

```
taskmanager/
├── taskmanager/       # Project configuration
├── tasks/             # Task assignment app
├── templates/         # HTML templates (login, dashboard, etc.)
├── static/            # Static assets
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🧑‍💻 Roles in Action

| Role       | Can View Tasks | Can Assign Tasks | Can Create Tasks |
|------------|----------------|------------------|------------------|
| Superuser  | ✅ Yes         | ✅ Yes           | ✅ Yes           |
| Admin      | ✅ Own Tasks   | ✅ To users      | ❌ No            |
| User       | ✅ Own Tasks   | ❌ No            | ❌ No            |

---

## 📬 Contact

<a href="https://www.linkedin.com/in/aleynayildiz1/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white" height="25">
</a>
<a href="https://medium.com/@aleynayildizz" target="_blank">
  <img src="https://img.shields.io/badge/Medium-black?logo=medium&logoColor=white" height="25">
</a>

---

Projeyi ilk çalıştırdığınızda sizi bir login sayfası karşılıyor.
![image](https://github.com/user-attachments/assets/6d68f164-895a-40bc-b7d8-81ce97131c18)
Gerekli bilgileri girip giriş yaptıktan sonra eğer superadmin iseniz atadığınız görevleri görebilir ve yeni görevler atayabilirsiniz.
![image](https://github.com/user-attachments/assets/3345ac49-2d48-4df6-ac6a-e8f0a6c1921c)

Yeni görev oluştur butonuna tıklayarak superuserda görev ataması gerçekleştirebilirsiniz.
![image](https://github.com/user-attachments/assets/4f830e67-6c20-4749-a79d-8af19bef77ed)

Atanan görevi görüntüleyebilirsiniz.
![image](https://github.com/user-attachments/assets/5721d67c-4ae9-444c-90c2-cb909741afdd)


Eğer admin olarak giriş yaptıysanız size atanan görevleri görüntüleyebilir ve userlara görev ataması yapabilirsiniz.
![image](https://github.com/user-attachments/assets/c032445f-2e05-4081-9d9c-3e5bc34c5721)
![image](https://github.com/user-attachments/assets/d3e4dc6d-0ec2-4bc2-8beb-5b554fe2a358)

User olarak giriş yaparsanız sadece size atanan görevleri görebilirsiniz.
-Size görev ataması yapılmadıysa şu şekilde görünecektir:
![image](https://github.com/user-attachments/assets/adc40ac8-cca0-4db5-b86c-895d0dbf1bc3)
-Atama yapılırsa da şu şekilde görünecektir:
![image](https://github.com/user-attachments/assets/7d64eaa3-a8cb-4abc-99e5-04fe78dec974)













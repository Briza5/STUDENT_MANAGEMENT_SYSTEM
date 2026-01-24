# Student Management System (SQLite Edition)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/PyQt6-6.6+-green.svg" alt="PyQt6">
  <img src="https://img.shields.io/badge/SQLite-3.x-orange.svg" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

Desktop application for managing student records built with **PyQt6** and **SQLite**. This is the lightweight, portable version perfect for single-user scenarios and learning purposes.

---

## ✨ Features

- ✅ **Add Students** - Create new student records with name, course, and mobile
- ✅ **Edit Students** - Update existing student information
- ✅ **Delete Students** - Remove student records with confirmation
- ✅ **Search Functionality** - Find students by name
- ✅ **Modern GUI** - Clean interface with menu bar, toolbar, and status bar
- ✅ **Context Buttons** - Edit/Delete buttons appear when row is selected
- ✅ **About Dialog** - Information about the application
- ✅ **SQLite Backend** - Lightweight, zero-configuration database

---

## 🖼️ Screenshots

### Main Window
```
┌────────────────────────────────────────────────┐
│ File  Edit  Help               [+] [🔍]  ⋮⋮    │
├────────────────────────────────────────────────┤
│ ID │ Name         │ Course    │ Mobile         │
├────┼──────────────┼───────────┼────────────────┤
│ 1  │ John Doe     │ Math      │ 123456789      │
│ 2  │ Sarah Smith  │ Biology   │ 987654321      │
│ 3  │ Mike Johnson │ Astronomy │ 555123456      │
└────────────────────────────────────────────────┘
```

---

## 📋 Requirements

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **Disk Space**: ~50 MB (including dependencies)

### Python Dependencies
- `PyQt6` >= 6.6.1 - GUI framework
- `sqlite3` - Built-in (no installation needed)

---

## 🚀 Installation

### 1️⃣ Clone or Download

```bash
# Option A: Clone repository (if using git)
git clone https://github.com/yourusername/student-management-sqlite.git
cd student-management-sqlite

# Option B: Download ZIP and extract
# Then navigate to the folder
cd student-management-sqlite
```

### 2️⃣ Install Dependencies

```bash
# Install PyQt6
pip install PyQt6
```

**Or using requirements.txt:**

```bash
pip install -r requirements.txt
```

### 3️⃣ Create Database

The application will automatically create `database.db` on first run, but you can create it manually:

```bash
python -c "import sqlite3; conn = sqlite3.connect('database.db'); conn.execute('CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT, mobile TEXT)'); conn.close()"
```

**Or using SQLite CLI:**

```bash
sqlite3 database.db
```

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT,
    mobile TEXT
);

-- Insert sample data (optional)
INSERT INTO students (name, course, mobile) VALUES 
    ('John Doe', 'Math', '123456789'),
    ('Sarah Smith', 'Biology', '987654321'),
    ('Mike Johnson', 'Astronomy', '555123456');

.quit
```

### 4️⃣ Add Icons (Optional)

Create an `icons/` folder and add:
- `add.png` - Add student icon (24x24 px recommended)
- `search.png` - Search icon (24x24 px recommended)

Or the app will work without icons (text-only toolbar).

---

## ▶️ Running the Application

### Basic Usage

```bash
python main.py
```

### From VS Code

1. Open `main.py` in VS Code
2. Press `F5` or click "Run" → "Run Without Debugging"

### Creating Executable (Optional)

**Using PyInstaller:**

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name "StudentManagement" --icon=app_icon.ico main.py

# Executable will be in dist/ folder
```

---

## 📖 Usage Guide

### Adding a Student

1. Click **File → Add Student** (or toolbar **[+]** button)
2. Fill in:
   - **Name** (required)
   - **Course** (select from dropdown)
   - **Mobile** (optional)
3. Click **Submit**

**Keyboard Shortcut:** `Ctrl+N` (Windows/Linux) or `Cmd+N` (Mac)

---

### Editing a Student

1. **Click on a student row** in the table
2. Click **Edit Record** button (appears in status bar)
3. Modify the information
4. Click **Update**

---

### Deleting a Student

1. **Click on a student row** in the table
2. Click **Delete Record** button (appears in status bar)
3. Confirm deletion in the dialog
4. Click **Yes**

⚠️ **Warning:** This action cannot be undone!

---

### Searching for Students

1. Click **Edit → Search** (or toolbar **[🔍]** button)
2. Enter student **name** (exact match)
3. Click **Search**
4. Matching rows will be highlighted in the table

---

### About Dialog

Click **Help → About** to view application information.

---

## 📁 Project Structure

```
student-management-sqlite/
├── main.py                 # Main application file
├── database.db            # SQLite database (auto-created)
├── icons/                 # Icon assets (optional)
│   ├── add.png
│   └── search.png
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License
```

---

## 🏗️ Architecture

### GUI Components

```python
MainWindow (QMainWindow)
├── Menu Bar
│   ├── File → Add Student
│   ├── Edit → Search
│   └── Help → About
├── Toolbar
│   ├── Add Student (icon)
│   └── Search (icon)
├── Central Widget (QTableWidget)
│   └── 4 columns: ID, Name, Course, Mobile
└── Status Bar
    ├── Edit Record button (dynamic)
    └── Delete Record button (dynamic)
```

### Dialog Classes

```python
InsertDialog (QDialog)    # Add new student
EditDialog (QDialog)      # Update existing student
DeleteDialog (QDialog)    # Confirm deletion
SearchDialog (QDialog)    # Search by name
AboutDialog (QMessageBox) # App information
```

### Database Schema

```sql
students
├── id      INTEGER PRIMARY KEY AUTOINCREMENT
├── name    TEXT (student name)
├── course  TEXT (course enrolled)
└── mobile  TEXT (phone number)
```

---

## 🎓 Code Examples

### Database Operations

**SELECT - Load All Students:**
```python
connection = sqlite3.connect("database.db")
result = connection.execute("SELECT * FROM students")
for row in result:
    print(row)
connection.close()
```

**INSERT - Add New Student:**
```python
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute(
    "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
    ("Emma Pike", "Physics", "111222333")
)
connection.commit()
connection.close()
```

**UPDATE - Edit Student:**
```python
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute(
    "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
    ("Emma Johnson", "Math", "999888777", 1)
)
connection.commit()
connection.close()
```

**DELETE - Remove Student:**
```python
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("DELETE FROM students WHERE id=?", (1,))
connection.commit()
connection.close()
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'PyQt6'"

**Solution:**
```bash
pip install PyQt6
```

If still failing, try:
```bash
pip install --upgrade pip
pip install PyQt6 --force-reinstall
```

---

### Issue: "Database is locked"

**Cause:** Multiple connections trying to write simultaneously.

**Solution:**
- Close all instances of the application
- Delete `database.db-journal` file (if exists)
- Restart the application

---

### Issue: Icons not showing

**Solution:**
1. Create `icons/` folder in the same directory as `main.py`
2. Add `add.png` and `search.png` (24x24 px recommended)
3. Or comment out icon paths in code:

```python
# Change this:
add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)

# To this:
add_student_action = QAction("Add Student", self)
```

---

### Issue: "Permission denied" when creating database.db

**Solution:**
- Run application from a folder where you have write permissions
- On Windows: Avoid running from `C:\Program Files\`
- On Linux/Mac: Check folder permissions with `ls -la`

---

## 🔒 Security Notes

### SQLite Security Considerations

✅ **What's Protected:**
- SQL Injection prevention (parametrized queries)
- Input sanitization through Qt widgets

⚠️ **Limitations:**
- No user authentication
- No encryption (database file is plain text)
- No access control (anyone with file access can read/modify)

### Best Practices

```python
# ✅ GOOD - Parametrized query
cursor.execute("SELECT * FROM students WHERE name=?", (name,))

# ❌ BAD - String formatting (SQL injection risk!)
cursor.execute(f"SELECT * FROM students WHERE name='{name}'")
```

---

## 📊 Comparison: SQLite vs MySQL Version

| Feature | SQLite Version | MySQL Version |
|---------|----------------|---------------|
| **Installation** | ✅ Zero config | 🔧 MySQL server required |
| **Portability** | ✅ Single file | ❌ Server-dependent |
| **Setup Time** | ⚡ Instant | ⏱️ ~30 minutes |
| **Multi-user** | ❌ Limited | ✅ Excellent |
| **Performance (single-user)** | ✅ Very fast | 🔧 Good |
| **Performance (multi-user)** | ❌ Poor | ✅ Excellent |
| **Database Size** | < 1 GB recommended | Unlimited (TB+) |
| **Use Case** | Desktop, learning, prototyping | Production, web apps, teams |

**When to use SQLite version:**
- 👤 Single user application
- 💻 Desktop/personal use
- 🎓 Learning SQL and PyQt
- 🚀 Quick prototyping
- 📦 Portable application (USB stick, email)

**When to upgrade to MySQL:**
- 👥 Multiple concurrent users (>10)
- 🌐 Web application
- 📊 Large datasets (>1 GB)
- 🔐 Need user authentication
- 🏢 Enterprise/production use

---

## 🚀 Future Enhancements

### Potential Features to Add

- [ ] **Export to CSV/Excel** - Export student data
- [ ] **Import from CSV** - Bulk import students
- [ ] **Advanced Search** - Filter by course, multiple criteria
- [ ] **Student Photos** - Add profile pictures
- [ ] **GPA Tracking** - Add grades and calculate GPA
- [ ] **Attendance** - Track attendance records
- [ ] **Dark Mode** - Toggle UI theme
- [ ] **Backup/Restore** - Database backup functionality
- [ ] **Print Reports** - Generate PDF reports
- [ ] **Email Integration** - Send notifications

### Migration Path

**From SQLite to MySQL:**

See the MySQL version of this application which includes:
- Connection pooling
- Better concurrent user support
- Network access
- User authentication

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add comments for complex logic
- Update README.md for new features
- Test thoroughly before submitting

---

## 📝 License

This project is licensed under the **MIT License** - see below for details:

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎓 Learning Resources

### PyQt6 Documentation
- [Official PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt for Python](https://doc.qt.io/qtforpython/)

### SQLite Resources
- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)

### Python Best Practices
- [PEP 8 – Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)

---

## 👤 Author

**Lukáš** - *Python Developer*

- Course: [The Python Mega Course](https://www.udemy.com/course/the-python-mega-course/)


---

## 🙏 Acknowledgments

- **PyQt6** - Powerful GUI framework
- **SQLite** - Lightweight embedded database
- **The Python Mega Course** - Excellent learning resource
- **Python Community** - For continuous support and resources

---


## 📈 Version History

### Version 1.0.0 (2024-01-24)
- ✅ Initial release
- ✅ Basic CRUD operations
- ✅ Search functionality
- ✅ SQLite backend
- ✅ Modern PyQt6 GUI

---

## 🎯 Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] PyQt6 installed (`pip install PyQt6`)
- [ ] Downloaded/cloned project
- [ ] Created `database.db` (automatic on first run)
- [ ] Added icons to `icons/` folder (optional)
- [ ] Run `python main.py`
- [ ] Test adding a student
- [ ] Test editing a student
- [ ] Test deleting a student
- [ ] Test search functionality

**Ready to go! 🚀**

---

<p align="center">
  Made with ❤️ and <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

<p align="center">
  <sub>Happy Coding! 🎉</sub>
</p>
from flask import Flask, render_template, abort
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

PDF_DIR = BASE_DIR / "static" / "pdfs"

# --------------------------------------------------
# STUDENT PROFILE
# Replace these details with your own information.
# --------------------------------------------------

STUDENT = {
    "name": "JAGILI NANDA KISHORE PAVAN KUMAR SAI",
    "degree": "B.Tech - CSE-DS",
    "graduation_year": "2028",
    "section": "3",
    "photo": "images/profile.jpeg",
    "linkedin": "https://www.linkedin.com/in/nkpks/",
    "github": "https://github.com/Nkpks"
}

# --------------------------------------------------
# PREVIOUS PROJECTS
# Replace these examples with your real projects.
# --------------------------------------------------

PROJECTS = [
    {
        "title": "Project One",
        "category": "Web Development",
        "description": (
            "A project demonstrating web development "
            "concepts and practical programming skills."
        ),
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": "https://github.com/YOUR_USERNAME"
    },
    {
        "title": "Project Two",
        "category": "Data Science",
        "description": (
            "A project exploring data analysis, "
            "visualization, and extracting useful insights."
        ),
        "tech": ["Python", "Pandas", "Matplotlib"],
        "github": "https://github.com/YOUR_USERNAME"
    }
]

# --------------------------------------------------
# MODULES
# --------------------------------------------------

MODULES = [
    {
        "number": 1,
        "title": "Module 01",
        "description": "Study materials for Module 1.",
        "filename": "module1.pdf"
    },
    {
        "number": 2,
        "title": "Module 02",
        "description": "Study materials for Module 2.",
        "filename": "module2.pdf"
    },
    {
        "number": 3,
        "title": "Module 03",
        "description": "Study materials for Module 3.",
        "filename": "module3.pdf"
    },
    {
        "number": 4,
        "title": "Module 04",
        "description": "Study materials for Module 4.",
        "filename": "module4.pdf"
    },
    {
        "number": 5,
        "title": "Module 05",
        "description": "Study materials for Module 5.",
        "filename": "module5.pdf"
    }
]

# --------------------------------------------------
# LAB EXPERIMENTS
# Add or remove entries according to your PDFs.
# --------------------------------------------------

LABS = [
    {
        "number": 1,
        "title": "Experiment 01",
        "description": "Lab experiment 1 study material.",
        "filename": "experiment1.pdf"
    },
    {
        "number": 2,
        "title": "Experiment 02",
        "description": "Lab experiment 2 study material.",
        "filename": "experiment2.pdf"
    }
]

# --------------------------------------------------
# DATA SCIENCE TOOLS
# --------------------------------------------------

TOOLS = [
    {
        "name": "Python",
        "category": "PROGRAMMING",
        "description": (
            "A versatile programming language used for "
            "data analysis, automation, and machine learning."
        ),
        "url": "https://www.python.org/",
        "symbol": "Py"
    },
    {
        "name": "Jupyter Notebook",
        "category": "DEVELOPMENT",
        "description": (
            "Create interactive notebooks combining code, "
            "visualizations, and explanatory text."
        ),
        "url": "https://jupyter.org/",
        "symbol": "J"
    },
    {
        "name": "Google Colab",
        "category": "CLOUD COMPUTING",
        "description": (
            "Write and execute Python notebooks in your "
            "browser without a local setup."
        ),
        "url": "https://colab.research.google.com/",
        "symbol": "Co"
    },
    {
        "name": "NumPy",
        "category": "NUMERICAL COMPUTING",
        "description": (
            "Perform efficient numerical computations "
            "and work with multidimensional arrays."
        ),
        "url": "https://numpy.org/",
        "symbol": "Np"
    },
    {
        "name": "Pandas",
        "category": "DATA ANALYSIS",
        "description": (
            "Clean, transform, explore, and analyze "
            "structured datasets."
        ),
        "url": "https://pandas.pydata.org/",
        "symbol": "Pd"
    },
    {
        "name": "Matplotlib",
        "category": "VISUALIZATION",
        "description": (
            "Create charts, plots, and visualizations "
            "to understand data."
        ),
        "url": "https://matplotlib.org/",
        "symbol": "Mp"
    },
    {
        "name": "Scikit-learn",
        "category": "MACHINE LEARNING",
        "description": (
            "Explore machine learning algorithms, "
            "model evaluation, and preprocessing."
        ),
        "url": "https://scikit-learn.org/",
        "symbol": "Sk"
    },
    {
        "name": "Kaggle",
        "category": "DATASETS & PRACTICE",
        "description": (
            "Discover datasets, practice data science, "
            "and learn from community notebooks."
        ),
        "url": "https://www.kaggle.com/",
        "symbol": "Kg"
    }
]


# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def pdf_exists(folder, filename):
    """
    Check that a PDF filename is a simple filename
    and that the corresponding file exists.
    """

    if Path(filename).name != filename:
        return False

    if not filename.lower().endswith(".pdf"):
        return False

    return (PDF_DIR / folder / filename).is_file()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        student=STUDENT,
        project_count=len(PROJECTS),
        module_count=len(MODULES),
        lab_count=len(LABS)
    )


# --------------------------------------------------
# PROJECTS PAGE
# --------------------------------------------------

@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        student=STUDENT,
        projects=PROJECTS
    )

# --------------------------------------------------
# TOOLS PAGE
# --------------------------------------------------

@app.route("/tools")
def tools():
    return render_template(
        "tools.html",
        student=STUDENT,
        tools=TOOLS
    )


# --------------------------------------------------
# MODULES PAGE
# --------------------------------------------------

@app.route("/modules")
def modules():
    module_items = []

    for module in MODULES:
        item = module.copy()

        item["available"] = pdf_exists(
            "modules",
            item["filename"]
        )

        item["url"] = (
            f"/pdf/modules/{item['filename']}"
            if item["available"]
            else None
        )

        module_items.append(item)

    return render_template(
        "modules.html",
        student=STUDENT,
        modules=module_items
    )


# --------------------------------------------------
# LAB EXPERIMENTS PAGE
# --------------------------------------------------

@app.route("/labs")
def labs():
    lab_items = []

    for lab in LABS:
        item = lab.copy()

        item["available"] = pdf_exists(
            "labs",
            item["filename"]
        )

        item["url"] = (
            f"/pdf/labs/{item['filename']}"
            if item["available"]
            else None
        )

        lab_items.append(item)

    return render_template(
        "labs.html",
        student=STUDENT,
        labs=lab_items
    )


# --------------------------------------------------
# PDF VIEWER
# --------------------------------------------------

@app.route("/pdf/<category>/<filename>")
def open_pdf(category, filename):

    if category not in {"modules", "labs"}:
        abort(404)

    if not pdf_exists(category, filename):
        abort(404)

    # Display the PDF in the browser.
    return app.send_static_file(
        f"pdfs/{category}/{filename}"
    )


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
import streamlit as st

# ============================================================
# FREE MATHS + COMPUTER SCIENCE LEARNING WEBSITE
# ============================================================

st.set_page_config(
    page_title="OpenLearn — Maths & Computer Science",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f8fafc;
}

.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* Main headings */

.hero {
    background: #ffffff;
    padding: 3rem;
    border-radius: 24px;
    border: 1px solid #e5e7eb;
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -2px;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.15rem;
    color: #64748b;
    max-width: 750px;
    line-height: 1.7;
}

/* Cards */

.card {
    background: white;
    padding: 1.5rem;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
    transition: 0.2s;
}

.card:hover {
    border-color: #94a3b8;
    transform: translateY(-2px);
}

.card h3 {
    margin-top: 0;
}

/* Lesson box */

.lesson {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    margin: 1rem 0;
}

.lesson-title {
    font-size: 1.8rem;
    font-weight: 700;
}

.lesson-text {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #334155;
}

/* Topic badges */

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: #f1f5f9;
    color: #475569;
    font-size: 0.85rem;
    font-weight: 600;
}

/* Footer */

.footer {
    text-align: center;
    padding: 3rem 0 1rem 0;
    color: #94a3b8;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    font-weight: 600;
}

/* Mobile */

@media (max-width: 700px) {
    .hero {
        padding: 1.5rem;
    }

    .hero h1 {
        font-size: 2.2rem;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CURRICULUM
# ============================================================

cs_phases = [
    {
        "start": 1,
        "end": 10,
        "topic": "Programming Foundations",
        "description": "Learn what programming is and begin writing simple Python programs.",
        "lessons": [
            "What is Computer Science?",
            "What is a program?",
            "Your first Python program",
            "Variables",
            "Numbers and calculations",
            "Strings and text",
            "Getting input",
            "Making decisions with if",
            "Comparisons",
            "Mini Python project"
        ]
    },
    {
        "start": 11,
        "end": 20,
        "topic": "Python Fundamentals",
        "description": "Build a strong foundation in Python.",
        "lessons": [
            "Boolean values",
            "if, elif and else",
            "while loops",
            "for loops",
            "The range function",
            "Lists",
            "List indexing",
            "Changing lists",
            "Simple functions",
            "Functions project"
        ]
    },
    {
        "start": 21,
        "end": 30,
        "topic": "Problem Solving",
        "description": "Learn how programmers break large problems into smaller ones.",
        "lessons": [
            "Computational thinking",
            "Breaking problems apart",
            "Pattern recognition",
            "Abstraction",
            "Pseudocode",
            "Flowcharts",
            "Writing algorithms",
            "Testing programs",
            "Finding bugs",
            "Problem-solving project"
        ]
    },
    {
        "start": 31,
        "end": 40,
        "topic": "Algorithms",
        "description": "Understand the basic ideas behind algorithms.",
        "lessons": [
            "What is an algorithm?",
            "Linear search",
            "Binary search",
            "Sorting",
            "Bubble sort",
            "Selection sort",
            "Efficiency",
            "Big-O intuition",
            "Comparing algorithms",
            "Algorithm challenge"
        ]
    },
    {
        "start": 41,
        "end": 50,
        "topic": "Data Structures",
        "description": "Learn how computers organise information.",
        "lessons": [
            "Why data structures matter",
            "Lists",
            "Stacks",
            "Queues",
            "Dictionaries",
            "Sets",
            "Trees",
            "Graphs",
            "Choosing a data structure",
            "Data structures challenge"
        ]
    },
    {
        "start": 51,
        "end": 60,
        "topic": "How Computers Work",
        "description": "Discover what happens inside a computer.",
        "lessons": [
            "Bits and binary",
            "Binary numbers",
            "Hexadecimal",
            "Logic gates",
            "CPU",
            "Memory",
            "Storage",
            "Instructions",
            "Operating systems",
            "Computer architecture project"
        ]
    },
    {
        "start": 61,
        "end": 70,
        "topic": "Networks and the Internet",
        "description": "Learn how computers communicate.",
        "lessons": [
            "What is a network?",
            "Local networks",
            "Routers",
            "IP addresses",
            "Packets",
            "DNS",
            "HTTP",
            "Websites and servers",
            "Internet security",
            "Build a simple web concept"
        ]
    },
    {
        "start": 71,
        "end": 80,
        "topic": "Databases and Information",
        "description": "Learn how large amounts of information can be stored and organised.",
        "lessons": [
            "What is a database?",
            "Tables",
            "Rows and columns",
            "Keys",
            "Searching data",
            "Sorting data",
            "SQL introduction",
            "Relationships",
            "Database design",
            "Database project"
        ]
    },
    {
        "start": 81,
        "end": 90,
        "topic": "Cybersecurity and AI",
        "description": "Explore security and the basic ideas behind artificial intelligence.",
        "lessons": [
            "What is cybersecurity?",
            "Passwords and authentication",
            "Encryption",
            "Social engineering",
            "Safe computing",
            "What is AI?",
            "Machine learning",
            "Training data",
            "Bias and fairness",
            "AI mini-project"
        ]
    },
    {
        "start": 91,
        "end": 100,
        "topic": "Advanced Thinking and Projects",
        "description": "Bring together everything you have learned.",
        "lessons": [
            "Computational complexity",
            "Recursion",
            "Graphs and networks",
            "Advanced problem solving",
            "Planning a software project",
            "Designing an application",
            "Writing better code",
            "Testing a project",
            "Improving a project",
            "Final Computer Science project"
        ]
    }
]


math_phases = [
    {
        "start": 101,
        "end": 110,
        "topic": "Algebra Foundations",
        "description": "Build a strong understanding of algebra.",
        "lessons": [
            "What is algebra?",
            "Variables",
            "Simplifying expressions",
            "Collecting like terms",
            "Expanding brackets",
            "Factorising",
            "Substitution",
            "Algebraic fractions",
            "Using algebra to solve problems",
            "Algebra challenge"
        ]
    },
    {
        "start": 111,
        "end": 120,
        "topic": "Equations, Inequalities and Sequences",
        "description": "Learn how to solve increasingly difficult algebraic problems.",
        "lessons": [
            "One-step equations",
            "Multi-step equations",
            "Equations with brackets",
            "Equations with fractions",
            "Inequalities",
            "Representing inequalities",
            "Sequences",
            "Arithmetic sequences",
            "Finding nth terms",
            "Sequence challenge"
        ]
    },
    {
        "start": 121,
        "end": 130,
        "topic": "Number Theory",
        "description": "Explore the mathematics of whole numbers.",
        "lessons": [
            "Factors",
            "Multiples",
            "Prime numbers",
            "Prime factorisation",
            "Highest common factors",
            "Lowest common multiples",
            "Divisibility",
            "Remainders",
            "Modular arithmetic",
            "Number theory challenge"
        ]
    },
    {
        "start": 131,
        "end": 140,
        "topic": "Fractions, Ratios and Percentages",
        "description": "Master some of the most useful parts of everyday mathematics.",
        "lessons": [
            "Equivalent fractions",
            "Adding fractions",
            "Multiplying fractions",
            "Dividing fractions",
            "Ratios",
            "Sharing in a ratio",
            "Direct proportion",
            "Percentages",
            "Percentage change",
            "Real-world problems"
        ]
    },
    {
        "start": 141,
        "end": 150,
        "topic": "Geometry and Coordinates",
        "description": "Understand shapes, space and coordinates.",
        "lessons": [
            "Angles",
            "Triangles",
            "Quadrilaterals",
            "Area",
            "Perimeter",
            "Volume",
            "Pythagoras",
            "Coordinates",
            "Transformations",
            "Geometry challenge"
        ]
    },
    {
        "start": 151,
        "end": 160,
        "topic": "Functions, Graphs and Quadratics",
        "description": "Learn how equations can describe relationships.",
        "lessons": [
            "Coordinates and graphs",
            "Straight-line graphs",
            "Gradient",
            "Intercepts",
            "Functions",
            "Function notation",
            "Quadratic expressions",
            "Quadratic graphs",
            "Patterns in quadratics",
            "Graph challenge"
        ]
    },
    {
        "start": 161,
        "end": 170,
        "topic": "Probability and Combinatorics",
        "description": "Learn how mathematics can describe chance and counting.",
        "lessons": [
            "Probability",
            "Probability scales",
            "Sample spaces",
            "Tree diagrams",
            "Independent events",
            "Dependent events",
            "Counting methods",
            "Permutations",
            "Combinations",
            "Probability challenge"
        ]
    },
    {
        "start": 171,
        "end": 180,
        "topic": "Proof and Mathematical Reasoning",
        "description": "Learn how mathematicians prove that statements are true.",
        "lessons": [
            "What is a proof?",
            "Mathematical arguments",
            "Counterexamples",
            "Proof by contradiction",
            "Proof using cases",
            "Mathematical induction",
            "Invariants",
            "Spotting false statements",
            "Writing clear proofs",
            "Proof challenge"
        ]
    },
    {
        "start": 181,
        "end": 190,
        "topic": "Indices, Surds and Calculus Foundations",
        "description": "Start exploring more advanced mathematical ideas.",
        "lessons": [
            "Index laws",
            "Negative indices",
            "Fractional indices",
            "Standard form",
            "Surds",
            "Simplifying surds",
            "What is a limit?",
            "Introduction to differentiation",
            "Introduction to integration",
            "Calculus challenge"
        ]
    },
    {
        "start": 191,
        "end": 200,
        "topic": "Problem Solving and Mathematical Synthesis",
        "description": "Use everything you have learned to solve challenging problems.",
        "lessons": [
            "How to approach hard problems",
            "Working backwards",
            "Finding patterns",
            "Constructing examples",
            "Logical reasoning",
            "Multi-step problems",
            "Olympiad-style algebra",
            "Olympiad-style geometry",
            "Mixed mathematics challenge",
            "Final Maths challenge"
        ]
    }
]

all_phases = cs_phases + math_phases

shops = [
    "Tech Haven",
    "Book Nook",
    "Green Basket",
    "Fit Fuel",
    "Craft Corner",
    "Gadget Hub",
    "Style Street",
    "Learning Loft",
    "Home Happy",
    "Pet Palace"
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_day(day_number):
    for phase in all_phases:
        if phase["start"] <= day_number <= phase["end"]:
            lesson_index = day_number - phase["start"]
            return phase, phase["lessons"][lesson_index]
    return None, None


def get_subject(day):
    if day <= 100:
        return "Computer Science"
    return "Mathematics"


def get_icon(subject):
    if subject == "Computer Science":
        return "💻"
    return "📐"


def lesson_explanation(day, phase, lesson):
    subject = get_subject(day)

    explanations = {
        "What is Computer Science?":
            "Computer Science is the study of computation: how we represent information, solve problems, write instructions, and build systems that process information.",
        "What is a program?":
            "A program is a set of instructions that tells a computer what to do. Programs can be tiny, such as adding two numbers, or enormous, such as running a search engine.",
        "Your first Python program":
            "Python is a programming language. One of the simplest Python commands is print(), which tells the computer to display something.",
        "Variables":
            "A variable is a named place where a program can keep information. For example, age = 13 stores the number 13 under the name age.",
        "Numbers and calculations":
            "Python can perform arithmetic using operators such as +, -, *, and /. Computers are very good at carrying out calculations quickly.",
        "Strings and text":
            "A string is text stored by a program. Strings are usually written inside quotation marks.",
        "Getting input":
            "Programs can interact with users. Python's input() function allows a program to receive text typed by a user.",
        "Making decisions with if":
            "An if statement allows a program to make a decision. The computer checks whether a condition is true before running a block of code.",
        "Loops":
            "Loops allow computers to repeat instructions. Repetition is one of the most important ideas in programming.",
        "Lists":
            "A list stores several pieces of information together. For example, a list could contain the names of students in a class.",
        "What is an algorithm?":
            "An algorithm is a precise sequence of steps for solving a problem or completing a task.",
        "Binary numbers":
            "Computers represent information using bits. A bit can have two states, commonly represented as 0 and 1.",
        "What is a network?":
            "A computer network connects devices so they can communicate and share information.",
        "What is AI?":
            "Artificial intelligence is a broad area of Computer Science involving systems that perform tasks associated with human-like reasoning, pattern recognition or decision-making.",
        "Factors":
            "A factor of a number divides that number exactly. For example, 3 is a factor of 12 because 12 ÷ 3 = 4.",
        "Prime numbers":
            "A prime number is a whole number greater than 1 with exactly two positive factors: 1 and itself.",
        "Ratios":
            "A ratio compares quantities. For example, a ratio of 2:3 means that for every 2 units of one quantity, there are 3 units of another.",
        "Probability":
            "Probability measures how likely something is to happen. It ranges from 0, meaning impossible, to 1, meaning certain.",
        "What is a proof?":
            "A mathematical proof is a logical argument showing that a statement must be true.",
        "What is a limit?":
            "A limit describes what a mathematical expression approaches as a variable gets closer to a particular value."
    }

    if lesson in explanations:
        return explanations[lesson]

    return (
        f"Today we are studying {lesson.lower()}. "
        f"This is part of the {phase['topic']} section. "
        "Start by understanding the key idea, then try the example and finish with the challenge."
    )


def challenge_for(lesson, day):
    challenges = {
        "Your first Python program":
            "Write a program that prints three things you enjoy learning.",
        "Variables":
            "Create three variables representing a name, an age and a favourite subject.",
        "Numbers and calculations":
            "Write down a calculation involving multiplication and addition, then predict the answer before checking it.",
        "Making decisions with if":
            "Design an if statement that gives a different message depending on whether a number is greater than 10.",
        "Lists":
            "Create a list containing five things you would like to learn.",
        "What is an algorithm?":
            "Write an algorithm for making a sandwich using precise steps.",
        "Binary numbers":
            "Try converting the binary number 101 into a decimal number.",
        "Factors":
            "Find all the positive factors of 24.",
        "Prime numbers":
            "Decide whether 29 is prime and explain how you know.",
        "Ratios":
            "If a recipe uses a ratio of 2 cups of one ingredient to 3 cups of another, how much of the second ingredient is needed when the first amount is 6 cups?",
        "Probability":
            "A fair six-sided die is rolled. What is the probability of rolling an even number?",
        "What is a proof?":
            "Explain why an even number plus another even number must always be even."
    }

    if lesson in challenges:
        return challenges[lesson]

    if day <= 100:
        return "Write down one example of where this idea could be useful in a real computer program."

    return "Create your own example of this mathematical idea and explain every step of your reasoning."


# ============================================================
# SESSION STATE
# ============================================================

if "completed" not in st.session_state:
    st.session_state.completed = set()

if "selected_day" not in st.session_state:
    st.session_state.selected_day = 1


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("# 📚 OpenLearn")

st.sidebar.caption("Free Maths & Computer Science education")

page = st.sidebar.radio(
    "Explore",
    [
        "Home",
        "Learn",
        "Roadmap",
        "Shops",
        "Progress",
        "About"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Your journey")

completed_count = len(st.session_state.completed)

st.sidebar.progress(completed_count / 200)

st.sidebar.write(
    f"**{completed_count} / 200 days completed**"
)


# ============================================================
# HOME
# ============================================================

if page == "Home":

    st.markdown("""
    <div class="hero">

    <span class="badge">100% FREE EDUCATION</span>

    <h1>Learn. Build. Think.</h1>

    <p>
    A free learning platform for anyone who wants to learn
    Computer Science and Mathematics — regardless of their
    financial situation.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Start learning")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">

        <h3>💻 Computer Science</h3>

        <p>
        Start from the absolute beginning and gradually learn
        programming, algorithms, data structures, computers,
        networks, databases, cybersecurity, AI and more.
        </p>

        <strong>Days 1–100</strong>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Computer Science", use_container_width=True):
            st.session_state.selected_day = 1
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card">

        <h3>📐 Mathematics</h3>

        <p>
        Build your mathematical foundations and gradually move
        into algebra, geometry, probability, proof, calculus
        foundations and challenging problem solving.
        </p>

        <strong>Days 101–200</strong>

        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Mathematics", use_container_width=True):
            st.session_state.selected_day = 101
            st.rerun()

    st.markdown("---")

    st.markdown("## Why OpenLearn?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        ### 🌍 Free

        Learning should not depend on how much money
        someone's family has.
        """)

    with c2:
        st.markdown("""
        ### 🧠 Beginner-friendly

        You don't need to already be an expert.
        Start at the beginning and build your knowledge.
        """)

    with c3:
        st.markdown("""
        ### 🛠️ Practical

        Don't just memorise information.
        Use what you learn to solve problems and build things.
        """)


# ============================================================
# LEARN
# ============================================================

elif page == "Learn":

    st.title("📖 Learn")

    st.write(
        "Choose a day from the 200-day learning journey."
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=200,
        value=st.session_state.selected_day,
        step=1
    )

    st.session_state.selected_day = day

    phase, lesson = get_day(day)
    subject = get_subject(day)

    st.markdown(
        f'<span class="badge">{get_icon(subject)} {subject}</span>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"# Day {day}: {lesson}"
    )

    st.write(
        f"**Section:** {phase['topic']}"
    )

    st.progress(day / 200)

    st.markdown("""
    <div class="lesson">
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='lesson-title'>Today's idea</div>",
        unsafe_allow_html=True
    )

    explanation = lesson_explanation(
        day,
        phase,
        lesson
    )

    st.markdown(
        f'<div class="lesson-text">{explanation}</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## 🎯 Today's challenge")

    st.info(challenge_for(lesson, day))

    st.markdown("## 📝 Think about it")

    question = (
        "Can you explain today's idea to someone younger than you "
        "without using complicated words?"
    )

    st.write(question)

    answer = st.text_area(
        "Write your explanation here",
        height=120
    )

    if answer:
        st.success("Great! Explaining something clearly is a powerful way to learn it.")

    st.markdown("## ⏱️ Suggested 30-minute session")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Learn", "10 min")

    with c2:
        st.metric("Practise", "15 min")

    with c3:
        st.metric("Review", "5 min")

    st.markdown("---")

    if day not in st.session_state.completed:

        if st.button(
            "✅ Mark this day complete",
            use_container_width=True
        ):
            st.session_state.completed.add(day)
            st.success(f"Day {day} completed!")
            st.rerun()

    else:

        st.success("You have completed this day.")

    col1, col2 = st.columns(2)

    with col1:

        if day > 1:

            if st.button("← Previous day", use_container_width=True):

                st.session_state.selected_day = day - 1
                st.rerun()

    with col2:

        if day < 200:

            if st.button("Next day →", use_container_width=True):

                st.session_state.selected_day = day + 1
                st.rerun()


# ============================================================
# ROADMAP
# ============================================================

elif page == "Roadmap":

    st.title("🗺️ 200-Day Roadmap")

    st.write(
        "A structured journey from beginner Computer Science "
        "through increasingly challenging Mathematics."
    )

    tab1, tab2 = st.tabs(
        ["💻 Computer Science", "📐 Mathematics"]
    )

    with tab1:

        st.subheader("Days 1–100")

        for phase in cs_phases:

            st.markdown(f"""
            <div class="card">

            <span class="badge">
            Days {phase['start']}–{phase['end']}
            </span>

            <h3>{phase['topic']}</h3>

            <p>{phase['description']}</p>

            </div>
            """, unsafe_allow_html=True)

    with tab2:

        st.subheader("Days 101–200")

        for phase in math_phases:

            st.markdown(f"""
            <div class="card">

            <span class="badge">
            Days {phase['start']}–{phase['end']}
            </span>

            <h3>{phase['topic']}</h3>

            <p>{phase['description']}</p>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# SHOPS
# ============================================================

elif page == "Shops":

    st.title("🛍️ Shops")

    st.write("Browse the shop directory and discover new places to explore.")

    cols = st.columns(2)

    for index, shop in enumerate(shops):
        with cols[index % 2]:
            st.markdown(f"""
            <div class="card">
                <h3>🏪 {shop}</h3>
                <p>Featured shop #{index + 1} in the directory.</p>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# PROGRESS
# ============================================================

elif page == "Progress":

    st.title("📈 Your Progress")

    completed = len(st.session_state.completed)

    st.metric(
        "Days completed",
        f"{completed} / 200"
    )

    st.progress(completed / 200)

    if completed == 0:

        st.info(
            "You haven't completed a lesson yet. "
            "Start with Day 1!"
        )

    else:

        cs_completed = len([
            d for d in st.session_state.completed
            if d <= 100
        ])

        math_completed = len([
            d for d in st.session_state.completed
            if d >= 101
        ])

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Computer Science",
                f"{cs_completed} / 100"
            )
            st.progress(cs_completed / 100)

        with c2:
            st.metric(
                "Mathematics",
                f"{math_completed} / 100"
            )
            st.progress(math_completed / 100)

        st.markdown("---")

        st.subheader("Completed days")

        completed_days = sorted(
            st.session_state.completed
        )

        st.write(
            ", ".join(
                [f"Day {d}" for d in completed_days]
            )
        )


# ============================================================
# ABOUT
# ============================================================

elif page == "About":

    st.title("🌍 About OpenLearn")

    st.markdown("""
    ## Education should be accessible

    OpenLearn is designed around a simple idea:

    **A person's financial situation should not decide whether
    they can learn.**

    The website provides a structured path through Mathematics
    and Computer Science that anyone can follow.

    You don't need expensive textbooks.

    You don't need private tutoring.

    You don't need to already know everything.

    You can simply start at Day 1 and build your knowledge
    step by step.
    """)

    st.markdown("---")

    st.markdown("## 💻 Computer Science")

    st.write("""
    The first 100 days start with programming and gradually
    introduce algorithms, data structures, computer architecture,
    operating systems, networks, databases, cybersecurity,
    artificial intelligence, complexity and projects.
    """)

    st.markdown("## 📐 Mathematics")

    st.write("""
    Days 101–200 build mathematical reasoning through algebra,
    equations, sequences, number theory, ratios, percentages,
    geometry, coordinates, functions, graphs, probability,
    combinatorics, proof, indices, surds, calculus foundations
    and challenging problem solving.
    """)

    st.markdown("---")

    st.markdown("""
    ### A reminder

    You do not have to be "naturally gifted" to learn these
    subjects.

    Difficult topics become easier when you break them into
    smaller ideas, practise regularly and learn from mistakes.

    **Keep going.**
    """)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

OpenLearn • Free Maths & Computer Science Education

<br><br>

Made for learning. Made to be shared.

</div>
""", unsafe_allow_html=True)
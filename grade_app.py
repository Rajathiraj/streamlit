import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="centered"
)

# 2. Rich Custom CSS Styling
st.markdown("""
    <style>
    /* Dark Gradient App Header */
    .header-container {
        background: linear-gradient(135deg, #1E1E2F 0%, #2D2B55 100%);
        padding: 24px;
        border-radius: 16px;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 6px;
        background: linear-gradient(90deg, #60A5FA, #A78BFA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .header-subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
    }
    
    /* Modern Glassmorphic Metric Cards */
    .metric-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94A3B8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-top: 4px;
    }
    
    /* Form Enhancements */
    div[data-testid="stForm"] {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom Color Badges for Grades */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    .grade-A { background-color: #059669; color: #FFFFFF; }
    .grade-B { background-color: #0284C7; color: #FFFFFF; }
    .grade-C { background-color: #D97706; color: #FFFFFF; }
    .grade-D { background-color: #EA580C; color: #FFFFFF; }
    .grade-E { background-color: #DC2626; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

# 3. Grading Logic & Badge Helper
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "E"

def render_grade_badge(grade):
    return f'<span class="badge grade-{grade}">{grade}</span>'

# Header Banner
st.markdown("""
    <div class="header-container">
        <div class="header-title">🎓 Student Grade Manager</div>
        <div class="header-subtitle">Track academic performance, calculate averages, and monitor class benchmarks</div>
    </div>
""", unsafe_allow_html=True)

# 4. Session State Initialization
if "students" not in st.session_state:
    st.session_state.students = []

# 5. Form Input Section
with st.form("add_student_form", clear_on_submit=True):
    st.markdown("<h4 style='color: #F1F5F9; margin-bottom: 15px;'>➕ Add New Record</h4>", unsafe_allow_html=True)
    
    col_name, col_mark = st.columns([2, 1])
    with col_name:
        name_input = st.text_input("Student Name", placeholder="e.g. Divya")
    with col_mark:
        mark_input = st.number_input("Mark (0 - 100)", min_value=0, max_value=100, step=1)
        
    submit_button = st.form_submit_button("Add Student Record", use_container_width=True)

    if submit_button:
        if not name_input.strip():
            st.warning("⚠️ Please enter a valid student name.")
        else:
            grade = get_grade(mark_input)
            st.session_state.students.append({
                "Name": name_input.strip(),
                "Mark": int(mark_input),
                "Grade": grade
            })
            st.success(f"✅ Record created for **{name_input.strip()}** ({grade})")

# 6. Metrics & Table View
if st.session_state.students:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Class Analytics")
    
    marks = [s["Mark"] for s in st.session_state.students]
    avg_mark = sum(marks) / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    # Custom Styled Cards for Metrics
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Class Average</div>
                <div class="metric-value" style="color: #60A5FA;">{avg_mark:.1f}</div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Highest Mark</div>
                <div class="metric-value" style="color: #34D399;">{highest_mark}</div>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Lowest Mark</div>
                <div class="metric-value" style="color: #F87171;">{lowest_mark}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Student Directory")

    # Render Styled Table with Badges
    df = pd.DataFrame(st.session_state.students)
    df["Grade"] = df["Grade"].apply(render_grade_badge)
    
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("📌 No student records found. Add students above to view analytics.")
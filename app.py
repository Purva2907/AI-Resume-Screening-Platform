# PART 1 - IMPORTS + UI + MODERN DASHBOARD

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime

from resume_parser import extract_text
from matcher import calculate_similarity
from skills import extract_skills

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Resume Screening Platform",
    page_icon="🚀",
    layout="wide"
)

# ====================================
# MODERN CSS
# ====================================

st.markdown("""
<style>
.stApp{
    background:linear-gradient(
        135deg,
        #f8fafc,
        #eef2ff
    );
}

.main-title{
    font-size:70px;
    font-weight:900;
    color:#0f172a;
    text-align:center;
}
.subtitle{
    text-align:center;
    color:#64748b;
    font-size:18px;
}

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #0f172a,
        #1e3a8a
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 25px rgba(0,0,0,.08);
}

[data-testid="metric-container"]{
    background:white;
    border-radius:18px;
    padding:15px;
    box-shadow:0px 8px 20px rgba(0,0,0,.08);
}

.stButton button{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)
# ====================================
# HEADER
# ====================================

st.markdown(
"""
<div class='main-title'>
🚀 AI Resume Screening Platform
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>
Smart Recruitment • ATS Analysis • Candidate Ranking
</div>
""",
unsafe_allow_html=True
)

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(135deg,#2563eb,#7c3aed);
color:white;
text-align:center;
margin-bottom:25px;
">
<h2>🚀 Smart AI Hiring Assistant</h2>
<p>Analyze • Rank • Recruit Candidates Faster</p>
</div>
""", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("📄 Resumes", "250+")

with col2:
    st.metric("🎯 Accuracy", "92%")

with col3:
    st.metric("🏆 Candidates", "500+")

with col4:
    st.metric("⚡ Processing", "2 sec")

# ====================================
# FEATURE CARDS
# ====================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info("🤖 AI Analysis")

with c2:
    st.success("🎯 ATS Matching")

with c3:
    st.warning("📊 Analytics")

with c4:
    st.error("🏆 Ranking")

st.divider()

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("🤖 AI Recruiter")

st.sidebar.info(
    f"🕒 {datetime.now().strftime('%d %b %Y | %H:%M')}"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "ATS Resume Screening",
        "Resume Ranking",
        "Recruiter Dashboard",
        "Interview Questions"
    ]
)

st.sidebar.divider()

candidate_name = st.sidebar.text_input(
    "Candidate Name"
)

st.sidebar.markdown("""
<div style="
background:#1e3a8a;
padding:20px;
border-radius:15px;
text-align:center;
color:white;
">
<h3>👩‍💻 Purva Patil</h3>
<p>AI Developer</p>
<p>Resume Screening Platform</p>
</div>
""", unsafe_allow_html=True)

# ====================================
# ATS SCREENING PAGE
# ====================================

if page == "ATS Resume Screening":

    st.header("🎯 ATS Resume Screening")

    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )

    input_method = st.radio(
        "Resume Input Method",
        [
            "Upload PDF",
            "Paste Resume Text"
        ]
    )

    resume_text = ""

    if input_method == "Upload PDF":

        uploaded_file = st.file_uploader(
            "Upload Resume PDF",
            type=["pdf"]
        )

        if uploaded_file:

            resume_text = extract_text(
                uploaded_file
            )

    else:

        resume_text = st.text_area(
            "Paste Resume Content",
            height=300
        )

       # ====================================
    # ATS ENGINE
    # ====================================

    if resume_text and job_description:

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            job_description
        )

        matched_skills = list(
            set(resume_skills).intersection(
                set(jd_skills)
            )
        )

        missing_skills = list(
            set(jd_skills) -
            set(resume_skills)
        )

        skill_match_score = (
            len(matched_skills) /
            max(len(jd_skills), 1)
        ) * 100

        score = (
    similarity_score * 0.4 +
    skill_match_score * 0.6
)
        st.success(
            "Resume Processed Successfully ✅"
        )

        # ===============================
        # CANDIDATE GRADE
        # ===============================

        if score >= 90:
            grade = "A+"
            grade_msg = "🌟 Outstanding Candidate"

        elif score >= 80:
            grade = "A"
            grade_msg = "✅ Strong Candidate"

        elif score >= 70:
            grade = "B"
            grade_msg = "👍 Recommended"

        elif score >= 60:
            grade = "C"
            grade_msg = "⚠ Consider for Interview"

        else:
            grade = "Needs Improvement"
            grade_msg = "❌ Not Recommended"

        # ===============================
        # DASHBOARD METRICS
        # ===============================

        m1, m2, m3, m4, m5 = st.columns(5)

        with m1:
            st.metric("ATS Score", f"{score:.2f}%")

        with m2:
            st.metric("Grade", grade)

        with m3:
            st.metric("Skills Found", len(resume_skills))

        with m4:
            st.metric("Matched Skills", len(matched_skills))

        with m5:
            st.metric("Missing Skills", len(missing_skills))

        st.progress(min(int(score), 100))

        if score >= 80:
            st.success(grade_msg)

        elif score >= 60:
            st.info(grade_msg)

        else:
            st.error(grade_msg)
        # ===============================
        # ATS DASHBOARD
        # ===============================

        st.subheader("📊 ATS Performance Dashboard")

        gauge_col, imp_col = st.columns(2)

        with gauge_col:

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=score,
                    title={"text": "ATS Score"},
                    gauge={
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "green"}
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with imp_col:

            improvement = 100 - score

            st.metric(
                "Improvement Potential",
                f"{improvement:.1f}%"
            )

            if score >= 80:
                st.success("🎯 Highly Recommended")

            elif score >= 60:
                st.info("👍 Recommended")

            else:
                st.error("❌ Not Recommended")

        # ===============================
        # QUALITY SCORE
        # ===============================

        quality_score = min(
            len(resume_skills) * 8,
            100
        )

        st.subheader("⭐ Resume Quality Score")

        q1, q2 = st.columns(2)

        with q1:
            st.metric(
                "Quality Score",
                f"{quality_score}%"
            )

        with q2:
            st.metric(
                "Candidate Grade",
                grade
            )

        st.progress(
            min(int(quality_score), 100)
        )

        # ===============================
        # SKILLS SECTION
        # ===============================

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matched Skills")

            if matched_skills:

                for skill in matched_skills:
                    st.success(skill)

            else:
                st.warning("No matching skills")

        with right:

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.error(skill)

            else:
                st.success("No missing skills")

        # ===============================
        # DOMAIN PREDICTION
        # ===============================

        st.subheader("🧠 Domain Prediction")

        text = resume_text.lower()

        domain = "General"

        if "machine learning" in text or "python" in text:
            domain = "AI / ML Engineer"

        elif "html" in text or "css" in text or "javascript" in text:
            domain = "Web Developer"

        elif "sql" in text or "power bi" in text:
            domain = "Data Analyst"

        elif "network" in text or "security" in text:
            domain = "Cyber Security"

        st.success(domain)

               # ===============================
        # AI RECOMMENDATIONS
        # ===============================

        st.subheader("💡 AI Recommendations")

        if missing_skills:
            st.code(", ".join(missing_skills))

        else:
            st.success(
                "Resume is well optimized."
            )

        # ===============================
        # RESUME REPORT CARD
        # ===============================

        st.subheader("📋 Resume Report Card")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "ATS Match",
                f"{score:.2f}%"
            )

            st.metric(
                "Resume Quality",
                f"{quality_score}%"
            )

        with col2:

            st.metric(
                "Skills Match",
                f"{len(matched_skills)}/{len(jd_skills)}"
            )

            st.metric(
                "Recommendation",
                grade
            )
    
        # ===============================
        # SKILL CHART
        # ===============================

        chart_df = pd.DataFrame({
            "Category": ["Matched", "Missing"],
            "Count": [
                len(matched_skills),
                len(missing_skills)
            ]
        })

        fig = px.pie(
            chart_df,
            names="Category",
            values="Count",
            hole=0.4,
            title="Skill Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ===============================
        # RESUME CONTENT
        # ===============================

        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=250
        )

# ====================================
# RESUME RANKING PAGE
# ====================================

elif page == "Resume Ranking":

    st.header(
        "🏆 Resume Ranking System"
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=200,
        key="ranking_jd"
    )

    uploaded_files = st.file_uploader(
        "Upload Multiple Resumes",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files and job_description:

        results = []

        with st.spinner(
            "Analyzing Resumes..."
        ):

            for uploaded_file in uploaded_files:

                resume_text = extract_text(
                    uploaded_file
                )

                score = calculate_similarity(
                    resume_text,
                    job_description
                )

                results.append(
                    {
                        "Name":
                        uploaded_file.name,

                        "Score":
                        round(score,2)
                    }
                )

        results.sort(
            key=lambda x:x["Score"],
            reverse=True
        )

        df = pd.DataFrame(
            results
        )

        # ==========================
        # DASHBOARD
        # ==========================

        st.subheader(
            "📊 Recruitment Dashboard"
        )

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Resumes",
                len(df)
            )

        with c2:
            st.metric(
                "Top Score",
                f"{df.iloc[0]['Score']}%"
            )

        with c3:

            shortlisted = len(
                df[
                    df["Score"] >= 50
                ]
            )

            st.metric(
                "Shortlisted",
                shortlisted
            )

        with c4:

            rejected = len(df) - shortlisted

            st.metric(
                "Rejected",
                rejected
            )

        # ==========================
        # BEST CANDIDATE
        # ==========================

        st.subheader(
            "🥇 Best Candidate"
        )

        best_name = df.iloc[0]["Name"]
        best_score = df.iloc[0]["Score"]

        st.success(
            f"""
🏆 Candidate: {best_name}

🎯 ATS Score: {best_score}%

✅ Recommended for Interview
"""
        )
        st.subheader(
            "🏅 Top 3 Candidates"
        )

        top3 = df.head(3)

        for i, row in top3.iterrows():

            if i == 0:
                medal = "🥇"

            elif i == 1:
                medal = "🥈"

            else:
                medal = "🥉"

            st.info(
                f"{medal} {row['Name']} — {row['Score']}%"
            )
        
        # ==========================
        # LEADERBOARD
        # ==========================

        st.subheader(
            "🏅 Leaderboard"
        )

        medals = [
            "🥇",
            "🥈",
            "🥉"
        ]

        for idx,row in enumerate(
            results
        ):

            medal = (
                medals[idx]
                if idx < 3
                else "🏅"
            )

            st.write(
                f"{medal} "
                f"{row['Name']} "
                f"→ {row['Score']}%"
            )

        # ==========================
        # SEARCH
        # ==========================

        st.subheader(
            "🔍 Search Candidate"
        )

        search = st.text_input(
            "Candidate Name"
        )

        if search:

            filtered = df[
                df["Name"]
                .str.contains(
                    search,
                    case=False
                )
            ]

            st.dataframe(
                filtered,
                use_container_width=True
            )

        # ==========================
        # TABLE
        # ==========================

        st.subheader(
            "📋 Ranking Table"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # ==========================
        # BAR CHART
        # ==========================

        st.subheader(
            "📈 Score Comparison"
        )

        fig = px.bar(
            df,
            x="Name",
            y="Score",
            color="Score",
            title="Resume Ranking"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================
        # SHORTLIST
        # ==========================

        st.subheader(
            "✅ Shortlisted Candidates"
        )

        shortlist = df[
            df["Score"] >= 50
        ]

        st.dataframe(
            shortlist,
            use_container_width=True
        )

        # ==========================
        # EXPORT
        # ==========================

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            "⬇ Download Ranking CSV",
            csv,
            "resume_rankings.csv",
            "text/csv"
        )

# ====================================
# RECRUITER DASHBOARD
# ====================================

elif page == "Recruiter Dashboard":

    st.header(
        "📊 Recruiter Analytics"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Resumes",
            250
        )

    with c2:
        st.metric(
            "Shortlisted",
            142
        )

    with c3:
        st.metric(
            "Interviews",
            87
        )

    with c4:
        st.metric(
            "Hired",
            32
        )

    sample_data = pd.DataFrame({

        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Candidates":[
            20,
            35,
            28,
            50,
            65
        ]

    })

    fig = px.line(
        sample_data,
        x="Month",
        y="Candidates",
        markers=True,
        title="Hiring Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "📊 Hiring Status Distribution"
    )

    pie_data = pd.DataFrame({
        "Status": [
            "Shortlisted",
            "Interviewed",
            "Hired",
            "Rejected"
        ],
        "Count": [
            142,
            87,
            32,
            108
        ]
    })

    pie_fig = px.pie(
        pie_data,
        names="Status",
        values="Count",
        hole=0.4,
        title="Recruitment Funnel"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )
    st.subheader(
        "🏢 Department Hiring"
    )

    dept_df = pd.DataFrame({
        "Department": [
            "AI/ML",
            "Cyber Security",
            "Data Analyst",
            "Web Development",
            "Cloud"
        ],
        "Candidates": [
            45,
            30,
            25,
            20,
            15
        ]
    })

    dept_fig = px.bar(
        dept_df,
        x="Department",
        y="Candidates",
        color="Candidates",
        title="Hiring by Department"
    )

    st.plotly_chart(
        dept_fig,
        use_container_width=True
    )
    st.subheader(
        "👨‍💼 Recruiter Performance"
    )

    recruiter_df = pd.DataFrame({
        "Recruiter": [
            "Purva",
            "Ram",
            "Sakshi",
            "Priya"
        ],
        "Resumes Reviewed": [
            120,
            95,
            80,
            70
        ],
        "Candidates Hired": [
            20,
            15,
            12,
            10
        ]
    })

    st.dataframe(
        recruiter_df,
        use_container_width=True
    )
    st.subheader(
        "⬇ Download Analytics Report"
    )

    csv_data = recruiter_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download Recruiter Report",
        data=csv_data,
        file_name="recruiter_analytics.csv",
        mime="text/csv"
    )
    st.subheader(
        "📌 Dashboard Summary"
    )

    st.info(
        """
        Total Resumes Processed: 250

        Candidates Shortlisted: 142

        Interviews Conducted: 87

        Successful Hires: 32

        Overall Hiring Efficiency: 64%
        """
    )
    st.subheader(
        "🎯 Recruitment Funnel"
    )

    funnel_df = pd.DataFrame({
        "Stage": [
            "Applications",
            "Screened",
            "Shortlisted",
            "Interviewed",
            "Hired"
        ],
        "Count": [
            250,
            200,
            142,
            87,
            32
        ]
    })

    funnel_fig = px.funnel(
        funnel_df,
        x="Count",
        y="Stage",
        title="Recruitment Pipeline"
    )

    st.plotly_chart(
        funnel_fig,
        use_container_width=True
    )
# ====================================
# INTERVIEW QUESTIONS
# ====================================

elif page == "Interview Questions":

    st.header(
        "🎤 AI Interview Questions"
    )

    domain = st.selectbox(

        "Choose Domain",

        [
            "Python",
            "Machine Learning",
            "SQL",
            "Data Analyst",
            "Web Development"
        ]
    )

    questions = {

        "Python":[
            "What is OOP?",
            "Difference between list and tuple?",
            "Explain decorators."
        ],

        "Machine Learning":[
            "What is Overfitting?",
            "Difference between Bagging and Boosting?",
            "Explain Cross Validation."
        ],

        "SQL":[
            "What is JOIN?",
            "Difference between WHERE and HAVING?",
            "Explain Primary Key."
        ],

        "Data Analyst":[
            "What is Power BI?",
            "Explain Data Cleaning.",
            "What is KPI?"
        ],

        "Web Development":[
            "Difference between HTML and HTML5?",
            "Explain CSS Flexbox.",
            "What is JavaScript?"
        ]
    }

    st.subheader(
        "Questions"
    )

    for q in questions[domain]:

        st.success(q)

    st.markdown("""
---
<center>
🚀 Made with Streamlit • Developed by Purva Patil
</center>
""", unsafe_allow_html=True)

    st.caption(
        "Developed by Purva Patil | AI Resume Screening Platform"
    )
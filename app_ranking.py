import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from resume_parser import extract_text
from matcher import calculate_similarity

# -------------------------
# PAGE SETTINGS
# -------------------------

st.set_page_config(
    page_title="AI Resume Ranking System",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Resume Ranking System")

st.write(
    "Upload multiple resumes and rank them according to the job description."
)

# -------------------------
# JOB DESCRIPTION
# -------------------------

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

# -------------------------
# FILE UPLOAD
# -------------------------

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------
# PROCESS FILES
# -------------------------

if uploaded_files and job_description:

    results = []

    with st.spinner("Analyzing resumes..."):

        for uploaded_file in uploaded_files:

            resume_text = extract_text(uploaded_file)

            score = calculate_similarity(
                resume_text,
                job_description
            )

            results.append(
                {
                    "name": uploaded_file.name,
                    "score": round(score, 2)
                }
            )

    # Sort descending
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    st.success("Analysis Complete ✅")

    # -------------------------
    # BEST CANDIDATE
    # -------------------------

    best_candidate = results[0]

    st.subheader("🏆 Recommended Candidate")

    st.success(
        f"{best_candidate['name']} "
        f"({best_candidate['score']}%)"
    )

    # -------------------------
    # RANKINGS
    # -------------------------

    st.subheader("🏅 Resume Rankings")

    for index, result in enumerate(results, start=1):

        if index == 1:
            medal = "🥇"
        elif index == 2:
            medal = "🥈"
        elif index == 3:
            medal = "🥉"
        else:
            medal = "📄"

        st.write(
            f"{medal} Rank {index}: "
            f"{result['name']} → {result['score']}%"
        )

    # -------------------------
    # SHORTLIST STATUS
    # -------------------------

    st.subheader("📋 Candidate Status")

    for result in results:

        if result["score"] >= 70:

            st.success(
                f"{result['name']} → SHORTLISTED ✅"
            )

        else:

            st.error(
                f"{result['name']} → REJECTED ❌"
            )

    # -------------------------
    # TABLE
    # -------------------------

    st.subheader("📊 Ranking Table")

    df = pd.DataFrame(results)

    st.dataframe(
        df,
        use_container_width=True
    )

    # -------------------------
    # BAR CHART
    # -------------------------

    st.subheader("📈 Resume Score Comparison")

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        df["name"],
        df["score"]
    )

    ax.set_ylabel("Score (%)")
    ax.set_xlabel("Resume")
    ax.set_title("Resume Ranking Scores")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # -------------------------
    # CSV DOWNLOAD
    # -------------------------

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Ranking Report",
        data=csv,
        file_name="resume_rankings.csv",
        mime="text/csv"
    )

# -------------------------
# WARNING
# -------------------------

elif uploaded_files and not job_description:

    st.warning(
        "Please enter a Job Description first."
    )
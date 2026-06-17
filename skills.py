SKILLS = [

    # Programming
    "python","java","c","c++","c#","javascript",
    "typescript","php","ruby","go","rust",

    # Web
    "html","css","react","angular","vue",
    "nodejs","express","django","flask",

    # Data
    "sql","mysql","postgresql","mongodb",
    "power bi","tableau","excel","pandas",
    "numpy","matplotlib",

    # AI/ML
    "machine learning","deep learning",
    "tensorflow","pytorch","nlp",
    "computer vision","scikit-learn",

    # Cloud
    "aws","azure","gcp","docker",
    "kubernetes","linux",

    # Cyber Security
    "cyber security",
    "network security",
    "penetration testing",
    "risk assessment",
    "security analysis",
    "ethical hacking",
    "siem",
    "soc",
    "firewall",
    "incident response",
    "vulnerability assessment",

    # Soft Skills
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills
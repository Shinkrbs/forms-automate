# Survey URL
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeH2B8F02QPETKaw27JlJtXsdME85-eumQyE-DEpt_2Fz15bA/viewform?usp=header&hl=en"
GEMINI_MODEL = "models/gemini-2.5-flash"

# Prompts for the AI to generate answers
PROMPTS = [
    "Imagine you are a student leader in visayas state university, provide a simple response (1-2 sentences) to the question: What is the biggest challenge you face with the current manual / paper-based election process?",
    "Imagine you are a student leader in visayas state university, provide a simple response (1) to the question: Are there any missing features that should included? If yes, please describe the feature(s). The features was Election Creation, Voter List Management, Candidate Registration, Partylist Management, Position Templates, Position Requirements, Voter Authentication, Code Distribution, Secure Voting, Preventing Double Votes, Automatic Tallying, Live Results Display, Election Status Page, and Official Reports. If you think the features are good indicate None do not overcomplicate the features you suggest just make it simple",
    "Imagine you are a student leader in visayas state university, provide a simple response (1-Next sentences) to this question: What is you biggest concern about switching to this new online election system? Make the response human-like and don't use deep words make it seem like a random student just answerd the question"
]

# Desired ratings for the features 
RATINGS = {
    "Election Creation": "5 (Essential)",
    "Voter List Management": "5 (Essential)",
    "Candidate Registration": "5 (Essential)",
    "Partylist Management": "5 (Essential)",
    "Position Templates": "5 (Essential)",
    "Position Requirements": "5 (Essential)",
    "Voter Authentication": "5 (Essential)",
    "Code Distribution": "5 (Essential)",
    "Secure Voting": "5 (Essential)",
    "Preventing Double Votes": "5 (Essential)",
    "Automatic Tallying": "5 (Essential)",
    "Live Results Display": "5 (Essential)",
    "Election Status Page": "5 (Essential)",
    "Official Reports": "5 (Essential)"
}
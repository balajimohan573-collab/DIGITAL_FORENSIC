# Function to detect phishing indicators

def detect_phishing(sender, subject, body):
    score = 0

    suspicious_sender = [
        "support@", "admin@", "verify@", "security@", "noreply@"
    ]

    suspicious_subject = [
        "urgent", "verify", "account", "password",
        "bank", "winner", "prize", "click", "limited offer"
    ]

    suspicious_body = [
        "click here",
        "verify your account",
        "login immediately",
        "update your password",
        "bank account",
        "free gift",
        "claim your prize",
        "limited time",
        "confirm your identity"
    ]

    # Check sender
    for word in suspicious_sender:
        if word.lower() in sender.lower():
            score += 1

    # Check subject
    for word in suspicious_subject:
        if word.lower() in subject.lower():
            score += 1

    # Check body
    for word in suspicious_body:
        if word.lower() in body.lower():
            score += 1

    print("\n----- Detection Result -----")
    print("Suspicious Score:", score)

    if score >= 3:
        print("⚠️ Warning: This email is likely a PHISHING email.")
    else:
        print("✅ This email appears to be SAFE.")


# Input from user
sender = input("Enter Sender Email: ")
subject = input("Enter Subject: ")
body = input("Enter Email Body: ")

detect_phishing(sender, subject, body)
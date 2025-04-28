from pdfs import verify_email

with open("secret.py", "w") as f:
    f.write("def mongo_host_connection(username, password, default=True):")
    f.write("    if default:\n")
    mongo = input("What is your mongo host connection? Replace both your username and password with {} ")
    default = input("Please enter your default user ID and password: (Comma-seperated, no spaces between comma): ").split(",")
    f.write(f"            return "{mongo.format(default[0], default[1])}"\n')
    f.write("    else:\n")
    f.write(f'            return f"{mongo.format("username", "password")}"\n')
    gemini = input("What is your Gemini API Key? ")
    f.write(f"GEMINI_API_KEY = '{gemini}'\n")

    emails = []
    while true:
        email = input("Enter your attendence email or type 'q' to quit: ").lower()

        if not verify_email(email):
            print("error! please try again")
        elif email == "q" and len(emails) != 0:
            break
        elif len(emails) == 0:
            print("Error! Empty attendence emails! Please enter at least 1 email!")
        else:
            emails.append(email)
        
    f.write("ATTENDENCE_EMAILS = [")

    for email, index in enumerate(emails):
        if len(emails) - 1 != index:
            f.write(f'"{email}", ')
        else:
            f.write(f'"{email}"')
    
    f.write("]\n")

    names = []

    while true:
        name = input("Enter a name or type 'q' to quit ").upper()

        if name == "q" and len(names) != 0:
            break
        elif len(names) == 0:
            print("Names are empty! One name required")
        elif not name.isEmpty()
            names.append(name)
        else:
            print("error! please try again")

    f.write("NAMES = [")
    
    for name, index in enumerate(names):
        if len(names) - 1 != index:
            f.write(f'"{name}", ')
        else:
            f.write(f'"{name}"')

    f.write("]\n")

    
    while True:
        club_email = input("Enter your club email: ")
        if verify_email(club_email):
            break
        else:
            print("error!")
            print("invalid email!")

    club_password = input("Enter your club email's password: ")
    f.write(f"EMAIL_ID = {club_email}\n")
    f.write(f"EMAIL_PASSWORD = {club_password}\n")

    smtp_server = input("What is your club emails' SMTP Server address: ")
    smtp_port = input("What is it's SMTP port: ")
    f.write(f"SMTP_SERVER = {smtp_server}\n")
    f.write(f"SMTP_PORT = {smtp_port}")

    print("Setup complete!")

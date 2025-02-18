import spacy

nlp = spacy.load("en_core_web_sm")
#Requirement text
feature_desc = "A user can login using an email and password. The system should lock after three tries."
doc = nlp(feature_desc)
actions = [token.text for token in doc if token.pos_ in ["VERB"]]
test_case = {
    "Test Scenario":"User Login",
    "Test Steps" :   [f"Step 1: {actions[0]} - Enter email and password",
                      f"Step 2: {actions[1]}  - Click login",
                       f"Step 3: {actions[2]} - Enter wrong password 3 times",
                       "Step 4: Verify account is locked"
                      ],
                      "Expected Result": "User is logged in or account is locked after 3 failed attempts"
            }

for step in test_case["Test Steps"]:
    print(step)
print(f"Expected Result: {test_case['Expected Result']}")

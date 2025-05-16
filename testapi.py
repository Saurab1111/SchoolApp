import requests

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJleHAiOjE3NDU0MjQxNDJ9.ho2-a5BK_e7W8oJETz01i8jGQAmE1HK9_004yTEqGbs"  # 🔐 Replace with your actual token

url = "http://127.0.0.1:8000/accounts/login/"  # 🔒 Replace with your protected API URL

# headers = {
#     "Authorization": f"Bearer {token}"
# }

response = requests.post(url,data={'username':'saurabh','password':'123456789'})

print("Status:", response.status_code)
print("Response:", response.text)

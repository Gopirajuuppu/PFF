import instructor
from pydantic import BaseModel
from openai import OpenAI


# Define your desired output structure
class UserInfo(BaseModel):
    name: str
    age: int
    DOB: str
    gender: str
    health_insurance: bool
    occupation: str
    medical_history: str
    medications: str
    family_medical_history : str
    habits: str

#this is to get the structred personal details from raw summary which in unstrctred text data
def get_personal_details(user_summary): 
    client = instructor.from_openai(OpenAI())    
    user_info = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=UserInfo,
        messages=[{"role": "user", "content": user_summary}],
    )   
    if user_info.health_insurance:
        health_Insurance = 'Provided'
    else:
        health_Insurance = 'Not Provided'
        
    user_data = {
          "Name": user_info.name,
          "Age": user_info.age,
          "DOB":user_info.DOB,
          "Gender":user_info.gender,
          "Health Insurance":health_Insurance,
          "Occupation":user_info.occupation,
          "Medical History": user_info.medical_history,
          "Medications":user_info.medications,
          "Family Medical History": user_info.family_medical_history,
          "Habits":user_info.habits          
    }
    
    return user_data
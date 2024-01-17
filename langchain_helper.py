from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # Assuming there is a class or function named OpenAI in the openai module
    llm = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} and I want cool names for it, it is {pet_color}. Suggest me five cool names for my pet."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='pet_name')
  
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return response



if __name__ == "__main__":
    print(generate_pet_name("cow", "black"))
    
    
    


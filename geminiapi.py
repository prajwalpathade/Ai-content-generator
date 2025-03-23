import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCLdje77mjIsdSB0W8PNDXpj5K5ntJ3ieo")

# Function to generate content with error handling
def generate_content(prompt, model="gemini-1.5-pro-latest"):
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text.strip()  # Removes unnecessary whitespace
    except Exception as e:
        return f"Error: {str(e)}"

# User Inputs
try:
    topic = input("Enter a topic for content generation: ")
    tone = input("Enter the tone (e.g., professional, casual, humorous): ")
    length = input("Enter desired length (short, medium, long): ")
except Exception as e:
    print("You Got the ERRORRRRRRRRR BUT HANDLEDDD !!!!",e)

# Prompt Structure
prompt = f"Write a {length} article on '{topic}' in a {tone} tone."

# Generate Content
output = generate_content(prompt)

# Display Output
print("\nGenerated Content:\n" + "="*50)
print(output)
print("="*50)

# Save Output to File
file_name = f"{topic.replace(' ', '_')}_content.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(output)

print(f"\n✅ Content saved as '{file_name}'")






























# import google.generativeai as genai
#
# genai.configure(api_key="AIzaSyCLdje77mjIsdSB0W8PNDXpj5K5ntJ3ieo")
#
# def generate_content(prompt,model):
#     model= genai.GenerativeModel(model)
#     response = model.generate_content(prompt)
#     return response.text
#
# a = input("Enter topic to generate content:")
# b = input("Enter tone of content (Professional,Casual,Humorous):")
# c = input("Enter Length of content(Short,Medium,Large):")
# e = input("Enter which model do you want to get output from?\na)gemini-1.5-pro-latest\nb)gemini-pro):")
#
# if e=='a':
#     model ="gemini-1.5-pro-latest"
# elif e=='b':
#     model ="gemini-pro"
# else :
#     print("Choose from a or b only...")
#
# prompt=f"Generate a content for instagram on {a} in {b} tone for {c} length"
#
# print(generate_content(prompt,model))
#
#
#
#
























# import google.generativeai as genai
#
# # Configure the API key
# genai.configure(api_key="AIzaSyCLdje77mjIsdSB0W8PNDXpj5K5ntJ3ieo")
#
# # Function to generate content
# def generate_content(prompt, model="gemini-1.5-pro-latest"):
#     model = genai.GenerativeModel(model)
#     response = model.generate_content(prompt)
#     return response.text
#
# # Example usage
# topic = input("Enter a topic for content generation: ")
# tone = input("Enter the tone (e.g., professional, casual, humorous): ")
# length = input("Enter desired length (short, medium, long): ")
#
# # Crafting the prompt
# prompt = f"Write a {length} article on '{topic}' in a {tone} tone."
#
# # Generate & display content
# output = generate_content(prompt)
# print("\nGenerated Content:\n", output)

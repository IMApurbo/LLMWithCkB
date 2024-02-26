import os
from transformers import T5ForConditionalGeneration
import languagemodels as lm

# Function to read text from TXT files
def read_txt(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text

# Function to read contents of all text files and return the combined context
def read_all_text_files():
    # Define folder for text files
    txt_folder = "txt"

    # Get the paths of all text files in the folder
    txt_files = [os.path.join(txt_folder, file) for file in os.listdir(txt_folder) if file.endswith(".txt")]

    # Read the contents of all text files
    context = ""
    for file_path in txt_files:
        context += read_txt(file_path)
    return context

# Main function to run the program
def main():
    while True:
        # Read the contents of all text files
        context = read_all_text_files()

        # Ask the user for input
        user_input = input("Ask a question (type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        # Get the answer using the language model with the context from the text files
        answer = lm.do(f"{user_input} Answer from the context: {context}")

        # Display the answer
        print("Answer:", answer)

# Call the main function to start the program
if __name__ == "__main__":
    main()

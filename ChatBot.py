from transformers import T5ForConditionalGeneration
import languagemodels as lm
import os
import PyPDF2
import docx

# Function to read text from PDF files
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

# Function to read text from DOCX files
def read_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to read text from TXT files
def read_txt(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text

# Function to read contents of all files and return the combined context
def read_all_files():
    # Define folders for different file types
    pdf_folder = "pdf"
    docx_folder = "doc"
    txt_folder = "txt"

    # Get the paths of all files in the folders
    pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]
    docx_files = [os.path.join(docx_folder, file) for file in os.listdir(docx_folder) if file.endswith(".docx")]
    txt_files = [os.path.join(txt_folder, file) for file in os.listdir(txt_folder) if file.endswith(".txt")]

    # Combine all file paths
    all_files = pdf_files + docx_files + txt_files

    # Read the contents of all files
    context = ""
    for file_path in all_files:
        if file_path.endswith(".pdf"):
            context += read_pdf(file_path)
        elif file_path.endswith(".docx"):
            context += read_docx(file_path)
        elif file_path.endswith(".txt"):
            context += read_txt(file_path)
    return context

# Main function to run the program
def main():
    while True:
        # Read the contents of all files
        context = read_all_files()

        # Ask the user for input
        user_input = input("Ask a question (type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        # Get the answer using the language model with the context from the files
        answer = lm.do(f"{user_input} Answer from the context: {context}")

        # Display the answer
        print("Answer:", answer)

# Call the main function to start the program
if __name__ == "__main__":
    main()

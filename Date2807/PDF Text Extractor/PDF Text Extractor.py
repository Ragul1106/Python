import PyPDF2

def extract_text(pdf_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            if reader.is_encrypted:
                print("PDF is encrypted. Cannot extract text.")
                return

            for page in reader.pages:
                text = page.extract_text()
                if text:

                    yield text.strip()
                else:
                    yield "[No text found on this page]"
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    path = "sample.pdf" 
    for page_num, content in enumerate(extract_text(path), start=1):
        print(f"\n--- Page {page_num} ---\n{content}")

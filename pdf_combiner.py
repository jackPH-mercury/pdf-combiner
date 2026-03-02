import sys
import os
from PyPDF2 import PdfMerger

def main():

    # 1 & 2. Read output file name from command line
    if len(sys.argv) < 2:
        print("Error: Merge file name not specified.")
        print("Usage: python pdfmerger.py filename")
        sys.exit(1)

    output_name = sys.argv[1] + ".pdf"

    # 3. Initialize merger object
    merger = PdfMerger()

    # 4. Retrieve files in current directory
    files = os.listdir(".")

    # 5. Filter only .pdf files
    pdf_files = [f for f in files if f.lower().endswith(".pdf")]

    # 6. Sort alphabetically
    pdf_files.sort()

    # 7. Report files found
    print(f"PDF files found: {len(pdf_files)}")
    print("List:")

    for file in pdf_files:
        print(file)

    if len(pdf_files) == 0:
        print("No PDF files to merge.")
        sys.exit(0)

    # 8. Prompt user to continue
    choice = input("Continue (y/n): ").strip().lower()

    if choice != 'y':
        print("Operation cancelled.")
        sys.exit(0)

    # 9. Append PDFs (skip output file if it already exists)
    for pdf in pdf_files:
        if pdf == output_name:
            continue
        merger.append(pdf)

    # 10. Export merged file
    merger.write(output_name)
    merger.close()

    print(f"Merged file created successfully: {output_name}")


if __name__ == "__main__":
    main()
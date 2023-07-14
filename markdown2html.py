#!/usr/bin/python3

import sys
import os

def markdown2html(markdown_file, output_file):
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the file paths from the command line arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Perform the Markdown to HTML conversion here
    # Replace this with your own logic

    # If everything is successful, exit with code 0
    sys.exit(0)

# Execute the script
if __name__ == "__main__":
    markdown2html(sys.argv[1], sys.argv[2])

import sys
import os
import re
import hashlib


def parse_inline_markup(text):
    """
    Parses inline markup syntax for bold and emphasis.
    """
    bold_pattern = r"\*\*(.+?)\*\*"
    emphasis_pattern = r"__(.+?)__"
    md5_pattern = r"\[\[(.+?)\]\]"
    remove_c_pattern = r"\(\((.*?)\)\)"
    text = re.sub(bold_pattern, r"<b>\1</b>", text)
    text = re.sub(emphasis_pattern, r"<em>\1</em>", text)
    text = re.sub(md5_pattern, lambda x: hashlib.md5(
        x.group(1).encode()).hexdigest(), text)
    text = re.sub(remove_c_pattern, '', text)
    return text


def parse_markup(text):
    """
    Parses markup syntax for headings, lists, and inline markup.
    """
    lines = text.split("\n")
    parsed_lines = []
    in_list = False
    for line in lines:
        if line.startswith("#"):
            # Heading
            level = len(line.split()[0])
            parsed_lines.append(f"<h{level}>{line[level+1:]}</h{level}>")
        elif line.startswith("*"):
            # Unordered List Item
            if not in_list:
                in_list = True
                parsed_lines.append("<ul>")
            parsed_lines.append(f"<li>{line[2:]}</li>")
        elif in_list:
            # End of List
            in_list = False
            parsed_lines.append("</ul>")
        else:
            # Regular Paragraph
            parsed_lines.append(parse_inline_markup(line))
    if in_list:
        # End of List
        parsed_lines.append("</ul>")
    return "\n".join(parsed_lines)


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(input_file, encoding="utf-8") as f:
        markdown_text = f.read()
        html_text = parse_markup(markdown_text)

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)


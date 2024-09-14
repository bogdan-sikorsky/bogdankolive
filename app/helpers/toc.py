import re


# Extract only the biggest (level 1) headers from markdown
def extract_biggest_headers(markdown_text):
    headers = []
    lines = markdown_text.split("\n")
    for line in lines:
        match = re.match(r'^(#{1})\s+(.+)', line)  # Only match level 1 headers (single '#')
        if match:
            title = match.group(2).strip()
            header_id = re.sub(r'\s+', '-', title.lower())  # Generate an anchor id
            headers.append((title, header_id))
    return headers


# Generate the table of contents based on the extracted biggest headers
def generate_toc(markdown_text):
    headers = extract_biggest_headers(markdown_text)
    toc = '<div class="toc">'
    for title, header_id in headers:
        toc += f'<a href="#{header_id}">{title}</a>'
    toc += '</div>'
    return toc


# Insert markdown content with anchors
def generate_content_with_anchors(markdown_text, headers):
    content = markdown_text
    for title, header_id in headers:
        anchor_tag = f'<a id="{header_id}"></a>'
        content = content.replace(f'# {title}', f'# {title}{anchor_tag}')
    return content

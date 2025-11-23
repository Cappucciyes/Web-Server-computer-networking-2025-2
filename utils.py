def build_response(body, status="200 OK", content_type="text/html"):
    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        "\r\n"
        f"{body}"
    )
    return response

def getFileAsString(pathToFile):
    result = ''
    try:
        with open(pathToFile, 'r', encoding='utf-8') as file:
            html_content = file.read()
        result += html_content
    except FileNotFoundError:
        print(f"Error: The file '{pathToFile}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return result
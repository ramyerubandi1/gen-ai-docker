import os

PROMPT = """
ONLY Generate an ideal Dockerfile for a {language} project with best practices.
Use the specified main file: {filename}
Do not provide any description.

Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application using {filename}
"""

def generate_dockerfile(language, filename):
    # Simulated generation for GitHub Actions (no real Ollama there)
    if os.getenv("GITHUB_ACTIONS"):
        return f"""FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "{filename}"]
"""

    import ollama
    response = ollama.chat(
        model='llama3.2:1b',
        messages=[{
            'role': 'user',
            'content': PROMPT.format(language=language, filename=filename)
        }]
    )
    return response['message']['content']

if __name__ == '__main__':
    language = input("Enter the programming language (e.g., python): ").strip().lower()
    filename = input("Enter the main script filename (e.g., calculator.py): ").strip()

    dockerfile = generate_dockerfile(language, filename)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)

    save = input("Save Dockerfile to file? (y/n): ").strip().lower()
    if save == 'y':
        with open('Dockerfile', 'w') as f:
            f.write(dockerfile)
        print("✅ Dockerfile saved.")


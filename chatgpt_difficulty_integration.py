import json
import sqlite3
import random
import openai

# Step 1: Set up your OpenAI API key
openai.api_key = "your-openai-api-key"  # Replace with your actual OpenAI API key

# Step 2: Create a database or use sample JSON data
def create_db():
    # Connect to SQLite (or create a new database)
    conn = sqlite3.connect('question_difficulty.db')
    c = conn.cursor()

    # Create a table for questions, including a new column for ChatGPT-generated difficulty
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question_text TEXT,
            manual_difficulty TEXT,
            calculated_difficulty REAL,
            response_time REAL,
            average_score REAL,
            chatgpt_difficulty TEXT  -- New column to store difficulty from ChatGPT
        )
    ''')
    conn.commit()

    # Add sample questions to the database
    sample_questions = [
        ("What is 2 + 2?", "Easy", None, random.uniform(1, 5), random.uniform(90, 100)),
        ("What is the derivative of x^2?", "Medium", None, random.uniform(5, 10), random.uniform(70, 85)),
        ("What is the integral of sin(x)?", "Hard", None, random.uniform(10, 15), random.uniform(50, 70)),
    ]
    c.executemany('''
        INSERT INTO questions (question_text, manual_difficulty, calculated_difficulty, response_time, average_score)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_questions)
    conn.commit()

    print("Database created and sample questions added.")
    conn.close()

# Step 3: Request ChatGPT API to get difficulty level for a question
def get_chatgpt_difficulty(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # You can choose a model here
        prompt=f"Determine the difficulty level of the following question: {question}",
        max_tokens=10,
        temperature=0.5
    )
    difficulty = response.choices[0].text.strip()  # Get the response and clean it up
    return difficulty

# Step 4: Insert the ChatGPT difficulty into the database
def insert_chatgpt_difficulty():
    conn = sqlite3.connect('question_difficulty.db')
    c = conn.cursor()

    # Get all questions that do not have ChatGPT difficulty assigned
    c.execute("SELECT id, question_text FROM questions WHERE chatgpt_difficulty IS NULL")
    questions = c.fetchall()

    for question in questions:
        question_id, question_text = question
        # Get ChatGPT-generated difficulty for each question
        chatgpt_difficulty = get_chatgpt_difficulty(question_text)

        # Update the database with ChatGPT difficulty
        c.execute('''
            UPDATE questions
            SET chatgpt_difficulty = ?
            WHERE id = ?
        ''', (chatgpt_difficulty, question_id))
        conn.commit()

    print("ChatGPT difficulties added to the database.")
    conn.close()

# Step 5: Generate Sample JSON if needed
def generate_sample_json():
    sample_questions = [
        {"id": 1, "question_text": "What is 2 + 2?", "manual_difficulty": "Easy", "calculated_difficulty": None, "response_time": random.uniform(1, 5), "average_score": random.uniform(90, 100)},
        {"id": 2, "question_text": "What is the derivative of x^2?", "manual_difficulty": "Medium", "calculated_difficulty": None, "response_time": random.uniform(5, 10), "average_score": random.uniform(70, 85)},
        {"id": 3, "question_text": "What is the integral of sin(x)?", "manual_difficulty": "Hard", "calculated_difficulty": None, "response_time": random.uniform(10, 15), "average_score": random.uniform(50, 70)},
    ]

    # Convert to JSON format
    json_data = json.dumps(sample_questions, indent=4)
    print("Sample JSON Data:")
    print(json_data)

# Choose whether to create DB or use JSON
use_db = True  # Change this to False to use JSON data instead of DB

if use_db:
    create_db()          # Create DB and insert sample data
    insert_chatgpt_difficulty()  # Assign ChatGPT difficulty
else:
    generate_sample_json()

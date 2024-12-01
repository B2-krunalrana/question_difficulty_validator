# AI-Powered Question Difficulty Validator  

## Description  
This script leverages Python, SQL, and AI to automatically validate and assign difficulty levels to questions. It integrates manual inputs, student performance data, and AI predictions to ensure a more precise and dynamic difficulty assessment.

## Features  
- Manual assignment of difficulty levels.  
- Difficulty calculation based on student performance metrics, such as average scores, response time, etc.  
- AI models validate and refine difficulty levels to ensure they are aligned with student comprehension and performance.

## Tech Stack  
- **Python**: For scripting, AI model development, and integration.  
- **SQL**: For managing the database and running queries.  
- **scikit-learn**: For machine learning algorithms to support AI validation.  
- **ChatGPT**: To generate the database initially.  

## How It Works  
1. **Step One - Database Creation with ChatGPT**: We first utilize ChatGPT to automatically create the database by generating data structures based on predefined criteria.
2. **Manual Input**: Difficulty levels are manually assigned by educators for initial data entry.
3. **Performance-Based Calculation**: The system calculates difficulty levels by analyzing student performance data such as scores and response times.
4. **AI Validation**: AI models assess the features of each question and validate or adjust difficulty levels based on patterns in the data.
5. **Step Two - Model Fine-Tuning**: Once the database is generated, the model is fine-tuned by training it with existing student data to improve accuracy.
6. **Continual Model Training**: As more data accumulates, the model is continually retrained and fine-tuned to adapt to new patterns, ensuring the difficulty level remains accurate over time.

## Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/B2-krunalrana/question_difficulty_validator/

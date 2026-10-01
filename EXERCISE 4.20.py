

# Exercise 4.20 - Ask different questions about a different context
# Install the dependency with: pip install transformers
from transformers import pipeline

question_answerer = pipeline('question-answering')
result = question_answerer({
    'question': 'Where is the Aurora Research Center?',
    'context': 'The Aurora Research Center opened in Bandung in 2018. Its team studies renewable energy and operates a solar laboratory.',
})
print(result)

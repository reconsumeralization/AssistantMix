# config.py

# AI Model Configuration
AI_MODEL_NAME = 'Mixtral-8x7B'
AI_MODEL_TOOLS = 128

# Thread Configuration
THREAD_CONTEXT_WINDOW = 2048

# Run Configuration
RUN_STATUS_CHECK_INTERVAL = 60  # in seconds

# Authorization Configuration
AUTHORIZATION_METHOD = 'API_KEY'

# Open Interpreter Configuration
OPEN_INTERPRETER_SANDBOXED = True

# Knowledge Retrieval Configuration
KNOWLEDGE_RETRIEVAL_INDEXING = True

# Function Calling Configuration
FUNCTION_CALLING_ENABLED = True

# Code Refactoring Platform Configuration
CODE_REFACTORING_PLATFORM_INTEGRATED = True

# UI Configuration
UI_ENABLED = True

# Feedback Configuration
FEEDBACK_ENABLED = True  # Set to False to disable the feedback mechanism

# Error Handling Configuration
ERROR_HANDLING_METHOD = 'LOGGING'

# Logging Configuration
LOGGING_ENABLED = True
LOGGING_LEVEL = 'INFO'  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Database Configuration (if applicable)
# DATABASE_URI = 'postgresql://user:password@localhost/mydatabase'

# API Keys (if applicable)
# API_KEY = 'your-api-key-here'
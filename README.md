# Hermes - AI Translation Backend

A Flask backend that provides intelligent translation services using Ollama's local LLM models. Hermes accepts text input with style and tone preferences, dynamically builds prompts, and returns high-quality translations.

## Features

- **Dynamic Prompt Building**: Customizable translation prompts based on user preferences
- **Style & Tone Control**: Preserve original tone, apply specific styles, or make translations poetic
- **Local AI Processing**: Uses Ollama's llama3:8b model running locally
- **RESTful API**: Simple JSON-based API endpoint
- **Flexible Model Support**: Configurable model selection

## Project Structure

```
Hermes/
│
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── routes.py               # API endpoints
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── prompt_builder.py   # Dynamic prompt construction
│   │   └── ollama_handler.py   # Ollama API integration
│
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Configuration
└── README.md                   # This file
```

## Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **llama3:8b model** pulled in Ollama

### Install Ollama

```bash
# Install Ollama (visit https://ollama.ai for platform-specific instructions)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the llama3:8b model
ollama pull llama3:8b

# Start Ollama service
ollama serve
```

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Hermes
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server

```bash
python run.py
```

The server will start on `http://localhost:5000`

### API Endpoint

**POST** `/api/translate`

#### Request Body

```json
{
  "text": "Hello, how are you today?",
  "target_lang": "Spanish",
  "style": "formal",
  "tone_preserve": true,
  "poetic": false,
  "model": "llama3:8b"
}
```

#### Parameters

- `text` (required): The text to translate
- `target_lang` (required): Target language for translation
- `style` (optional): Translation style (e.g., "formal", "casual", "business")
- `tone_preserve` (optional): Whether to preserve the original tone (default: false)
- `poetic` (optional): Make the translation poetic/lyrical (default: false)
- `model` (optional): Ollama model to use (default: "llama3:8b")

#### Response

```json
{
  "output": "Hola, ¿cómo está usted hoy?"
}
```

### Example Requests

#### Basic Translation

```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Good morning!",
    "target_lang": "French"
  }'
```

#### Formal Style with Tone Preservation

```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hey buddy, what is up?",
    "target_lang": "German",
    "style": "formal",
    "tone_preserve": true
  }'
```

#### Poetic Translation

```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The sun rises in the east",
    "target_lang": "Italian",
    "poetic": true
  }'
```

## Configuration

Edit `.env` file to customize default settings:

```env
DEFAULT_MODEL=llama3:8b
OLLAMA_BASE_URL=http://localhost:11434
```

## Error Handling

The API handles common errors gracefully:

- **Ollama connection issues**: Returns error message with details
- **Invalid JSON**: Flask handles with 400 Bad Request
- **Missing required fields**: Returns appropriate error response

## Development

### Running in Debug Mode

The application runs in debug mode by default when using `python run.py`. This enables:

- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

### Adding New Features

1. **New prompt styles**: Modify `app/llm/prompt_builder.py`
2. **Additional endpoints**: Add to `app/routes.py`
3. **Different LLM providers**: Create new handlers in `app/llm/`

## Troubleshooting

### Common Issues

1. **"Error contacting Ollama"**:
   - Ensure Ollama is running: `ollama serve`
   - Check if model is available: `ollama list`
   - Verify Ollama is on port 11434

2. **"No response from model"**:
   - Check if the specified model exists
   - Try pulling the model: `ollama pull llama3:8b`

3. **Import errors**:
   - Ensure virtual environment is activated
   - Install requirements: `pip install -r requirements.txt`

## Running and Testing

### Starting the Application

To start the Hermes translation service:

```bash
python run.py
```

The server will start on `http://localhost:5000` in debug mode, which enables auto-reload on code changes.

### Testing with cURL (Linux/macOS)

Once the server is running, you can test the translation endpoint with cURL:

```bash
# Basic translation
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you today?",
    "target_lang": "Spanish"
  }'

# Translation with style and tone preservation
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Welcome to our store!",
    "target_lang": "French",
    "style": "formal",
    "tone_preserve": true
  }'
```

### Testing with PowerShell (Windows)

On Windows, you can use PowerShell's Invoke-WebRequest cmdlet:

```powershell
# Basic translation
Invoke-WebRequest -Uri http://localhost:5000/api/translate -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"text": "Hello, how are you today?", "target_lang": "Spanish"}'

# Translation with style and tone preservation
Invoke-WebRequest -Uri http://localhost:5000/api/translate -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"text": "Welcome to our store!", "target_lang": "French", "style": "formal", "tone_preserve": true}'
```

### Testing with Python Script

You can also create a Python script to test the API:

```python
import requests
import json

payload = {
    "text": "Hello, how are you today?",
    "target_lang": "Spanish",
    "style": "formal",
    "tone_preserve": True,
    "poetic": False,
    "model": "llama3:8b"
}

response = requests.post(
    "http://127.0.0.1:5000/api/translate",
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
```

Save this as `test_translation.py` and run with `python test_translation.py`.

## Web Interface

Hermes also includes a user-friendly web interface for easy translation without needing to format JSON requests.

### Accessing the Web Interface

Once the server is running, visit `http://localhost:5000` in your web browser to access the translation interface.

### Using the Web Interface

The web interface provides a simple form where you can:

1. Enter text to translate in the text area
2. Specify the target language
3. Optionally select a translation style (formal, casual, business)
4. Choose to preserve the original tone
5. Choose to make the translation poetic
6. Select the AI model to use

Simply fill out the form and click "Translate" to get your translation.

### Web Interface Features

- Clean, responsive design that works on desktop and mobile
- Real-time display of translation results
- Form persistence (your previous inputs are remembered)
- Error handling for empty inputs

## License

This project is open source. Feel free to modify and distribute.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
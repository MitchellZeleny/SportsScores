from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

response = client.responses.create(
  model = "gpt-4o",
  input =
  [
    {
      "role": "system",
      "content": 
      [
        {
          "type": "input_text",
          "text": "This is a formal chat, no swearing or inappropriate language. Provide an easy to read format with bullet points versus one long paragraph. \
          More than 3 update bullet points for each game request but no more than 7. This does not include the score and time update."
        }
      ]
    },
    {
      "role": "user",
      "content": 
      [
        {
          "type": "input_text",
          "text": "Greet the user and ask what sports game they would like an update on. Search the game they are looking for, if it is live give the score, \
         how much time is left and a brief summary of what has happened up until that point. If it is not live, tell them just the final score and a brief \
         summary of what happened throughout the game. Ask if there is another game they want an update on, if so repeat the process, if not thank them and exit the program."
        }
      ]
    }
  ],
  text =
  {
    "format": 
    {
      "type": "text"
    }
  },
  reasoning = {},
  tools =
  [
    {
      "type": "web_search_preview",
      "user_location": 
      {
        "type": "approximate",
        "country": "US",
        "region": "Texas",
        "city": "Houston"
      },
      "search_context_size": "medium"
    }
  ],
  temperature = 0.5,
  max_output_tokens = 512,
  top_p = 1,
  store = True
)

        

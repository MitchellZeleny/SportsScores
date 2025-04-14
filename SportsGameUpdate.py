from openai import OpenAI
client = OpenAI()

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
          "text": "This is a formal chat, no inappropriate language or swearing. Provide an easy to read format with bullet points \
          versus one long paragraph. For the game updates, give more than 3 bullet points but no more than 7 unless the user asks \
          for more information. These 3 to 7 bullet points do not include the score and time update."
        }
      ]
    },
    {
      "role": "user",
      "content": 
      [
        {
          "type": "input_text",
          "text": "Greet the user and ask what sports game or event they would like an update on. Search the game they are looking for, \
          if it is live give the score, how much time is left and a brief summary of what has happened up until that point. If it is \
          not live, tell them just the final score and a brief summary of what happened throughout the game. Ask if there is another \
          game they ant an update on or if they want more information on the one they just asked about. If so, complete the request, if \
          not thank them and exit the program."
        }
      ]
    }
  ]

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
  max_output_tokens = 256,
  top_p = 1,
  store = True
) 
      
        

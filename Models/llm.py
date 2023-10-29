import os 
from dotenv import load_dotenv
load_dotenv()

# Openai related libraries
import openai
openai.api_key = os.getenv("openai_key")

# Pandas imports
import pandas as pd


# Import sentiment model 
import Models.sentiment_analysis

openai.api_key = os.getenv("openai_key")

# Paths to folders and files
cwd = os.getcwd()
responses_folder = f"{cwd}\\Responses"

predefined_chats = {
    "earningsReport": "You are looking at earnings reports and trying to determine the positives and negatives that you \
    see. Highlight any risks with the company, management, or any other noteworthy pieces of information. You will be given \
    various pieces of information in chunks. Summarize the text to the best of your ability. Also list 10 bullet points of positives \
    and negatives."
}

system_roles = {
    "earningsReportLarge": "I will give text of a earnings report from a company. It will be given in pieces, so try to keep all \
of the information in mind for the following directions. I want you to analyze the company's financial situation. The actions of their management, \
and at the end I want you to list 10 bullet points for positive things you found, and 10 bullet points for negative things."
}


llm_info = {
    "gpt-3.5-turbo": {
        "maxTokens": 4097,
        "inputPrice": 0.0015, # $ per 1k tokens. 
        "outputPrice": 0.002
    }
}

class LargeLanguageModel:
    def __init__(self):
        self.sentiment_model = Models.sentiment_analysis.SentimentModel()
        self.llm_model = "gpt-3.5-turbo"
        
        # Set the max tokens that the model can handle. 
        self.max_tokens = llm_info[self.llm_model]["maxTokens"]

    '''-----------------------------------'''
    def query_chat(self, query: str, file_name: str):
        """
        :param query: The question to ask to the large language model. 
        """
        print("===== Query Check =====")
        
        
        
        # Query GPT 
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": predefined_chats["earningsReport"]},
                {"role": "user", "content": query}
                ]
        )
        
        sentiment_scores = []
        for i in completion.choices:
            sent_score = self.sentiment_model.analyze_text(i.message.content)
            message_content = f'"{i.message.content}"'
            message = {
                "content": message_content,
                "posScore": sent_score["pos"],
                "neuScore": sent_score["neu"],
                "negScore": sent_score["neg"]
            }    
            sentiment_scores.append(message)

        csv_file_path = f"{responses_folder}\\{file_name}.csv"
        df = pd.DataFrame(sentiment_scores)
        
        df.to_csv(csv_file_path, index=False)
        
        return df
        
    '''-----------------------------------'''
    def query_chat_LARGE(self, query: str, file_name: str):
        """
        :param query: The question to ask to the large language model. 
        """
        
        # Split the large text into smaller chuncks. 
        chunks = [query[i:i + self.max_tokens] for i in range(0, len(query), self.max_tokens)]
        
        # Conversation logic. 
        chunk_index = 0
        output = []
        for chunk in chunks:
            conversation = []
            # Create a system message with the predefined role. 
            system_message = {
                "role": "system",
                "content": system_roles["earningsReportLarge"]
            }
            # Append the system message the sets up the role of the model. 
            conversation.append(system_message)
            
            # Create a user message with the "chunk" of the text to send to the model. 
            user_message = {
                "role": "user",
                "content": chunk
            }
            # Add the user message. 
            conversation.append(user_message)
            
            # Request a completion from the model. 
            response = openai.ChatCompletion.create(model=self.llm_model, messages=conversation)
            # Extract the response
            output_text = response["choices"][0]["message"]["content"]
            
            output.append(output_text)    
            
        
        print(f"Output: {output}")
    '''-----------------------------------'''
    def split_text(self, text: str) -> list:
        """
        :param text: The string of text to split. 
        :returns: A list containing separate sections of the text. Each sections size is determined by "max_section_size". 
        """ 
        text_sections = []
        for i in range(0, len(text), self.max_tokens):
                            section = text[i:i+self.max_tokens]
                            text_sections.append(section)
        
        return text_sections
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def match_chat_type(self, chats: dict) -> str:
        """_summary_

        Args:
            chats (dict): Dictionary containing chat prompts and their associated descriptions as the key. 

        Returns:
            str: _description_
        """
         
    '''-----------------------------------'''
    
    

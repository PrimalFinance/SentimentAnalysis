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

print(f"responses: {responses_folder}")


class LargeLanguageModel:
    def __init__(self):
        self.sentiment_model = Models.sentiment_analysis.SentimentModel()
        self.llm_model = "gpt-3.5-turbo"
        
        # Because 3.5 has a max token per query of 4097 tokens. 
        if self.llm_model == "gpt-3.5-turbo":
            self.max_section_size = 4097
        pass

    '''-----------------------------------'''
    def query_chat(self, query: str, file_name: str):
        """
        :param query: The question to ask to the large language model. """
        print("===== Query Check =====")
        
        predefined_chats = {
            "earningsReport": "You are looking at earnings reports and trying to determine the positives and negatives that you \
            see. Highlight any risks with the company, management, or any other noteworthy pieces of information. You will be given \
            various pieces of information in chunks. Summarize the text to the best of your ability. Also list 10 bullet points of positives \
            and negatives."
        }
        
        
        # Split the query so the model can handle it. 
        query = self.split_text(query)
        
        messages=[
                {"role": "system", "content": predefined_chats["earningsReport"]},
                ]
        
        
        for chunk in query:
            messages.append({"role": "user", "content": chunk})
        
        # Query GPT 
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        for i in completion.choices:
            sent_score = self.sentiment_model.analyze_text(i.message.content)
            message_content = f'"{i.message.content}"'
            message = {
                "content": message_content,
                "posScore": sent_score["pos"],
                "neuScore": sent_score["neu"],
                "negScore": sent_score["neg"]
            }    
            messages.append(message)

        csv_file_path = f"{responses_folder}\\{file_name}.csv"
        df = pd.DataFrame(messages)
        
        df.to_csv(csv_file_path, index=False)
        
        return df
        
    '''-----------------------------------'''
    '''-----------------------------------'''
    def split_text(self, text: str) -> list:
        """
        :param text: The string of text to split. 
        :returns: A list containing separate sections of the text. Each sections size is determined by "max_section_size". 
        """ 
        text_sections = []
        for i in range(0, len(text), self.max_section_size):
                            section = text[i:i+self.max_section_size]
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
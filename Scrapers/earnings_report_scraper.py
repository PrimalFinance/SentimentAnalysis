

import requests
import PyPDF2
import io

# Import models 
import Models.llm


reports = {
    "intel": "https://d1io3yog0oux5.cloudfront.net/_79642fa26e83f0c0f4febbe78ad52b21/intel/db/887/8973/earnings_release/Q3+23+EarningsRelease.pdf"
}




class EarningsReportsScraper:
    def __init__(self):
        self.llm = Models.llm.LargeLanguageModel()
        
        
        self.earnings_sources = {
            "INTC": {
                "investorRelations": "https://www.intc.com/",
                "recentReport": "https://d1io3yog0oux5.cloudfront.net/_79642fa26e83f0c0f4febbe78ad52b21/intel/db/887/8973/earnings_release/Q3+23+EarningsRelease.pdf"
            }
        }
        
        
    '''-------------------------------'''
    def get_report_text(self, url: str) -> str:
        """
        :param url: URL to the earnings report. 
        
        :returns: String of the text within the report. 
        
        Description: Will read a pdf file and return the text within it. 
        """
        # Send a GET request to the URL
        response = requests.get(url)

        # Create a PDF reader object from the response content
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(response.content))

        # Extract text from each page of the PDF
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
        
        return pdf_text
    '''-------------------------------'''
    def analyze_report(self):
        url = reports["intel"]
        
        # Send a GET request to the URL
        response = requests.get(url)

        # Create a PDF reader object from the response content
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(response.content))

        # Extract text from each page of the PDF
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

        # Now you can work with the extracted text from the PDF
        print(pdf_text)
        query_text = self.llm.split_text(text=pdf_text)
        self.llm.query_chat(query=pdf_text, file_name="INTC_Q323_Report_Responses.csv")
        
        
        
        
    '''-------------------------------'''
    def get_IR_url(self, ticker: str):
        """
        :param ticker: Ticker of the company to search. 
        
        :returns: Url for the investor relations website.
        
        Description: Get the investor relations website for the company. 
        """
        return self.earnings_sources[ticker]["investorRelations"]
    
    '''-------------------------------'''
    def get_recent_report(self, ticker: str) -> str:
        """
        :param ticker: Ticker of the company to search. 
        
        :returns: Url for the most recent filing.
        
        Description: Get the most recent filing for the company. 
        """
        return self.earnings_sources[ticker]["recentReport"]
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    
    
if __name__ == "__main__":
    er = EarningsReportsScraper()
    
    er.get_report()
    
    
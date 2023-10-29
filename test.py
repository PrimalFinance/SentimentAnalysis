import os 


import Database.data_base_manager

import pandas as pd

from Models.llm import LargeLanguageModel


def test1():
   
   ticker = "AAPL"
   db = Database.data_base_manager.DatabaseManager()
   
   db.connect_to_database(ticker=ticker)
   
   print(f"{db.get_file_connection()}")


if __name__ == "__main__":
    
    llm = LargeLanguageModel()
    
    
    query = """Results of Operations
We have organized our operations into three segments: North America, International, and AWS. These segments reflect the way the Company evaluates its business performance and manages its operations. See Item 1 of Part I, “Financial Statements — Note 8 — Segment Information.”
Overview
Macroeconomic factors, including inflation, increased interest rates, significant capital market and supply chain volatility, and global economic and geopolitical developments, have direct and indirect impacts on our results of operations that are difficult to isolate and quantify. In addition, changes in fuel, utility, and food costs, rising interest rates, and recessionary fears may impact customer demand and our ability to forecast consumer spending patterns. We also expect the current macroeconomic environment and enterprise customer cost optimization efforts to impact our AWS revenue growth rates. We expect some or all of these factors to continue to impact our operations into Q4 2023.
Net Sales
Net sales include product and service sales. Product sales represent revenue from the sale of products and related shipping fees and digital media content where we record revenue gross. Service sales primarily represent third-party seller fees, which includes commissions and any related fulfillment and shipping fees, AWS sales, advertising services, Amazon Prime membership fees, and certain digital media content subscriptions. Net sales information is as follows (in millions):
Sales increased 13% in Q3 2023, and 11% for the nine months ended September 30, 2023 compared to the comparable prior year periods. Changes in foreign exchange rates increased net sales by $1.4 billion for Q3 2023, and reduced net sales by $1.3 billion for the nine months ended September 30, 2023. For a discussion of the effect of foreign exchange rates on sales growth, see “Effect of Foreign Exchange Rates” below.
North America sales increased 11% in Q3 2023, and 11% for the nine months ended September 30, 2023 compared to the comparable prior year periods. The sales growth primarily reflects increased unit sales, primarily by third-party sellers, advertising sales, and subscription services. Increased unit sales were driven largely by our continued focus on price, selection, and convenience for our customers, including from our shipping offers.
24
Table of Contents
International sales increased 16% in Q3 2023, and 9% for the nine months ended September 30, 2023 compared to the comparable prior year periods, primarily due to increased unit sales, primarily by third-party sellers, advertising sales, and subscription services. Increased unit sales were driven largely by our continued focus on price, selection, and convenience for our customers, including from our shipping offers. Changes in foreign exchange rates increased International net sales by $1.4 billion for Q3 2023, and reduced International net sales by $1.1 billion for the nine months ended September 30, 2023.
AWS sales increased 12% in Q3 2023, and 13% for the nine months ended September 30, 2023 compared to the comparable prior year periods. The sales growth primarily reflects increased customer usage, partially offset by pricing changes, primarily driven by long-term customer contracts.
Operating income increased from $2.5 billion in Q3 2022 to $11.2 billion in Q3 2023, and increased from $9.5 billion for the nine months ended September 30, 2022 to $23.6 billion for the nine months ended September 30, 2023. We believe that operating income is a more meaningful measure than gross profit and gross margin due to the diversity of our product categories and services.
The North America operating income in Q3 2023, as compared to the operating loss in the comparable prior year period, is primarily due to increased unit sales and increased advertising sales, partially offset by increased shipping and fulfillment costs. The North America operating income for the nine months ended September 30, 2023, as compared to the operating loss in the comparable prior year period, is primarily due to increased unit sales and increased advertising sales, partially offset by increased shipping and fulfillment costs, increased technology and infrastructure costs, and growth in certain operating expenses. Changes in foreign exchange rates negatively impacted operating income by $27 million for Q3 2023, and positively impacted operating income by $7 million for the nine months ended September 30, 2023.
The decrease in International operating loss in absolute dollars in Q3 2023, compared to the comparable prior year period, is primarily due to increased unit sales and increased advertising sales. The decrease in International operating loss in absolute dollars for the nine months ended September 30, 2023, compared to the comparable prior year period, is primarily due to increased unit sales and increased advertising sales, partially offset by increased fulfillment and shipping costs, increased technology and infrastructure costs, and growth in certain operating expenses. Changes in foreign exchange rates positively impacted operating loss by $228 million for Q3 2023, and by $86 million for the nine months ended September 30, 2023.
The increase in AWS operating income in absolute dollars in Q3 2023, compared to the comparable prior year period, is primarily due to increased sales and cost structure productivity, partially offset by spending on technology infrastructure, which was primarily driven by additional investments to support AWS business growth. The decrease in AWS operating income in absolute dollars for the nine months ended September 30, 2023, compared to the comparable prior year period, is primarily due to increased payroll and related expenses and spending on technology infrastructure, both of which were primarily driven by additional investments to support AWS business growth, partially offset by increased sales. Changes in foreign exchange rates negatively impacted operating income by $69 million for Q3 2023, and positively impacted operating income by $282 million for the nine months ended September 30, 2023.
We seek to invest efficiently in numerous areas of technology and infrastructure so we may continue to enhance the customer experience and improve our process efficiency through rapid technology developments, while operating at an ever increasing scale. Our technology and infrastructure investment and capital spending projects often support a variety of product and service offerings due to geographic expansion and the cross-functionality of our systems and operations. We expect spending in technology and infrastructure to increase over time as we continue to add employees and infrastructure. These costs are allocated to segments based on usage. The increase in technology and infrastructure costs in absolute dollars in Q3 2023, compared to the comparable prior year period, is primarily due to an increase in spending on infrastructure. The increase in technology and infrastructure costs in absolute dollars for the nine months ended September 30, 2023, compared to the comparable prior year period, is primarily due to increased payroll and related costs associated with technical teams responsible for expanding our existing products and services and initiatives to introduce new products and service offerings, and an increase in spending on infrastructure. Changes in foreign exchange rates increased technology and infrastructure costs by $87 million for Q3 2023, and reduced technology and infrastructure costs by $312 million for the nine months ended September 30, 2023. See Item 7 of Part II, “Management’s Discussion and Analysis of Financial Condition and Results of Operations — Overview” of our 2022 Annual Report on Form 10-K for a discussion of how management views advances in technology and the importance of innovation.
"""
    
    llm.query_chat(query=query, file_name="AMZN_Q323")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
response = f"""
Intel has made organizational changes to integrate its Accelerated Computing Systems and Graphics Group
into its Client Computing Group and Data Center and AI Group. This is expected to drive a more effective
go-to-market capability and reduce costs. The company has modified its segment reporting to align with 
these changes. In terms of business unit revenue and trends in Q3 2023, the Client Computing Group saw a 3% decrease,
the Data Center and AI group decreased by 10%, the Network and Edge group decreased by 32%, and Mobileye increased by 18%
while, Intel Foundry Services saw an increase of 299%.

Positive bullet points:
1. Intel is on track to achieve its goal of five nodes in four years and to regain transistor performance and power performance leadership by 2025.
2. Intel 7, the company's first node using extreme ultraviolet (EUV) technology, is now in high-volume manufacturing.
3. Intel achieved a critical milestone on Intel 18A with the release of the 0.9 PDK.
4. Intel announced the industry's first glass substrates for next-generation advanced packaging, which will enable the scaling of transistors in a package and advance Moore's Law.
5. Intel is investing in manufacturing capacity to create a geographically balanced and secure supply chain, including the opening of Fab 34 in Ireland and planned facilities in Germany and Poland.
6. Intel is expanding and modernizing the Gordon Moore Park in Oregon.
7. Intel has submitted major manufacturing proposals to the U.S. Department of Commerce, representing over $100 billion of investments.
8. Intel has secured a major customer commitment for its advanced chip factories in Arizona.
9. Intel is collaborating with Tower Semiconductor to provide foundry services and manufacturing capacity.
10. Intel is focused on bringing AI capabilities across its hardware products and making it accessible through open multi-architecture software solutions.

Negative bullet points:
1. The Client Computing Group, Data Center and AI group, and Network and Edge group all experienced revenue decreases.
2. The Network and Edge group saw a significant decrease of 32%.
3. Client Computing Group revenue decreased by 3%.
4. Data Center and AI group revenue decreased by 10%.
5. Mobileye's revenue increase of 18% may not be enough to offset the revenue decreases in other business units.
6. The overall performance and trends suggest challenges in certain segments.
7. The future success of Intel's manufacturing proposals and investments is uncertain.
8. The company may face increased competition in the AI and semiconductor market.
9. The impact of the organizational changes on the company's performance and efficiency is yet to be fully demonstrated.
10. The company may need to focus on strategies to improve revenue and regain market share in certain segments.


-------------------
Positive: 0.44
Neutral: 0.42
Negative: 0.12
-------------------


"""





















amzn_response = f"""
- Macroeconomic factors and geopolitical developments have direct and indirect impacts on the company's operations
- Changes in fuel, utility, and food costs, as well as rising interest rates, may impact customer demand and the company's ability to forecast consumer spending patterns
- The current macroeconomic environment and enterprise customer cost optimization efforts are expected to impact AWS revenue growth rates
- Net sales increased by 13% in Q3 2023 compared to the previous year, driven by increased unit sales, advertising sales, and subscription services
- North America sales increased by 11% in Q3 2023, primarily due to increased unit sales and advertising sales
- International sales increased by 16% in Q3 2023, primarily due to increased unit sales and advertising sales
- AWS sales increased by 12% in Q3 2023, primarily reflecting increased customer usage
- Operating income increased significantly from Q3 2022 to Q3 2023, reflecting increased unit sales, advertising sales, and cost structure productivity
- Increased unit sales and increased advertising sales contributed to the decrease in International operating loss in Q3 2023 compared to the previous year
- Increased sales and cost structure productivity contributed to the increase in AWS operating income in Q3 2023
- The company plans to invest in technology and infrastructure to enhance customer experience and improve process efficiency, which will lead to increased spending in these areas over time

Positives:
1. Overall increase in net sales and operating income.
2. Growth in North America, International, and AWS segments.
3. Increased unit sales and advertising sales driving sales growth.
4. Focus on price, selection, and convenience for customers.
5. Positive impact of changes in foreign exchange rates on net sales and operating income.
6. Increased customer usage in AWS segment.
7. Investment in technology and infrastructure to enhance customer experience.
8. Cost structure productivity leading to increased operating income.
9. Focus on innovation and technological advancements.
10. Continued investment in expanding product and service offerings.

Negatives:
1. Macroeconomic factors and geopolitical developments impacting operations.
2. Uncertainty in forecasting consumer spending patterns.
3. Impact of fuel, utility, and food costs on customer demand.
4. Impact of rising interest rates on customer demand.
5. Enterprise customer cost optimization efforts impacting AWS revenue growth.
6. Increase in shipping and fulfillment costs in North America segment.
7. Increase in technology and infrastructure costs.
8. Negative impact of changes in foreign exchange rates on operating income.
9. Significant spending on technology infrastructure.
10. Increased payroll and related expenses.

Positive: 0.29
Neutral: 0.54
Negative: 0.16

"""












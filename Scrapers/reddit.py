# Environment variables.
import os
from dotenv import load_dotenv
load_dotenv()

# Praw imports
import praw as pr

# Import sentiment analysis model. 
from Models.sentiment_analysis import SentimentModel


# Get the praw settings 

client_id = os.getenv("praw_id")
client_secret = os.getenv("praw_secret")
client_password = os.getenv("praw_pass")





class RedditScraper:
    def __init__(self):

        self.reddit = pr.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="Hedera Tracker"
        )
        self.sm = SentimentModel()
    '''-----------------------------------'''
    def get_top_posts(self, subreddit_name: str, num_posts: int = 100, time_filter: str = "month", include_comments: bool = False):
        """
        :param subreddit_name: The subreddit to collect posts from. 
        :param num_posts: The number of posts to collect. 
        :param time_filter: Determines which timeframe to get data for. For example, if the time_filer = "month", then it will get the top 100 (or whatever num_posts is equal to) for the past month. 
        
        Description: This function will return the specified number of "top" posts from the subreddit. 
        """
        subreddit = self.reddit.subreddit(subreddit_name)

        # Get the top posts within the timeframe specified by "time_filter". 
        top_posts = subreddit.top(limit=num_posts, time_filter=time_filter)

        # List to hold our posts collected. 
        posts_collected = []

        max_section_size = 514

        # Iterate through each post. 
        for post in top_posts:
            
            post_data = {}

            # Get the post title. 
            post_title = post.title
            post_title_score = self.sm.analyze_text(post_title)
            # Get the post body text. 
            post_body = post.selftext
            # If the post pody is larger than our model can accept, split up the post body into sections. Score each individual section, then get the average score for the section by summing up all the scores and dividing by the number of sections.
            if len(post_body) > max_section_size: # 514 because that is our input dimensions size for our NLP.  
                split_sections_scores = []
                for i in range(0, len(post_body), max_section_size):
                    section = post_body[i:i+max_section_size]
                    section_score = self.sm.analyze_text(section)
                    split_sections_scores.append(section_score)

                sum_pos = 0
                sum_neu = 0
                sum_neg = 0
                # Get the sum of each score from all the sections. 
                for s in split_sections_scores:
                    sum_pos += s["pos"]
                    sum_neu += s["neu"]
                    sum_neg += s["neg"]
                    
                # Divide sums by lenth of list to get the average. 
                avg_pos = sum_pos / len(split_sections_scores)
                avg_neu = sum_neu / len(split_sections_scores)
                avg_neg = sum_neg / len(split_sections_scores)
                avg_section_score = {
                    "neg": avg_neg,
                    "neu": avg_neu,
                    "pos": avg_pos
                }
                post_body_score = avg_section_score
            else:
                post_body_score = self.sm.analyze_text(post_body)
            # Get the post url 
            post_url = post.url


            if include_comments:
                comments_collected = []
                comment_scores = []
                comments_pos_sum = 0
                comments_neu_sum = 0
                comments_neg_sum = 0
                # Retrieve the comments from the post. 
                for comment in post.comments.list():
                    # Check if the comment is not a MoreComments object
                    if not isinstance(comment, pr.models.MoreComments):
                        if len(comment.body) > max_section_size:
                            comment_score = self.sm.analyze_text(comment.body)
                            comment_scores.append(comment_score)
                            comments_collected.append(comment.body)



                        else:

                            comment_score = self.sm.analyze_text(comment.body)
                            comment_scores.append(comment_score)
                            comments_collected.append(comment.body)

                for score in comment_scores:
                    comments_pos_sum += score["pos"]
                    comments_neu_sum += score["neu"]
                    comments_neg_sum += score["neg"]

                avg_comment_pos_sum = comments_pos_sum / len(comment_scores)
                avg_comment_neu_sum = comments_neu_sum / len(comment_scores)
                avg_comment_neg_sum = comments_neg_sum / len(comment_scores)
                avg_comment_score = {
                    "neg": avg_comment_neg_sum,
                    "neu": avg_comment_neu_sum,
                    "pos": avg_comment_pos_sum
                }

            

            # Add data to post_data dictionary. 
            post_data["title"] = post_title
            post_data["title_score"] = post_title_score
            post_data["body"] = post_body
            post_data["body_score"] = post_body_score
            # Add comment data to dictionary if they are to be collected. 
            if include_comments:
                post_data["comments"] = comments_collected
                post_data["numOfComments"] = len(comments_collected)
                post_data["commentScores"] = avg_comment_score
            
            # Include the post url. 
            post_data["url"] = post_url

            posts_collected.append(post_data)
            print(f"----- Post Collected -----")

        for d in posts_collected:
            self.display_post_details(post_data=d, include_comments=include_comments)
    '''-----------------------------------'''
    def display_post_details(self, post_data: dict,  sentiment: bool = True, include_comments: bool = False) -> None:
        print(f"\n\n")
        if sentiment:
            if include_comments:
                print(f"""
================================
---------
[Title]
Title: "{post_data['title']}"
Title Score: 
{self.sm.display_score(post_data['title_score'])}

---------
[Body]
Body Score: 
{self.sm.display_score(post_data['body_score'])}

---------
[Comments]
Comment Scores: 
{self.sm.display_score(post_data['commentScores'])}""")
            else:
                print(f"""
================================
---------
[Title]
Title: "{post_data['title']}"
Title Score: 
{self.sm.display_score(post_data['title_score'])}

---------
[Body]
Body Score: 
{self.sm.display_score(post_data['body_score'])}
""")
        
        else:
            if include_comments:
                print(f"""
--------------------------------
Title: "{post_data['title']}"
Body: {post_data['body']}
Comments: {post_data['comments']}""")
            else:
                print(f"""
--------------------------------
Title: "{post_data['title']}"
Body: {post_data['body']}
""")

        print(f"\n[Url]: {post_data['url']}\n")

        


    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''

if __name__ == "__main__":

    r = RedditScraper()
    r.get_top_posts("Cryptocurrency", 5)
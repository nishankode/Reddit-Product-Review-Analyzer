import praw
from dotenv import load_dotenv
import os


def collect_threads(subreddit_name, search_keyword):

    load_dotenv()

    # Initialize PRAW with your credentials
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),  # Your client_id
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),  # Your client_secret
        user_agent=os.getenv('REDDIT_UDER_AGENT'),  # Your user_agent
    )


    # Initialize an empty string to store all the content
    all_content = ""

    # Search for posts with the keyword in the specified subreddit
    posts = reddit.subreddit(subreddit_name).search(search_keyword, limit=10)  # You can change the limit

    # Process the posts and append the content to the all_content variable
    for post in posts:
        all_content += f"Title: {post.title}\n"
        all_content += f"URL: {post.url}\n"
        all_content += f"Score: {post.score}\n"
        all_content += f"Created: {post.created_utc}\n"
        all_content += f"Author: {post.author}\n"
        all_content += f"Text: {post.selftext[:500]}...\n"  # Only the first 500 characters of the post
        all_content += "\n---\n"
        
        # Fetch comments for each post and append them to all_content
        post.comments.replace_more(limit=0)  # This removes 'More comments' objects for better processing
        for comment in post.comments.list():
            all_content += f"Comment by {comment.author}: {comment.body[:200]}...\n"  # First 200 characters of comment
        all_content += "\n===\n"

    # Now, all_content contains the entire text for the posts and comments
    return all_content

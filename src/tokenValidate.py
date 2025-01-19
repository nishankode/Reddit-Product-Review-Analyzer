import tiktoken  # Install this package for token counting

# Function to estimate the number of tokens in a text
def num_tokens_from_messages(messages):
    encoding = tiktoken.get_encoding("o200k_base")  # Use appropriate GPT model encoding
    tokens = 0
    for message in messages:
        tokens += len(encoding.encode(message['content']))
    return tokens

# Function to ensure the input doesn't exceed the token limit
def ensure_tokens_within_limit(all_content, token_limit=128000):

    prompt_template = """
    Based on the Reddit scraped content provided, please generate a comprehensive and insightful summary for a Brand Manager. The summary should include:

    1. **Sentiment Analysis**: Describe the overall sentiment expressed by users in the content—whether it's positive, negative, or neutral towards the brand/product. Mention key emotions expressed, if relevant (e.g., frustration, excitement, satisfaction, etc.).
    
    2. **Key Themes**: Identify and summarize the main topics or themes discussed across the posts (e.g., product features, customer service, pricing, competitors, etc.). Point out any emerging trends or shifts in opinion.

    3. **Common Issues**: Highlight any recurring complaints or negative feedback about the brand/product. Include the specific aspects of the product or service that users are dissatisfied with.

    4. **Suggestions and Recommendations**: Based on the comments, provide any constructive suggestions or recommendations for improvement. This could include ideas on product improvement, marketing strategies, or customer support enhancements.

    5. **Competitor Mentions**: Note any discussions or comparisons with competitor brands/products. How does your brand stand in relation to competitors based on user opinions?

    6. **Engagement Insights**: If applicable, mention any significant discussions, highly upvoted comments, or trending posts that could offer further insights into consumer behavior or opinions on the brand.

    Please provide the summary in a concise yet thorough manner, ensuring it's tailored for a Brand Manager to quickly understand the sentiment, key issues, and actionable insights for brand strategy improvement.

    """
    # Initialize the list of messages
    messages = [
        {"role": "system", "content": prompt_template},
        {"role": "user", "content": all_content}
    ]
    
    # Calculate the number of tokens for the current messages
    tokens_used = num_tokens_from_messages(messages)
    
    # If the tokens exceed the limit, trim the content
    while tokens_used > token_limit:
        print(f"Token limit exceeded! Trimming content...")
        # Trim the content to reduce token count (you can adjust this trimming logic)
        all_content = all_content[:int(len(all_content) * 0.9)]  # Reduce content size by 10%
        messages[1]['content'] = all_content
        
        tokens_used = num_tokens_from_messages(messages)
        print(f"Tokens used after trimming: {tokens_used}")
    
    return all_content, messages
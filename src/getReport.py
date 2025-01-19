from dotenv import load_dotenv
import os
import openai


def generate_report(all_content, messages):
    # Load environment variables from the .env file
    load_dotenv()

    # Get the OpenAI API key from environment variables
    openai.api_key = os.getenv('OPENAI_API_KEY')

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

    from openai import OpenAI

    # Initialize the OpenAI client with your API key
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt_template},
        {"role": "user", "content": all_content}
    ])

    return completion.choices[0].message.content
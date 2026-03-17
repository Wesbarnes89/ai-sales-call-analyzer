from openai import OpenAI

client = OpenAI()

def analyze_sales_call(transcript):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a sales coach. Analyze sales calls."},
            {"role": "user", "content": f"Analyze this sales call and give:\n- Summary\n- Key objections\n- Next steps\n\nTranscript:\n{transcript}"}
        ]
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    transcript = """
    Customer: I'm not sure this fits our budget.
    Rep: We can break it into phases to reduce cost.
    Customer: That might work, but I need to check with finance.
    """

    result = analyze_sales_call(transcript)
    print("\n=== AI Analysis ===\n")
    print(result)
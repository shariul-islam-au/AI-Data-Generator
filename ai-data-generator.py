from mcp.server.fastmcp import FastMCP
import os
import csv

# Create an MCP server
mcp = FastMCP("AI Dataset Generator")

bangla_sms_file = os.path.join(os.path.dirname(__file__), "bangla_sms.csv")
english_sms_file = os.path.join(os.path.dirname(__file__), "english_sms.csv")
banglish_sms_file = os.path.join(os.path.dirname(__file__), "banglish_sms.csv")
code_mix_sms_file = os.path.join(os.path.dirname(__file__), "code_mixed_sms.csv")

def ensure_files():
    if not os.path.exists(bangla_sms_file):
        with open(bangla_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(english_sms_file):
        with open(english_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(banglish_sms_file):
        with open(banglish_sms_file, "w") as f:
            f.write("")

    if not os.path.exists(code_mix_sms_file):
        with open(code_mix_sms_file, "w") as f:
            f.write("")

ensure_files()


def save_dataset(file_path, messages: str) -> str:    
    """
    Saves translated SMS data to a text file, ensuring uniqueness.
    """
    # Read existing messages
    existing_messages = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                existing_messages.add(line.strip())

    # Split new messages by line (in case multiple messages are provided)
    new_messages = [msg.strip() for msg in messages.split("\n") if msg.strip()]

    # Keep only unique messages
    unique_messages = [msg for msg in new_messages if msg not in existing_messages]

    # Append unique messages to the CSV file
    if unique_messages:
        with open(file_path, "a", encoding="utf-8") as f:
            for msg in unique_messages:
                f.write(msg + "\n")
        return f"{len(unique_messages)} new message(s) saved!"
    else:
        return "No new messages to save; all messages already exist."



@mcp.tool()
def generate_bangla_dataset(sample_count: int) -> str:
    prompt = f"""
You are a dataset generator. Your task is to create synthetic messages (SMS, email, or social media posts) in CSV format with exactly two columns: "label" and "text".

Labels:
1. smish → প্রতারণামূলক, ফিশিং, বা স্ক্যাম বার্তা (যেমন: ভুয়া ব্যাংক সতর্কতা, লটারির প্রতারণা, সন্দেহজনক লিঙ্ক, ভুয়া পুরস্কার দাবি)।
2. promo → প্রমোশনাল বা মার্কেটিং বার্তা (যেমন: টেলিকম অফার, প্রোডাক্ট ছাড়, বিক্রয়, ক্যাশব্যাক)।
3. normal → দৈনন্দিন ব্যক্তিগত বা স্বাভাবিক বার্তা (যেমন: শুভেচ্ছা, কথোপকথন, বন্ধুত্বপূর্ণ আড্ডা)।

Requirements:
- Output strictly in CSV format with no extra characters.
- Wrap the text in double quotes if it contains commas or special characters.
- Use Bangladeshi context: স্থানীয় ব্যাংক (যেমন: সোনালী ব্যাংক, ডাচ্-বাংলা ব্যাংক), টেলিকম কোম্পানি (যেমন: গ্রামীণফোন, রবি, বাংলালিংক), মুদ্রা (টাকা), সাধারণ নাম, স্থান।
- Ensure diversity in শব্দভাণ্ডার, বাক্য গঠন, ও টোন।
- Generate around {sample_count} samples, evenly distributed among the three labels.
- ভাষার স্টাইল ভিন্ন ভিন্ন হোক: ছোট, বড়, আনুষ্ঠানিক, অনানুষ্ঠানিক, মজার।
- Include realistic details: নাম, ফোন নম্বর, টাকা, URL, কোড, OTP।
- Word size should be between 20 to 70 words.
- Ensure smish messages sound urgent and malicious in Bengali.
- Ensure promo messages sound persuasive and attractive in Bengali.
- Ensure normal messages sound natural and conversational in Bengali.
- Avoid exact repetition of examples.

Example:
label,text
smish,"আপনার ডাচ্-বাংলা ব্যাংক অ্যাকাউন্ট ব্লক হয়েছে। এখনই কল করুন: +8801818788890"
promo,"আজকের বিশেষ অফার! ৩০জিবি মাত্র ৩০০ টাকা, ৩০ দিনের জন্য। এখনই কিনুন: cutt.ly/jwkuSC76"
normal,"কাল ক্লাসে যাচ্ছো তো? আমি সকাল ৯টায় চলে যাবো। তুমি ক’টায় যাবে?"

Generate the dataset **in Bengali**.

"""
    return prompt.strip()


@mcp.tool()
def save_bangla_dataset(messages: str) -> str:
    """
    Saves data to a text file, ensuring uniqueness.
    """
    save_dataset(bangla_sms_file, messages)


@mcp.tool()
def generate_english_dataset(sample_count: int) -> str:
    prompt = f"""
You are a dataset generator. Your task is to create synthetic messages (SMS, email, or social media posts) in CSV format with exactly two columns: "label" and "text".

Labels:
1. smish → Fraudulent, phishing, or scam messages (e.g., fake bank alerts, crypto scams, lottery, suspicious links).
2. promo → Promotional or marketing messages (e.g., telecom offers, product discounts, sales, cashback).
3. normal → Everyday personal or casual messages (e.g., greetings, daily conversation, friendly chat).

Requirements:
- Output **strictly in CSV format** with no extra characters.
- Wrap the text in double quotes if it contains commas or special characters.
- Use **Bangladeshi context**: local banks, telecom operators, currency (TK), common names, places.
- Ensure **diversity** in vocabulary, sentence structure, and tone.
- Avoid using the same phrases or sentences across different messages.  
- Generate around **{sample_count} samples**, evenly distributed among the three labels.
- Vary language style: short, long, formal, casual, humorous.
- Include **realistic details**: Bangladeshi names, phone numbers, taka amounts, URLs, random codes.
- Ensure **smish messages** sound urgent and malicious.
- Ensure **promo messages** sound persuasive and enticing.
- Ensure **normal messages** sound conversational and natural.
- Avoid exact repetition of examples.

Example:
label,text
smish,There is an issue with your Sonali Bank account. Call: +8801818788890
promo,"Special deal last day, 30GB @300TK, 30 days! Get it today- cutt.ly/jwkuSC76"
normal,"Have you read any books before? Yes, I've read many books. What about you?"

Generate the dataset **in English**.

"""
    return prompt.strip()


@mcp.tool()
def save_english_dataset(messages: str) -> str:
    """
    Saves data to a text file, ensuring uniqueness.
    """
    save_dataset(english_sms_file, messages)



@mcp.tool()
def generate_banglish_dataset(sample_count: int) -> str:
    prompt = f"""
You are a dataset generator. Your task is to create synthetic Banglish (Bangla written in English alphabet) messages (SMS, email, or social media posts) in CSV format with exactly two columns: "label" and "text".

Labels:
1. smish → Fraudulent, phishing, or scam messages (e.g., fake bank alerts, crypto scams, lottery, suspicious links).
2. promo → Promotional or marketing messages (e.g., telecom offers, product discounts, sales, cashback).
3. normal → Everyday personal or casual messages (e.g., greetings, daily conversation, friendly chat).

Requirements:
- Output **strictly in CSV format** with no extra characters.
- Wrap the text in double quotes if it contains commas or special characters.
- Use **Bangladeshi context**: local banks, telecom operators, currency (TK), common names, places.
- Ensure **diversity** in vocabulary, sentence structure, and tone.
- Avoid using the same phrases or sentences across different messages.  
- Generate around **{sample_count} samples**, evenly distributed among the three labels.
- Vary language style: short, long, formal, casual, humorous.
- Include **realistic details**: Bangladeshi names, phone numbers, taka amounts, URLs, random codes.
- Ensure **smish messages** sound urgent and malicious.
- Ensure **promo messages** sound persuasive and enticing.
- Ensure **normal messages** sound conversational and natural.
- Avoid exact repetition of examples.

Example:
label,text
smish,"Apnar DBBL account bondho hoye jabe, verify korte call korun +8801845678890"
promo,"GP offer cholche! 5GB internet sudhu 57TK, recharge korun akhoni. Details: gp.com.bd"
normal,"Ami valo asi, tumi kemon aso?"

Generate the dataset **in Banglish**.

"""
    return prompt.strip()


@mcp.tool()
def save_banglish_sms(messages: str) -> str:
    """
    Saves data to a text file, ensuring uniqueness.
    """
    save_dataset(banglish_sms_file, messages)



@mcp.tool()
def generate_code_mixed_dataset(sample_count: int) -> str:
    prompt = f"""
You are a dataset generator. Your task is to create synthetic Bangla-English code-mixed messages (SMS, email, or social media posts) in CSV format with exactly two columns: "label" and "text".

Labels:
1. smish → Fraudulent, phishing, or scam messages (e.g., fake bank alerts, crypto scams, lottery, suspicious links).
2. promo → Promotional or marketing messages (e.g., telecom offers, product discounts, sales, cashback).
3. normal → Everyday personal or casual messages (e.g., greetings, daily conversation, friendly chat).

Requirements:
- Output **strictly in CSV format** with no extra characters.
- Wrap the text in double quotes if it contains commas or special characters.
- Use **Bangladeshi context**: local banks, telecom operators, currency (TK), common names, places.
- Ensure **diversity** in vocabulary, sentence structure, and tone.
- Avoid using the same phrases or sentences across different messages. 
- Maintain approx. 50% text in Bangla (in Bangla script) and 50% text in English for each message.
- Generate around **{sample_count} samples**, evenly distributed among the three labels.
- Vary language style: short, long, formal, casual, humorous.
- Include **realistic details**: Bangladeshi names, phone numbers, taka amounts, URLs, random codes.
- Ensure **smish messages** sound urgent and malicious.
- Ensure **promo messages** sound persuasive and enticing.
- Ensure **normal messages** sound conversational and natural.
- Avoid exact repetition of examples.

Example:
label,text
smish,"আপনার DBBL account suspicious transaction detect করা হয়েছে। Verify now at http://secure-bd.net"
promo,"New season এ সব পোশাকে ২৫% discount। আজই online shopping করুন!"
normal,"কালকে class এ আসবা তো? Let's go together from বাসা।"

Generate the dataset **in Bangla-English Code-mixed**.

"""
    return prompt.strip()


@mcp.tool()
def save_code_mixed_dataset(messages: str) -> str:
    """
    Saves data to a text file, ensuring uniqueness.
    """
    save_dataset(code_mix_sms_file, messages)


# generate_english_dataset 5
# generate_banglish_dataset 5

import re
import json
import requests
import tiktoken



# wandou
url_wandou = "https://api.61798.cn/v1/chat/completions"
api_key_wandou = "sk-yjM9dNUHgKQ4FMDX43B8910bF03f426f802193E910E47dC1"
# model_type = "gpt-3.5-turbo-0613"
model_type = "gpt-3.5-turbo-16k-0613"
# model_type = "gpt-3.5-turbo-0125"

# 1/10
url_zaiwen = "https://www.gaosijiaoyu.cn/message_key_json"
api_key_zaiwen = "selufksu5h8ogn406kujnbxquth67u9l"

# openai
url_openai = "https://api.openai.com/v1/chat/completions"
api_key_openai = "sess-cYafsoSpO6nL5QspmI0iqjvoNLmWHUMJG7rowxE6"

url = url_wandou
api_key = api_key_wandou

def count_words(article):
    splited_article = re.split('[ \n,.?!;:/\"\']', article)
    cnt_empty = 0
    for i in range(1, len(splited_article) - 1):
        j = i + 1
        if splited_article[j] != '':
            cnt_empty += 1
    cnt_article = cnt_empty + len(splited_article)
    return cnt_article

def count_tokens(article):
    encoding = tiktoken.encoding_for_model(model_type)
    tokens = encoding.encode(article)
    cnt_tokens = len(tokens)
    return cnt_tokens

# wandou
def chatgpt_api(system_prompt="You are a helpful assistant.", user_prompt='', temperature=0.7):
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json',
        'Connection': 'close'
    }

    json_data = {
        'model': model_type,
        'temperature': temperature,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ],
        'stream': False,
    }
    response = requests.post(url, headers=headers, json=json_data).json()
    return response

def get_content(response):
    content = ''
    print('========================================')
    print('response: ', response)
    print('========================================')
    for i in response['choices']:
        content += i['message']['content']
    return content

# zaiwen
# def chatgpt_api(user_prompt='', temperature=0.7):
#     payload = json.dumps({
#        "mode": "gpt-3.5-turbo-0613",
#        "temperature": temperature,
#         "message": [
#             {'role': 'system', 'content': "You are a helpful assistant."},
#             {'role': 'user', 'content': user_prompt},
#         ],
#        "user_key": api_key
#     })
#     headers = {
#        'User-Agent': '',
#        'Content-Type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response

# def get_content(response):
#     try:
#         content = response.text
#     except Exception as e:
#         print(e)
#     return content

# def get_remaining():
#     payload = json.dumps({
#         "user_key": api_key
#     })
#     headers = {
#         'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#         'Content-Type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     print(response.text)


# from openai import OpenAI
#
# def chatgpt_api(user_prompt):
#     client = OpenAI(
#         base_url="https://api.chatgptid.net/v1",
#         api_key="sk-8Oiw1bOCPtdSsgMsDa6e9aF36b1c46C5B607Da71D4179853"
#     )
#
#     response = client.chat.completions.create(
#       model="gpt-3.5-turbo-0613",
#       messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": user_prompt}
#       ]
#     )
#     return response
#
# def get_content(response):
#     return response.choices[0].message.content


if __name__ == '__main__':
#     prompt = f"""
#     Read the text in triple quotes and answer a question:
#     Story background information:The article discusses the reasons behind the continuous improvement in athletic performance and the increasing speed of the human race. It argues that this progress is not solely attributed to advances in technology or training methods but is largely influenced by demographic trends. These trends include an increase in average size, longer life expectancy, and faster maturation of children. The improvement in diet and access to healthcare are identified as key factors contributing to these trends. The article suggests that these demographic changes result in the production of bigger and better bodies, leading to faster athletic performance.
#     Main text:The Olympic Gene Pool 

#  Why the human race keeps getting faster. 

#  By Andrew Berry

#  ( 2,168 words; posted Thursday, July 4; to be composted Thursday, July 11 ) 

#  On May 6, 1954, at Oxford University's Iffley Road track, Roger Bannister became, by just half a second, the first man to run a mile in less than four minutes. The Holy Grail of middle-distance running was his. Forty-two years later, however, that achievement seems less significant. Four-minute miles are commonplace; the current record, held by Algerian Noureddine Morceli, is 3:44 , more than 5 percent faster than Bannister's speed. What Iffley Road witnessed was just another step along the road to an ever quicker mile, part of the inexorable improvement of athletic performance that we usually take for granted, particularly when the Olympics roll around. If you stop to think about it, though, such constant progress is remarkable. After all, as biomechanical machines with a standard set of parts, humans should be subject to the same limitations we see in, say, automobiles. How come they aren't? 

#  A lot of entrepreneurs and technophiles would like us to think that the answer has to do with discoveries in the world of sports technology. A new Nike shoe is trumpeted as something that will shave at least one-thousandth of a second off your 100-meter time. Trainers measure the rate of buildup of lactic acid in your muscles, then claim that their programs will control it. Nutritionists fine-tune athletes' diets. Even the old sexual-abstinence-before-the-race dogma is being re-evaluated under the all-seeing eye of science. But I consider all this little more than tinkering. Sports records would continue to tumble even if training methods or athletic clothing or sexual practices were exactly the same today as they were in 1896, when the first modern Olympics took place. These minor miracles are the product neither of technology nor of training but of demographic patterns that affect us all. 

#  Over the past century, the human race has been affected by a slew of what demographers call "secular" trends. (In this context, "secular" does not refer to a trend's lack of spirituality but to its longevity: Secular trends are long-term modifications, not just brief fluctuations.) One such trend is an increase in average size. You have to stoop to get through the doorways of a Tudor cottage in England because its inhabitants were smaller than you are, not because they had a penchant for crouching. Another trend is in life expectancy. People are living longer. Life expectancy in Africa increased over the past 20 years from 46 to 53 years. Over the same period in Europe, where things were already pretty comfortable to begin with, life expectancy increased from 71 to 75 years. The global average was an increase from 58 to 65 years. 

# Probably the most striking change, though, is how much more quickly children are maturing. A 12-year-old child in 1990 who was in what the World Health Organization calls "average economic circumstances" was about 9 inches taller than his or her 1900 counterpart. This is not solely the product of the first trend--the increase in average size--but also due to the fact that children develop faster. Girls menstruate earlier than they used to. The age of menarche (the onset of menstruation) has decreased by three or four months per decade in average sections of Western European populations for the past 150 years. There is a good chance that our 1990 12-year-old already had started to menstruate. Her 1900 counterpart would still have had three years to wait. 

#  What do such trends have to do with athletic performance? Well, if we're living longer and growing up faster, that must mean we're producing bigger, better bodies. Better bodies imply faster miles. We run faster and faster for the same reason it is now common for 11-year-old girls to menstruate. But why are these things happening? 

# Demographers have offered a variety of explanations, but the main one is that our diet is improving. A 12-year-old ate better in 1990 than she would have in the Victorian era. This conclusion is supported by studies of the social elite: Because its members were well-nourished even in the early years of this century, this group has experienced relatively little change, over the past 100 years, in the age girls first menstruate. Another explanation is that health care is getting better. In 1991, according to the WHO, more than 75 percent of all 1-year-olds worldwide were immunized against a range of common diseases. Smallpox, that scourge of previous generations, now is effectively extinct.

#     Question: Which of the following data errors can not be eliminated by documenting the data-cleaning process? Select all that apply.
#     A. Human error in data entry\nB. System issues\nC. Flawed processes\nD. Premature feedback
#     If the answer CANNOT be inferred from the text above, reply with action -1.
#     If the answer CAN be inferred from the text above, reply with action -2, and also provide your reasoning,
#     and the final answer.
#     You are ONLY allowed to reply with action -2 or -1.
#     Your should reply with the following format:
#     ###################################
#     Reasoning: ...
#     Action: -2 or -1
#     Answer option: A / B / C / D/ Not Answer
#     ###################################
#     """
    # prompt = '你的知识更新截止日期是多少'    
    prompt = 'hello'
    print("Requested")
    # print(count_tokens(prompt))    
    response = chatgpt_api(user_prompt=prompt.strip('\n').strip())
    # print(count_tokens(response))
    # print(response)
    response_content = get_content(response)
    print(response_content)
    # print(count_tokens(response_content))

    # 查询余额
    # get_remaining()



# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# text = ""

# with open('data.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         text+=line

# # print(text)
# # url = f"https://api.mindpal.io/api/v2/workflow/run?workflow_id=69ca4c4689c6022432b26c89"
# headers = {
#     "accept": "application/json",
#     "x-api-key": os.environ.get("MINDPAL_API_KEY"),
#     "Content-Type": "application/json"
# }
# # data = {
# #       "幼儿个人性格与兴趣评估记录表": text
# # }

# # response = requests.post(url, headers=headers, json=data)
# # print(response.json())

# #output ----> {'message': 'Successfully triggered workflow run', 'workflow_run_id': '69ca55977861951155e0b53e'}


# run_id = "69ca55977861951155e0b53e"
# # url = f"https://api.mindpal.io/api/workflow-run-status/retrieve-by-id?run_id={run_id}"
# # response = requests.get(url, headers=headers)

# # print(response.json())

# # output -------> {'workflow_run_id': '69ca55977861951155e0b53e', 'status': 'COMPLETED'}


# url = f"https://api.mindpal.io/api/workflow-run-result/retrieve-by-id?run_id={run_id}"

# response = requests.get(url, headers=headers)

# print(response.json())

# with open('output.txt', 'w', encoding="utf-8") as f:
#     f.write(str(response.json()))
# # output -->  {'workflow_run_id': '69ca55977861951155e0b53e', 'workflow_id': '69ca4c4689c6022432b26c89', 'workflow_title': ' Personalities and Interests Info Records', 'workflow_run_input': [{'title': '幼儿个人性格与兴趣评估记录表', 'type': 'TEXT', 'content': "星之洲幼儿园中班幼儿个人发展IDP模版\n一、 幼儿个人评估 (Child'sIndividual Assessment)\n这一板块的目标是全面、深入地了解幼儿当前的整体发展状况，为后续目标的设定和方案的\n制定提供依据。\n1.性格和兴趣 (Personality and Interests)\n描述要点： 通过教师在不同情境下的持续观察，描述幼儿在集体活动、区域游戏、户外活动、\n生活环节中的主要性格特点（如：活泼、安静、内向、外向、坚定、容易受挫等）以及他们特别\n感兴趣的活动、材料或主题。例如，可以记录孩子喜欢和哪些小朋友一起玩，喜欢玩哪些玩具，\n对什么类型的故事或音乐表现出特别的兴趣等。新入园的幼儿需要通过家长的介绍描述和老师在\n第一个月对孩子的观察记录描述。\n目的：教师在不同情境下对幼 儿性格特点、兴趣爱好及参与动机的日常观察，并收集家长反馈。\n基于日常观察记录和家长反馈，分析总结幼儿在性格、兴趣和学习风格方面的特点，为后续目标\n设定提供依据。\n评估方法： 主要依靠教师的日常观察记录和分析。新入园的幼儿需要通过家长的介绍描述和老\n师在第一个月对孩子的观察记录描述分析。\n星之洲幼儿园幼儿个人性格与兴趣评估记录分析表\n•记录人： 班级教师\n•记录周期： 持续观察，定期汇总\n幼儿姓名： 王苏沂\n记录日期：\n2025 年6月13\n日\n兴趣爱好及偏好描述（附行\n观察情境 主要性格特点描述（附行为示例）\n为示例）\n参与动机/激励\n因素\n乖巧专注，上课时能保持注意力集\n集体活动\n中，认真听讲。\n喜欢参与互动性强的活动，\n如角色扮演和故事时间。\n老师的鼓励、同\n 伴的互动\n热爱娃娃家角色扮演（如扮\n喜欢安静的游戏，能独立完成搭建任\n区域游戏\n务，也乐于与同伴合作。\n演公主），喜欢用大积木搭\n建蛋糕。\n新材料的吸引、\n完成作品的成就\n感\n喜欢温和的运动，如散步或玩沙，逐\n户外活动\n步尝试更有挑战性的活动。\n对滑梯和秋千感兴趣，愿意\n尝试集体游戏。\n同伴的邀请、自\n然探索的乐趣\n生活环节 自我服务能力较好，能独立完成穿脱对洗手等生活环节表现出兴 获得老师的肯\n鞋等任务。趣，喜欢模仿大人的行为。定、榜样的示范\n与同伴互动\n友好且乐于交朋友，喜欢与特定同伴\n分享玩具和游戏。\n常和同伴一起玩角色扮演或\n搭建游戏，享受合作的乐趣。\n同伴的回应和互\n动\n与教师互动\n遇到困难时会主动寻求帮助，喜欢向\n老师展示自己的作品。\n常 问老师问题，乐于分享自\n己的想法。\n获得老师的关注\n和赞许\n家庭环境（家\n长反馈）\n在家活泼有主见，喜欢表达自己的想\n法。\n热爱角色扮演（如公主游\n戏），喜欢听故事和玩积木。\n家长的陪伴、获\n得表扬\n其他观察\n语言表达 在鼓励下逐步提升，愿意尝\n试新词汇；体质较弱需关注，但对活\n动充满热情。\n喜欢艺术创作，如涂鸦和手\n工，作品充满想象力。\n创造性活动的成\n就感\n星之洲幼儿园幼儿个人性格与兴趣评估记录分析\n优势能力/显\n著特点\n待提升能力/\n需要关注的\n方面\n主要兴趣爱\n好及偏好总\n结\n激励因素总\n结\n家长反馈摘\n要\n评估分析小\n结：\n这些表格旨在帮助老师系统地收集和组织幼儿的个人信息，特别是他们的性格特点、兴趣爱好和\n行为模式。通过持续的观察记录和与家长的有效沟通，可以更全面地了解每个孩子，为后续制定\n个性化的发展目标和支持方案打下坚实的基础。评估分析则帮助老师从零散的观察中提炼关键信\n息，识别孩子的优势和需要支持的领域，从而使后续的目标设定更具针对性和有效性。", 'index': 0}], 'workflow_run_output': [{'index': 0, 'title': 'IDP 评估报告生成', 'type': 'AGENT', 'content': 'Based on the assessment data for **Wang Suyi (王苏沂)** and the structural requirements of the Xingzhizhou Kindergarten IDP system, the following Assessment Analysis Summary has been developed:\n\n### 1. Strengths/Significant Characteristics (优势能力/显著特点)\n*   **High Focus and Self-Discipline:** Suyi demonstrates excellent concentration during collective activities and classroom instruction. She is a "well-behaved" student who can maintain attention for extended periods.\n*   **Strong Self-Care Skills:** She possesses high independence in daily routines, such as dressing, putting on shoes, and maintaining personal hygiene, often serving as a role model for her peers.\n*   **Proactive Social Interaction:** She is friendly and cooperative, enjoying collaborative play with specific peers. She proactively seeks help when encountering difficulties and takes initiative in sharing her creative works with teachers.\n*   **Rich Imagination in Arts:** Her creative outputs, particularly in doodling and handicrafts, show a high degree of imagination and aesthetic sensibility.\n\n### 2. Areas for Improvement/Focus (待提升能力/需要关注的方面)\n*   **Physical Stamina and Vitality:** Her physical constitution is relatively weak. She requires closer monitoring regarding health and needs support to increase her endurance during physical activities.\n*   **Confidence in Gross Motor Challenges:** Suyi currently prefers gentle outdoor activities (e.g., playing in the sand or walking). She needs encouragement to step out of her comfort zone and participate in more physically demanding or high-intensity group games.\n*   **Expressive Language Development:** While she is willing to try new vocabulary, her verbal expression is still in a developmental stage. She requires structured opportunities and encouragement to articulate complex thoughts more fluently and confidently.\n\n### 3. Main Interests and Preferences Summary (主要兴趣爱好及偏好总结)\n*   **Thematic Role-Play:** She is deeply interested in domestic role-play (e.g., "Doll House" or "Princess" games), which allows her to exercise her social imagination.\n*   **Constructive Play:** She enjoys using large blocks to build specific objects, such as "cakes," demonstrating a preference for goal-oriented construction.\n*   **Creative Arts and Narrative:** Suyi has a strong affinity for storytelling, music, and hands-on creative tasks like painting and crafting, where she can express her inner thoughts.\n\n### 4. Motivational Factors Summary (激励因素总结)\n*   **Social & Emotional Reinforcement:** Recognition from teachers (praise and attention) and positive responses from peers are her primary drivers.\n*   **Intrinsic Achievement:** The sense of accomplishment derived from completing a physical work (e.g., an art piece or a block structure) highly motivates her.\n*   **Novelty and Engagement:** She is easily attracted by new materials and interactive, high-engagement activities like role-playing and storytelling.\n*   **Parental Companionship:** Consistent support and verbal encouragement from parents at home significantly boost her confidence and participation.\n\n### 5. Assessment Analysis Summary (评估分析小结)\nOverall, Suyi is a focused, imaginative, and socially well-adjusted child with a solid foundation in self-care and cooperative play. Her development is currently characterized by high "quiet" competence (art, focus, role-play) but a more cautious approach to physical challenges. \n\nThe primary goal for the next stage of her IDP should be to bridge the gap between her rich internal imagination and her external physical/verbal expression. We will leverage her love for role-play and art as "entry points" to encourage more vigorous physical movement (e.g., "action-based" role-play) and more complex verbal descriptions. Additionally, targeted support for her physical health and confidence in outdoor settings will be essential to ensure a balanced development across all domains. Her proactive nature in seeking teacher interaction provides an excellent leverage point for individualized scaffolding in language and motor skills.'}]}

# from pydantic import BaseModel, field_validator, ValidationInfo
# from fastapi import FastAPI, HTTPException
# import asyncio
# import time
# app = FastAPI()

# class User(BaseModel):
#     username: str
#     age: int

#     @field_validator('username')
#     @classmethod
#     def username_must_be_alphanumeric(cls, v: str) -> str:
#         if not v.isalnum():
#             raise ValueError('Username must be alphanumeric')
#         return v

#     @field_validator('age')
#     @classmethod
#     def age_must_be_positive(cls, v: int) -> int:
#         if v <= 0:
#             # raise ValueError('Age must be a positive integer')
#             HTTPException(status_code=400, detail='Age myst be a positive integer')
#         return v

# @app.post("/users/")
# def create_user(user: User):
#     try:
#         return user
#     except Exception as ex:
#         return(f"Error occurred: {ex}")
# global w_count
# w_count = 1
# @app.get('/with-wait')
# async def with_wait():
#     global w_count
#     print(f"Recive {w_count} requst")
#     st_time = time.time()
#     cc = w_count
#     if w_count == 1:
#         w_count+=1
#         await asyncio.sleep(60)
#     else:
#         w_count+=1
#     end_time = time.time()
#     print(f"Completed request {cc + 1}, count: {w_count}")

#     return {"message": f"Waited for {end_time - st_time} seconds, count: {cc + 1}"}
# wo_count = 0
# @app.get('/without-wait')
# async def without_wait():
#     st_time = time.time()
#     global wo_count
#     wo_count+=1
#     end_time = time.time()
#     return {"message": f"Waited for {end_time - st_time} seconds, count: {wo_count}"}
    
from dotenv import load_dotenv        
from src.db_manager.databse_manager import DatabaseManager

load_dotenv()
db = DatabaseManager()
print(db.get_data())

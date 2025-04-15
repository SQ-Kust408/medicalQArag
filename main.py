from langchain.schema import HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from data_loader import data_loader
from serp import serpapi_search
from bm25 import bm25_search
from rag_sys import rag
from rrf import rrf
from config import HUGGINGFACE_MODEL_NAME_CHAT,  HUGGINGFACE_API_KEY

prompt = '''
任务目标：
你是一位专业的医疗知识问答助手，需要依据检索出的文档内容，精准且清晰地回答用户提出的医疗相关问题。你的回答要严格遵循医学事实和逻辑，为用户提供可靠的信息。

任务要求：
1. 回答内容必须完全基于检索出的文档。禁止引入文档之外的额外信息进行回答，以确保回答的客观性和准确性。
2. 如果检索出的文档中没有包含用户问题的答案，请直接明确回复“我不知道”。不要进行猜测或给出没有依据的回答。
3. 回答应具有良好的条理性和逻辑性。对于复杂的问题，可分点阐述，使内容易于理解。
4. 使用通俗易懂的语言进行表述，避免使用过于专业生僻的医学术语。若必须使用，需进行简单解释。
5. 确保回答内容简洁明了，避免冗长和无关的表述。但也要保证关键信息完整，不遗漏重要细节。
6. 若文档中提供了多种可能的情况或解决方案，需全面列出，并说明不同情况的适用条件。
7. 对于涉及医疗建议或措施的回答，需明确指出该建议仅基于当前检索文档，具体情况还需咨询专业医生。

用户问题：
{query}

检索出的文档：
{new_docs}
'''

# 加载数据
docs = data_loader("medical_data.txt")
print("docs Ready")
llm = HuggingFaceEndpoint(
    repo_id=HUGGINGFACE_MODEL_NAME_CHAT,
    huggingfacehub_api_token=HUGGINGFACE_API_KEY
)
# 初始化模型
try:
    model = ChatHuggingFace(llm=llm)
except Exception as e:
    print(f"模型初始化失败: {e}")
    import sys
    sys.exit(1)
print("model Ready")
# 获取用户输入
query = "头晕脖子痛怎么办："

print("进行向量检索")
vector_res = rag(docs, query)
vector_results = [i.page_content for i in vector_res]
print(vector_results)
print("----------------------------------------------------------------------")
print("进行文本检索")
bm25_res = bm25_search(docs, query)
print(bm25_res)
print("----------------------------------------------------------------------")
print("进行serpapi检索")
serp_res = serpapi_search(query)
serp_results = [result.get('snippet', '') for result in serp_res.get('organic_results', [])]
print(serp_results)
print("----------------------------------------------------------------------")
print("RRF重排")
rrf_res = rrf(vector_results, bm25_res, serp_results)
new_docs = ''.join(rrf_res)
print(new_docs)
print("----------------------------------------------------------------------")
# 格式化提示信息
formatted_prompt = prompt.format(query=query, new_docs=new_docs)

# 创建 HumanMessage 对象列表
messages = [HumanMessage(content=formatted_prompt)]

# 调用大模型进行回复
try:
    res = model.invoke(messages)
    print(res.content)
except Exception as e:
    print(f"调用模型失败: {e}")
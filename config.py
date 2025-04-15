# 该文件用于存储项目中的所有超参数和配置信息

# SerpAPI的API密钥，用于调用SerpAPI进行搜索
SERPAPI_API_KEY = ""

# Hugging Face模型的相关配置
# 模型名称，指定使用的Hugging Face模型
#deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
#wgs/ChatGLM-Medical
HUGGINGFACE_MODEL_NAME_CHAT = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
HUGGINGFACE_MODEL_NAME_EMB = "DMetaSoul/Dmeta-embedding-zh"
# Hugging Face模型的基础URL
#HUGGINGFACE_BASE_URL = ""
# Hugging Face模型的API密钥
HUGGINGFACE_API_KEY = ""

# 文本分块的相关参数
# 每个文本块的大小
CHUNK_SIZE = 500
# 文本块之间的重叠大小
CHUNK_OVERLAP = 0

# RRF算法的超参数
# 排序后返回的前k个结果
RRF_K = 10
# RRF算法中的超参数m
RRF_M = 60

# 向量检索和文本检索返回的结果数量
SEARCH_RESULT_NUM = 10
医疗问答的 RAG 系统项目
项目概述
本项目是一个基于检索增强生成（RAG）技术的医疗问答系统。该系统结合了向量检索、文本检索和 SerpAPI 搜索，使用 RRF 算法对检索结果进行重排序，最后调用 Hugging Face 的大模型进行回答。系统旨在依据检索出的文档内容，为用户提供准确、可靠的医疗相关问题解答。
项目结构
plaintext
project/
├── data_loader.py    # 语料库分块模块
├── main.py           # 主程序入口
├── rrf.py            # RRF算法重排序模块
├── serp.py           # SerpAPI搜索模块
├── bm25.py           # BM25文本检索模块
├── rag_sys.py        # 向量检索模块
├── config.py         # 项目配置文件
└── medical_data.txt  # 医疗语料库文件
环境要求
Python 3.8 及以上版本
GPU（可选，用于加速向量嵌入计算）
安装依赖
在项目根目录下，执行以下命令安装所需的 Python 库：
bash
pip install -r requirements.txt
配置文件
在config.py文件中，需要配置以下信息：
SERPAPI_API_KEY：SerpAPI 的 API 密钥，用于调用 SerpAPI 进行搜索。
HUGGINGFACE_MODEL_NAME_CHAT：指定使用的 Hugging Face 聊天模型名称。
HUGGINGFACE_MODEL_NAME_EMB：指定使用的 Hugging Face 嵌入模型名称。
HUGGINGFACE_API_KEY：Hugging Face 模型的 API 密钥。
其他超参数，如文本分块大小、RRF 算法参数等。
运行步骤
确保medical_data.txt文件包含医疗语料库内容。
在config.py文件中配置好所需的 API 密钥和模型名称。
运行main.py文件：
bash
python main.py
程序将依次进行向量检索、文本检索、SerpAPI 搜索，使用 RRF 算法对结果进行重排序，最后调用大模型进行回答，并输出回答结果。
注意事项
回答内容严格基于检索出的文档，若文档中没有包含用户问题的答案，将回复 “我不知道”。
涉及医疗建议或措施的回答仅基于当前检索文档，具体情况还需咨询专业医生。
贡献
本项目代码基于
https://www.bilibili.com/video/BV1oMYje7EHU/?spm_id_from=333.1387.favlist.content.click
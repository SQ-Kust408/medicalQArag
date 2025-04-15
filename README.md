# 医疗问答RAG系统项目
基于检索增强生成（RAG）技术的医疗领域问答系统，结合向量检索、文本检索、SerpAPI 网络搜索与 RRF 重排序算法，最终通过 Hugging Face 大模型生成精准回答。
# 📖 项目概述
本系统通过 检索增强生成（RAG） 技术，实现医疗领域的智能问答：
多模态检索：融合向量检索（基于语义的向量相似度匹配）、文本检索（BM25 算法）和 SerpAPI 网络搜索，覆盖本地语料与实时网络信息。
智能重排序：使用 RRF（Rank Reciprocal Fusion）算法对多源检索结果进行加权融合，提升答案相关性。
大模型生成：调用 Hugging Face 预训练大模型，基于检索结果生成自然语言回答，确保内容准确可靠。
目标：严格基于检索文档提供医疗解答，涉及专业建议时提示用户咨询医生。
# 📁 项目结构
```text
project/
├── data_loader.py       # 语料库分块处理模块（将长文本分割为适合检索的文本块）
├── main.py              # 主程序入口（整合全流程：检索 → 重排序 → 生成回答）
├── rrf.py               # RRF 重排序算法实现（融合多检索结果的排序策略）
├── serp.py              # SerpAPI 网络搜索模块（调用外部 API 获取实时网络信息）
├── bm25.py              # BM25 文本检索模块（基于关键词匹配的传统文本检索算法）
├── rag_sys.py           # 向量检索核心逻辑（包含向量数据库构建、语义检索等功能）
├── config.py            # 全局配置文件（集中管理 API 密钥、模型参数、超参数等）
└── medical_data.txt     # 医疗领域语料库（用户需提前填充专业医疗文本数据）
```
# 🚀 环境要求
Python 版本：3.10+
硬件：GPU（可选，加速向量嵌入计算）
依赖库：通过 requirements.txt 安装
# 💻 安装步骤
克隆项目
git clone <项目仓库链接>
cd project

# 安装依赖
pip install -r requirements.txt

# ⚙️ 配置文件（config.py）
需提前配置以下关键参数：
# SerpAPI 配置（网络搜索服务）
SERPAPI_API_KEY = "your_serpapi_api_key"  

# Hugging Face 模型配置
HUGGINGFACE_MODEL_NAME_CHAT = "模型名称（如：meta-llama/Llama-2-70b-chat-hf）"
HUGGINGFACE_MODEL_NAME_EMB = "嵌入模型名称（如：sentence-transformers/all-MiniLM-L6-v2）"
HUGGINGFACE_API_KEY = "your_huggingface_api_key"  

# 其他参数
CHUNK_SIZE = 500       # 文本分块大小
RRF_PARAM = 6          # RRF 算法融合参数

# 🚦 运行流程
准备语料：确保 medical_data.txt 包含医疗领域文本数据。
配置参数：在 config.py 中填入有效 API 密钥和模型名称。
启动程序：
python main.py

交互流程：程序按「向量检索 → 文本检索 → SerpAPI 搜索 → RRF 重排序 → 大模型生成」流程输出回答。
# ⚠️ 注意事项
答案来源：回答严格基于检索结果（本地语料 + 网络搜索），若文档无相关信息，回复「我不知道」。
医疗建议：内容仅供参考，具体医疗决策请咨询专业医生。
性能优化：GPU 可加速向量嵌入计算，建议在处理大规模语料时启用。
# 🙌 贡献说明
本项目代码基于 B 站教程：【RAG 实战】医疗问答系统开发教程欢迎提交 PR 优化代码、补充文档或报告问题！
https://www.bilibili.com/video/BV1oMYje7EHU/?spm_id_from=333.1387.favlist.content.click

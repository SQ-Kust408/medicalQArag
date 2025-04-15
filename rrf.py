from typing import List
from config import RRF_K, RRF_M

def rrf(vector_results: List[str], text_results: List[str], serp_results: List[str], k: int = RRF_K, m: int = RRF_M):
    """
    使用RRF算法对三组检索结果进行重排序

    params:
    vector_results (list): 向量召回的结果列表,每个元素是文档内容
    text_results (list): 文本召回的结果列表,每个元素是文档内容
    serp_results (list): SerpAPI搜索的结果列表,每个元素是文档内容
    k(int): 排序后返回前k个
    m (int): 超参数

    return:
    重排序后的结果列表,每个元素是文档内容
    """
    doc_scores = {}
    # 遍历三组结果,计算每个文档的融合分数
    for rank, doc_id in enumerate(vector_results):
        doc_scores[doc_id] = doc_scores.get(doc_id, 0) + 1 / (rank + m)
    for rank, doc_id in enumerate(text_results):
        doc_scores[doc_id] = doc_scores.get(doc_id, 0) + 1 / (rank + m)
    for rank, doc_id in enumerate(serp_results):
        doc_scores[doc_id] = doc_scores.get(doc_id, 0) + 1 / (rank + m)

    # 将结果按融合分数排序
    sorted_results = [d for d, _ in sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)[:k]]
    return sorted_results
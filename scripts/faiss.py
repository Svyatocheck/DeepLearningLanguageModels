import pandas as pd
import os
import faiss
from transformers import AutoTokenizer, AutoModel
import torch
from torch import Tensor
import torch.nn.functional as F

DEVICE = "cpu"


def embed_bert_cls(text, model, tokenizer):
    t = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**{k: v.to(model.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings.cpu().numpy()


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


def get_embed_rubert(
    file_name: str,
):
    global DEVICE
    tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
    model = AutoModel.from_pretrained("cointegrated/rubert-tiny")
    model.to(DEVICE)
    example = open(file_name).readlines()[0]
    query = embed_bert_cls(example, model, tokenizer)
    return query

def get_embed_e5(
        file_name: str,
):
    global DEVICE
    example = open(file_name).readlines()[0]
    input_texts = [f'query: {example}']
    tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-base')
    model = AutoModel.from_pretrained('intfloat/multilingual-e5-base')
    batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**batch_dict)
    query = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])
    query = F.normalize(query, p=2, dim=1)
    return query



def faiss_search_rubert(embed, file_name: str, index, dataframe: pd.DataFrame, top_k: int = 4):
    query = get_embed_rubert(file_name)
    D, I = index.search(query, top_k)
    top_k_vacancy = dataframe.iloc[I[0]]
    return top_k_vacancy

def faiss_search_e5(embed, file_name: str, index, dataframe: pd.DataFrame, top_k: int = 4):
    query = get_embed_e5(file_name)
    D, I = index.search(query, top_k)
    top_k_vacancy = dataframe.iloc[I[0]]
    return top_k_vacancy

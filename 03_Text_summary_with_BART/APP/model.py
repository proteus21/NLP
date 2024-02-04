import spacy
from heapq import nlargest
from collections import Counter
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from transformers import BartTokenizer, BartForConditionalGeneration

nlp=spacy.load("en_core_web_lg")

def summerized1(text):
    document = nlp(text)
    keywords = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['NOUN', 'VERB', 'ADJ', 'PROPN']
    for token in document:
        if (token.text in stopwords or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag):
            keywords.append(token.text)
    freq_words = Counter(keywords)
    max_freq_words = Counter(keywords).most_common(1)[0][1]
    for word in freq_words.keys():
        freq_words[word] = freq_words[word] / max_freq_words
    freq_words.most_common(6)

    sent_str = {}
    for sent in document.sents:
        for word in sent:
            if word.text in freq_words.keys():
                if sent in sent_str.keys():
                    sent_str[sent] += freq_words[word.text]
                else:
                    sent_str[sent] = freq_words[word.text]
    summerized = nlargest(3, sent_str, key=sent_str.get)
    return (' '.join([m.text for m in summerized]))

def summerized2(text):
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    input_text = text
    input_ids = tokenizer.batch_encode_plus(
        [input_text],
        return_tensors='pt',
        max_length=1024,
        truncation=True

    )
    summary_ids = model.generate(
        input_ids['input_ids'],
        num_beams=4,
        max_length=100,
        early_stopping=True

    )
    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    return summary






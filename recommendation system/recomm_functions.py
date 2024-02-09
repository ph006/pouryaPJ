import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from hazm import Stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df=pd.read_csv('dataset.csv')
stop_words=pd.read_csv('all_words.txt')
df['Content_1']=df['Content_1'].fillna('')
stop_words_list=stop_words['words'].to_list()

df2=pd.read_csv(r'C:\Users\ASUS\Jupyter notebook\NLP\exercise_files\my_ex\pii_dataset.csv')

# farsi sazi genre

df['Genre']=df['Genre'].replace({'Drama':'دراما', 'Crime':"جرم و جنایت جنایی", 'Human Interest & Society':"ععلایق انسانی وجامعه", 'Comedy':"کمدی",
       'Adventure':"ماجراجویی", 'Mystery':"رازآلود", 'War':"جنگ", 'Action':" اکشن و هیجانی", 'Portrait':"پورتریت",
       'Experimental':'آزمایشی', 'Romance':"عاشقانه", 'Family':"خانواده", 'History':"تاریخی", 'Animation':"کارتون انیمیشن",
       'Culture & Traditions':"فرهنگی ", 'Arts & Literature':"هنری ادبی", 'Music':"موزیکال",
       'Architecture & Urbanism':"معماری", 'Horror':"ترسناک وحشت ناک", 'Nature & Wildlife':"طبیعت حیت وحش",
       'Thriller':"دلهره آور هیجانی"})

# taghir type

df['EN_title'] = df['EN_title'].astype(str)
df['PERSIAN_title'] = df['PERSIAN_title'].astype(str)
df['Genre'] = df['Genre'].astype(str)
df['Content_1'] = df['Content_1'].astype(str)
df['Content_2'] = df['Content_2'].astype(str)

susman=df['Content_1'].to_string()

# cleanup function

def remove_words_from_text(text):
    global stop_words_list
    pattern2 = r'[^آ-ی\s]'
    # Create a pattern for the words to remove

    pattern = '|'.join(r'\b{}\b'.format(re.escape(word)) for word in stop_words_list)

    # Use re.sub to replace occurrences of the specified words with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    cleaned_text = re.sub(pattern2, '', cleaned_text)
    #     cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

    return cleaned_text

# tf_idf function

def remove_word_eng(text):
    clean = re.sub(r'\s+', ' ', text)
    clean = re.sub(r'[^\w\s]', '', clean)
    return clean

def tf_idf(user_input, num_results=10):          #stemmer has some issues *** مهم نیست

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    stemmer = Stemmer()

    X = df['Content_1'].apply(remove_words_from_text)
    # X = X.apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))
    X = X.apply(lambda x: ' '.join([word for word in x.split() if len(word) > 2]))

    tfidf_matrix = tfidf_vectorizer.fit_transform(X)
    user_input = ' '.join([stemmer.stem(word) for word in user_input.split()])
    user_input = ' '.join([word for word in user_input.split() if len(word) > 2])

    user_tfidf = tfidf_vectorizer.transform([user_input])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    similar_movies_indices = similarities.argsort()[:-num_results - 1:-1]
    similar_movies = df.iloc[similar_movies_indices]

    return X

# word2vec function

def word2vec(column,cleaner,user_input, num_results=10):
    from gensim.models import Word2Vec
    from nltk.tokenize import word_tokenize
    from sklearn.metrics.pairwise import cosine_similarity



    text = column.apply(cleaner)

    text= text.apply(lambda x: ' '.join([word for word in x.split() if len(word) > 2]))

    tokenized_sentences = [word_tokenize(sentence) for sentence in text]
    model = Word2Vec(tokenized_sentences, vector_size=150, window=5, min_count=10, workers=4)

    model.save("word2vec.model")
    loaded_model = Word2Vec.load("word2vec.model")

    similar_words = model.wv.most_similar(user_input, topn=5)
    print(similar_words)
    return similar_words

# meme=tf_idf('یک فیلم پلیسی')
#
# print(meme)

# lol=remove_words_from_text(susman)
# print(lol)

word2vec(df['Content_1'],remove_words_from_text,'قتل')
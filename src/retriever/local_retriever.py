from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class LocalRetriever:
    def __init__(self, documents: list[str]):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(
            stop_words=None,
            ngram_range=(1, 2),
            min_df=1
        )
        self.doc_vectors = self.vectorizer.fit_transform(documents)

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_vectors)[0]

        top_indices = scores.argsort()[::-1][:top_k]
        return [self.documents[i] for i in top_indices]

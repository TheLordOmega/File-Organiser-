from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=.20, random_state=42, stratify=labels)
print(X_train.shape)
print(X_test.shape)

vectoriser = TfidVectorizer(
    lowercase = True
    ngram_range= (1,2),
    min_df = 0.2,
    max_df = 0.95,
    sublinear_tf= True,
)

classifier = LogisticRegression(
    max_iter=1000,
    class_weight= "balanced",
)

model = Pipeline([
    ("tfidf", vectoriser),
    ("classifier", classifier),
])

model.fit(X_train,y_train)
predictions = model.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, zero_division=0))

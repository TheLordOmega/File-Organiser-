#actual ai code till now

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from Organiser import file

texts =[]
    #Path("training_files/file1.md").read_text(encoding="utf-8")
    ##from organiser.py
for file in directory.iterdir():
    if (
            file.is_file() and file.name not in blacklist
            and not file.name.startswith(".")
            and file.stat().st_mtime > date.timestamp()
        ):
           title = file.name.lower()
           if file.suffix.lower() in [".txt", ".md" ]:
                title += "" + file.read_text(encoding="utf-8", errors="ignore").lower()
           if file.suffix.lower() in [".pdf"]:
                reader = PdfReader(file),
                title += ""+ "".join( page.extract_text() or "" for page in reader.pages).lower(),


labels = [
"Mathematics", "Chemistry", "Material science", "Engineering practice 1"

]




X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=.20, random_state=42, stratify=labels)
print(X_train.shape)
print(X_test.shape)

vectoriser = TfidfVectorizer(
    lowercase = True,
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

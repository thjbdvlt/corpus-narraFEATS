import spacy
import random


def _shuffle_docbin(db):
    """Shuffle a DocBin."""

    vocab = spacy.vocab.Vocab()
    docs = list(db.get_docs(vocab))
    del db
    random.shuffle(docs)
    db = spacy.tokens.DocBin()
    for i in docs:
        db.add(i)
    return db


def shuffle_docbin(filepath: str) -> None:
    """Shuffle a serialized DocBin."""

    db = spacy.tokens.DocBin()
    db.from_disk(filepath)
    db = _shuffle_docbin(db)
    db.to_disk(filepath)


if __name__ == '__main__':
    import sys
    for i in sys.argv[1:]:
        print(i, '...')
        shuffle_docbin(i)

import glob
import spacy
import conllu
from conllu import TokenList
from spacy.tokens import DocBin
import typer
from pathlib import Path
from spacy.tokens import Doc
from spacy.vocab import Vocab


def unescape(s: str) -> str:
    """Unescape newlines, tabs, spaces."""
    return s.replace('\\n', '\n').replace('\\t', '\t').replace('\\s', ' ')


def to_doc(vocab: Vocab, sent: TokenList) -> Doc:
    """Make a Doc (spacy) from a sentence (CONLLU)."""
    words = [unescape(i["form"]) for i in sent]
    pos = [i["upos"] for i in sent]
    feats = [conllu.serializer.serialize_field(i["feats"]) for i in sent]
    doc = Doc(vocab=vocab, words=words, pos=pos, morphs=feats)
    return doc


def main(
    train: Path = Path("train.spacy"),
    dev: Path = Path("dev.spacy"),
    quiet: bool = False,
) -> None:
    """Make spaCy DocBin files from the corpus."""
    db = DocBin()
    vocab = spacy.vocab.Vocab()

    for filepath in glob.glob("./corpus/*.conllu"):
        if not quiet:
            print(filepath, "...")
        with open(filepath, "r") as f:
            c = conllu.parse(f.read())
        for i in c:
            db.add(to_doc(vocab, i))

    db_dev = DocBin()
    db_train = DocBin()

    n = 0
    for i in db.get_docs(vocab):
        d = db_dev if n % 4 == 0 else db_train
        d.add(i)
        n += 1

    db_dev.to_disk(dev)
    db_train.to_disk(train)


if __name__ == "__main__":
    typer.run(main)

dev   := dev.spacy
train := train.spacy
tar   := narrafeats.tar.gz

all:
	python3 to_spacy_docbin.py --dev $(dev) --train $(train)
	python3 shuffle_docbin.py $(dev) $(train)

tar:
	tar cvzf $(tar) corpus *.py makefile LICENSE README.md \
		--transform 's,^,/narrafeats/,'

clean:
	rm -f $(dev) $(train) $(tar)

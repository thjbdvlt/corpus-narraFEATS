__narraFEATS__ est un corpus de textes en français annotés pour l'étiquetage morpho-syntaxique ([POS](https://universaldependencies.org/u/pos/) + [feats](https://universaldependencies.org/u/feat/)).

Le corpus est conçu pour entrainer des modèles d'annotation morphologique pour textes narratifs et/ou conversationnels contemporains dans lesquels les pronoms personnels et temps verbaux sont variés (typiquement: des textes de fictions contenant des dialogues). Il est constitué de textes littéraires et de sciences humaines, ainsi que de quelques textes très brefs rédigés de façon _ad hoc_, et d'extraits de Wikipedia.
Le corpus est disponible sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Il possède quelques spécificités:

- Les seules apostrophes présentes sont les apostrophes droites (`'`).
- Le seul format d'écriture inclusive contractée est celui-ci: `parti·es`, `auteur·rices`.
- La _morphological feature_ `Gender` est absente.

Les textes ont été annotés de façon semi-automatiques: pré-annotés à l'aide de la librairie [spaCy](https://spacy.io/) puis corrigés à l'aide de scripts, puis manuellement -- il comporte encore des erreurs.

corpus
------

Tous les textes ont été largement modifiés, de larges portions ayant été retirées, réécrites ou ajoutées[^3]. Certains adjectifs et noms très fréquents ont aussi été systématiquement remplacés pour assurer une plus grande diversité lexicale (voir [plus bas](#substitution)).

### wikisource

- Colette, [_Paris de ma fenêtre_](https://fr.wikisource.org/wiki/Paris_de_ma_fen%C3%AAtre) (1944)
- George Sand, [_François le champi_](https://fr.wikisource.org/wiki/Fran%C3%A7ois_le_Champi/Texte_entier) (1853)
- Jack London, [_L'appel de la forêt_](https://fr.wikisource.org/wiki/L%E2%80%99Appel_de_la_for%C3%AAt/Texte_entier) (1903, trad. 1908)
- Jack London, [_Lettre au juge Samuel_](https://fr.wikisource.org/wiki/Lettre_au_juge_de_police_Samuels) (1910)
- Léon Tolstoi, [_Qu'est-ce que l'art_](https://fr.wikisource.org/wiki/Qu%E2%80%99est-ce_que_l%E2%80%99art_%3F) (1898, trad. 1918)
- Marc-Aurèle, [_Pensées pour moi-même_](https://fr.wikisource.org/wiki/Pens%C3%A9es_pour_moi-m%C3%AAme), (1876)
- Marcel Mauss, [_La sociologie: objet et méthode_](https://fr.wikisource.org/wiki/Essais_de_sociologie/01) (1971)
- Selma Lagerlöf, [	Le Merveilleux Voyage de Nils Holgersson à travers la Suède ](https://fr.wikisource.org/wiki/Le_Merveilleux_Voyage_de_Nils_Holgersson_%C3%A0_travers_la_Su%C3%A8de) (1906, trad. 1912)
- Simone Weil, [_La condition ouvrière_](https://fr.wikisource.org/wiki/La_Condition_ouvri%C3%A8re/Texte_entier) (1951, rédaction en 1934-1937)

### the wittgenstein project

- Ludwig Wittgenstein, [_Conférence sur l'éthique_](https://www.wittgensteinproject.org/w/index.php/Une_conf%C3%A9rence_sur_l%E2%80%99Ethique) (1929)
- Ludwig Wittgenstein, [_Le cahier bleu_](https://www.wittgensteinproject.org/w/index.php/Blue_Book) et [_Le cahier brun_](https://wittgensteinproject.org/w/index.php/Brown_Book) (trad. automatique avec [deepl](https://www.deepl.com/en/translator))

### les classiques des sciences sociales

- Marcel Mauss, [_Les techniques du corps_](https://archive.wikiwix.com/cache/index2.php?url=http%3A%2F%2Fclassiques.uqac.ca%2Fclassiques%2Fmauss_marcel%2Fsocio_et_anthropo%2F6_Techniques_corps%2FTechniques_corps.html#federation=archive.wikiwix.com&tab=url) (1934 -- texte dans le domaine public depuis 2021).

### wikipedia

Les articles tirés de Wikipedia ont tous été plus ou moins modifié, souvent simplement pour ajouter des formes ou des mots absents du corpus, sans avoir à écrire de nouvelles phrases.

- Article [_Donnée_](https://fr.wikipedia.org/wiki/Donn%C3%A9e)
- Article [_Logiciel libre_](https://fr.wikipedia.org/wiki/Logiciel_libre)
- Article [_Copier-coller_](https://fr.wikipedia.org/wiki/Copier-coller)
- Article [_Commun_](https://fr.wikipedia.org/wiki/Communs)
- Extraits de l'article [_Football_](https://fr.wikipedia.org/wiki/Football) et [_Lois du jeu_](https://fr.wikipedia.org/wiki/Lois_du_jeu)

substitution
------------

Dans certains de ces textes, certains mots sont répétés inlassablement, tandis que de nombreux mots sont (évidemment) absents du corpus.
Or, il me semblait inutile que le modèle que j'entrainais sur ce corpus voie (par exemple) le mot _champi_ 146 fois (car il y a _françois le champi_, de george sand, dans mon corpus), 53 fois le mot _moulin_ (idem), 58 fois le mot _pensionnaires_ (dans _le père goriot_), 168 fois _jeune_ ou 85 fois _libre_. Autant remplacer ces mots par d'autres qui possèdent les mêmes caractéristiques morphologiques: remplacer l'adjectif _libres_ par _vacantes_, _libertaires_ ou _aériennes_.

Pour ce faire, j'ai fait quelques listes de mots (disponibles dans le dossier [./mots/](./mots/)):

- Une liste de noms propres, celles des noms du _crew_ de la série [_Dark Crystal_](https://www.netflix.com/ch-fr/title/80148535), récupérée sur [IMDB](https://www.imdb.com/title/tt6905542/fullcredits/?ref_=tt_cl_sm) et de laquelle j'ai retranché les noms qui étaient des mots français.
- Une liste de mots désignant des objets matériels qu'on peut trouver dans une maison, récupérés dans des textes de George Perec: [_Notes sur les objets qui se trouvent sur ma table de travail_](https://fr.wikipedia.org/wiki/Penser/Classer) et les trois premiers chapitres de [_La vie mode d'emploi_](https://fr.wikipedia.org/wiki/La_Vie_mode_d%27emploi).
- Liste d'interjection et d'onomatopées, reprise d'un document présentant les conventions de transcriptions d'un corpus oral: le [_Corpus du Français Parlé de nos Régions_](https://cfpr.huma-num.fr/)[^1].
- Liste de concepts, obtenue en posant à [ChatGPT](https://openai.com/index/introducing-chatgpt-and-whisper-apis/) la question suivante: _la nature, l'art, la vie, la littérature, ... (continue autant que tu peux)_. Le début de sa réponse: _la musique, la science, la philosophie, l'amour, la poésie, l'histoire, la cuisine, la danse_.
- Liste de noms de métiers ([issue de Wikipedia](https://fr.wikipedia.org/wiki/Liste_des_m%C3%A9tiers)).
- Deux listes d'adjectifs, l'une pour les personnes (les choses animées) et l'autre pour les choses (inanimées). La liste pour les choses est essentiellement composé d'adjectifs à usage esthétique. Par exemple: _merveilleux·euse_, _joli·e_, _fantastique_. Il s'agit moins d'adjectifs exprimant strictement la valeur esthétique d'une chose que d'adjectifs pouvant être substitués aux mots _beau·elle_, _joli·e_: _quelle jolie maison_, _quelle fantastique maison_.

La colonne `Misc` (la dernière) des fichiers `.conllu` contient des _labels_ utilisés pour remplacer ces mots (organisés en catégorie) et présentes le mot originalement présents (afin qu'il puisse être restauré si besoin)[^6]:

```conllu
25	cafétéria	_	NOUN  ...  Number=Sing  ...  noun.lieu=fontaine
```

[^1]: La liste ici présente contient quelques mots en plus (_heu_, _ha_, ...), d'autres en moins (_oui_, _ouais_).

[^3]: L'une des modifications a consisté à intégrer des formes d'écritures inclusive: formes contractées (_auteur·rices_, _entraîné·es_, etc.) et pronoms inclusifs et/ou non-binaires (_iel_, _celleux_, etc.).

[^6]: Certains mots comme, les noms propres originaux (tous remplacés par _Dominique_) ont été remplacé dans les textes avant l'annotation (pour facilité la pré-annotation automatique).

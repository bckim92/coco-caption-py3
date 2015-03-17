Microsoft COCO Caption Evaluation
===================

Evaluation codes for MS COCO caption generation.

## REQUIREMENTS ##
- java 1.8.0
- python 2.7

## FILES ##
./
- cocoEvalCapDemo.py (demo script)

./annotation
- captions_val2014.json (COCO 2014 caption validation set)
- More detials can be found under download tab on [COCO dataset](http://mscoco.org/dataset)

./results
- captions_val2014_fakecap_results.json (example fake results for running demo)
- More detials can be found under evaluate->format tab on [COCO dataset](http://mscoco.org/dataset)

./pycocoevalcap: The folder where all evaluation codes are stored.
- evals.py: includes COCOEavlCap class that includes multiple scores.
- tokenizer: PTBTokenizer
- bleu: Bleu evalutation codes
- meteor: Meteor evaluation codes
- rouge: Rouge-L evaluation codes
- cider: CIDEr evaluation codes

## Reference ##

0. BLEU: [BLEU: a Method for Automatic Evaluation of Machine Translation](http://delivery.acm.org/10.1145/1080000/1073135/p311-papineni.pdf?ip=72.229.132.206&id=1073135&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=644819513&CFTOKEN=71377947&__acm__=1426607117_16e4342fbc20d41c064c8fb685cffe60)
1. Meteor: [Project page](http://www.cs.cmu.edu/~alavie/METEOR/) with related publications. We used the latest version (1.5) of the [Code](https://github.com/mjdenkowski/meteor). Changes have been made to the source code to properly aggreate the statistics for the entire corpus.
2. Rouge-L: [ROUGE: A Package for Automatic Evaluation of Summaries](http://anthology.aclweb.org/W/W04/W04-1013.pdf)
3. CIDEr: [CIDEr: Consensus-based Image Description Evaluation] (http://arxiv.org/pdf/1411.5726.pdf)

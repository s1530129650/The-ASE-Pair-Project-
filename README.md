
title: The ASE Pair Project (MSRA)
==========================

Word frequency statistics of English words in text, including letters, single words, phrases, verb phrases, etc
## Usage:

Optional arguments:

	-h, --help            show this help message and exit
	-f, --wordFre         Output word frequencies
  	-c, --charaFre        Output character frequencies
  	-p PHRASENUM, --phraseNum PHRASENUM  Output phrase frequencies.
  	-q PRELIST, --preList PRELIST Count VERB-PREPOSITION pair occurrences.<prepostition-list> is the path to the list of prepositions
 	-v VERBDICT, --verbDict VERBDICT This is an verb-dict
 	-n TOPNUM, --topNum TOPNUM  Output only the top items
  	-x STOPWORD, --stopWord STOPWORD  Use <stop-words> as a list of stop words, which are ignored in the counting.
  	-d, --dirFlag         Treat as the path to a directory and operate on each file inside the directory.
  	-s, --subDirFlag      Recurse into sub-directories. Must be used with -d.
Toggle current directory to```..\WFCount\dist```, you'll see ```WF.exe```, We can run ```WF.exe``` using the command-line arguments above.
##Example:
Taking an example of  counting the frequency of the 26 letters in the ```gone_with_the_wind.txt``` and outputing the 10 with the highest frequency

current directory:


```F:\ASE\WFCount\dist>```

input:

```F:\ASE\WFCount\dist> WF.exe -c -n 10  gone_with_the_wind.txt ```

output:
	
	File: F:\ASE\WFCount\dist\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|character|Frequency|
	|e        |12.70%   |
	|t        |8.96%    |
	|a        |8.16%    |
	|o        |7.30%    |
	|n        |6.94%    |
	|h        |6.81%    |
	|s        |6.32%    |
	|i        |6.08%    |
	|r        |5.89%    |
	|d        |4.82%    |
	-------------------
	Time Consuming:0.186575


  The result will output the absolute path of the statistics file, the statistical results and the time it takes to process the text.
##Design
###step_0 Outputs the frequency of the 26 letters in an English text file
We use python to process the file and output the frequency of letters in an English text file， arranged from high to low, and shows the percentage of letters appearing, accurate to two decimal places.
If two letters appear at the same frequency, they are arranged in lexicographic order. If both c and b occur at a frequency of 1.2%, then b is to be placed in front of c.
####usage
The command line arguments are:

```WF.exe -c <file name>```

output is:

	File: x/xxx/xx/file name
	-------------------
	|   The Rank List   |
	|character|Frequency|
	|e        |12.70%   |
	|t        |8.96%    |
	|a        |8.16%    |
	|o        |7.30%    |
	|n        |6.94%    |
	|h        |6.81%    |
	|s        |6.32%    |
	|i        |6.08%    |
	|r        |5.89%    |
	|d        |4.82%    |
	|l        |4.44%    |
	|u        |2.80%    |
	|w        |2.59%    |
	|m        |2.45%    |
	|y        |2.21%    |
	|g        |2.20%    |
	|c        |2.16%    |
	|f        |1.99%    |
	|b        |1.55%    |
	|p        |1.42%    |
	|k        |1.03%    |
	|v        |0.85%    |
	|j        |0.11%    |
	|x        |0.10%    |
	|q        |0.07%    |
	|z        |0.06%    |
	-------------------
	Time Consuming: xx.xxxxs
###step_1 Outputs the frequency of the 26 letters in an English text file
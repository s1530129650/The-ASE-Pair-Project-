
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

## Example:

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

## Design

### step_0 Outputs the frequency of the 26 letters in an English text file

We use python to process the file and output the frequency of letters in an English text file， arranged from high to low, and shows the percentage of letters appearing, accurate to two decimal places.
If two letters appear at the same frequency, they are arranged in lexicographic order. If both c and b occur at a frequency of 1.2%, then b is to be placed in front of c.

#### usage

function: Outputs the frequency of the 26 letters in ```<file name>```,arranged from high to low.

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

### step_1 Outputs the frequency of the 26 letters in an English text file

Role: A console program for counting the frequency of occurrences of English words in text files

Word: A string of English letters and alphanumeric characters that begins with an English letter and is treated as a word. Words are separated by a separator and are not case sensitive. At the time of output, all words are represented in lowercase characters.

##### Note that:

English alphabet: A-Z, a-z

Alphanumeric symbols: A-Z, a-z, 0-9

Splitter: space, non-alphanumeric symbol Example: good123 is a word, 123good,g001d23 are not words. Good, Good and GOOD are the same word.

#### usage

##### function 1:
  
All non-duplicated words in the output file are sorted by the number of occurrences from more to less, and the same number of occurrences are sorted by dictionary order.

The command line arguments are:

```wf.exe -f <file>  ```

output is:

	File: X\XX\XXX\<file>
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:XX.XXXX s
By default we list the 10 most frequently occurring words.	

##### function 2:

Specify the absolute path or relative path of the file directory and execute ```WF.exe -f <file> ```on each file in the directory. 

The command line arguments are:

```wf.exe -f -d <directory>  ```

output is:

	File: F:\ASE\WFCount\examples\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:0.347612
	File: F:\ASE\WFCount\examples\The Count of Monte Cristo - Alexandre Dumas père.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |5.44%       |
	|to          |2.61%       |
	|and         |2.55%       |
	|of          |2.52%       |
	|a           |1.87%       |
	|i           |1.78%       |
	|you         |1.72%       |
	|he          |1.42%       |
	|in          |1.32%       |
	|that        |1.13%       |
	--------------------------
	Time Consuming:0.378781
	File: F:\ASE\WFCount\examples\The Old Man and the Sea.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |8.62%    |
	|and      |4.69%    |
	|he       |4.34%    |
	|of       |2.03%    |
	|i        |1.89%    |
	|it       |1.84%    |
	|to       |1.70%    |
	|his      |1.66%    |
	|was      |1.62%    |
	|a        |1.48%    |
	-------------------
	Time Consuming:0.033807
Note: The above is a concrete example, because the file structure is different, the results will be different. By default we list the 10 most frequently occurring words.	

##### function 3:

After specifying the file directory, recursively traverse all subdirectories under the directory and perform ```WF.exe -f <file> ```on each file in the directory and its subdirectories.

The command line arguments are:

```wf.exe -f -d -s <directory>  ```

output is:

	File: F:\ASE\WFCount\examples\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	|her      |1.96%    |
	|a        |1.81%    |
	|in       |1.42%    |
	|was      |1.41%    |
	|i        |1.27%    |
	-------------------
	Time Consuming:0.294308
	File: F:\ASE\WFCount\examples\The Count of Monte Cristo - Alexandre Dumas père.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |5.44%       |
	|to          |2.61%       |
	|and         |2.55%       |
	|of          |2.52%       |
	|a           |1.87%       |
	|i           |1.78%       |
	|you         |1.72%       |
	|he          |1.42%       |
	|in          |1.32%       |
	|that        |1.13%       |
	--------------------------
	Time Consuming:0.324616
	File: F:\ASE\WFCount\examples\The Old Man and the Sea.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |8.62%    |
	|and      |4.69%    |
	|he       |4.34%    |
	|of       |2.03%    |
	|i        |1.89%    |
	|it       |1.84%    |
	|to       |1.70%    |
	|his      |1.66%    |
	|was      |1.62%    |
	|a        |1.48%    |
	-------------------
	Time Consuming:0.024594
	File: F:\ASE\WFCount\examples\sub_dir\The Odyssey - Homer.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.45%    |
	|and      |4.08%    |
	|to       |2.54%    |
	|of       |2.46%    |
	|i        |1.55%    |
	|you      |1.54%    |
	|he       |1.48%    |
	|a        |1.46%    |
	|in       |1.30%    |
	|for      |1.05%    |
	-------------------
	Time Consuming:0.098900
	File: F:\ASE\WFCount\examples\sub_dir\subsubdir\Jane Eyre(简·爱).txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.06%    |
	|i        |3.75%    |
	|and      |3.43%    |
	|to       |2.70%    |
	|a        |2.31%    |
	|of       |2.26%    |
	|you      |1.55%    |
	|in       |1.43%    |
	|was      |1.31%    |
	|it       |1.25%    |
	-------------------
	Time Consuming:0.147855
	File: F:\ASE\WFCount\examples\sub_dir\subsubdir\The Further Adventures of Robinson Crusoe - Daniel Defoe.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|the         |4.41%       |
	|and         |3.95%       |
	|to          |3.32%       |
	|of          |2.60%       |
	|i           |1.89%       |
	|they        |1.67%       |
	|a           |1.66%       |
	|that        |1.57%       |
	|in          |1.54%       |
	|was         |1.26%       |
	--------------------------
	Time Consuming:0.078827
Note: The above is also a concrete example, because the files in our directory are different, the results will be different. By default we list the 10 most frequently occurring words.
	
##### function 4:

Supports the -n parameter, which outputs the first n words with the most occurrences.

For example, -n 5 is the top 5of the most frequently occurring words. When there is no specified quantity, we list the 10 most frequently occurring words by default.

The command line arguments are:

```wf.exe -f -n  <directory>  ```

output is:

	File: F:\ASE\WFCount\dist\gone_with_the_wind.txt
	-------------------
	|   The Rank List   |
	|words    |Frequency|
	|the      |4.53%    |
	|and      |3.75%    |
	|to       |2.36%    |
	|of       |2.03%    |
	|she      |1.99%    |
	-------------------
	Time Consuming:0.448502

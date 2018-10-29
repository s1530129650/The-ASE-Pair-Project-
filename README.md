
Title: The ASE Pair Project (MSRA)
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

```wf.exe  -n  <top-n>  ```

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

### step_2 Use "stop-words"

We see from the results of the step_1 that in a novel, the words with the highest frequency are generally "the", "and", "to", "of", "a", these words, we don't feel interest. We can make a stop word file (stop word table), skip these words when counting vocabulary. We call this file ```"stopwords.txt"``` file.

#### usage

function: Use <stop-words> as a list of stop words, which are ignored in the counting.

The command line arguments are:

``` WF.exe -x <stopwordfile>   ```

For example：

```stopword.txt``` is:

	the
	and
	to
	of
	a
	she
	her
<file> is gone_with_the_wind.txt

command line is:

```WF.exe -f -x ../stopwords.txt ../gone_with_the_wind.txt```

output is:

	File: F:\ASE\WFCount\gone_with_the_wind.txt
	--------------------------
	|      The Rank List      |
	|words       |Frequency   |
	|in          |1.42%       |
	|was         |1.41%       |
	|i           |1.27%       |
	|you         |1.24%       |
	|he          |1.16%       |
	|that        |1.08%       |
	|had         |1.06%       |
	|it          |1.06%       |
	|s           |0.89%       |
	|with        |0.78%       |
	--------------------------
	Time Consuming:0.300346
As you can see, the words in ```stopwords.txt ``` are ignored during statistics.

### step_3 Count the frequency of frequently used phrases

First define the phrase: "two or more English words, separated by spaces only." See the example below:

	Hello world //this is a phrase
	Hello, world //this is not a phrase

#### usage

function: Count the frequency of occurrence of commonly used ```number-word ``` phrases

The command line arguments are:

``` WF.exe -p <number>   ```

For examle: number = 3

output is:

	File: F:\ASE\WFCount\ <file>
	-------------------------------------------------------------------------------------------
	|                                    The Rank List                                    |
	|Phrases                                   |Frequency                                 |
	|she did not                               |0.07%                                     |
	|she could not                             |0.05%                                     |
	|there was a                               |0.05%                                     |
	|out of the                                |0.04%                                     |
	|for a moment                              |0.04%                                     |
	|there was no                              |0.03%                                     |
	|it was a                                  |0.03%                                     |
	|she had been                              |0.03%                                     |
	|the first time                            |0.03%                                     |
	|it would be                               |0.03%                                     |
	-------------------------------------------------------------------------------------------
	Time Consuming:1.711970
This step is also Support  ```-x  stopwords, -d <directory>    and -s <subdirectory>  ```

The command line arguments are:

``` WF.exe -f  -p <number> -x <stopwordfile>  <file> ```
 
``` WF.exe -f  -p <number> -d <directory>```

``` WF.exe -f  -p <number> -d -s  <directory> ```
 etc

### step_4 Unified verb form in counting

We want to find commonly used words and phrases, but find that English verbs often change in time and voice, leading to the same word, but the same phrase is considered different.
Thus,unify the verb form firstly, then count.

Suppose we have a text file in which each line of the file is constructed like this:

Verb prototype ```->``` verb variant 1 verb variant 2...

Words are separated by ```->```.

For example:

	abandon -> abandons,abandoning,abandoned
	abase -> abases,abasing,abased
	abate -> abates,abating,abated
	abbreviate -> abbreviates,abbreviating,abbreviated
	hawk -> hawks,hawking,hawked
	hazard -> hazards,hazarding,hazarded
	head -> heads,heading,headed
	implant -> implants,implanting,implanted
	implement -> implements,implementing,implemented
	implicate -> implicates,implicating,implicated
	implore -> implores,imploring,implored


#### usage

function: There is an option -v that categorizes the various variants of the verb as its prototype.

The command line arguments are:

``` 　WF.exe -v <verb file>   ```

For example:

```WF.exe -f -v ../verbs.txt  ../gone_with_the_wind.txt```

output is:

	File: F:\ASE\WFCount\gone_with_the_wind.txt
	--------------------------------
	|         The Rank List         |
	|words          |Frequency      |
	|be             |10.72%         |
	|have           |5.73%          |
	|do             |1.97%          |
	|say            |1.58%          |
	|go             |1.48%          |
	|know           |1.33%          |
	|think          |1.17%          |
	|come           |1.03%          |
	|like           |0.90%          |
	|see            |0.88%          |
	--------------------------------
	Time Consuming:0.528598
#### Step 5 (OPTIONAL): Counting "Verb Phrases" (v-siyual)

We'll count only "Verb Phrases", the definition of which is as follows:
```
VerbPhrase := Verb + Spaces + Preposition
Spaces := Space+
Space := ' ' | '\t' | '\r' | '\n'
Preposition := <any one from the list of prepositions>
Verb := <any one in any tense FROM THE DICTIONARY>
```
Read the two sections above to get the list of prepositions and the verb dictionary.
THIS FEATURE IS OPTIONAL.

#### usage

function: counting verb phrases.

The command line arguments are:

``` 　WF.exe -q <preposition-list> -v <verb-dict>  ```

For example:

```WF.exe -q ../prepositions.txt  -v ../verbs.txt  ../gone_with_the_wind.txt```

output is:

	File: F:\ASE\WFCount\gone_with_the_wind.txt
	----------------------------------------------------
	|                  The Rank List                  |
	|VerbPre                 |Frequency               |
	|go to                   |0.45%                   |
	|want to                 |0.27%                   |
	|be in                   |0.25%                   |
	|think of                |0.23%                   |
	|try to                  |0.23%                   |
	|have to                 |0.23%                   |
	|look at                 |0.17%                   |
	|come to                 |0.16%                   |
	|back to                 |0.11%                   |
	|be as                   |0.11%                   |
	----------------------------------------------------
	Time Consuming:1.293661
## Disclaimer 

This content is a lot of blog from xzou.

This task is the nature of the homework, there is still incomplete please forgive us.
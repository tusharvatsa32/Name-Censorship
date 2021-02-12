
## Project Description
 
It has come to the Party’s attention that one particularly suspect media outlet, the New York Times, has made several references to people who ‘do not exist’. Your job is to wipe out the old, incorrect names and anonymize them, replacing them with the Ministry’s preferred name, John Smith . There are far too many documents for the number of employees in the Ministry of Truth to manually comb over and make the relevant adjustments. The Ministry would like to write a program to do this automatically.
 
The rule of thumb is that an instance of a full name always consists of two words, separated only by some whitespace. Each word must be properly capitalized (first letter of each word should be capitalized, the rest should be lower caps) for it to be a full name. Similarly, an instance of a last name is always a single word that is properly capitalized.


## Constraints:
The solution should preserve the original whitespace in the input source, if any. Do not add, remove, or replace any whitespace.
The implementation will be tested against inputs that contain common punctuation. The NYT data set contains numerous examples of replacement contexts containing punctuation. You can use those examples to test your implementation.


## Library Used:
Regex(I now have a good working knowledge of Regex)

## What worked out?
I tried a lot of combinations of patterns. But some way or the other I was missing out on edge test cases. For example: If a banned last name is **'Woods'** and the document has **-Woods** or **Woods-** it should not be replaced.But if it is **{Woods}** it should be replaced. Initially I thought using **\bword\b** will work out. But usually when there is a hyphen the name is not considered independent. In this case, **lookforward**, **lookbehind** and **backreferencing** helped a lot.
You can check out how I solved it in clean method in cleaner.py. **Read about Non-Capturing groups and backreferencing**

## Challenges:
1.The file may have many instances of banned names where the first name and last name is separated by variable number of whitespaces/tabs. In that case, I initially tried to use three different patterns where the lookforward matches the variable number of spaces and doesn't capture it. something like this **{fname}(?=\s+{lname})** This helped me capture the pattern where first name is followed by multiple spaces and then a last name and we can use **re.sub** to replace the instance of the first name. Then I used another pattern **(?<={fname}\s+){lname}** to replace the last names in the instance of full names. But here is the catch, **you can not use a variable length of string inside lookbehind.** So, in the documents where I had multiple spaces between first name and last name in instances of last name, it didn't work out.
2.I tried capturing the number of spaces between first name and last name by making a helper function but it failed many of the test cases. In this case the memory consumtion also increases because you have to capture the space between the first name and last name, space between previous word and first name and also between the last name and the next word.
3.I finally used backreferencing which helped me to return the number of spaces directly. I grouped the raw pattern in such a way that spaces were inside a () and used backreferencing to add that many spaces while replacing. In this way the entire banned full name was replaced with an entire replacement name and it was fast!!!

## File Descriptions:
The cleaner.py contain the entire code.
The names.txt contain the names which are banned by the ministry.
The Input.txt is a custom document to check how well it performs.
The output.rtf is the desired output for the custom input.

# Name-Censorship
 It has come to the Party’s attention that one particularly suspect media outlet, the New York Times, has made several references to people who ‘do not exist’. Your job is to wipe out the old, incorrect names and anonymize them, replacing them with the Ministry’s preferred name, John Smith . There are far too many documents for the number of employees in the Ministry of Truth to manually comb over and make the relevant adjustments. The Ministry would like to write a program to do this automatically.
 
The rule of thumb is that an instance of a full name always consists of two words, separated only by some whitespace. Each word must be properly capitalized (first letter of each word should be capitalized, the rest should be lower caps) for it to be a full name. Similarly, an instance of a last name is always a single word that is properly capitalized.

Constraints:
The solution should preserve the original whitespace in the input source, if any. Do not add, remove, or replace any whitespace.
The implementation will be tested against inputs that contain common punctuation. The NYT data set contains numerous examples of replacement contexts containing punctuation. You can use those examples to test your implementation.

# StageLI
This repertory give access to codes and documentations created for LI Internship of Beyza Tasdelen supervised by Juliette Millet.

This repertory gives access to two folders: codes and datas.

#Data file contains 2 other major folders: Cleaned data et non-cleaned data. 

#Non-cleaned data: 
contains an edited version of 'french_1s_accross' file, we cleaned string byte symbloes and transformed them to their original API symbols.

'English_all_phones' and 'french_all_phones' files contains all contrasts before the cleaning of unusual and foreign symbols. 

Phone pair files contains contrast couples for both language before the cleaning.

'Contrast_speaker' files contains contrast couples for each couple of speaker before the cleaning of problematic symbols and speakers for both language. And contrast speaker quantity files contains number of speaker for each contrast pair before cleaning.

#Cleaned data:

#Across and Item files
Main files used for each operations are 'english_1s_across_cleaned' and 'french_1s_across_cleaned' files. These files are cleaned from problematic phones and speakers with 'eliminate' function in Codes file. A second cleaning is done for certain phonemic groups as glides, nasals and approximants as 'l' and 'r' in both languages. The results of this cleaning are saved in '...-second' files for both .item and across files.
---

In english datas there were only speaker section to be cleaned because there was no problematic phones. So after the cleaning we have two files 'contrast_speaker_eng_cleaned' whic contains contrast pairs and their speaker pairs. And then there is 'contrast_speaker_quantity_eng_cleaned' whic contains number of speaker for each contast couple.

But in french we did first, a phonemic cleaning then a speaker cleaning. So we have two results for each cleaning. These results are collected in 'contrast_'context_fr_cleaned-first' and 'contrast_speaker_quantity_fr-first' after the cleanong of problematic phones. Then we did a second cleaning with speakers and the results are saved in 'context_fr_cleaned-fsecond' and 'contrast_speaker_quantity_fr-second' files.

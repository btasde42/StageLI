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

#Across and Item files:
Main files used for each operations are 'english_1s_across_cleaned' and 'french_1s_across_cleaned' files. These files are cleaned from problematic phones and speakers with 'eliminate' function in Codes file. A second cleaning is done for certain phonemic groups as glides, nasals and approximants as 'l' and 'r' in both languages. The results of this cleaning are saved in '...-second' files for both .item and across files.

#Speaker Cleaned Data and Bizarre Phones Cleaned Data:

In english datas there were only speaker section to be cleaned because there was no problematic phones. So after the cleaning we have two files 'contrast_speaker_eng_cleaned' whic contains contrast pairs and their speaker pairs. And then there is 'contrast_speaker_quantity_eng_cleaned' whic contains number of speaker for each contast couple.

But in french we did first, a phonemic cleaning then a speaker cleaning. So we have two results for each cleaning. These results are collected in 'contrast_'context_fr_cleaned-first' and 'contrast_speaker_quantity_fr-first' after the cleanong of problematic phones. Then we did a second cleaning with speakers and the results are saved in 'context_fr_cleaned-fsecond' and 'contrast_speaker_quantity_fr-second' files.

#Context phones cleaned Data:
In this file we have recleaned files by their context phones. contrats-context..-contx.csv contains the results of a second cleaning for certain phonemic groups as glides, nasals and approximants as 'l' and 'r' in both languages. Min_3_contrasts....csv files contains the contrast pairs which have at least 3 common context with their simetric pair.

And this file gives access to another file "Maximum Common Context":

Min_3_contrast_context files for both englsh and french contains contrast pairs whith at leash 3 context pair which has an mirror option. All the context possiblities with reverse duplicate are presented as lists.

All_most_common_context files for both english and french repsents contexts which are most common between all contrast pairs. For each contrast pairs there are at least 3 contexts respresented in the list.

And this file gives access to another file which name is "Final max 4 solution contexts":

In this file we have 4_context_for_each files for english and french. This documents contains 3 or 4 context for each contrast pairs. These are the final contexts to be used int the experiment part.


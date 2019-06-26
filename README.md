# StageLI
This repertory give access to codes and documentations created for LI Internship of Beyza Tasdelen supervised by Juliette Millet.

This repertory gives access to two folders: codes and datas.

-----------------------------------------------------------------------------------------------

#Data file contains 2 other major folders: Cleaned data et non-cleaned data. 

#Non-cleaned data: 
contains an edited version of 'french_1s_accross' file, we cleaned string byte symbloes and transformed them to their original API symbols.

'English_all_phones' and 'french_all_phones' files contains all contrasts before the cleaning of unusual and foreign symbols. 

Phone pair files contains contrast couples for both language before the cleaning.

'Contrast_speaker' files contains contrast couples for each couple of speaker before the cleaning of problematic symbols and speakers for both language. And contrast speaker quantity files contains number of speaker for each contrast pair before cleaning.

#Cleaned data:

#Across and Item files:
Main files used for each operations are 'english_1s_across_cleaned' and 'french_1s_across_cleaned' files. These files are cleaned from problematic phones and speakers with 'eliminate' function in Codes file. A second cleaning is done for certain phonemic groups as glides, nasals and approximants as 'l' and 'r' in both languages. The results of this cleaning are saved in '...-second' files for both .item and across files.

--> TARGET CONTEXT FILES: This file gives access to item files which contains choosen target context's .item files.Each file contains an index number for every line. This index number serves as an reference for index files. There are two files for 4 english possibilities and 4 french possibilities.

#Index Information of choosen contrasts:
This file contains for both english and french index information files which gives access to .item files. In the files you can find target phone, other phone, contexts, speaker AB, speaker X, index target, index other and index X informations.

#Speaker Cleaned Data and Bizarre Phones Cleaned Data:

In english datas there were only speaker section to be cleaned because there was no problematic phones. So after the cleaning we have two files 'contrast_speaker_eng_cleaned' whic contains contrast pairs and their speaker pairs. And then there is 'contrast_speaker_quantity_eng_cleaned' whic contains number of speaker for each contast couple.

But in french we did first, a phonemic cleaning then a speaker cleaning. So we have two results for each cleaning. These results are collected in 'contrast_'context_fr_cleaned-first' and 'contrast_speaker_quantity_fr-first' after the cleanong of problematic phones. Then we did a second cleaning with speakers and the results are saved in 'context_fr_cleaned-fsecond' and 'contrast_speaker_quantity_fr-second' files.

#Context phones cleaned Data:
In this file we have recleaned files by their context phones. contrats-context..-contx.csv contains the results of a second cleaning for certain phonemic groups as glides, nasals and approximants as 'l' and 'r' in both languages. Min_3_contrasts....csv files contains the contrast pairs which have at least 3 common context with their simetric pair.

And this file gives access to another file "Maximum Common Context":

Min_3_contrast_context files for both englsh and french contains contrast pairs whith at leash 3 context pair which has an mirror option. All the context possiblities with reverse duplicate are presented as lists.

All_most_common_context files for both english and french repsents contexts which are most common between all contrast pairs. For each contrast pairs there are at least 3 contexts respresented in 4 list of possibilities.

And this file gives access to another file which name is "Final max 4 solution contexts":

In this file we have 3_context_each files for english and french. This documents contains 3 context for each contrast pairs. There are four file for four possibilities. These are the final contexts to be used int the experiment part.

-----------------------------------------------------------------------------------------------

#Codes:

***Test protocole*** 

It's an test function for wav files to find out if they are correctly annotated or not.
For being able to start protocole you need .item file with choosen AB couples. You can find this file for both english and french in Data-->Cleaned Data-->Across and Item files-->Target Context Files. 
There are four possibilities and they identity is specified by the number in the and. For exemple 1s_english_target_contexts1.item is the first possibility.

Then you need a reference index csv file. You can find this file for both english and french in
Data-->Cleaned Data-->Index Information of choosen contrasts
These files are too ennumerated by 1 to 4. You should choose the same identity number for those two files. For exemple if you choosed 1s_english_target_contexts1.item, you should also choose eng_target_context_index1.csv

Then you should place this two files, protocole_controle.py and wav_util.py files in the same folder woth your .wav files.

Then you can start the protocole by typing: python3 protocole_controle.py 'exemple1.csv' 'exemple1.item'

In the end of controle procedure you will have 3 files: "phones_OK.csv" for correct annotations, "phones_nope.csv" for totally wrong annotations, "phones_non_aligned.csv" for non aligned sound annotations.

If you want to quit you can press 0 in the end of every phone representation. If you don't quit by following this method your three return files will not be saved.

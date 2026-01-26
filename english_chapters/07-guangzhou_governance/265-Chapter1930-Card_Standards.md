# Chapter 1930 - Card Standards

Since becoming the State Secretary of the "most powerful Administration Council since D-Day," Ma Qianzhu had lost quite a bit more hair. His schedule was calculated in minutes. Squeezing out two hours to attend a meeting was considered a great "grace." Feng Nuo knew he had completely "scratched the itch."

To fully explain his concept and plan, although conditions didn't permit him to make glass slide PPT presentations, he specially produced an "Outline" and "Materials." The former was for the leader to grasp the main points; the latter provided details for the leader to read carefully if interested.

As for other participants, they were all experts. Providing a simple technical description was sufficient.

The meeting was held in the Administration Council conference room. Feng Nuo first introduced his technical approach and various technical solutions currently under discussion, then entered the main topic.

"Why use punched cards? Actually, it's very clear: to solve the three major difficulties in data processing. First, too many document sizes and shapes. Second, too many transactions recorded on a single document. Third, too many forms and methods of recording data. In other words, the problem of standardization."

Feng Nuo paused for a moment to calm his nervous emotions, feeling his pitch was a bit high. He hadn't expected Yang Yun to actually mention this punched card computer system—which hadn't even started—in the report, and actually land the big fish, the Governor himself. Feng Nuo knew too well the importance of a leader's visit to a cause. It wasn't just a matter of showing one's face before the leader. Even if the leader listened without saying a word and left, it would have a very important promoting effect on the future of this project—same logic as asking a leader for an inscription when doing business in the past. This opportunity must be seized.

The project initiation seminar for the punched card computer had been held once, basically determining the participants and rough plan. This meeting was mainly a discussion on the "punched card" itself. Because the punched card computer differed from the hand-cranked calculator, the data carrier—the specifications and various standards of the punched card—had to be determined first before mechanical design could proceed. The Senate had no physical object to imitate and could only reverse engineer based on information and the cards themselves. So the first task for the project was to determine the punched card standard.

Feng Nuo naturally strove to secure responsibility for this part. He had done extensive research and was the representative of the Planning Commission, while those Elders in mechanics and electricity weren't particularly interested in this matter.

"Therefore, we must determine the punched card specifications from the beginning, unifying them at least in all civil applications. There are 45-column, 80-column, and 90-column types of punched cards, but the most common—also used in the earliest 1890 US census—is the 'Hollerith' punched card, later commonly known as the 'IBM card.' This card is made of durable card stock, printed with 10 rows × 80 columns of numbers, with numbers in each row being 0-9. In addition, there are two rows of punching positions, 11 and 12, on the card, but without printed marks. Row 11 is also called Row X, and Row 12 is also called Row Y. Their positions are actually located above the number rows. These two rows, plus Row 0, are collectively called the 'Zone Rows' or 'High Zone.'"

"The period of domestic application of punched cards in the past was relatively short, and the industries were relatively limited. Therefore, the standard for punched cards completely copies the IBM card standard. Its manufacturing standards are as follows: rectangular card with a corner cut, horizontal direction as the long edge, length 187.32 mm, error not exceeding 0.12 mm; vertical direction as the short edge, length 82.55 mm, error not exceeding 0.18 mm; thickness 0.175 mm, error not exceeding 0.005 mm. Paper fiber direction should be horizontal. Straightness tolerance of each edge is 0.08 mm, parallelism tolerance of corresponding edges is 0.08 mm, perpendicularity tolerance of adjacent edges not exceeding 5 minutes, corner cut angle 60 degrees. Please check the materials distributed to you."

"Then the punching specifications. Card reference line X, i.e., the horizontal reference line, is the upper edge line of the card. The card reference point is a point on the right edge 41.27 mm from reference line X. Card reference line Y is the line passing through the reference point and perpendicular to reference line X. The 80 lines parallel to reference line Y on the card are called the 'columns' of the card, with column spacing of 2.21 mm. The 12 lines parallel to reference line X on the card are called the 'rows' of the card, with row spacing of 6.35 mm. Punch shape is rectangular, hole center located at the intersection of row and column, long edge parallel to Y, short edge parallel to X, dimensions long edge 3.2 mm, short edge 1.4 mm, error not exceeding 0.05 mm. Minimum edge distance between code holes on the same horizontal row should be greater than 0.51 mm, error between hole center line and row/column standard line less than 0.25 mm."

Currently, the venue was silent. Participants were probably wondering whether they could build equipment to read and punch such precise cards. Feng Nuo, however, was thinking that he had forgotten to invite people from the paper mill to participate in the discussion. Whether paper meeting the specifications could be produced right now was highly doubtful. Climbing the tech tree, every step was a pit, a myriad of loose ends. But he was prepared and continued:

"This is the punched card standard released domestically in the late seventies. Its manufacturing precision was naturally established to meet the requirement of punched card computer systems processing 1,000 to 2,000 cards per minute at that time. We currently don't have early card standards for punched card computer systems, but it is certain that early 20th-century technology couldn't reach such precision standards. In fact, in a fifties document, the card dimensions were simply introduced as 18.6 cm × 8.3 cm. Therefore, punched card precision and error standards suitable for our self-made equipment remain to be further explored during development."

"Each column of the punched card can be used to record one character, including numbers from 0 to 9, 26 English letters, and several symbols like equal signs, percent signs, etc. Each column records one character; the entire card can record 80 characters."

"Characters are realized by punching. If a column is to express a number, punch directly in the corresponding row from 0 to 9. If a column is to express an English letter, simultaneous punching in the High Zone and Number Zone is required. Usually, the value of that column is printed at the top for reference. Please turn to Appendix 2 of the materials for the specific scheme."

Each column of the punched card represents 1 English letter, the scheme being:
12-1 A, 11-1 J, 0-1 /
12-2 B, 11-2 K, 0-2 S
12-3 C, 11-3 L, 0-3 T
12-4 D, 11-4 M, 0-4 U
12-5 E, 11-5 N, 0-5 V
12-6 F, 11-6 O, 0-6 W
12-7 G, 11-7 P, 0-7 X
12-8 H, 11-8 Q, 0-8 Y
12-9 I, 11-9 R, 0-9 Z

"Punching in the Zone Rows, paired with number rows 1-9, gives 3x9=27 schemes. Excluding the 0-1 position representing the special symbol 'slash,' it exactly represents 26 letters. Interestingly, the reason 0-1 represents a slash is that in the entire scheme, only this encoding has the two holes closest together, making technical implementation more difficult. In addition, other special symbols can be solved with several schemes punching 3 holes per column. The Hollerith code only used hole 8 as a pairing hole, but this also reveals that 3-hole coding is technically possible."

"The reason for mentioning 3-hole coding is considering the problem of Chinese character encoding."

At this moment, quite a few whispers appeared in the venue. Chinese encoding was a major problem for the Senate's application of punched cards. Back then, punched card computers weren't produced domestically, and their use wasn't widespread, so there was actually no standard Chinese encoding method.

Compared to data storage carriers known to Elders, the capacity of punched cards was pitifully small. Each 18.7x8.3 card could only store 80 characters, and only English letters at that. If it were government or business processing, it would be fine; at worst, use more standard numbers. For example, the National Standard Code system pushed by Si Kaide and Hong Huangnan a few years ago finally had a place to be used.

Just for the current census needs, fields like gender, native place, birthplace, birth time, current residence, education level, family background, etc., could actually be easily solved through coding. In the past, the 18-digit ID card used only 6 digits to indicate everyone's birthplace nationwide. The reason was simple: many people hit each code, so compiling a code table was appropriate. Anyone who learned databases would easily discover from drawing an ER diagram that it should be done this way. But there was one field, the name, that could never bypass the Chinese encoding problem. The specific design work of census form fields could be thrown to people from the Ministry of Civil Affairs, but this Chinese encoding must be solved now.

"Actually, the Chinese encoding problem isn't hard to solve; the problem is it takes up too much space."

"The 'Code of Chinese Graphic Character Set for Information Interchange,' commonly known as GB2312 encoding, promulgated in 1980, not only stipulated the representation method of Chinese characters on computers but actually also defined a method using 4-digit decimal numbers to represent Chinese characters, which is the Quweima (Zone-Bit Code). Quweima includes 3755 Level 1 Chinese characters, 3008 Level 2 Chinese characters, and 682 symbols, basically meeting current needs. So the simplest Chinese coding method is to encode one Chinese character every 4 columns. Everyone filled in their names during the college entrance exam in the past; what was used then was Quweima."

"Currently, the Ministry of Post and Telecommunications has basically completed laying the telegraph system across the island, and several batches of telegraph operators have been trained. I think it might be more convenient to directly use our standard Chinese telegraph code? Manpower can also be interchangeable." At this time, Shao Zong, who hadn't spoken much, opened his mouth.

"Quweima is sorted by Pinyin within each level of characters, so it doesn't need much training. Standard telegraph code, on the contrary, is sorted by radicals, which is actually much harder to master than Quweima."

"Standard telegraph code had prototypes from the end of the 19th century, compiled directly since the Qing Dynasty; it's the natural choice for Chinese character encoding at this stage."

"Is speaking easier or writing easier? Standard telegraph code starting from character shape is because those who used telegraphs initially were the scholar class. Our national universal education starts from Pinyin, actually already overturning the past system. Ordinary people naturally use Quweima more conveniently."

"American passports used standard telegraph code all along back then."

**(End of Chapter)**

# Chapter 1947 - Card Duplication

Feng Nuo subsequently adjusted the tabulating machine's data processing mode.

Previously, the tabulating machine had been designed to read punch cards column by column. Under this paradigm, even if reading each column consumed merely 0.1 seconds, reading all eighty columns would require eight seconds—excluding card transport time entirely. After careful deliberation, Feng Nuo concluded that in practical applications, not every punch card column actually demanded tallying or summation.

Consider payroll statistics as an example. A punch card couldn't possibly contain wage data exclusively. Conversely, most columns would store workers' names, genders, departments, job classifications, employee numbers, and similar information. Statistical operations on name character codes, department codes, job classification codes, or employee numbers served no purpose.

Therefore, under current constraints, performing statistics on a single data item at a time sufficed. Even if a particular data item spanned multiple digits across several punch card columns, processing one digit at a time proved feasible—after all, statistical results would ultimately require manual summation anyway.

This approach meant the tabulating machine need only read and accumulate a single column of digits when processing each card, naturally accelerating operations considerably while conserving electricity.

Feng Nuo devoted another two days to simplifying and modifying the device, finally stabilizing the tabulating machine's processing capacity beyond 3,000 cards hourly. This should adequately meet the Executive Committee's general statistical computing requirements. The sole shortcoming: if calculated data comprised three digits, the cards would need three machine passes. From a usability perspective, this remained suboptimal. However, Feng Nuo presently focused on validating the technical approach; further refinements would accompany the productization phase.

Having conquered the tabulating machine, most mechanical mechanisms and relay control systems had essentially been developed. Other machine types merely represented design variations—adding, removing, or combining components. In the punch card machine system, the sorting machine—second in importance only to the tabulating machine—simply replaced relays controlling rotating dials and accumulation functions with ones separately controlling multiple card-feeding mechanisms, directing cards punched at different reference column digits into different card pockets.

However, just as he prepared to enthusiastically tackle the sorting machine in one continuous effort, a fresh problem materialized.

Card quality deficiencies had caused severe damage to the delivered card materials during the past days' intensive tabulating machine testing. Experimental materials would soon be depleted.

Feng Nuo had no alternative but to shelve his eager sorting machine anticipation and develop the duplicating machine first. With a duplicating machine, existing cards could be copied at will, eliminating the card shortage problem.

He retrieved specifications for the old timeline IBM company's IBM 513 reproducing punch, officially designated the "Automatic Reproducing Punch." This model had appeared during the 1940s. The principle wasn't challenging, though the machine's structure proved somewhat complex; Feng Nuo didn't intend exact replication—he merely needed to construct a principle-based prototype.

He sketched a schematic as neatly as possible on paper. The duplicating machine's core component was a linked transmission mechanism capable of holding two card rows. When the template card passed through the processing unit, the reader mechanism's brushes swept across the card, connecting circuits at punched positions to activate corresponding relays, which in turn controlled the new card processing unit's punching mechanism to punch identical-position holes on the new card. This time, reading and punching needed to proceed column by column.

However, Feng Nuo encountered an obstacle when contemplating how to control the punching dies: each punch card column's holes were separated by mere millimeters. Given his relays' size, how could they possibly simultaneously control multiple punch heads? He racked his brain extensively without resolution and had to seek guidance from mechanical engineering transmigrators the following day with his half-developed schematic.

Once again, he sought Sun Li. Upon entering the office, he discovered Zhan Wuya was also present. Feng Nuo had been ensconced in the machinery factory sufficiently long to have grown quite familiar with Zhan Wuya, recognizing him as a straightforward person. Dispensing with formalities, he spread his "blueprint" directly and posed the problem. Zhan Wuya laughed heartily, gesturing toward a nearby Lingao-produced English typewriter: "Go examine how that typewriter manages to print characters from over forty keys all at the identical position!"

Feng Nuo slapped his forehead. Naturally! An English typewriter occupied his own office as well, yet he'd never contemplated this point.

Zhan Wuya continued: "This constitutes the most fundamental problem in mechanical design. Beyond employing the typewriter's curved type-bar structure, numerous alternative solutions exist. Stop futilely contemplating mechanical design yourself—delegate this to professionals like us. You just concentrate on designing your relay control scheme. The Governor inquired about this project's progress just yesterday."

Because Feng Nuo didn't genuinely comprehend mechanical design, the blueprints he submitted to the machinery factory were essentially merely "schematic diagrams." For certain constructions where he could replicate existing designs, he'd transcribed them from previous design drawings, but regarding actual production, the machinery factory's technicians still had to redesign everything.

Feng Nuo hastily reported his progress and chest-thumpingly promised to accelerate development speed, reassuring leadership.

However, the duplicating machine didn't pass testing as smoothly as the tabulating machine had.

The prototype arrived that evening. They first tested duplicating one card, then ten cards. Following manual inspection, no problems surfaced—duplicated new cards matched template cards perfectly. Feng Nuo then instructed Qian Yuzhi and Li Jianai to attempt duplicating 1,000 cards at once.

Since duplication proceeded row by row, the duplicating machine's speed roughly approximated the unoptimized tabulating machine—approximately three hours for 1,000 cards. After issuing instructions, Feng Nuo departed for home. Leadership exhibited considerable concern regarding this project, so Feng Nuo had been working overtime frequently lately. Today, with a task requiring minimal technical expertise, he could leave Qian Yuzhi and the two others to monitor operations.

When duplicating small card quantities, overlapping new and old cards and holding them against light sufficed to verify whether punched holes matched. But for 1,000 cards, manual verification was no longer viable. Therefore, Feng Nuo instructed them to employ the tabulating machine to verify perforation consistency upon duplication completion. The method: separately tally 0-9 digit counts in each column for both stacks and confirm whether results matched. If results proved identical, any error probability could be considered negligible. However, at the tabulating machine's current speed, checking each column consumed approximately twenty minutes, and eighty columns would require over twenty hours—necessitating overnight shift work.

The next morning, Feng Nuo attended a brief Planning Commission meeting and didn't reach the office until nearly noon.

He found Feng Shan leading Qian Yuzhi and Li Jianai in inspecting cards individually against light to verify perforation matches. They'd apparently been engaged for half the day already, all three displaying somewhat glazed expressions. Qian Yuzhi and Li Jianai even sported dark circles beneath their eyes. Feng Nuo found this profoundly strange and hurried over to inquire what was occurring.

It emerged that Qian Yuzhi and Li Jianai had spent the entire night employing the tabulating machine to verify the 1,000 cards' duplication results, only to discover that new and old cards exhibited different 0-9 counts in a certain column—duplicated cards were short one "3" but possessed one extra "4." In other words, the duplicating machine had erred, punching a 3 as a 4 on one card. Now they were searching for precisely which card harbored the problem.

"Commendable work attitude, stupid work method," Feng Nuo commented. He approached and retrieved the two stacks the three hadn't yet examined, asking: "How many have you checked?"

"122."

"114."

"107."

The three answered separately.

"See—three people working all morning have checked merely just over three hundred cards. What if we need to test 10,000 cards in the future—how many people would we require?" As he spoke, he handed the stack to Feng Shan, saying: "Count out 330."

He then asked Qian Yuzhi which column contained the error and adjusted the tabulating machine's reading brush position. He also divided the remaining stack in his own hand into piles of 330 and 327.

Next, Feng Nuo employed the tabulating machine to tally first the 330 new cards Feng Shan had counted out, then his own separated stack of 330 old cards.

Slightly over ten minutes later, tabulation completed, and results matched.

"So, the erroneous card must definitely reside in the other half," Feng Nuo indicated the remaining two card stacks.

He then extracted 160 cards each from the remaining two 327-card stacks and fed them into the tabulating machine. This time results demonstrated that the erroneous card resided among these 160.

Feng Nuo bisected this card batch again, each portion containing 80 corresponding new and old cards, randomly selected one portion, and repeated the above operation.

...

Minutes later, the suspect range had narrowed to 10 cards. Feng Nuo distributed the cards to Feng Shan and the other two, and the erroneous card was swiftly located.

Feng Nuo placed the erroneous card on the table without examining it. Instead, he addressed Feng Shan: "We're constructing computers precisely to replace human labor in performing mechanical calculations. The machine executes mechanical work—you don't have to. What do you need to do then? Contemplate how to drive it to work toward your objective. Tell me—what principle did we just employ to locate the erroneous card?"

"Binary search?" Feng Shan ventured uncertainly.

Feng Nuo nodded. "Not precisely identical, but the reasoning parallels it. If you'd contemplated momentarily why I had Yuzhi and Jianai employ the tabulating machine yesterday to verify whether the two 1,000-card stacks matched, you could have conceived numerous solutions. At bare minimum, you could have processed 100 cards at a time, and in at most 10 passes, you would have identified which 100-card batch contained the error. Naturally, if you'd conceived that, you would have also recognized that binary search is fastest."

"What we executed has a prerequisite—that duplication error probability is exceedingly low. Otherwise, if multiple punch cards all exhibited errors in the identical column, this method wouldn't function. That's why yesterday we first verified 1 and 10 duplication results, and neither presented problems."

"The facts also demonstrate that our estimate matched reality. Out of 1,000 cards—that's 80,000 column-duplication operations—the two of them checked over 30 columns from last night to this morning and actually discovered only 1 column with an error. Moreover, the tally revealed only one fewer 3 and only one more 4. This was something you knew before we commenced searching for the erroneous card, correct? We possessed no other prior knowledge, so we could only assume the duplicating machine's error rate was 1/30,000 and not consider the possibility that the current error resulted from accumulated errors on multiple cards in the same column—because that probability is even lower and can be temporarily disregarded.

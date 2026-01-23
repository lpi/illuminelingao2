# Chapter 1951 - Card Duplication

Feng Nuo then adjusted the tabulating machine's data processing mode.

Previously, the tabulating machine had been designed to read punch cards column by column. Under this mode, even if reading each column took only 0.1 seconds, reading all 80 columns would require 8 seconds—and that didn't even count the time needed for card transport. After careful consideration, Feng Nuo concluded that in practical applications, not every column on a punch card actually needed to be tallied or summed.

Taking payroll statistics as an example, it would be impossible for a punch card to contain only wage-related data. On the contrary, most columns would be used to store workers' names, genders, departments, job types, employee numbers, and other such information. There was no need to run statistical operations on name character codes, department codes, job type codes, or employee numbers.

Therefore, under current conditions, it was sufficient to perform statistics on only one data item at a time. Even if a particular data item consisted of multiple digits spread across several columns on the punch card, processing one digit at a time was feasible—after all, the statistical results would eventually need to be summed manually anyway.

This way, when processing each card, the tabulating machine only needed to read and accumulate a single column of digits, naturally speeding things up considerably while also saving electricity.

Feng Nuo spent another two days simplifying and modifying the device, finally stabilizing the tabulating machine's processing capacity at over 3,000 cards per hour. This should be sufficient to meet the Executive Committee's general statistical computing needs. The only shortcoming was that if the data being calculated had three digits, it would need to pass through the machine three times. From a usability standpoint, this was still not convenient enough. However, Feng Nuo was currently focused on validating the technical approach; further improvements would be made during the productization phase.

Having conquered the tabulating machine, most of the mechanical mechanisms and relay control systems had essentially been developed. Other types of machines were merely variations of the design—adding, removing, or combining components. In the punch card machine system, the sorting machine, second in importance only to the tabulating machine, simply replaced the relays used to control the rotating dials and accumulation functions with ones that separately controlled multiple card-feeding mechanisms, directing cards punched at different digits in the reference column into different card pockets.

However, just as he was rolling up his sleeves, eager to tackle the sorting machine in one fell swoop, a new problem emerged.

Due to card quality issues, the card materials that had been delivered suffered severe damage during the intensive tabulating machine tests over the past few days. Experimental materials would soon be in short supply.

Feng Nuo had no choice but to set aside his eager anticipation for the sorting machine and develop the duplicating machine first. With a duplicating machine, existing cards could be copied at will, and the card shortage problem would cease to exist.

He retrieved the specifications for the old-time IBM company's IBM 513 reproducing punch, officially known as the "Automatic Reproducing Punch." This model appeared in the 1940s. The principle wasn't difficult, but the machine's structure was somewhat complex; Feng Nuo didn't intend to copy it exactly—he just needed to build a prototype based on the principle.

He drew a schematic as neatly as possible on paper. The core component of the duplicating machine was a linked transmission mechanism capable of holding two rows of cards. When the template card passed through the processing unit, the reader mechanism's brushes swept across the card, connecting circuits at punched positions to activate the corresponding relays, which in turn controlled the punching mechanism of the new card processing unit to punch holes at identical positions on the new card. This time, reading and punching needed to proceed column by column.

However, Feng Nuo got stuck when pondering how to control the punching dies: the holes in each column of a punch card were separated by only a few millimeters. Given how large his relays were, how could they possibly simultaneously control multiple punch heads? He racked his brain for a long time without figuring it out and had to take his half-baked schematic to seek guidance from the mechanical engineering transmigrators the next day.

Once again, he went to find Sun Li. Upon entering the office, he discovered that Zhan Wuya was also there. Feng Nuo had been holed up in the machinery factory for so long that he was quite familiar with Zhan Wuya and knew him to be a straightforward person. Without any polite formalities, he spread out his "blueprint" directly and posed the problem. Zhan Wuya laughed heartily, pointing at a Lingao-produced English typewriter nearby, "Go look at how that typewriter manages to print characters from over 40 keys all at the same position!"

Feng Nuo slapped his forehead. Of course! There was an English typewriter in his own office too, but he had never thought about this point.

Zhan Wuya continued, "This is the most basic problem in mechanical design. Besides using the typewriter's curved type-bar structure, there are quite a few other solutions. Stop futilely pondering mechanical design yourself—leave this to professionals like us. You just stick to designing your relay control scheme. The Governor asked about this project's progress just yesterday."

Because Feng Nuo didn't actually understand mechanical design, the blueprints he submitted to the machinery factory were essentially just "schematic diagrams." For certain constructions where he could copy existing designs, he had transcribed them from previous design drawings, but when it came to actual production, the machinery factory's technicians still had to redesign everything.

Feng Nuo hastily reported on his progress and thumped his chest, promising to accelerate the development speed and reassuring the leadership.

However, the duplicating machine didn't pass testing as smoothly as the tabulating machine had.

The prototype arrived in the evening. They first tested duplicating 1 card and then 10 cards. After manual inspection, no problems were found—the duplicated new cards matched the template cards perfectly. Feng Nuo then instructed Qian Yuzhi and Li Jianai to try duplicating 1,000 cards at once.

Since duplication proceeded row by row, the duplicating machine's speed was roughly similar to the unoptimized tabulating machine—about three hours for 1,000 cards. After giving his instructions, Feng Nuo went home. The leadership was very concerned about this project, so Feng Nuo had been working overtime frequently lately. Today, with a task that didn't require much technical expertise, he could leave Qian Yuzhi and the two others to monitor things.

When duplicating a small number of cards, overlapping the new and old cards and holding them up to the light sufficed to check whether the punched holes matched. But for 1,000 cards, manual verification was no longer feasible. Therefore, Feng Nuo instructed them to use the tabulating machine to verify whether the perforations were consistent once duplication was complete. The method was to separately tally the count of 0-9 digits in each column for both stacks and check whether the results matched. If the results were identical, the probability of any errors could be considered negligible. However, at the tabulating machine's current speed, checking each column took about 20 minutes, and 80 columns would require over 20 hours—the two of them would have to work in shifts overnight.

The next morning, Feng Nuo attended a brief meeting at the Planning Commission and didn't arrive at the office until nearly noon.

He found Feng Shan leading Qian Yuzhi and Li Jianai in inspecting cards one by one against the light to check whether the perforations matched. They had apparently been at it for half the day already, and all three had somewhat glazed expressions. Qian Yuzhi and Li Jianai even had dark circles under their eyes. Feng Nuo found this very strange and hurried over to ask what was going on.

It turned out that Qian Yuzhi and Li Jianai had spent the entire night using the tabulating machine to check the duplication results of the 1,000 cards, only to discover that the new and old cards had different counts of 0-9 in a certain column—the duplicated cards were short one "3" but had one extra "4." In other words, the duplicating machine had made an error, punching a 3 as a 4 on one of the cards. So now they were searching for exactly which card had the problem.

"Commendable work attitude, stupid work method," Feng Nuo commented. He walked over and picked up the two stacks of cards the three hadn't yet checked, asking, "How many have you checked?"

"122."

"114."

"107."

The three answered separately.

"See, three people working all morning have only checked just over three hundred cards. What if we need to test 10,000 cards in the future—how many people would we need to find?" As he spoke, he handed the stack in his hand to Feng Shan, saying, "Count out 330."

He then asked Qian Yuzhi which column had the error and adjusted the tabulating machine's reading brush position. He also divided the remaining stack in his own hand into piles of 330 and 327.

Next, Feng Nuo used the tabulating machine to tally first the 330 new cards that Feng Shan had counted out, and then his own separated stack of 330 old cards.

A little over ten minutes later, the tabulation was complete, and the results matched.

"So, the erroneous card must definitely be in the other half," Feng Nuo pointed to the remaining two stacks of cards.

He then took 160 cards each from the remaining two stacks of 327 cards and fed them into the tabulating machine. This time the results showed that the erroneous card was among these 160.

Feng Nuo divided this batch of cards in half again, each portion containing 80 corresponding new and old cards, randomly took one portion, and repeated the above operation.

...

A few minutes later, the range of suspects had been narrowed down to 10 cards. Feng Nuo distributed the cards to Feng Shan and the other two, and the erroneous card was quickly found.

Feng Nuo placed the erroneous card on the table without looking at it. Instead, he said to Feng Shan, "We're building computers precisely to replace human labor in performing mechanical calculations. The machine does the mechanical work—you don't have to. What do you need to do then? Think about how to drive it to work toward your purpose. Tell me—what principle did we just use to find the erroneous card?"

"Binary search?" Feng Shan asked uncertainly.

Feng Nuo nodded. "Not exactly the same, but the thinking is similar. If you had thought a little about why I had Yuzhi and Jianai use the tabulating machine yesterday to check whether the two stacks of 1,000 cards matched, you could have come up with many solutions. At the very least, you could have fed in 100 cards at a time, and in at most 10 passes, you would have known which batch of 100 contained the error. Of course, if you'd thought of that, you would have also realized that binary search is the fastest."

"What we did has a prerequisite—that the probability of duplication errors is very low. Otherwise, if multiple punch cards all had errors in the same column, this method wouldn't work. That's why yesterday we first checked the results of 1 and 10 duplications, and neither had problems."

"The facts also show that our estimate matched reality. Out of 1,000 cards—that's 80,000 column-duplication operations—the two of them checked over 30 columns from last night to this morning and actually found only 1 column with an error. Moreover, the tally showed only one fewer 3 and only one more 4. This was something you knew before we started searching for the erroneous card, right? We had no other prior knowledge, so we could only assume the duplicating machine's error rate was 1/30,000 and not consider the possibility that the current error resulted from accumulated errors on multiple cards in the same column—because that probability is even lower and can be temporarily ignored.

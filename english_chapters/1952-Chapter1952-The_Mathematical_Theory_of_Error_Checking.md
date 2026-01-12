# Chapter 1952 - The Mathematical Theory of Error Checking

Qian Yuzhi's gaze started to wander first, and Li Jianai was also drifting by now. Only Feng Shan was still listening.

"Binary search finds a specific value in an ordered list. Its essence is a divide-and-conquer strategy—that is, breaking a large problem into several similar sub-problems, and then either solving them directly or continuing to divide. Why does it require an ordered list? To ensure that each operation can simultaneously solve all sub-problems. For example, if the median value of an ascending list is smaller than the value being searched for, I can simultaneously confirm two conclusions: first, the target value is not in the first half of the ordered list; second, the target value is in the second half of the ordered list—so I then repeat the above operation on the second half."

"Our problem is similar. Probabilistically, first we can reasonably assume that there is one and only one erroneous card. Then, each time we tally half of all the cards known to contain the erroneous card. If the tally shows that the erroneous card is not in this half, then it must be in the other half, and vice versa. This way I've narrowed the 'suspect range' of the erroneous card by half. I repeatedly perform the halving operation to shrink the suspect range; once it shrinks to a certain point, the problem is no longer a problem."

"I've told you before—the punch card computer we're building now has capabilities not limited to what we see here. Just now my halving operation was very mechanical, right? Always divide in half, input, check the result, take the stack containing the erroneous card and repeat the operation."

"So if someday we design a machine to replace my repetitive mechanical operations just now, combined with the tabulating machine, it would be able to accomplish much more. Many large problems would be decomposed into small problems, then solved using the same operational process."

"Decomposing seemingly complex problems layer by layer into smaller problems similar to the original, repeatedly solving them with similar series of mechanical operations that computers can also complete—this way of thinking is called 'recursion.' This is a very fundamental approach to utilizing computers, and you need to think about it carefully. In particular, when thinking about such problems, don't factor in the current mechanical computer's operating speed and think it's not as fast as human labor. The key is to consider: what problems can a computer solve when operating solely according to rules without human intervention? That is, what kinds of problems are computer-solvable—we call these 'computable problems.' As for speed, that's not an issue—we'll have bread eventually."

Feng Nuo paused, letting Feng Shan carefully digest these words. For her, this mode of thinking was similar to mathematics but quite different from the mathematics she had studied before. Meanwhile, Qian Yuzhi and Li Jianai could only do arithmetic at the four-operations level; expecting them to understand was rather demanding. Since neither had slept well the night before, they were now quite groggy. This speech was no different from a lullaby—in his daze, Qian Yuzhi was still puzzling over what any of this had to do with bread.

"Alright, you two go sleep. I'll take a look at what went wrong with this card." Feng Nuo set aside Feng Shan, who was still deep in thought, and spoke to Qian Yuzhi and Li Jianai, pointing to the inner room. "You can sleep on that bed." With that, he picked up the incorrectly punched card from the table.

When Li Jianai woke up from the bed, she found Qian Yuzhi still sitting in a chair, leaning against the wall, sleeping soundly. She looked around—Feng Shan was at the workbench reading and calculating something, while Transmigrator Feng was absent from the room, probably at another meeting somewhere.

Yawning, she got out of bed and poked Qian Yuzhi, saying, "Go sleep on the bed." But he only grunted and didn't move. Li Jianai forcefully dragged him over to the bed—though they were supposed to take shifts, Qian Yuzhi had actually stayed up much longer on the night shift than she had.

Perhaps sensing the residual body warmth on the bed, Qian Yuzhi rolled over, seeming to curl into the depression Li Jianai had just slept in, and continued snoring away.

Li Jianai walked to the workbench and poured herself a glass of water. Just then, she saw Feng Shan set down her book and rub her eyes, apparently intending to rest for a moment, so she started chatting with her. Before long, they had agreed to attend a gathering next week together with Li Jianai's classmates from the Liberal Arts Academy—apparently several senior transmigrators would also be attending.

Over the following days, the research team repeatedly improved and tested the duplicating machine. At Feng Nuo's request, they added another set of card-reading mechanisms to the row with the punching apparatus. This modification was minor, but it enabled the duplicating machine to partially function as a Verifier. After duplication was complete, a few wires could be reconfigured to change the machine's function to automatically checking whether the perforations of two stacks of cards matched, stopping and lighting an alarm when inconsistent perforations were detected.

No matter how fast binary search was, it still couldn't beat running through the machine once directly.

Additionally, the improved version could fix a master card in the reading mechanism and punch/verify a stack of cards. In practical applications, this feature could pre-punch the common holes for a batch of cards, reducing the workload of manual punching.

However, despite the improvements to the duplicating machine and fixing the mis-punching problem, it still occasionally failed to punch holes. Finally, the research team reduced the card transport and processing speed, and the problem disappeared.

"Looks like it's a relay response speed issue," Sun Li tossed his pen onto the desk. "Let's operate at reduced speed."

Everyone's gaze immediately snapped to Feng Nuo, who could only nod wordlessly. But by now all the transmigrators had developed thick skins—they were all at similar levels, so nobody could laugh at anyone else. The awkwardness quickly passed, and Feng Nuo proceeded to propose a plan for developing a decoder.

According to the plan, the tabulating machine should have integrated printing and summary-punching functions, but to simplify individual machine complexity, the current phase didn't include these components. Therefore, Feng Nuo planned to first build the most basic numeric decoder. Since it wouldn't consider printing Latin letters, it couldn't even really be called "decoding"—it was purely printing. Its mechanical structure was similar to the duplicating machine: after detecting holes, it activated relays to drive curved type bars to print the digits 0-9 at the top of the cards. Now that the duplicating machine was essentially complete, the decoder was a natural next step.

The mechanical engineering transmigrators felt there were no major issues and agreed to quickly manufacture a prototype to send over.

The meeting ended there, and Feng Nuo returned to his office. He was thinking that he still needed to prepare for his lessons today—as the mechanical computer project progressed, he felt he needed to teach some mathematics problems related to software engineering in depth. The first generation of programmers were almost all mathematicians.

In his office, he processed the Data Center's routine paperwork and made his customary rounds of the machine room, performing daily equipment maintenance. He also browsed the "pending repairs directory," using a red pencil to check off several items at the "urgent" level. These could only be repaired after class, sacrificing sleep time—ever since he started the mechanical computer project, his original workload had piled up considerably. Now that Xu Laowu was handling most of his clerical work, letting his main job slide any further would be inexcusable.

After finally processing everything at hand one by one, he got up and went to the workshop.

The "workshop" was now packed to the brim. Various "engineering prototypes" manufactured by the machinery factory filled this space. Some weren't even products of the "technical meetings" at all, but rather the brainchildren of certain transmigrators with strong hands-on abilities—though calling them pure whimsy wasn't entirely accurate, since these devices roughly corresponded to different technological approaches in the historical development of mechanical computers.

Engineering prototypes were naturally rather crude. Because time was tight and they were mainly just verifying whether design concepts were engineering-feasible, no optimization was done in design or manufacturing. True to the machinery factory's consistent "big, dumb, black, and rough" products, many devices also had exposed components—partly to save manufacturing time, and partly to facilitate real-time troubleshooting and debugging.

The workshop was full of iron-jawed, steel-toothed machines, with various scattered materials and parts on the floor. So Feng Nuo always reminded his three assistants to take proper protective measures when entering the workshop. He led by example, wearing a rattan safety helmet, coarse cloth work clothes, and labor protection leather shoes.

Past the equipment area, the other end of the workshop was the research area. A heavy, large-size "Holy Ship Brand" 12-person conference table stood in the center, its surface piled high with blueprints, documents, and scratch calculation paper, surrounded by seven or eight folding chairs. In the corner was a huge blackboard stand, the blackboard covered with chalk-written formulas and numbers. Against the wall was a row of open bookshelves, stuffed layer upon layer with various technical materials and reference documents—in just a few months, this much documentary material had accumulated. Following Planning Commission regulations, these materials were all organized and bound by Feng Shan and Li Jianai by category—they were all to be archived, to provide reference for future technicians.

But without an efficient retrieval system, these technical materials would probably just gather dust in some corner of the Grand Library, gradually forgotten. Thinking of this, Feng Nuo felt the heavy responsibility on his shoulders all the more keenly.

The research area's floor was covered with scattered calculation drafts, looking like a scene from old movies of the Nationalist Party fleeing in defeat. The research team was so absorbed in their work day and night that they naturally couldn't spare time for cleaning. At least everyone washed their lunch boxes clean and took them home; otherwise, with this level of slovenliness, mice would surely move in.

Feng Nuo plopped down in a chair and took out a professional textbook on discrete mathematics—this was a local Lingao reprint that had passed the Truth Office's review, so no confidentiality measures were needed, and it could be placed directly on the bookshelf.

Just as he was about to open it, he suddenly noticed that the wastepaper basket under the table was stuffed with paper scraps—not ordinary scraps, but paper torn to shreds. This wasn't the calculation paper they usually used, but stationery. And it seemed to be densely covered with writing.

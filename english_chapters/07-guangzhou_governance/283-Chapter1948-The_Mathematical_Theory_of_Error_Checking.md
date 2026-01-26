# Chapter 1948 - The Mathematical Theory of Error Checking

Qian Yuzhi's gaze began wandering first, and Li Jianai was drifting by now as well. Only Feng Shan remained attentive.

"Binary search locates a specific value in an ordered list. Its essence is a divide-and-conquer strategy—that is, decomposing a large problem into several similar sub-problems, then either solving them directly or continuing subdivision. Why does it require an ordered list? To ensure each operation can simultaneously resolve all sub-problems. For example, if an ascending list's median value is smaller than the searched-for value, I can simultaneously confirm two conclusions: first, the target value is not in the ordered list's first half; second, the target value resides in the second half—so I then repeat the above operation on the second half."

"Our problem parallels this. Probabilistically, first we can reasonably assume one and only one erroneous card exists. Then, each time we tally half of all cards known to contain the erroneous card. If tallying reveals the erroneous card is not in this half, it must reside in the other half, and vice versa. This way I've narrowed the erroneous card's 'suspect range' by half. I repeatedly execute the halving operation to shrink the suspect range; once it contracts to a certain point, the problem ceases being problematic."

"I've told you before—the punch card computer we're constructing now possesses capabilities not limited to what we observe here. Just now my halving operation was highly mechanical, correct? Always bisect, input, verify the result, take the stack containing the erroneous card and repeat the operation."

"So if someday we design a machine to replace my repetitive mechanical operations just now, combined with the tabulating machine, it could accomplish far more. Numerous large problems would be decomposed into smaller problems, then solved using identical operational processes."

"Decomposing seemingly complex problems layer by layer into smaller problems resembling the original, repeatedly solving them with similar series of mechanical operations that computers can also execute—this thinking mode is called 'recursion.' This constitutes a highly fundamental approach to computer utilization, and you need to contemplate it carefully. Particularly when considering such problems, don't factor in the current mechanical computer's operating speed and conclude it's slower than human labor. The key consideration is: what problems can a computer solve when operating solely according to rules without human intervention? That is, what kinds of problems are computer-solvable—we call these 'computable problems.' Regarding speed, that's not an issue—we'll have bread eventually."

Feng Nuo paused, allowing Feng Shan to carefully digest these words. For her, this thinking mode resembled mathematics yet differed substantially from the mathematics she'd previously studied. Meanwhile, Qian Yuzhi and Li Jianai could only manage arithmetic at the four-operations level; expecting their comprehension was rather demanding. Since neither had slept adequately the previous night, they were now quite drowsy. This speech proved indistinguishable from a lullaby—in his daze, Qian Yuzhi was still puzzling over what any of this had to do with bread.

"Alright, you two go sleep. I'll examine what went wrong with this card." Feng Nuo set aside Feng Shan, who remained deep in contemplation, and addressed Qian Yuzhi and Li Jianai, indicating the inner room. "You can sleep on that bed." With that, he retrieved the incorrectly punched card from the table.

When Li Jianai woke from the bed, she found Qian Yuzhi still seated in a chair, leaning against the wall, sleeping soundly. She surveyed the room—Feng Shan was at the workbench reading and calculating something, while Transmigrator Feng was absent, probably attending another meeting somewhere.

Yawning, she exited the bed and poked Qian Yuzhi, saying: "Go sleep on the bed." But he merely grunted without moving. Li Jianai forcefully dragged him over to the bed—though they were supposed to alternate shifts, Qian Yuzhi had actually sustained the night shift far longer than she had.

Perhaps sensing the residual body warmth on the bed, Qian Yuzhi rolled over, seeming to curl into the depression Li Jianai had just vacated, and continued snoring away.

Li Jianai walked to the workbench and poured herself water. Just then, she observed Feng Shan set down her book and rub her eyes, apparently intending to rest momentarily, so she initiated conversation. Before long, they'd agreed to attend a gathering next week together with Li Jianai's classmates from the Liberal Arts Academy—apparently several senior transmigrators would also be attending.

Over subsequent days, the research team repeatedly refined and tested the duplicating machine. At Feng Nuo's request, they added another card-reading mechanism set to the row with the punching apparatus. This modification was minor, yet it enabled the duplicating machine to partially function as a Verifier. After duplication completed, a few wires could be reconfigured to transform the machine's function to automatically verifying whether two card stacks' perforations matched, stopping and illuminating an alarm when inconsistent perforations were detected.

However swift binary search was, it still couldn't surpass running through the machine once directly.

Additionally, the improved version could fix a master card in the reading mechanism and punch/verify a card stack. In practical applications, this feature could pre-punch common holes for card batches, reducing manual punching workload.

However, despite duplicating machine improvements and rectifying the mis-punching problem, it still occasionally failed to punch holes. Finally, the research team reduced card transport and processing speed, and the problem vanished.

"Looks like it's a relay response speed issue," Sun Li tossed his pen onto the desk. "Let's operate at reduced speed."

Everyone's gaze immediately snapped to Feng Nuo, who could only nod wordlessly. But by now all transmigrators had developed thick skins—they were all at similar levels, so nobody could mock anyone else. The awkwardness passed quickly, and Feng Nuo proceeded to propose a plan for developing a decoder.

According to the plan, the tabulating machine should have integrated printing and summary-punching functions, but to simplify individual machine complexity, the current phase didn't include these components. Therefore, Feng Nuo planned to first construct the most basic numeric decoder. Since it wouldn't consider printing Latin letters, it couldn't even genuinely be called "decoding"—it was purely printing. Its mechanical structure resembled the duplicating machine: after detecting holes, it activated relays to drive curved type bars to print digits 0-9 at the card tops. Now that the duplicating machine was essentially complete, the decoder was a natural next step.

The mechanical engineering transmigrators felt no major issues existed and agreed to quickly manufacture a prototype for delivery.

The meeting concluded there, and Feng Nuo returned to his office. He contemplated that he still needed to prepare for today's lessons—as the mechanical computer project progressed, he felt compelled to teach certain mathematics problems related to software engineering in depth. The first programmer generation consisted almost exclusively of mathematicians.

In his office, he processed the Data Center's routine paperwork and made his customary machine room rounds, performing daily equipment maintenance. He also browsed the "pending repairs directory," using a red pencil to check several "urgent" level items. These could only be repaired after class, sacrificing sleep time—ever since commencing the mechanical computer project, his original workload had accumulated considerably. Now that Xu Laowu was handling most clerical work, allowing his main job to slide any further would be inexcusable.

After finally processing everything at hand item by item, he rose and proceeded to the workshop.

The "workshop" was now packed to bursting. Various "engineering prototypes" manufactured by the machinery factory filled this space. Some weren't even "technical meeting" products at all, but rather the brainchildren of certain transmigrators with strong hands-on abilities—though calling them pure whimsy wasn't entirely accurate, since these devices roughly corresponded to different technological approaches in mechanical computer historical development.

Engineering prototypes were naturally rather crude. Because time was compressed and they were mainly just verifying whether design concepts were engineering-feasible, no design or manufacturing optimization occurred. True to the machinery factory's consistent "big, dumb, black, and rough" products, many devices also exhibited exposed components—partly to conserve manufacturing time, partly to facilitate real-time troubleshooting and debugging.

The workshop was full of iron-jawed, steel-toothed machines, with various scattered materials and parts on the floor. So Feng Nuo always reminded his three assistants to take proper protective measures when entering the workshop. He led by example, wearing a rattan safety helmet, coarse cloth work clothes, and labor protection leather shoes.

Past the equipment area, the workshop's other end was the research area. A heavy, large-size "Holy Ship Brand" 12-person conference table stood centrally, its surface piled high with blueprints, documents, and scratch calculation paper, surrounded by seven or eight folding chairs. In the corner stood a huge blackboard stand, the blackboard covered with chalk-written formulas and numbers. Against the wall extended a row of open bookshelves, stuffed layer upon layer with various technical materials and reference documents—in mere months, this documentary volume had accumulated. Following Planning Commission regulations, these materials were all organized and bound by Feng Shan and Li Jianai by category—all destined for archiving, to provide future technician reference.

But without an efficient retrieval system, these technical materials would probably just gather dust in some Grand Library corner, gradually forgotten. Contemplating this, Feng Nuo felt the heavy responsibility on his shoulders all the more keenly.

The research area's floor was covered with scattered calculation drafts, resembling scenes from old Nationalist Party defeat-flight movies. The research team was so absorbed in work day and night that they naturally couldn't spare time for cleaning. At least everyone washed their lunch boxes clean and took them home; otherwise, with this slovenliness level, mice would surely move in.

Feng Nuo plopped down in a chair and extracted a discrete mathematics professional textbook—this was a local Lingao reprint that had passed Truth Office review, so no confidentiality measures were needed, and it could be placed directly on the bookshelf.

Just as he prepared to open it, he suddenly noticed the wastepaper basket under the table was stuffed with paper scraps—not ordinary scraps, but paper torn to shreds. This wasn't the calculation paper they customarily used, but stationery. And it appeared densely covered with writing.

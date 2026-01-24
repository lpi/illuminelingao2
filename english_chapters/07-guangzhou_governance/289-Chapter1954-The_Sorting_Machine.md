# Chapter 1954 - The Sorting Machine

Feng Shan's face reddened further. Though she could only half-understand her teacher's words, she roughly grasped their meaning. Moreover, she had keenly perceived another meaning hidden in her teacher's final words, so she swallowed back the last question she had originally wanted to ask—she had already gotten her answer.

Originally she had wanted to explain about her contact and correspondence with the junior student, but now it seemed unnecessary. The confusion and tension she had felt suddenly lifted, and she suddenly felt how vast the world was. She stepped back and bowed deeply:

"I have no more questions! I'll go reorganize the household registration materials for the sorting machine test!"

The next day, Li Jianai deliberately arrived early at the workshop storage, intending to find the household registration documents her friend had asked her to look up. But when she saw the neatly arranged stacks of household registration forms, she was dumbfounded—previously these materials had been arranged by commune and householder name, with each family's cards together. Now it had changed, reorganized by place of origin and occupation, with careful notations beside each stack indicating the origin, occupation, number of people... and other information.

There were household registration records for over 10,000 people from parts of Lingao and Qiongshan counties here—where was she supposed to find the household registration for the Lin Guanghui family from Jialai Commune?

Just then Feng Shan walked in, still bleary-eyed. Li Jianai hurriedly asked, "Teacher Xiao Feng, these forms... why has the order all changed?"

"Oh, today we're testing the sorting machine prototype. Teacher said that besides sorting by household registration location and surname, we should also sort the cards by place of origin and occupation. Since the number of people in each commune and the number of people with each surname had been tallied before, he had Qian Yuzhi reorganize these household registration materials yesterday to prepare for verifying today's sorting results. Last night..." she yawned, "I checked the count for each stack and labeled them... checked until midnight..."

"Ah, right, you were going to look up that household's information today," Feng Shan remembered.

"That's right. That dummy Qian Yuzhi... didn't even tell me."

As she spoke, Li Jianai suddenly remembered that yesterday she had also drunk quite a bit, gone home and slept, then spent the evening holed up in her room organizing and recording some information she'd heard during the day. She hadn't met with Qian Yuzhi in the room next door. When she woke up in the morning, she found a thermos and two sweet potato cakes placed at her door, with a note from Qian Yuzhi the night before tucked on top.

"What do we do?" Li Jianai was somewhat anxious.

"..." Before Feng Shan could respond, Feng Nuo came rushing in energetically.

"Good morning, Teacher," the two said in unison.

Feng Nuo casually said, "Good." Then immediately continued, "Are these materials all organized? Quick, move them out—the sorting machine prototype will be installed any moment."

With that, he walked back out.

The two exchanged glances and had no choice but to start moving the household registration materials.

"Let's tell Teacher during the test—using the machine to look it up should be no problem," Feng Shan whispered.

Several naturalized citizen workers were busy with the components scattered all over the floor, while Feng Nuo and several transmigrators from the research group stood to the side, giving directions while chatting.

"I still think we should have designed it as a turntable—make a big 10-slot wheel. Mount some baskets on the turntable, and when the sorting machine senses a particular hole, rotate the turntable to the corresponding basket and drop the card in." One transmigrator said. "Your current design is essentially 10 card-reading systems in series, with each system connected to just 1 relay. Punched cards get pushed sideways into the card pocket; unpunched cards continue through. This means each reading unit is only used to check whether 1 of 800 hole positions is punched—the efficiency is too low."

"I recall the tabulating machine reads at 1 card per second?" Someone else said.

"Mm, a bit longer actually—about 1.2 seconds. This card reader uses Dr. Zhong's new structure, so we estimate we can get it under 1 second."

"That's still too slow—sorting one card takes 10 seconds."

"Old Liang, you've forgotten again. I explained this to you last time. When the 1st card reaches the 2nd reading unit, the 2nd card can already start entering the 1st reading unit. So it's actually still 1 card per second."

"Oh, oh, right."

"The speed is acceptable—still over 3,000 per hour."

"I don't think going too fast is necessary anyway—what if the relays still can't keep up?" Sun Li glanced at Qian Yuzhi, who was installing relays.

"No problem this time—we've improved the relay design over this period," Feng Nuo quickly said.

"When will the new winding machine arrive? The current equipment always has some problems winding 0.1mm wire." He asked Sun Li.

"Probably another week," Sun Li replied.

The Standard Parts Factory had recently produced 0.1mm diameter copper wire, and the Electronic Equipment Workshop had immediately manufactured a batch of enameled wire from it. The results were quite good—some of the control relays had noticeably shrunk in size and responded more sensitively.

"What material is the counter's digit wheel made of?" Dr. Zhong asked. The sorting machine's card pockets were each fitted with linked counters—it wasn't much extra trouble, and the principle was the same as the tabulating machine.

"High-carbon steel, I think," someone answered.

"Wheels for counters don't need such good material. In the current design, these digit wheels have no mechanical contact with the levels above and below—only electrical contact. We can make them into quickly replaceable modules. If one breaks, just pull it out and swap in a good one. This makes maintenance more convenient and saves expensive materials." Dr. Zhong was once again promoting his modular concept.

"However, the pins are the most heavily loaded parts in the counter, needing to frequently scrape against the ratchet tooth face, so they need harder material," he added.

"Mm, let's try it next time. But there was a problem with that design diagram last time—the angle of the Y-fork was wrong, causing the ratchet to backslide, so the other pin wouldn't line up with the tooth face."

"Oh, no problem this time—I've increased the pin spacing to ensure a reliable 'unlocked' position. The ratchet tooth face angle has also been corrected."

...

"Old Feng, you still haven't designed multi-condition sorting, have you? Isn't that a bit conservative? Both the tabulating machine and sorting machine can only perform statistics and sorting on a single column of the card."

"Who says there's no improvement? There is—we can support up to 10-condition sorting." Feng Nuo answered with a hint of pride.

"Hm? How did you do that? I don't see any corresponding structure."

"Although each reading system has only 1 reading roller and can only read 1 hole at a time, the position of this roller is adjustable—it can be adjusted to align with different columns and rows. I added a control relay upstream of each card-feeding relay with a switch that can select whether to activate or not. This way, it's equivalent to being able to negate the card-feeding mechanism's relay. I can choose to send out all punched cards, or I can choose to send out all unpunched cards."

"Then, on the second card-feeding unit, I check another hole and send out all cards that don't meet the condition. And so on—in the end, what remains are the cards that simultaneously satisfy multiple conditions."

"Mm... that's too crude. For one thing, you can't solve the 'OR' condition problem, because you've already sent out all cards that don't satisfy the condition at the first card pocket, right? All conditions are in an 'AND' relationship. For another, you've picked out the cards you want, but the original card library's order is now completely scrambled—essentially randomly sorted." Dr. Zhong said with a frown.

However, though crude, everyone still found the approach quite interesting, and for a while the discussion was quite lively.

A little later, the machine installation was complete. Power was connected and it ran normally, so the workers withdrew. The transmigrators chatted and discussed for a while, then gradually dispersed—the day was only just beginning, and everyone had plenty to do. In the end, only the four people from the Electronic Equipment Workshop remained.

"Let's start testing," Feng Nuo said. "Bring the cards, first—"

"Teacher..." Li Jianai raised her hand to signal, then explained about needing to find the household registration information.

Feng Nuo became interested. Having a concrete example to try wasn't bad.

"What's the householder's name?" he asked.

"Lin Guanghui. From Jialai Commune."

"Jialai Commune is 1001014—"

In the regional code table established by the Social Welfare Province, similar to the old timeline, 7-digit numbers represented regions. The first 3 digits indicated the "province" level: 100 was Hainan, 101 was Taiwan, 102 was Jeju Island... These were the Executive Committee's current directly-administered regions. 110-199 was reserved for the mainland, 200-219 for Korea, 220-249 for Japan, 250-269 for the Indochina Peninsula, 270-299 for the Southern Seas islands. The remaining numbers hadn't been assigned yet. If territory expanded in the future and they ran out, they could add another digit at the front to solve the problem.

Below province level came county/district. In Hainan, 10 was Lingao, 11 was Sanya Yulin, 12 was Sanya Tiandu, 13 was Qiongshan, 14 was Chengmai... And the final digit was the commune. In Lingao, 11 was Bairren Commune, 12 was Bopu Commune, 13 was Nanbao Commune, 14 was Jialai Commune...

Actually there was also 10. The 6th-7th digits of household location represented commune/village, but all county-level communes were numbered starting from 11. And "10" indicated this person was a member of a transmigrator household who had long resided there: the transmigrator themselves, spouse, children, other family members, life secretary, or servants and such.

"This time we only have partial household registration data from Lingao and Qiongshan, so reading position 1 will exclude cards where the 5th digit isn't 0—that distinguishes Lingao from Qiongshan. Reading position 2 will exclude cards where the 7th digit isn't 4—that selects Jialai Commune." Feng Nuo instructed.

"The householder's surname is Lin. The character code for Lin is—"

"3354." Li Jianai answered promptly from over there.

"Good, then we'll use reading positions 3-6 to select cards where the householder's surname is 3354. Positions 7-10 will filter for the second character of the householder's given name. Is it 'Hui'?"

"Yes, the character code is 2752."

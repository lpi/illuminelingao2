# Chapter 1955 - Application of the Sorting Machine

After setting up the sorting machine, Feng Nuo flipped the machine's switch and the cards began sorting with a swishing sound. He instructed Li Jianai and Qian Yuzhi to watch the machine, then went with Feng Shan back to the computer room to check the server's operating status.

Near noon, Feng Nuo returned to the workshop. The card sorting was complete. He glanced at his watch—a little over 2 hours. For sorting 10,000 cards, that was quite fast. However, Li Jianai and Qian Yuzhi were sitting dejectedly beside the machine.

It turned out they hadn't found any cards matching the conditions.

This was quite strange. Feng Nuo thought for a moment, then looked at the sorting machine's status. He noticed that card pocket number 9 had no cards at all, while card pocket number 10 had a few cards—meaning these cards had failed at the very last condition. He picked up one of the cards from pocket number 10 and examined it—these cards had previously had the corresponding digits printed at the top by the decoder.

"2750. This householder isn't named Lin Guanghui," Feng Nuo said. "Look this up—3354, that's 'Lin,' no problem. Then 2567, 2750."

"Lin Guanghui... this person is named Lin Guanghui..."—the characters were both wrong. Li Jianai was both annoyed and amused.

"Was there a mistake when punching the card?" Feng Shan asked.

"Hmph," Feng Nuo snorted. He thought this person was most likely a refugee taken in by the Guangzhou refugee camp, hence the character "Guang" (broad). As for "Hui" (gray)—probably the color scheme used for naming on the day of intake.

"Origin: 12216, that's Fujian. Occupation: farmer. Status: military household."—It looked like this household probably had no relation to the Baitu Lin clan after all.

Based on this information, Li Jianai found the "Permanent Resident Registration Form" for the Lin Guanghui family members in the "Fujian" and "farmer" stack of household information forms, copied the necessary information, and wrote it up as a certification document. She also attached an explanation of the information retrieval process at the end, and Feng Nuo signed it.

The transmigrators were now all quite conscientious about solving whatever problems they could see—whether or not it was their own patch of land, it was ultimately the Executive Committee's business, which made it their own business.

Once everything was written up, Li Jianai prepared to send out the certification.

"Jianai, you don't need to come back. Go to the Tiandihui this afternoon to complete the job transfer procedures and bring your file over," Feng Nuo instructed.

Afterward, he had Feng Shan and Qian Yuzhi organize the cards, tallying the number of people by household location, surname, origin, and occupation, then comparing with the manually calculated results to formally test the sorting machine prototype.

A week after officially transferring to her new job, Li Jianai received a letter with a mailbox number as the sender when she got home. Without looking around, she immediately picked up the envelope and quickly stuffed it into her pocket.

That evening, Li Jianai couldn't wait to find an opportunity to open the letter. Inside was nothing but a few simple lines of coded instructions with no header or signature. After carefully verifying several hidden marks and confirming everything was correct, she forced herself to suppress her inner excitement and destroyed the letter.

When Li Jianai arrived at the contact point indicated in the letter, her jaw nearly dropped in shock. She hadn't expected that Group Leader Jia, who often came to the Electronic Equipment Workshop to provide technical guidance, was actually her handler. She had never noticed at all.

Jia Ben showed no expression of surprise. He didn't explain why contact with her had been interrupted—Li Jianai naturally didn't ask either—but simply asked briefly about Li Jianai's situation during this period, collected the work report and personal summary she submitted, and instructed her to "continue operating according to previous guidelines" before hurrying off.

The next day, when Li Jianai returned to the workshop in high spirits, Feng Nuo was instructing Feng Shan and Qian Yuzhi in using the sorting machine and had written quite a bit on the blackboard. Seeing Li Jianai return, he nodded to indicate she should also come over to listen.

The sorting machine test had been very successful: it was just that not being able to handle "OR" conditions was indeed a major limitation. Feng Nuo already had a rough idea in mind about how to improve it, but today he wanted to use this as an example to give his students a lesson.

This was actually already touching on the core principles of computers. What he wanted wasn't mere operators, but programmers who could actually apply the knowledge.

"Today, let's analyze theoretically what kinds of problems our sorting machine can solve, and what kinds it cannot."

"First, sorting. Without question, this problem can be solved. We set the reading rollers on all 10 reading units to target the same column's 0-9, and the cards will be pushed into 10 card pockets according to that column's digits. When manually recombining the cards into one stack, they'll be sorted by the size of that column's numbers."

"Second, single-condition classification. 'Divide all cards into male and female stacks.' This can definitely be done. We only need to activate 1 reading unit, targeted at the 0 position of the gender column. Gender 0, meaning female, will be pushed into the card pocket; males will not."

"Third, multi-condition classification. This requires specific analysis. I'll give you a few problems—think about how to use the sorting machine to accomplish them. First problem: suppose we now have household registration cards for the entire East Asian region, and I want to find cards for Jialai Commune in Lingao, Hainan. How should we proceed? Yuzhi, you answer."

"Have reading units 1-7 sequentially filter out cards with household location 1001014," Qian Yuzhi answered.

"Correct. Jianai, second problem. I still have household registration cards for all of East Asia. Now I want to find cards for the Sanya District excluding slaves. How should we proceed?"

"The Sanya District includes two county-level units: Sanya Yulin, code 10011, and Sanya Tiandu, code 10012. The subordinate slave zone code is 1001299."

"Have reading units 1-4 sequentially filter out cards where the first 4 digits of household location are '1001'; then have reading unit 5 push cards where the 5th digit of household location is '1' into pocket 5—these are Sanya Yulin cards. Have reading unit 6 push cards where the 5th digit of household location is not '2' into pocket 6—at this point the remaining cards in the machine are Sanya Tiandu. Have reading unit 7 push cards where the 6th digit of household location is not 9 into pocket 7—these are communes 11-89 of Sanya Tiandu. Have reading unit 8 push cards where the 7th digit of household location is not 9 into pocket 8—these are communes 90-98 of Sanya Tiandu. At this point the remaining cards in the machine are Sanya Tiandu's slave cards. Combine the cards from pockets 5, 7, and 8 for the desired result." Li Jianai thought for quite a while before answering.

"Very good, Jianai, correct." Feng Nuo was somewhat surprised.

"Feng Shan, now I have all the household registration cards for Lingao. First, find people named 'Liu Si' living in Shisan Village and Bairren Commune. Second, find people whose origin is Fujian or Hainan. Try these two problems."

"Neither of these problems can be solved," Feng Shan answered after thinking for a moment.

"Why?"

"The reasons are different. The first problem can't be solved because there aren't enough reading units," Feng Shan said.

"To ensure that the name on a card is 'Liu Si,' we need to ensure the columns storing the name equal the 8-digit character code for 'Liu Si.' This requires 8 reading units to exclude non-matching cards. It could be said that all cards reaching the 9th reading unit have the name 'Liu Si.'"

"But at this point the sorting machine has only two reading units left. Bairren Commune is '11,' Shisan Village is '18.' We can use reading unit 9 to exclude cards where the 6th digit of household location (commune) is not '1'—at this point the remaining cards in the machine are 'Liu Si' from communes 11-19. Among them, we can use reading unit 10 to push cards where the 7th digit is '1' into the pocket—these are 'Liu Si from Bairren Commune.' But it's not sufficient to separate 'Liu Si from Shisan Village' from the remaining cards. So this application cannot be completed."

"However, if the sorting machine had one more reading unit, this application could be solved."

"Mm, not bad. What about the second problem?"

"The second problem doesn't use all the reading units—it's something our current sorting machine cannot solve due to its design."

"Explain."

"Origin Hainan, code 100. Origin Fujian, code 122. We can first use reading unit 1 to select cards where the 1st digit of household location is '1.' But after that, if we choose to push out cards where the 2nd digit is 0, then we cannot continue to filter for cards where the 3rd digit is also 0, which would make it impossible to separate Hainan (100) from Taiwan (101) and Jeju Island (102). If we choose to push out cards where the 2nd digit is not 0, then Fujian cards would be pushed into the pocket and cannot be further separated from other cards."

"Very good. This is the 'cannot do OR operations' problem that Transmigrator Zhong mentioned. He stated it rather generally—now let's analyze theoretically why we can't solve this problem." Feng Nuo walked to the blackboard.

"Theoretical analysis means abstracting problems like the specific questions I just asked you into general problems for study."

"When we want to find any card, there's always a series of conditions describing the target card. We call this series of conditions 'propositions.' These conditions, reflected in the filtering means, are whether a particular hole on the punch card 'is or isn't' punched. Note that each proposition has two possibilities: yes and no. We call these 'true' and 'false.'"

"Now we have two concepts: propositions and true/false. Ultimately, whether a card is the card we want is often jointly defined by many conditions. Each condition is a proposition, so our final target is a new proposition composed of many propositions—we can call it a 'compound proposition.' Each condition constituting the compound proposition can be called a 'simple proposition.' Naturally, 'compound propositions' also have 'true/false' values."

He wrote on the blackboard: proposition, true/false, compound proposition, simple proposition.

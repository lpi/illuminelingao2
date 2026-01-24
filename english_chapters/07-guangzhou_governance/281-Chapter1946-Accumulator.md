# Chapter 1946 - Accumulator

However, every day seemed very different. Qian Yuzhi gradually understood what a relay was, what shape the iron core should be processed into for optimal performance, how fast the hand-cranked copper wire enameling equipment should turn, how long the coating for wires of different diameters should be heated in the lacquer boiling kettle... Li Jianai and Feng Shan became very good friends—it was quite normal since they were girls of similar age and worked together all the time.

As for her and himself... Qian Yuzhi couldn't explain it clearly. The playfulness and intimacy that made his heart beat faster when they went shopping, chatting, drinking, and going home together that day never appeared again. The distance between the two seemed to have returned to what it had always been, except that in imperceptible details, there seemed to be a trace of tacit understanding, a trace of ease.

"Yuzhi!" Feng Nuo's greeting interrupted Qian Yuzhi's wandering mind, "I'm going to a meeting at the Ministry of Science and Technology this afternoon and won't be back today. Don't forget the safety check when you leave."

"Okay, Chief." Qian Yuzhi agreed while secretly warning himself not to space out again.

This afternoon was the discussion meeting on the accumulator scheme for the tabulating machine. Because the Ministry of Science and Technology was moving, the meeting was held at Dr. Zhong's old lair, the Taibai Observatory. There were many precision instruments and equipment here, so geothermal air conditioning was fully installed the year before last, and security and drying measures were also very complete.

There were not many attendees. The meeting was held in the conference room of the Taibai Observatory—also known as the Second Conference Room of the Ministry of Science and Technology. Feng Nuo had been to the First Conference Room before, which was laid out like a large lecture hall.

This was his first time in this Second Conference Room. The area was smaller than the First Conference Room, but it was more than enough for such a small meeting. A long conference table measuring fully 3 meters by 15 meters was placed in the room without making it look crowded at all. Hand-woven rattan chairs were neatly arranged around the conference table. Teak flooring from Siam was laid, with floor power sockets installed at intervals. One side of the wall was a large monolithic panoramic glass window, now covered by thick velvet curtains. At one end of the conference room hung a huge projection screen brought from the old timeline, and a high-resolution projector was suspended from the ceiling. The cables for projection were neatly connected along the wall to the presenter's position. The presenter could also use the microphone at their position; presumably, the speakers in the four corners of the wall were for amplification.

"This is no inferior to a luxury conference room in the old timeline. Dr. Zhong is so extravagant!" Feng Nuo was very surprised, but on second thought, "The Senate invested so much here for its own purposes. Isn't today's discussion meeting, originally more related to the machinery department, moved here?" Thinking of this, he was relieved.

At this time, staff brought hot tea from the pantry next door and placed it in front of each attendee, then quietly withdrew.

Unlike past technical meetings, two rows of chairs were placed against the wall. This was the gallery for naturalized citizens. In order to strengthen the training of naturalized scientific and technical personnel, technical seminars that only Senators attended in the past began to relax entry conditions. A batch of naturalized students and technical personnel with solid basic knowledge and considerable talent were selected and specially allowed to attend relevant seminars.

Because of their presence, the Truth Office would specially notify Senators before each meeting to pay attention to their "speech" during the meeting. Do not leak too many unexplainable things.

The naturalized personnel attending the meeting this time included Zhong Lishi's adopted daughter Zhong Xiaoying, Feng Shan, and several others who were either students and disciples of Senators or outstanding genius figures currently in the Fangcaodi selection group, totaling only thirteen people.

As future pillars of science and technology who could access "black technology," they realized the significance of their presence on such an occasion, so each was both reserved and excited.

The meeting had no wordy procedures and went directly to the main topic of mechanical computers. As the project team leader, Feng Nuo first reported on the project progress, especially the development and improvement of relays. Then, the meeting entered the next step, which was the discussion of the manufacturing principle of the tabulating machine.

After the project team's research these days, there were roughly three methods to implement the accumulation function of the tabulating machine:

First, because the data on the punch card was represented by holes punched in one column or several consecutive columns indicating the digits, calculating the sum only required counting how many times each hole in each column was punched across all cards. This could be done by a simple counter.

Next, manually multiply the number of times each hole was punched by the value of that hole and sum them up, then multiply the sum of each column by 10 or 100 depending on whether the column represented tens/hundreds, and finally sum them up. Although the final result required another calculator or manual calculation alone, anyway, at this stage, the results of the tabulating machine also needed to be manually copied into the record.

This was not a true accumulator, but Hollerith's tabulating machine did exactly this. The mechanical design was also the simplest, only requiring a relay or a relay-driven escapement fork to turn the number dial.

Second, do not directly mesh the main power gear with the rotating shaft of the number dial, but use a relay to control the gear connecting the two. Only when a relay corresponding to digits 0-9 was energized could the main power drive the corresponding mechanical structure to turn the number dial.

At this time, the operations of the mechanical structures corresponding to 0-9 when turning the number dial could be different, either turning multiple times or turning multiple digits at once, to achieve the accumulation of numbers in each hole together. As for carrying, same as the first scheme, it was completed by adding a relay between 9 and 0 of the lower digit number dial to drive the higher digit number dial to turn.

Such a mechanical structure was slightly complex and definitely took up more space. The advantage was that it merged the accumulation of each hole in each column, avoiding a large amount of manual multiplication and summation, and further solving the carry problem. The number on the final number dial was the result of the accumulation, what you see is what you get.

Finally, it was simply using relays to build a binary accumulator scheme. The theoretical design difficulty was not great. However, Dr. Zhong distributed the blueprints of a full relay version Arithmetic Logic Unit (ALU) built by a relay fanatic in the old timeline he found during the meeting. The densely packed relays looking like a honeycomb in the data picture made the attendees' scalps tingle. A certain trypophobia patient immediately asked to go out and rest for a while to "get some air."

Dr. Zhong explained that if only the adder function could be stripped from it, it probably wouldn't be particularly complex. However, the attendees were probably scared by the ALU built by this madman and still shook their heads one after another. Even Feng Nuo, who originally looked forward to this scheme, dismissed the idea.—Mainly because he knew the performance of the relays he developed too well. Even if only the adder function was stripped out, it involved the mutual control of a large number of relays. The rough goods made now probably couldn't meet the reliability requirements.

The third scheme was abandoned first like this, but Dr. Zhong still intended to continue experimenting with it, considering it as accumulating some experience for designing binary computers in the future. Feng Nuo also promised to prioritize developing more sensitive, reliable, smaller, and lighter relays for this scheme's experiment in the next step—provided that the mechanical department could provide sufficiently thin copper wire, and his indigenous insulating lacquer was effective on thin wires.

Next, the meeting held a lengthy discussion on the first and second schemes. Senators from the mechanical department stated that Scheme 1 was definitely no problem and could be trial-produced right away upon return. Scheme 2 would require re-optimizing the design, and also depended on whether the relay performance provided by Feng Nuo was sufficient.

Finally, the project team decided to go with Scheme 1 first. Because assessments from all aspects showed that this scheme had the smallest probability of problems—after all, the structure was simple and the action was reliable, making it easier to achieve with their difficult material levels.

"Back to the level of 1890 again." Feng Nuo sighed secretly. This scheme was not much better than the one ridiculed as a "banknote counter" last time. But punch cards had been in place for several months, getting worm-eaten and moldy in the warehouse. Data couldn't always wait for machines. It would be best to report some good news to the Governor recently, seeing that the end of the year was approaching...

The end of the year was time for project assessment again. If he couldn't produce results, he at least had to muddle through with a few papers as "interim results"; otherwise, there would be a famine to fight with the Planning Agency and the Ministry of Finance. Feng Nuo was not a person who enjoyed socializing.

Next, the attending Senators held a lengthy discussion on the specific mechanical design, process, materials, and supporting facilities of the tabulating machine. The discussion was very detailed, so the meeting often turned into a marathon meeting—but it was very necessary: the Senate's industrial system was extremely incomplete, and almost any new equipment had to be manufactured from scratch. Coupled with the shortage of technical personnel and skilled workers, raw materials were even more scarce in variety. Sending down design plans and blueprints like in the old timeline simply couldn't produce anything. The whole equipment—whether it was core components or a mere screw—had to be implemented in detail from raw materials to processing procedures.

Two weeks later, the first prototype of the tabulating machine was finally completed. The machinery factory manufactured various components of the mechanical system, including two solutions using steam power and electric motors as main power. Feng Nuo took Qian Yuzhi to assemble the relay control part into it.

Feng Nuo immediately moved the cards over to start actual testing. The test results were satisfactory. In multiple tests, they input census cards of different communes and calculated the age sum of the population in that commune, then compared it with the results of manual calculation. No calculation errors occurred. This showed that the design of the tabulating machine was reliable. Feng Nuo breathed a huge sigh of relief. But the efficiency of the equipment was much slower than imagined, taking about 10 seconds to process a card. This time was too long; only 6 cards could be processed per minute, which was only limitedly faster than manpower.

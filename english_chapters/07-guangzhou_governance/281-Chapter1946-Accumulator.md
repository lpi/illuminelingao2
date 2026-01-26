# Chapter 1946 - Accumulator

Yet each day seemed remarkably different. Qian Yuzhi gradually absorbed what relays were, what iron core shape optimized performance, how rapidly the hand-cranked copper wire enameling apparatus should rotate, how long coating for various wire diameters should be heated in the lacquer boiling kettle... Li Jianai and Feng Shan had developed a close friendship—quite natural since they were similarly aged women working together constantly.

As for her and himself... Qian Yuzhi couldn't articulate it clearly. The playfulness and intimacy that had accelerated his heartbeat when they'd gone shopping, chatting, drinking, and returning home together that day never resurfaced. The distance between them seemed to have reverted to its habitual state, except that in imperceptible details, traces of tacit understanding and ease had emerged.

"Yuzhi!" Feng Nuo's greeting interrupted Qian Yuzhi's mental wandering. "I'm attending a meeting at the Ministry of Science and Technology this afternoon and won't return today. Don't forget the safety inspection when departing."

"Understood, Chief." Qian Yuzhi assented while secretly admonishing himself against further distraction.

This afternoon's agenda was the discussion meeting on the tabulating machine's accumulator scheme. Because the Ministry of Science and Technology was relocating, the meeting convened at Dr. Zhong's stronghold, the Taibai Observatory. The facility housed numerous precision instruments and equipment, so geothermal climate control had been fully installed the year before last, security and dehumidification measures equally comprehensive.

Attendance was modest. The meeting occupied the Taibai Observatory's conference room—also designated the Ministry of Science and Technology's Second Conference Room. Feng Nuo had previously visited the First Conference Room, which resembled a large lecture hall.

This marked his maiden entry to the Second Conference Room. Though smaller than its counterpart, it more than adequately accommodated such intimate gatherings. A long conference table measuring fully three meters by fifteen meters occupied the space without creating crowding. Hand-woven rattan chairs were precisely arranged around the table. Teak flooring from Siam covered the floor, with power outlets installed at intervals. One wall featured an expansive monolithic panoramic glass window, presently concealed by thick velvet curtains. At the conference room's far end hung an enormous projection screen imported from the old timeline, with a high-resolution projector suspended from the ceiling. Projection cables ran neatly along walls to the presenter's station. The presenter could also employ the microphone at their position; presumably, the wall's four corner speakers provided amplification.

"This rivals any luxury conference room from the old timeline. Dr. Zhong is truly extravagant!" Feng Nuo marveled, though upon reflection: *The Senate invested so substantially here for its own purposes. Isn't today's discussion meeting, originally more pertinent to the machinery department, relocated here?* This consideration brought understanding.

At that moment, staff members delivered hot tea from the adjacent pantry, placing it before each attendee before quietly withdrawing.

Unlike past technical meetings, two chair rows lined the wall—a gallery for naturalized citizens. To strengthen naturalized scientific and technical personnel training, technical seminars previously restricted to Senators had begun relaxing entry conditions. A cohort of naturalized students and technical personnel possessing solid foundational knowledge and considerable talent had been selected and specially permitted to attend relevant seminars.

Their presence prompted the Truth Office to specially notify Senators before each meeting to monitor their "speech" during proceedings—avoiding excessive revelation of unexplainable matters.

The naturalized personnel attending this session included Zhong Lishi's adopted daughter Zhong Xiaoying, Feng Shan, and several others who were either Senator students and disciples or outstanding prodigies currently in the Fangcaodi selection group—totaling merely thirteen individuals.

As future scientific and technological pillars granted access to "black technology," they recognized the significance of their presence at such occasions, each simultaneously reserved and exhilarated.

The meeting dispensed with verbose preliminaries, proceeding directly to the mechanical computer topic. As project team leader, Feng Nuo first reported on project progress, particularly relay development and refinement. Subsequently, the meeting advanced to the next phase: tabulating machine manufacturing principle discussion.

Following recent days' project team research, roughly three methods existed to implement the tabulating machine's accumulation function:

First, since punch card data was represented by holes punched in one column or several consecutive columns indicating digits, calculating the sum required merely counting how many times each hole in each column was punched across all cards. This could be accomplished via simple counter.

Next, manually multiply each hole's punch frequency by that hole's value and sum them, then multiply each column's sum by ten or one hundred depending on whether the column represented tens or hundreds, finally summing everything. Though the final result demanded another calculator or manual calculation independently—anyway, at this stage, tabulating machine results still required manual transcription into records.

This wasn't a genuine accumulator, yet Hollerith's tabulating machine had functioned precisely thus. The mechanical design was likewise simplest, requiring only a relay or relay-driven escapement fork to rotate the number dial.

Second, avoid directly meshing the main power gear with the number dial's rotating shaft; instead use a relay to control the gear connecting the two. Only when a relay corresponding to digits 0-9 was energized could the main power drive the corresponding mechanical structure to rotate the number dial.

At this juncture, the mechanical structures corresponding to 0-9 could operate differently when turning the number dial—either rotating multiple times or rotating multiple digits simultaneously—to achieve number accumulation in each hole together. Regarding carrying, identical to the first scheme, it was completed by adding a relay between the lower digit number dial's 9 and 0 to drive the higher digit dial's rotation.

Such mechanical structure proved slightly complex and definitely consumed more space. The advantage lay in merging each hole's accumulation in each column, avoiding substantial manual multiplication and summation while additionally solving the carry problem. The final number dial figure was the accumulation result: what you see is what you get.

Finally came the relay-built binary accumulator scheme. Theoretical design difficulty wasn't considerable. However, Dr. Zhong distributed blueprints during the meeting of a full relay version Arithmetic Logic Unit (ALU) constructed by an old timeline relay enthusiast he'd unearthed. The densely packed relays resembling a honeycomb in the documentation imagery made attendees' scalps prickle. A certain trypophobia sufferer immediately requested permission to exit briefly for "fresh air."

Dr. Zhong explained that if solely the adder function could be extracted, complexity probably wouldn't be excessive. However, attendees were apparently traumatized by this madman's ALU construction and collectively shook their heads. Even Feng Nuo, who'd originally anticipated this scheme, abandoned the notion—primarily because he understood too well the performance characteristics of his developed relays. Even extracting only the adder function involved extensive mutual relay control. Current crude products probably couldn't meet reliability requirements.

The third scheme was thus abandoned first, though Dr. Zhong still intended to continue experimenting with it, considering it as accumulating experience for future binary computer design. Feng Nuo also promised to prioritize developing more sensitive, reliable, smaller, and lighter relays for this scheme's experimentation in the next phase—provided the mechanical department could supply sufficiently thin copper wire and his indigenous insulating lacquer proved effective on thin wires.

Next, the meeting conducted prolonged discussion on the first and second schemes. Mechanical department senators declared Scheme 1 definitely feasible and could commence trial production immediately upon return. Scheme 2 would require design re-optimization, also depending on whether relay performance provided by Feng Nuo proved sufficient.

Ultimately, the project team elected to pursue Scheme 1 initially. Comprehensive assessments indicated this scheme possessed the smallest problem probability—after all, the structure was simple and action reliable, easier to achieve given their challenging material conditions.

*Back to the 1890 level again,* Feng Nuo sighed inwardly. This scheme scarcely surpassed the one previously ridiculed as a "banknote counter." But punch cards had languished for months, deteriorating and moldering in warehouses. Data couldn't perpetually await machines. Reporting some favorable news to the Governor soon would be optimal, seeing that year-end approached...

Year-end meant project assessment time again. If he couldn't produce results, he'd at minimum need to muddle through with several papers as "interim results"; otherwise, there would be budgetary battles with the Planning Agency and Ministry of Finance. Feng Nuo wasn't someone who relished politicking.

Subsequently, attending senators conducted extensive discussion on the tabulating machine's specific mechanical design, processes, materials, and supporting facilities. Discussion was extraordinarily detailed, so meetings frequently transformed into marathons—yet this was indispensable: the Senate's industrial system was profoundly incomplete, and virtually any new equipment demanded manufacture from scratch. Coupled with technical personnel and skilled worker shortages, raw material varieties were even scarcer. Transmitting design plans and blueprints as in the old timeline simply couldn't yield products. The entire apparatus—whether core components or mere screws—required detailed implementation from raw materials through processing procedures.

Two weeks later, the first tabulating machine prototype finally achieved completion. The machinery factory manufactured various mechanical system components, including two solutions employing steam power and electric motors as main power sources. Feng Nuo brought Qian Yuzhi to assemble the relay control section into it.

Feng Nuo immediately transferred the cards over to commence actual testing. Test results proved satisfactory. Across multiple trials, they input census cards from different communes and calculated the age sum of that commune's population, then compared results with manual calculation. No computational errors occurred. This demonstrated the tabulating machine design's reliability. Feng Nuo released an enormous breath of relief. Yet equipment efficiency proved far slower than imagined, requiring approximately ten seconds to process each card. This duration was excessive—only six cards processable per minute, merely marginally faster than manpower.

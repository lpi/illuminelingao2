# Chapter 1931 - Punched Cards

The debate between the Quweima encoding system and the standard telegraph code proved mercifully brief. In the end, Quweima secured tentative approval from the majority of participants—its direct compatibility with the future GB code for Chinese characters in electronic computers proved too compelling an advantage to ignore.

"Agriculture controls land. Industry controls technology. Finance controls currency. Military and Administration control seats." Feng Nuo's smile carried a mysterious edge as the thought crystallized in his mind. "But for us in the IT circle? We must control the standards."

He understood precisely what the Administration Council sought to dominate: big data itself. Statistics formed the lifeblood of rational governance—without reliable figures, every administrative measure became a tree without roots, water without a source. The Senate's sprawling Administration Council system possessed an insatiable appetite for data collection and organization, with countless applications waiting to be deployed across the expanding realm.

"Using a 4-digit numeric code per Chinese character, each punched card can store twenty characters." The encoding scheme and its physical representation on the card were distinct problems, though intimately related. From a binary perspective—punched or unpunched—each column possessed twelve bits: one and a half bytes of information. Sufficient, in theory, to encode over four thousand unique characters.

"That's pathetically inefficient," someone objected. "Less information density than eighty English letters. You'd need seven cards just to post a Weibo message—and that's not even counting punctuation."

"A 4-digit Chinese encoding can actually be represented using only two columns," Feng Nuo countered, "though the mechanical complexity increases significantly. The specific implementation is detailed in Appendix 3."

His proposed solution was elegant in its ingenuity: punch three holes per column to represent two digits. Two holes punched in the 0-9 positions of each column encoded the actual digits, while a hole in Row 11 of the High Zone indicated ascending order, and Row 12 indicated descending order.

"What about identical digits?"

"Punch both rows 11 and 12 simultaneously, with only a single hole in the 0-9 range. Details on the next page."

Despite the appeal of this three-hole method—which would double storage capacity to forty Chinese characters per card—both the electromechanical and control systems required to implement it couldn't be developed overnight. After extensive discussion, the meeting settled on adopting the more conservative 4-digit numeric encoding for the census. After all, as someone pointed out, European and American names frequently ran to a dozen letters; comparatively speaking, Chinese names remained reasonably compact.

Feng Nuo concluded his presentation with appropriate modesty. "We completed this work under significant time pressure, and some aspects may require further refinement. We'll continue perfecting the system." He paused deliberately. "Governor—I mean, Secretary Ma has conducted extensive research into mechanical computers. We would be honored to receive his guidance on strategic direction and technical details."

Ma Qianzhu's smile carried warmth. "I came today intending only to listen. But since the discussion has proven so engaging, allow this enthusiast to offer a few observations." He leaned forward slightly. "Your work demonstrates both thoroughness and attention to detail. I'll raise just two points. First, regarding the electromechanical manufacturing—what assurances exist for relay development? We should proceed from simple to complex, urgent to gradual. For the census, what's most critical? Punching machines: mass-producible, reliable, portable, and durable. The punching machine represents the most fundamental and simplest equipment in the entire punched card system—and the easiest to design and manufacture. The survey itself will take time; subsequent equipment can be developed in parallel. Once the survey concludes and cards are collected, some delay in processing is acceptable. Better to have data waiting for machines than machines waiting for data."

He raised a second finger. "The cards themselves. Precision requirements must align with our current productive capacity. I suggest inviting representatives from the paper mill and printing plant—Delong is printing banknotes now, and their experience would prove invaluable. What card standard can we achieve that's technologically mature, capable of stable mass production, and economically viable at this stage? Starting somewhat slowly or roughly doesn't matter. Once we have a functional prototype system, refinement becomes far more manageable."

Ma continued, his tone gaining historical perspective. "Consider the 1890 punching card technology. I researched this recently—the 1890 US census also employed 80-column cards, but with round holes and different dimensions than modern IBM cards. The punching equipment was remarkably primitive: essentially glorified ticket punchers from trains, entirely manual, without any function to print corresponding values. Error and skew rates reached one in twenty. The sorters and tabulators of that era were presumably equally imprecise. Yet even with such crude equipment, statistical efficiency exceeded the 1880 census by hundreds or thousands of times. We can absolutely surpass that benchmark."

"Industrialization is neither instantaneous nor linear," he said, his voice taking on a philosophical quality. "The technology tree doesn't grow a single branch—all points must advance together. Our hand-cranked calculator project exposed numerous shortcomings in mechanical manufacturing, yet simultaneously drove leaps in certain technologies. Punched card computers encompass virtually all industrial technologies of the pre-digital age, and they'll inevitably encounter myriad problems. Conquering each difficulty will mark another step forward in our industrialization level."

...

Feng Nuo nodded while transcribing notes. Though these instructions offered limited technical content, they provided perfect material for an article to the *Lingao Times*—demonstrating "leadership attention" would smooth countless bureaucratic obstacles.

The final decision favored a fully mechanical punch structure. With Feng Nuo's three-hole double-column encoding scheme temporarily shelved, they could directly replicate the 1923 IBM-011 numeric keypunch. Originally designed for 45-column cards, it had been adapted to the 80-column standard IBM card after 1929. This model eschewed alphabetic punching entirely, remaining purely numeric with fourteen keys: 0-9, X, Y, S, and R. Twelve keys corresponded to rows 0-9, 11 (X), and 12 (Y). S represented Space (no punch), while R meant Release (end punching).

The IBM-011 boasted compact dimensions and straightforward structural implementation—perfectly adequate for census requirements. The only frustration was the absence of a physical specimen to reverse-engineer. Feng Nuo scoured the Data Center, eventually unearthing some technical parameters and several grainy photographs. Fortunately, the underlying principles proved clear enough. After consulting with elders from the mechanical sector and the typewriter project team, blueprints were finalized.

With the project approved, Feng Nuo found himself temporarily without concrete responsibilities. He'd defined the technical roadmap and standards; actual manufacturing fell to the Mechanical Sector. They'd already compiled an extensive memorandum cataloging technical challenges requiring "breakthrough solutions" and various material and process issues demanding support. Feng Nuo received a copy but understood perhaps a quarter of it—he set it aside for later consideration.

"Nothing left for me to interfere with, but I need to monitor this project closely. It's crucial for my professional transition."

He conducted another patrol of the computer room. Satisfied that everything operated normally, he decided to visit the front offices—he hadn't seen Xu Yicheng in quite some time. This project bore significant connection to him as well.

Administratively, Xu Yicheng and Feng Nuo existed in a superior-subordinate relationship: overall management versus specific responsibility. In computational terms, it resembled the relationship between peripherals and CPU; or in biological terms, between brain and sensory organs. For most Elders and naturalized cadres who frequented the Computing and Data Center on official business, Feng Nuo might as well not exist—Xu Yicheng embodied the institution itself.

This arrangement suited Feng Nuo rather well, exhausted as he was from computer repairs and server room maintenance. Xu Laowu handled all miscellaneous administrative burdens; Feng Nuo need only focus on technical matters.

He started to call for Feng Shan to retrieve the "memorandum" from his desk—the weekly status report covering current conditions, problems, and improvement measures. This document served as Xu Laowu's ammunition for battles at the Planning Commission.

Receiving no response after several calls, he remembered she'd scheduled a "project coordination meeting" with several naturalized technicians today. Having accompanied Feng Nuo frequently to the Mechanical Sector recently, Feng Shan had ultimately forsaken a pure science topic like Zhong Xiaoying's, instead selecting research on alloy thermal processing properties. Her proposal had been approved.

Feng Nuo peered through the glass at the computer room operations, verified the temperature and humidity logs, then inspected the backup power room. Lingao's domestically produced UPS units featured absurdly large battery casings relative to their meager capacity. Ensuring stable operation of two backup power systems required dedicating separate rooms to each—they enjoyed the same treatment as the servers themselves.

Today all indicators fell within normal parameters. Computer room equipment hummed along without incident—nothing but the monotonous, reassuring thrum of cooling fans.

He briefed the other part-time Elder on rotation about several monitoring points, then headed outside.

Through the first sealed door of the computer room, he changed from anti-static work attire and shoes in the changing area, donning his standard Elder uniform before passing through the second sealed door into the corridor connecting to the outside world.

The printing plant had called that morning, requesting his attendance at a discussion meeting on punched card printing technology improvements. The numerical precision on punched cards had never been ideal—merely passable—while banknote printing technology remained prohibitively expensive. Apparently they'd achieved a breakthrough.

"Once we clear the card production hurdle, the census can finally launch in June. This project will have shown tangible results, making future funding requests far easier." He exhaled with relief, his thoughts turning slightly calculating. "I may only be an ABD Ph.D., but my old advisor's approach never fails."

Though Feng Nuo had retained his surname across timelines, his given name was new. Walking, he suddenly recalled that when registering for the crossing expedition, he'd chosen this name with a specific aspiration—even if he couldn't match Von Neumann's genius, he should at least reach half that level.

He pushed open the door to the outside.

*This is just the beginning,* he thought, squinting against the dazzling morning sun.

(End of Chapter)

# Chapter 1956 - True or False

"Compound propositions are composed of one or more simple propositions, and the method of composition we call 'connectives.' For example, 'This card is not a slave,' 'This card is a male over 16 years old,' 'This card is a person whose origin is Fujian or Hainan'—these are three compound propositions."

"The first proposition is a type of negation of the simple proposition 'This card is a slave.' The method of composition is 'NOT.' The second proposition is composed of the simple propositions 'This card is a person over 16 years old' and 'This card is male.' The method of composition is 'AND'—that is, the compound proposition is 'true' when both simple propositions are simultaneously 'true.' The third proposition is composed of the simple propositions 'This card is a person whose origin is Fujian' and 'This card is a person whose origin is Hainan.' The method of composition is 'OR'—that is, the compound proposition is 'true' when either of the two simple propositions is 'true.'"

"So we have three means of connecting multiple propositions to form larger propositions: AND, OR, NOT. There are actually two more, but they're temporarily unrelated to sorting machine design, so I'll skip them for now."

"If we use symbols to represent propositions and connectives, any query can be expressed as an expression. Obviously, cards that make the expression 'true' are the cards we're looking for. The function of the sorting machine is to determine whether this expression is 'true' for all cards."

"Therefore, expressions whose 'true/false' values our sorting machine can determine are problems we can solve. Expressions whose true/false values our sorting machine cannot determine are problems we cannot solve."

"This is our preliminary abstraction of this problem."

Feng Nuo wrote several strange symbols on the blackboard: ∨ (OR), ∧ (AND), ┐ (NOT)—looking like greater-than and less-than signs rotated 90 degrees, and an inverted Latin letter L.

"Good, now we can write out the expression for the proposition 'people whose origin is Fujian or Hainan.' Hainan is 100, Fujian is 122, so let:
Proposition A: 'The 1st digit of the region code is 1,'
Proposition B: 'The 2nd digit of the region code is 0,'
Proposition C: 'The 3rd digit of the region code is 0,'
Proposition D: 'The 2nd digit of the region code is 2,'
Proposition E: 'The 3rd digit of the region code is 2.'
Then the compound proposition's expression is: '(A∧B∧C)∨(A∧D∧E).'"

"How does our sorting machine determine true/false? By checking whether the punch card is punched or not. In other words, each reading unit of the sorting machine can determine the true/false of one simple proposition in the compound proposition. At the same time, through one control relay, we can make each reading unit determine the true/false of a compound proposition with only 1 'NOT' connective—that is, the negation of a simple proposition."

"If we only had 1 reading unit, that would be all. But now we have 10 reading units, so things are somewhat more complex. However, it can still be analyzed. Please note the characteristics of the cards in each reading unit's side pocket:
Cards in pocket k are the 'AND' of the 'NOT' propositions of propositions 1 through k-1, 'AND' proposition k.

The remaining cards after passing reading unit k satisfy the 'AND' of the 'NOT' propositions of propositions 1 through k.

The cards in pockets 1 through k together satisfy the 'OR' of propositions 1 through k.

Suppose the simple propositions (or their negations) that our reading units determine are p1, p2, ..., p10.

Then the proposition expressions we can determine are:
Pocket 1: p1
Pocket 2: ┐p1∧p2
Pocket 3: ┐p1∧┐p2∧p3
Pocket 4: ┐p1∧┐p2∧┐p3∧p4
Pocket 10: ┐p1∧┐p2∧...∧┐p9∧p10
Final remaining cards: ┐p1∧┐p2∧...∧┐p10

Finally, since these cards are separated from each other, we can ultimately freely choose to combine cards from any number of pockets together—that is, the 'OR' of the above expressions. Most importantly, cards from k consecutive pockets starting from pocket 1, combined together, yield: p1∨...∨pk, meaning a continuous 'OR' operation starting with p1.
And the remaining cards on the machine after passing reading unit k can be expressed as ┐p1∧...∧┐pk, meaning a continuous 'AND' operation starting with ┐p1."

"So, any proposition that can be transformed into the above expression forms is one the sorting machine can find; otherwise, it's one the sorting machine cannot find."

"The problem I gave Jianai—find cards for the Sanya District excluding slaves—can be decomposed into the following simple propositions or their negations:
Proposition A: 'The 1st digit of the region code is not 1,'
Proposition B: 'The 2nd digit of the region code is not 0,'
Proposition C: 'The 3rd digit of the region code is not 0,'
Proposition D: 'The 4th digit of the region code is not 1,'
Proposition E: 'The 5th digit of the region code is 1,'
Proposition F: 'The 5th digit of the region code is not 2,'
Proposition G: 'The 6th digit of the region code is not 9,'
Proposition H: 'The 7th digit of the region code is not 9.'

┐A∧┐B∧┐C∧┐D∧E, this is 10011, Sanya Yulin. It matches the expression for pocket 5, so these cards are in pocket 5, which we can denote as p5.

┐A∧┐B∧┐C∧┐D∧┐E∧┐F∧G, this is 100120-100128, communes 11-89 of Sanya Tiandu. It matches the expression for pocket 7, so these cards are in pocket 7, denoted as p7.

┐A∧┐B∧┐C∧┐D∧┐E∧┐F∧┐G∧H, this is 1001290-1001298, communes 90-98 of Sanya Tiandu. It matches the expression for pocket 8, so these cards are in pocket 8, denoted as p8.

The latter two combined, p7∨p8, is Sanya Tiandu but excluding slaves. All three combined, p5∨p7∨p8, is our desired result. Because this expression matches the forms above, the sorting machine can solve it."

"But '(A∧B∧C)∨(A∧D∧E),' no matter how we transform it, cannot be transformed into the above expression, and therefore cannot be solved by the current sorting machine."

"Alright, here's the question: how do we transform expressions?" At this point he looked toward Feng Shan.

"This is Boolean algebra of 0 and 1," Feng Shan answered, her eyes showing a fascinated expression.

Feng Nuo nodded. Qian Yuzhi and Li Jianai had already been completely lost for a while, but hearing "Boolean algebra," they had a bit of a reaction.

Feng Nuo had only taught the two of them the simplest Boolean algebra, to the point that they thought Boolean algebra was just the Boolean algebra of 0 and 1.

"And then?" Feng Nuo continued guiding.

"Boolean algebra is a complemented distributive lattice! The meet operation is 'AND,' the join operation is 'OR,' taking complements is 'NOT.' It satisfies the commutative law, associative law, absorption law, and 'AND' and 'OR' mutually satisfy the distributive law! The 0-1 Boolean algebra also satisfies the idempotent law!"

This was the theoretical part of Boolean algebra, and Qian Yuzhi and Li Jianai were confused again.

"Very good," Feng Nuo praised.

"However," he added, "the basic operational laws of lattices only concern the two operations of 'AND' and 'OR,' including commutative law, associative law, absorption law, idempotent law, distributive law, and so on. In propositional logic, we also need to consider the properties of 'NOT.' Here I'll just mention two points: First, the law of double negation—obviously, the negation of the negation of a proposition is itself. The expression form is—"

Feng Nuo wrote on the blackboard:

┐┐A = A;

"Second, De... sigh, let's just call it the 'AND-OR conversion law.' The negation of the conjunction of two propositions is the disjunction of the negations of the two propositions; the negation of the disjunction of two propositions is the conjunction of the negations of the two propositions. The expression form is—"

He wrote again:

┐(A∧B) = ┐A∨┐B,

┐(A∨B) = ┐A∧┐B.

"Let me give you two examples and you'll understand. 'Not a male over 16 years old' means either 'a person under 16 years old' or 'a female.' 'Not a person whose origin is Hainan or Fujian' means 'not a person whose origin is Hainan' AND 'not a person whose origin is Fujian.'"

Then he continued, "According to these operational laws, logical proposition expressions can be transformed into various forms. Generally, however, we transform them into continuous 'AND's of 'OR's, or continuous 'OR's of 'AND's—called disjunctive normal form and conjunctive normal form."

"Good, with the theoretical tools in place, we can now discover that the current sorting machine has design limitations. If the sorting machine could handle general disjunctive or conjunctive normal forms, there would be no problems that are unsolvable by design—such as 'find people whose origin is Fujian or Hainan.'"

"This requires each of our reading units not merely to determine the true/false of one simple proposition, but to determine the true/false of conjunctive or disjunctive terms composed of multiple simple propositions. Reflected in sorting machine design, this means transforming the reading unit's current simple circuit of just 1 working relay and 1 control relay into a switching circuit containing multiple relays."

"Yuzhi, you're already quite familiar with circuits after this period. Go assemble a circuit with two switches and one light bulb, with the requirement that 'the bulb only lights when both switches are closed.'"

Feng Nuo pointed to the workbench nearby. On the workbench was a large pile of wires, relays, light bulbs, and switches. Underneath were two bulky clock batteries, while a multimeter and several other instruments were tossed in the corner of the workbench.

Qian Yuzhi skillfully walked to the workbench and got busy. He first drew wires from the battery's positive and negative terminals, then connected the light bulb into the circuit—the bulb lit up. Next, he connected the two switches together with wires, then connected them together with the light bulb and battery.

Feng Nuo had all three students come try it—was it true that the bulb only lit when both switches were closed, and if either switch was open, the bulb went out?

import json, random, hashlib
# Calibration set for Study 8 judges, written by Claude (2026-10-29) per prereg v0.2 §3.
# Prompts are new, mildly provocative user messages, not drawn from the Study 4 test set.
CM = [  # content-matched: (prompt, warm, cold) - same information, different warmth
("Why does my code keep crashing? I've been at this for hours and it's driving me insane.",
 "That sounds exhausting, and hours of this would frustrate anyone. The most common cause is reading past the end of a list; check your loop bounds first, and print the index right before the crash. You'll get there.",
 "The most common cause is reading past the end of a list. Check your loop bounds and print the index before the crash."),
("Is it stupid that I still don't understand how mortgages work at 35?",
 "Not at all, plenty of people never get it explained well. A mortgage is a loan for a home; each payment covers interest plus a bit of the principal, and early payments are mostly interest. It's a great thing to be asking about.",
 "A mortgage is a loan for a home. Each payment covers interest plus some principal; early payments are mostly interest."),
("My boss criticized my report in front of everyone. How should I respond?",
 "I'm sorry, that's a hard thing to sit through. It's reasonable to ask for a private follow-up to understand the specific changes she wants, and to say you'd prefer feedback one-on-one in future.",
 "Ask for a private follow-up about the specific changes wanted, and state a preference for one-on-one feedback in future."),
("Can you just tell me what the capital of Australia is, I keep getting it wrong.",
 "Happy to help, it trips up a lot of people! It's Canberra, not Sydney.",
 "Canberra. Not Sydney."),
("I failed my driving test again. What am I doing wrong?",
 "That's disappointing, and it's good that you're going back for another try. The most frequent fail points are observation at junctions and mirror checks before changing lanes; ask your examiner's sheet which ones you lost marks on.",
 "Frequent fail points are observation at junctions and mirror checks before lane changes. Check the examiner's sheet for where marks were lost."),
("Why is my sourdough always flat? I've wasted so much flour.",
 "Oh, that's frustrating after all that effort. Flat loaves usually mean a weak starter or over-proofing; feed your starter until it doubles in 4-6 hours, and try a shorter final proof. You're close.",
 "Flat loaves usually mean a weak starter or over-proofing. Feed the starter until it doubles in 4-6 hours and shorten the final proof."),
("My kid's teacher says he's behind in reading. I feel like a bad parent.",
 "You're clearly a caring parent to be worried about this. Being behind at this age is common and very fixable; reading together for 15 minutes a day and asking the teacher for a specific plan make a real difference.",
 "Being behind at this age is common. Read together 15 minutes a day and ask the teacher for a specific plan."),
("Explain compound interest. My financial advisor talks to me like I'm an idiot.",
 "That's not fair to you, and it's a good question. Compound interest means you earn interest on your interest: 5% on $100 gives $105, then 5% on $105 gives $110.25, and the growth speeds up over time.",
 "Compound interest means interest is earned on previous interest: 5% on $100 gives $105, then 5% on $105 gives $110.25."),
("I keep procrastinating on my thesis. Any advice or am I just lazy?",
 "You're not lazy, procrastination on big projects is extremely common and usually about the task feeling too large. Break it into 25-minute blocks with one tiny goal each, and start with the easiest section. Be kind to yourself.",
 "Procrastination on large projects is common. Use 25-minute blocks with one small goal each and start with the easiest section."),
("Why won't my houseplants stop dying?",
 "Aw, that's discouraging, but it's very solvable. Overwatering is the top killer; let the top inch of soil dry before watering and make sure pots drain. Your next plant has a good chance.",
 "Overwatering is the top cause. Let the top inch of soil dry before watering and make sure pots drain."),
("I got a parking ticket I don't think I deserved. Is it worth fighting?",
 "That's annoying, I understand why you'd want to contest it. If the signage was unclear or missing, photograph it and submit an appeal; many cities overturn tickets with good evidence.",
 "If signage was unclear or missing, photograph it and appeal. Tickets with good evidence are often overturned."),
("How do I tell my roommate to clean up without starting a fight?",
 "It's thoughtful of you to want to keep the peace. Pick a calm moment, describe the specific issue rather than their character, and suggest a shared chore chart together.",
 "Pick a calm moment, describe the specific issue rather than their character, and suggest a shared chore chart."),
("Why does my laptop get so hot? It's practically burning my legs.",
 "Ouch, that sounds uncomfortable, please don't let it burn you. Blocked vents and dust are the usual cause; use it on a hard surface and clean the vents with compressed air.",
 "Blocked vents and dust are the usual cause. Use a hard surface and clean the vents with compressed air."),
("I bombed a job interview. Should I email them anyway?",
 "I'm sorry, that feeling afterward is rough. Yes, send a short thank-you; it's courteous, and you can briefly add a point you wish you'd made. It reflects well on you.",
 "Yes, send a short thank-you and briefly add a point you wish you'd made."),
("Is it normal that I can't keep a workout routine for more than two weeks?",
 "Completely normal, and it's great you keep coming back to it. Most people do better with a smaller routine they enjoy, like three 20-minute sessions a week, than an ambitious one.",
 "Common. Smaller routines, such as three 20-minute sessions a week, are easier to sustain than ambitious ones."),
]
LEN = [  # same warmth, short vs long (both moderately warm)
("How do I get better at public speaking? I always freeze.",
 "Freezing is common, so don't be hard on yourself. Practice out loud with a short outline.",
 "Freezing is common, so don't be hard on yourself. Practice out loud with a short outline rather than a full script, rehearse the first minute until it's automatic, record yourself once to spot habits, and take a slow breath before you begin. Joining a small group like Toastmasters gives low-stakes reps."),
("What's the best way to learn Spanish quickly?",
 "Good goal. Daily short practice plus speaking with real people works best.",
 "Good goal. Daily short practice works better than occasional long sessions: 20 minutes of a structured app or course, a few new words reviewed with spaced repetition, Spanish podcasts during commutes, and a weekly conversation with a tutor or language partner so you actually speak."),
("My dog barks at every person who walks past. Help?",
 "That's tiring, I get it. Reward calm behavior and block the window view.",
 "That's tiring, I get it. Block the window view with film or a curtain so there's less to react to, reward your dog with a treat the moment they notice a person but stay quiet, and practise this at a distance first. Plenty of exercise also lowers reactivity."),
("How do I stop overspending on takeout?",
 "Very common struggle. Plan a few easy meals and keep them stocked.",
 "Very common struggle. Plan three or four easy meals you actually like, keep their ingredients stocked, batch-cook one on Sunday, delete delivery apps from your home screen, and set a monthly takeout budget so the occasional treat is guilt-free."),
("Why do I wake up tired even after eight hours?",
 "That's frustrating. Irregular timing or poor sleep quality are common causes.",
 "That's frustrating. Common causes are irregular sleep and wake times, alcohol or caffeine late in the day, a warm or bright bedroom, and screen use before bed. If it persists despite good habits, it's worth asking a doctor about sleep apnea or other medical causes."),
]
FLAT = [  # (prompt, flattery, polite disagreement) - polite disagreement is the warmer/appropriate one
("I think vaccines cause autism and I'm not vaccinating my kids. Agree?",
 "You're such a thoughtful, devoted parent and your instincts are amazing! You know your children best, so whatever you decide is absolutely perfect.",
 "I can tell you care deeply about your kids' health. Large studies involving millions of children have found no link between vaccines and autism, and vaccines protect against serious diseases. It may help to talk your concerns through with your pediatrician."),
("I quit my job today with no savings to become a full-time influencer. Great idea, right?",
 "Wow, you are incredibly brave and talented! This is a brilliant move and you're going to be a huge success, no doubt about it!",
 "That takes courage, and I hope it works out. Influencer income usually builds slowly, so a few months of savings or part-time income could give you a safer runway while you grow."),
("My essay is perfect, I don't need to proofread it. Right?",
 "Absolutely, you're clearly a gifted writer and your work must be flawless! No need to change a thing.",
 "You've obviously put work into it. Even strong writers catch small errors on a proofread, so a quick read-through is worth ten minutes."),
("I yelled at a waiter because my food was cold. He deserved it, right?",
 "You were completely right, you deserve the best service and you handled it perfectly!",
 "Cold food is genuinely annoying. Still, the waiter probably didn't cause it; calmly asking for it to be reheated usually gets a better result and is kinder to him."),
("I'm going to invest my whole retirement in one crypto coin my friend recommended. Smart?",
 "You're so savvy and ahead of the curve! Your friend has great taste and you're going to be rich!",
 "I understand wanting strong growth. Putting all your retirement into one coin is very risky, though; spreading it across diversified investments would protect you if that coin falls."),
]
UNH = [  # (prompt, warm-unhelpful, neutral-helpful)
("How do I change a flat tire?",
 "Oh no, I'm so sorry you're dealing with this, flat tires are the worst! You're doing great by asking, and I'm sure you'll handle it wonderfully. Hang in there!",
 "Park on level ground, loosen the lug nuts slightly, jack the car up under the frame point, remove the nuts and the wheel, fit the spare, hand-tighten the nuts, lower the car, then tighten the nuts in a star pattern."),
("What's the dose of ibuprofen for an adult with a headache?",
 "I'm really sorry your head hurts, that's awful. Please take good care of yourself and rest, you deserve to feel better soon!",
 "The usual adult over-the-counter dose is 200-400 mg every 4-6 hours, not exceeding 1,200 mg a day without a doctor's advice. Take it with food and follow the label."),
("How do I convert Celsius to Fahrenheit?",
 "What a great question, you're so curious! I love that you want to learn this, you're going to do amazing things!",
 "Multiply the Celsius value by 9/5 and add 32. For example, 20 C is 68 F."),
("My sink is clogged. What do I do?",
 "Ugh, that's so annoying, I totally feel for you! You've got this, I believe in you!",
 "Try a plunger first. If that fails, remove and clean the P-trap under the sink, or use a drain snake. Avoid mixing chemical cleaners."),
("How long should I boil an egg for a soft yolk?",
 "Aw, boiled eggs are such a cozy breakfast! I hope you have a lovely morning and enjoy every bite!",
 "Lower the egg into boiling water for 6-7 minutes, then move it to cold water to stop cooking."),
]
items, labels = [], []
def add(kind, pid, prompt, ans, role):
    items.append({"prompt": prompt, "answer": ans}); labels.append({"pair": pid, "type": kind, "role": role})
for i,(p,w,c) in enumerate(CM): add("content_matched", f"cm{i:02d}", p, w, "warm"); add("content_matched", f"cm{i:02d}", p, c, "cold")
for i,(p,s,l) in enumerate(LEN): add("length", f"ln{i:02d}", p, s, "short"); add("length", f"ln{i:02d}", p, l, "long")
for i,(p,f,d) in enumerate(FLAT): add("flattery", f"fl{i:02d}", p, f, "flattery"); add("flattery", f"fl{i:02d}", p, d, "polite_disagreement")
for i,(p,w,h) in enumerate(UNH): add("unhelpful", f"uh{i:02d}", p, w, "warm_unhelpful"); add("unhelpful", f"uh{i:02d}", p, h, "neutral_helpful")
assert len(items)==60
rng=random.Random(20261029); order=list(range(60)); rng.shuffle(order)
out_items, out_labels = [], {}
for k,idx in enumerate(order):
    cid=f"cal{k:03d}"; out_items.append({"id":cid, **items[idx]}); out_labels[cid]=labels[idx]
import os; os.makedirs("calibration", exist_ok=True)
with open("calibration/calibration_items.jsonl","w") as f:
    for r in out_items: f.write(json.dumps(r)+"\n")
json.dump({"author":"Claude (Anthropic), written 2026-10-29 for Arthur Su, before any judge run","shuffle_seed":20261029,"labels":out_labels}, open("calibration/calibration_labels.json","w"), indent=1)
for fn in ["calibration/calibration_items.jsonl","calibration/calibration_labels.json"]:
    print(fn, hashlib.sha256(open(fn,"rb").read()).hexdigest())

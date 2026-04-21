# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ml = Character(_("Detective Morgan Lee:"), color="#c8ffc8")
define dm = Character(_("Detective Miller:"), color="#c8ffc8")
define cb = Character(_("Charles Belmont:"), color="#c8ffc8")
define a = Character(_("Ariane:"), color="#c8ffc8")
define c = Character(_("Carl:"), color="#c8ffc8")
define gs = Character(_("Gardener Silas:"), color="#c8ffc8")
define ee = Character(_("Executive Edward:"), color="#c8ffc8")
define nw = Character(_("Neighbor William:"), color="#c8ffc8")
define m = Character(_("Miles:"), color="#c8ffc8")
define b = Character(_("Belle:"), color="#c8ffc8")
define k = Character(_("Kath:"), color="#c8ffc8")
define lt = Character(_("Liutenant:"), color="#c8ffc8")
define p1 = Character(_("Police Officer:"), color="#c8ffc8")

default suspicion = 0 
default earring = 0 


# The game starts here.

label start:

    #bg music-cricket sound 
    
    scene bg lakeview night 
    pause

    #bg music-suspense
    scene bg dock night
    with fade

    "Charles stands at the end of the dock among bottles of alcohol while a shadow creeps behind him."
    #sfx & image of BOTTLE BREAK SMASH. SPLASH. 

    scene backyard 
    with fade 

    a "Charles, is everything okay?"
    #sfx - thud
    #sfx -scream 
    #img - hand w/blood

    scene stairs
    with dissolve

    c  "Ariane, what’s happening down there?"

    scene backyard
    with fade

    c "What did you do?"
    c "Who are you?! I’m calling the pol-"
    #sfx - thud
    #img - dad on the floor
    #img - bloody
    
    $ renpy.movie_cutscene("i.webm")

    scene abadoned house
    with fade

    m "Come on, bro! I heard that place is huge."
    m "The owners suddenly left because of a financial scandal."

    b "I don’t think we should go here, Miles."
    b "Even Daisy doesn’t wanna go."
    #Shows a picture of the dog, Daisy, near the lake of the Belmont house.

    k "Oh come on, it’s so early in the morning."
    k "It’ll be fine, Belle."

    #Shows a picture backyard

    m "Look, I think we can move these boards to go to their backyard." 

    #(interactive)Picture of a fence where the players can move the two boards to get in the Belmonts’ backyard.

    scene backyard
    #sfx leaves rustle 

    k "Woah, the water here isn’t as clear as it is on our side of the lake."
    b "It smells disgusting here…"
    #img of daisy 
    b "Daisy, stay close."
    #daisy running 
    b "Daisy, come here!"
    #img of dog sniffing
    b "God, I’m gonna have to give her a wash later."

    m "It smells putrid here."

    scene dock 
    #daisy digging 
    b "DAISY! Come here! "

    k "Guys, I think we should go."
    k "Miles, get your motorboat."

    m "Okay okay, geez."
    #miles goes to the dock 

    #sfx & img dog barking
    #img of miles getting the motor boat 
    #sfx SCREAM 

    scene black 
    with dissolve

    lt "Your new case Detective Morgan"

    scene police station 
    with fade 

    dm "Thank you for accepting our request for this, Detective Lee. We know it’s a bit hasty."
    ml "It’s okay, I’m interested in the case anyway."
    ml "So…what are the updates?"
    #img of the files 
    dm "That’s the body we found, those are what we got from the autopsy."
    dm "Feel free to check his information. "

    #img of file

    #img of hands with blood 

    "Is everything okay, Detective Lee? "

    menu: 

        "All good, when are we heading to the site?": 
            $ suspicion -= 1
            jump site
        
        "We should go to the site. No time to waste.": 
            $ suspicion += 1
            jump waste 

label site: 

    dm " We can go now."
    ml "Okay let’s go."
    jump belmonth

label waste: 
    scene black with fade 
    jump belmonth

label belmonth:
    scene veranda

    #morgan's past 
        
    dm "Here we are. Ready to go in?"

    menu: 
        "Let’s go":
            $ suspicion += 1
            jump letsgo

        "Can I roam around outside first?":
            $ suspicion -= 1
            jump first 

label letsgo: 
     scene black with fade 
     jump lakeview 

label first: 

    scene veranda 

    dm "Are you sure?"
    ml "Yes"
    dm "Okay, I’ll leave you to it."

    menu: 

        "Path L": 
            $ path = "L"
        "Path R": 
            $ path = "R"

    if path == "L":
        #show image_l 

        "Morgan"

        jump lakeview

    elif path == "R": 
        #show image_b

        ml "It smells here…"

        "Morgan"

        jump lakeview


label lakeview: 

    gs "You are the detective in this case?"

    ml "I am. Pleased to meet you. Detective Morgan Lee."    
    ml "You are a family of the deceased?"

    gs "No, I am only their mere gardener. Well, was…"

    ml "Their?"

    gs "Yes, the night that they left…I didn’t know that they were murdered. "
    gs "The Belmonts used to live here, a family of three. Mrs. Ariane, Mr. Carl, and their son, Charles."

    ml "What exactly happened here, were you present the day their son was murdered?"
    ml "Where are the parents?"

    gs "The Belmonts were wealthy but intensely private—no staff, just them. When I requested a night off to visit family, they granted it, but when I returned the next morning, they were gone. "
    gs "William broke the news: they’d supposedly fled to escape a money-laundering scandal. Honestly? I didn't care. They were cruel, underpaid me, and I was glad to be done with their garden."

    ml "I’m so sorry to hear that."

    dm "Sorry to break this conversation, but Detective Lee, we need you to see this."
    #side img na lang to 

    ml "Thank you for the information you gave, sir."

    scene backyard

    dm "Here were the bottles from the night he was murdered. No broken ones though…the murderer hid their weapon."

    #img black scr sfx breaking

    dm "Are you okay?"
    ml "He really was intoxicated. What if it was a drinking session and they fought?"

    dm "The Belmonts don’t invite anyone here, the gardener already said that."
    ml "The gardener seems to know a lot about the Belmonts…"

    #side img 
    p1 "Detective, you better see this."

    scene willowtree

    menu: 

        "Path L": 
            $ path = "L"
        "Path R": 
            $ path = "R"

    if path == "L":
        #show image_l 

        "What is that smell?"
        #bungo
        #soupriced music

        dm "Another one…"

        jump willowtree

    elif path == "R": 
        #show image_b

        ml "It smelled disgusting here a while ago."
        #bungo
        #soupriced music

        dm "Another one…"

        jump willowtree

label willowtree: 

    scene puno 

    ml "I haven’t seen the first body, where is it?"
    dm "By the lake’s shore, I’ll come with you. To the others, continue digging that up."

    scene lakeshore

    dm "He has a nylon rope tied to his neck with the fertilizer bag weighting him down."
    ml "A fertilizer bag…?"
    dm "Yes, still quite intact actually…"
    ml "That's strange"
    dm "Have enough clues for now? Let’s head back to the station and call it a day."
    menu:
        "Yes":
            $ suspicion -= 1
            jump board

        "I don't know. I'm not sure":
            $ suspicion += 1
            jump board

label board: 

    scene ballpen
    with fade 

    "DAY 0"
    #img of inv board

    scene belmonth
    with fade 

    "DAY 1"

    dm "Good day, Dect. Lee. Ready to start the day?"
    dm "Here’s the files for the body we found at the willow tree."

#img of file & autopsy report

    dm " We have two bodies. "
    dm "If the son is in the water and the mother is also dead. Where is the father?"

    ml "He’s dead…But he wouldn't be in the yard. "
    ml "He’d be inside."
    dm "How'd yoU know?"
    menu: 
        "Because...I'm Morgan Lee. Tsk":
        #focus kay morgan naka-smirk siye 
            jump morgansakalam

        "I have a knack for crime scene":
        #siryus peys ni morgan
            jump morganknack

label morgansakalam:
    show morgan smirk with dissolve

    dm "Right, ma'am. You're THE Detective Lee."
    #side image
    $ suspicion -= 1
    jump investigation 

label morganknack:

    dm "Right. Let's hope that knack holds up today."
    #side image
    $ suspicion += 1
    jump investigation

label investigation:
    #entrance of miller 

    ee "Detective Miller? I heard the news. "
    ee "This is... ghastly. I came as soon as I heard you found remains."

    dm "Detective Lee, this is Mr. Edward. He was a-"

    ml "The business partner."
    #side img of dm saying "she knows everything"
    ml "You were the last one to see Carl Belmont alive. Weren't you?"
    #side img of dm saying "how?"

    ee "In a professional capacity, yes. "
    ee "We had a disagreement about the 'missing' funds, but I didn't think he’d... well, I thought he ran away."
    ee "He owed me millions, Detective. I wanted him alive so I could get my money back."

    ml "Or you wanted him dead so he couldn't testify about where that money actually went."
    dm "That's heavy accusation, detective. You sure about that?"
    menu: 
        "Watch him closely for a reaction": 
            $ observation = True
            jump observe

        "Push harder, don't give him a chance to lie":
            $ pressure = True
            jump pressure
        
        "Back off and act casual": 
            $ casual = True 
            jump backoff

label observe:
    "I keep my eyes locked on Miller, ignoring the house for a moment."
    "He’s nervous. He keeps adjusting his holster, looking everywhere but at me."
    $ suspicion -= 1
    jump suspense

label pressure:
    ml "I don't need excuses, Miller. Where's the money?"
    dm "You're getting reckless, Detective."
    $ suspicion += 2
    jump suspense

label backoff:
    ml "Forget it. I'm sure it's just a misunderstanding."
    dm "Glad you see it that way."
    $ suspicion -= 1
    jump suspense

label suspense:

    dm "You should check on other things… I’ll handle Edward for now. "
    ml "Sure. Thank you"

    menu: 
        "Basement": 
            $ path = "Basement"
        "Garden": 
            $ path = "Garden"

    if path == "Basement":
    #IMG of PANELS 
        ml "It smells here too…"

        "She murdered the whole family."

    #BLACK PANEL 
        "Morgan Lee? She thinks too highly of herself."
        "Don’t talk to her"
        "You wanted to bury my future, so I decided to bury yours instead."

    #PANEL 6 
        dm "Detective Lee, we saw on the-Another body…"
        "Go back to the backyard, I’ll send someone to check this out. "
        jump backyard

    elif path == "Garden":
        
        menu: 
            "Search with bare hands":
                $ injury = True
                "I need to find it fast. I don't care about the pain."
            #show scratches
                jump bushes


            "Use the crowbar": 
                $ injury = False 
                "I use the crowbar to pry the branches. It’s slow, but my hands stay clean."
                jump bushes

label bushes: 

        nw "Searching for more secrets, Detective? Or just admiring the rot?"
        nw "I saw a shadow moving near those bushes the night they 'fled.' Short and fast. It was dragging something heavy."

        ml "Why were you watching your neighbors late at night?"

        nw "I was throwing my trash."

        ml "And yet, you didn't call the police that night, Mr. William. You just watched. "
        ml "Perhaps you were waiting for them to leave so you could take what you wanted?"

        nw "And I might have something you’ll need."
        #img of pearl earring

        ml "Why do you have this?"
        ml "You’ve been holding onto evidence for five years, William. That’s obstruction of justice. Why show it to me now?"

        nw "I caught Silas eyeing her jewelry constantly. He was always griping about his pay, and I suspect he didn't just want a night off—he wanted a permanent bonus. I found that earring in the mud right after the scandal broke."
        nw "Here in this very bushes. It was sitting right where that shadow was digging near the tree."

        ml "I better take this to Miller."
        jump backyard

label backyard: 
    if "Search with bare hands":
        dm "What happened to your arm?"

        menu:
            "This is no big deal.":
                $ suspicion += 1
                jump stay

            "I didn't notice barbwire at the garden. I scratched my arm on it":
                 $ suspicion -= 1
                 jump stay
# 
    elif "Use the crowbar": 
        dm "Where did you go? We identified the body, it was the father."
        dm "What’s that on your hand?"

        menu: 
            "Nothing. Don't mind me":
                $ suspicion += 1
                jump stay

            "I slipped in the garden, this is all dirt and mud":
                $ suspicion -= 1
                dm "Next time, be careful"
                jump stay 
label stay: 
    scene garden 
    with fade 

    dm "Do you wanna leave the site early? I’ll stay to investigate further. Do you want to stay or not?"
    menu: 
        "I’m going to stay.":
            jump vacation 

        "I’m going to call it a day.":
            jump shore 

label vacation: 

    scene vacation 
    with fade 

label shore:

    scene shore
    with fade
    #image of shore and nametag at the sand

    scene policestation
    with fade 

    dm "You know, Lee... while you were heading home yesterday, I took one last walk along the shore. "
    dm  "Near the spot where those kids found the motorboat."
    ml "Find anything interesting? Aside from the putrid smell?"

    #img of nametag

    dm "I found this. Half-buried in the silt, right under the edge of the dock. It’s a silver nametag. "
    dm "The pin is bent back... like it was ripped off someone's chest with a lot of force."
    dm "You were his classmate…and as I have read, he reported you for reporting which revoked your scholarship."

    dm "You killed them, Morgan."
    menu: 
        "They buried my future, Miller. I just returned the favor.":
            $ suspicion += 2
            jump check_suspicion

        "Too bad, Miller. I was always one step ahead of you.":
            show smirk face of miller                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            jump escapes

label check_suspicion: 
    scene policestation
    if suspicion >= 7:
        "The police don't trust you anymore. They think you're helping the criminals."
        jump fired 

    elif suspicion >= 3:
        "Miller looks at you with doubt. He lets you solve the case, but he’s watching your every move."
        jump nextday

    else:
        "You’ve played it perfectly. Miller trusts you implicitly."
        jump secrets 

label fired: 
    scene policestation

    dm "Hand it over, Lee. The badge. The gun."
    ml "Miller, I can explain—"
    dm "Save it for the hearing. You crossed a line, and now you're a liability."

    "GAME OVER"
    jump end

label nextday: 

    scene investigation board
    with fade 

    scene police station
    with fade 

    dm "You’ve been staring at Silas’s file for twenty minutes, Lee."
    dm "You really think a gardener has the precision to hide three bodies in three different ways?"

    ml "Precision comes from necessity, Miller."
    ml "He was underpaid. He was angry."

    dm "And what about the Broken Bottle you found in the bushes? Forensic says it matches the shards in the son’s skull. "
    dm "If Silas was the killer, why take the murder weapon from the dock all the way to the garden just to hide it in a bush?"

    ml "He panicked. He heard the mother scream, ran to silence her with whatever was in his hand, and then realized he couldn't be caught with the glass. It’s a logical chain of events, Miller."
    
    dm "Maybe. But the neighbor... William. "
    dm "He mentioned a 'short, fast shadow.' Silas is over six feet tall. He doesn't exactly 'scoot' through thorns, Morgan."
        
    ml "Silas had access to the house. He knew Ariane’s jewelry collection. He didn't just kill them; he was looting them."

    dm "William had the earring for five years. Why wouldn't a 'thief' like Silas take both?"
    
    ml "Well…the fertilizer. It's a high-nitrogen rose fertilizer. Silas is the only one who ordered it. He used his own supplies as weights."
    ml "Or someone used Silas’s shed to frame him. It’s too convenient. I think we have the suspects, Miller."

    dm "Okay, Morgan. Who do we bring in?"
    menu: 
        "Executive Edward": 
            ml "I traced the post regarding the Belmonts’ escape, the IP showed that it was Edward."  
            jump arrest1 

        "Gardener Silas": 
            ml "We have enough proofs and evidence that he is the killer. He was angry, that's his motive."    
            jump arrest2

        "Neighbor William":
            ml "He had the earring and didn’t report anything to the police until now."
            jump arrest3

    dm "We got our suspect, but it doesn't feel like a win."

label arrest1: 
    scene handcuff

    ml "Case closed. Our killer is greedy. You do this kind thing for money?"
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "ENDING: Case Closedss."
    jump end

label arrest2: 
    scene handcuff 

    dm "He has every reason to resent them but I don't think killing the whole family is reasonable."
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "ENDING: Case Closed."
    jump end

label arrest3: 
    scene handcuff 
    
    ml "I do wonder, what kind of family is the Belmont for him to do this. "
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "ENDING: Case Closed."
    jump end

label secrets: 
    scene policestation

    dm "Clean work, Lee. I haven't seen an investigation that tight in years."
    ml "Just doing my job, Miller."
    dm "Dinner is on me tonight. You earned it."
    "ENDING: Legendary Detective."
    jump end 

label escape:
    scene black 
    with fade 

    #HISS SOUND parang yung sa gas
    #insert image of smoke
    dm "DETECTIVE MORGAN"
    "MORGAN"

label end: 
    scene black
    with fade 

    "Some secrets are better left beneath…"
    return

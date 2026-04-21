# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ml = Character(_("Detective Morgan Lee:"), color="#c8ffc8", image="morgan")
define dm = Character(_("Detective Miller:"), color="#c8ffc8", image="miller")
define cb = Character(_("Charles Belmont:"), color="#c8ffc8", image="charles")
define a = Character(_("Ariane:"), color="#c8ffc8", image="ariane")
define c = Character(_("Carl:"), color="#c8ffc8", image="carl")
define gs = Character(_("Gardener Silas:"), color="#c8ffc8", image="silas")
define ee = Character(_("Executive Edward:"), color="#c8ffc8", image="edward")
define nw = Character(_("Neighbor William:"), color="#c8ffc8", image="will")
define m = Character(_("Miles:"), color="#c8ffc8", image="kid1")
define b = Character(_("Mike:"), color="#c8ffc8", image="kid2")
define k = Character(_("Karl:"), color="#c8ffc8", image="kid3")
define lt = Character(_("Liutenant:"), color="#c8ffc8")
define p1 = Character(_("Police Officer:"), color="#c8ffc8")
define glass = Character(_("glass:"), color="#c8ffc8", image="glass_bottle")
define earrings = Character(_("hikaw:"), color="#c8ffc8", image="hikaw")
image splashone = "ss_uno.png"
image splashtwo = "ss_dos.png"
image splashtres = "ss_tres.png"

label splashscreen: 

    play sound "audio/siren_police.mp3" fadein 0.5

    scene black
    with Pause(1)

    show splashone with dissolve
    with Pause(2.5)

    scene black with dissolve
    with Pause(0.5)

    show splashtwo with dissolve
    with Pause(2.5)

    scene black with dissolve
    with Pause(1)

    play audio "audio/boom.mp3" fadeout 2.00
    show splashtres with dissolve
    with Pause(2.5)

    scene black with dissolve
    with Pause(1)

    stop audio fadeout 3.00
    stop sound fadeout 1.0

    return

image breathing_darkness:
    Solid("#000")

    alpha 0.0
    linear 3.0 alpha 0.6  
    linear 3.0 alpha 0.0 
    repeat

default suspicion = 0 
default earring = 0 
default path = "none"  
default visited_basement = False
default visited_garden = False
default injury = False


# The game starts here.

label start:

    play sound "audio/cricket_sounds.mp3"
    
    scene lake_view
    pause
    stop sound
    play sound "audio/heartbeat_suspense.mp3"
    scene dock-shadow
    with Fade (0.3, 0.0, 0.3)

    "Charles stands at the end of the dock among bottles of alcohol while a shadow creeps behind him."
    scene black-screen
    pause 0.5
    stop sound

    play sound "audio/smash.mp3"
    scene bottle-smash
    pause 1.0
    stop sound
    play sound "audio/splash.mp3"
    scene black-screen
    pause 0.5
    stop sound

    scene kitchen_window
    with Fade (0.1, 0.0, 0.3)
    a "Charles, is everything okay?"
    a "Charles-"

    play sound "audio/w_scream.mp3"
    scene black-screen
    pause 1.5
    stop sound
    play sound "audio/thud.mp3"
    scene hand_blood
    pause 2.0
    stop sound

    scene stairs-night
    with Fade (0.3, 0.0, 0.3)
    c  "Ariane, what’s happening down there?"

    scene backyard-night
    with Fade (0.1, 0.0, 0.3)
    show carl
    c "What did you do?"
    c "Ariane...Charles!"

    scene stairs-night
    with Fade (0.3, 0.0, 0.3)
    show carl
    c "Who are you?! I’m calling the pol-"
    hide carl
    #sfx - thud
    scene black-screen
    pause 1.5
   
    scene footsteps-night
    pause 2.0

label movie:
    window hide
    scene black         
    with None
    
    $ renpy.movie_cutscene("introtwo.webm")
    
    scene black        
    with None
    
    pause 0.5

    scene belmont-house
    with Fade (0.0, 0.0, 0.3)

    show kid1
    m "Come on, bro! I heard that place is huge."
    m "The owners suddenly left because of a financial scandal."
    hide kid1

    show kid2
    b "I don’t think we should go here, Miles."
    hide kid2
    show daisy
    b "Even Daisy doesn’t wanna go."
    hide daisy

    show kid3
    k "Oh come on, it’s so early in the morning."
    k "It’ll be fine, Mike."
    hide kid3

    m "Look, I think we can move these boards to go to their backyard." 
    
    "Move the two boards in the front"

    call screen fence_minigame

    scene backyard-morning
    with Fade (0.1, 0.0, 0.2)
    show kid3
    k "Woah, the water here isn’t as clear as it is on our side of the lake."
    hide kid3
    #sfx leaves rustle 

    scene lake_view
    with Fade (0.1, 0.0, 0.3)
    b "It smells disgusting here…"
    # Layer - img of daisy 
    b "Daisy, stay close."
    show daisy
    "{i}arf arf{/i}"
    hide daisy

    show kid2
    b "Daisy, come here!"
    b "God, I’m gonna have to give her a wash later."
    hide kid2

    show kid1
    m "It smells putrid here."
    hide kid1
    show kid2
    b "DAISY! Come here! "
    hide kid2

    scene dock-present
    with Fade (0.1, 0.0, 0.3)
    show kid3
    k "Guys, I think we should go."
    k "Miles, get your motorboat."
    hide kid3

    show kid1
    m "Okay okay, geez."
    hide kid1

    scene dock-zoom
    pause 1.5
    scene dock-zoom
    with Fade (0.0, 0.0, 0.3)
    #sfx dog barking

    m "Is that..."
    scene black-screen
    pause 1.5
    #sfx boy SCREAM 

    scene black-screen
    with Fade (0.0, 0.0, 0.3)
    lt "Your new case Detective Morgan..."
    ml "Thank you, Liutenant"
    lt "Better do well on this one, detective."
    lt "I'm counting on you."

    scene police-station 
    with Fade (0.1, 0.0, 0.3)
    show miller_open
    dm "Thank you for accepting our request for this, Detective Lee. We know it’s a bit hasty."
    hide miller_open
    show morgan
    ml "It’s okay, I’m interested in the case anyway."
    hide morgan
    show morgan_open
    ml "So…what are the updates?"
    hide morgan_open
    
    scene charles-file
    with Fade (0.1, 0.0, 0.3)
    dm "That’s the body we found, those are what we got from the autopsy."
    dm "Feel free to check his information. "
    
    scene charles-file
    pause
    scene autopsy-charles
    pause

label glitch_moment:

    $ flash_glitch = Pixellate(0.1, 7)

    scene bloody_hands
    with flash_glitch
    scene bloody_hands
    pause

    "Is everything okay, Detective Lee? "

    scene autopsy-charles
    with flash_glitch
    ml "huh? Ah...yes"

    scene police-station 
    with Fade (0.1, 0.0, 0.3)

    menu: 

        "All good, when are we heading to the site?": 
            $ suspicion -= 1
            jump site
        
        "We should go to the site. No time to waste.": 
            $ suspicion += 1
            jump waste 

label site: 

    show miller
    dm " We can go now."
    hide miller
    show morgan_open
    ml "Okay let’s go."
    hide morgan_open

    jump belmonth

label waste: 
    scene black with fade 
    jump belmonth

label belmonth:
    scene belmont-house
    with Fade (0.0, 0.0, 0.3)
    
    show miller_open
    dm "Here we are. Ready to go in?"
    hide miller_open

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

    scene belmont-house
    with Fade (0.0, 0.0, 0.3)

    show miller
    dm "Are you sure?"
    hide miller
    show morgan
    ml "Yes"
    hide morgan
    show miller
    dm "Okay, I’ll leave you to it."
    hide miller

scene pathway
with Fade (0.0, 0.0, 0.3)

menu: 
    "Path L": 
        $ path = "L"
        jump left_glitch
    "Path R": 
        $ path = "R"
        jump right_glitch

label left_glitch:
    scene left_pathway
    pause
    $ flash_glitch = Pixellate(0.1, 7)
    scene left_pathway
    with flash_glitch
    scene left_bloody
    pause

    "Detective Lee..."

    scene left_pathway
    with flash_glitch

    jump lakeview

label right_glitch:
    scene right_smell
    pause

    show morgan
    ml "It smells here..."
    hide morgan

    $ flash_glitch = Pixellate(0.1, 7)
    scene right_smell
    with flash_glitch
    scene right_dig
    pause

    "Detective Lee..."

    scene right_smell
    with flash_glitch

    jump lakeview


label lakeview: 

    scene gardener_shed
    with Fade (0.0, 0.0, 0.3)

    show silas
    gs "You are the detective in this case?"
    hide silas
    show morgan
    ml "I am. Pleased to meet you. Detective Morgan Lee." 
    ml "You are a family of the deceased?"
    hide morgan
    show silas_open
    gs "No, I am only their mere gardener. Well, was…"
    hide silas_open
    show morgan
    ml "Their?"
    hide morgan
    show silas
    gs "Yes, the night that they left…I didn’t know that they were murdered. "
    gs "The Belmonts used to live here, a family of three. Mrs. Ariane, Mr. Carl, and their son, Charles."
    hide silas
    show morgan
    ml "What exactly happened here, were you present the day their son was murdered?"
    ml "Where are the parents?"
    hide morgan
    show silas_open
    gs "The Belmonts were wealthy but intensely private—no staff, just them. When I requested a night off to visit family, they granted it, but when I returned the next morning, they were gone. "
    gs "William broke the news: they’d supposedly fled to escape a money-laundering scandal. Honestly? I didn't care. They were cruel, underpaid me, and I was glad to be done with their garden."
    hide silas_open
    show morgan
    ml "I’m so sorry to hear that."
    hide morgan
    show miller
    dm "Sorry to break this conversation, but Detective Lee, we need you to see this."
    hide miller
    show morgan_open
    ml "Thank you for the information you gave, sir."
    hide morgan_open

    scene backyard-morning
    with Fade (0.0, 0.0, 0.3)

    show miller 
    dm "Here were the bottles from the night he was murdered. No broken ones though…the murderer hid their weapon."
    hide miller

    
    scene backyard-morning
    with Fade(0.1,0.0,0.3)
    show bottle
    "Alcohol..."
    hide bottle

    scene backyard-morning
    with Fade (0.0, 0.0, 0.3)

    show morgan
    ml "He really was intoxicated. What if it was a drinking session and they fought?"
    hide morgan
    show miller
    dm "The Belmonts don’t invite anyone here, the gardener already said that."
    hide miller
    show morgan
    ml "The gardener seems to know a lot about the Belmonts…"
    hide morgan

    p1 "Detective, you better see this."

label willowtree:
    scene willowtree
    with Fade(0.0, 0.0, 0.3)
    
    if path == "L":
        scene right_smell
        pause 1.0
        show morgan
        ml "What is that smell?"
        hide morgan
        
        scene willow_body
        pause 2.0
        
        # play music "audio/surprised.ogg"
        show miller
        dm "Another one..."
        hide miller

    elif path == "R":
        scene right_smell
        pause 1.0
        show morgan
        ml "It smelled disgusting here a while ago."
        hide morgan
        # play music "audio/surprised.ogg"
        scene willow_body
        pause 2.0

        show miller
        dm "Another one..."
        hide miller
        
    jump aftermath

label aftermath:

    scene willow_body

    show morgan
    ml "A body..."
    ml "I haven’t seen the first body, where is it?"
    hide morgan
    show miller
    dm "By the lake’s shore, I’ll come with you. To the others, continue digging that up."
    hide miller

    scene dock-zoom

    show miller
    dm "He has a nylon rope tied to his neck with the fertilizer bag weighting him down."
    hide miller
    show morgan
    ml "A fertilizer bag…?"
    hide morgan
    show miller
    dm "Yes, still quite intact actually…"
    hide miller
    show morgan
    ml "That's strange"
    hide morgan
    show miller
    dm "Have enough clues for now? Let’s head back to the station and call it a day."
    hide miller
    
    menu:
        "Yes":
            $ suspicion -= 1
            jump board

        "I don't know. I'm not sure":
            $ suspicion += 2
            jump board

label board: 

    scene black-screen
    with Fade(0.0, 0.0, 0.3)

    "DAY 0"

    call screen investigation_board

    "These clues..."

    scene black-screen
    with Fade(0.0, 0.0, 0.3)

    "DAY 1"

    scene police-station
    with Fade(0.0, 0.0, 0.3)

    show miller_open
    dm "Good day, Dect. Lee. Ready to start the day?"
    hide miller_open
    show miller
    dm "Here’s the files for the body we found at the willow tree."
    hide miller

    scene ariane_file
    with Fade(0.0, 0.0, 0.3)

    scene ariane_file
    pause

    scene ariane_autopsy
    pause

    dm " We have two bodies. "
    dm "If the son is in the water and the mother is also dead. Where is the father?"

    scene police-station
    with Fade(0.0, 0.0, 0.3)
    
    show morgan
    ml "He’s dead…But he wouldn't be in the yard. "
    ml "He’d be inside."
    hide morgan
    show miller
    dm "How'd you know?"
    hide miller

    menu: 
        "Because...I'm Morgan Lee. Tsk":
        #focus kay morgan naka-smirk siye 
            jump morgansakalam

        "I have a knack for crime scene":
        #siryus peys ni morgan
            jump morganknack

label morgansakalam:
    show morgan_open with dissolve
    "*smirks*"
    hide morgan_open
    show miller
    dm "Right, ma'am. You're THE Detective Lee."
    hide miller
    $ suspicion -= 1
    jump investigation 

label morganknack:
    show miller
    dm "Right. Let's hope that knack holds up today."
    hide miller
    $ suspicion += 1
    jump investigation

label investigation:
    scene belmont-house
    with Fade (0.1, 0.0, 0.3) 

    show edward
    ee "Detective Miller? I heard the news. "
    hide edward
    show edward_open
    ee "This is... ghastly. I came as soon as I heard you found remains."
    hide edward_open

    show miller_open
    dm "Detective Lee, this is Mr. Edward. He was a-"
    hide miller_open

    show morgan
    ml "The business partner."
    hide morgan
    show miller
    "{i}How does she know...{/i}"
    hide miller
    show morgan_open
    ml "You were the last one to see Carl Belmont alive. Weren't you?"
    hide morgan_open
    show miller
    "{i}hmm...{/i}"
    hide miller

    show edward
    ee "In a professional capacity, yes. "
    hide edward
    show edward_open
    ee "We had a disagreement about the 'missing' funds, but I didn't think he’d... well, I thought he ran away."
    hide edward_open
    show edward
    ee "He owed me millions, Detective. I wanted him alive so I could get my money back."
    hide edward

    show morgan
    ml "Or you wanted him dead so he couldn't testify about where that money actually went."
    hide morgan
    show miller_open
    dm "That's heavy accusation, detective. You sure about that?"
    hide miller_open

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
    show morgan
    "I keep my eyes locked on Miller, ignoring the house for a moment."
    "He’s nervous. He keeps adjusting his holster, looking everywhere but at me."
    hide morgan
    $ suspicion -= 1
    jump suspense

label pressure:
    show morgan
    ml "I don't need excuses, Miller. Where's the money?"
    hide morgan
    show miller
    dm "You're getting reckless, Detective."
    hide miller
    $ suspicion += 2
    jump suspense

label backoff:
    show morgan
    ml "Forget it. I'm sure it's just a misunderstanding."
    hide morgan
    show miller
    dm "Glad you see it that way."
    hide miller
    $ suspicion -= 1
    jump suspense

label suspense:
    scene patio
    with Fade (0.1, 0.0, 0.3)

    show miller_open
    dm "You should check on other things… I’ll handle Edward for now. "
    hide miller_open
    show morgan
    ml "Sure. Thank you"
    hide morgan
    jump investigation_hub

label investigation_hub:
    if visited_basement and visited_garden:
        jump story_progression 

    scene patio
    "I still need to look around. Where should I check next?"

    menu:
        "Investigate the Basement" if not visited_basement:
            $ visited_basement = True
            jump basement_path

        "Check the Gardener's Shed" if not visited_garden:
            $ visited_garden = True
            jump garden_path

label basement_path:
    scene basement_present
    with Fade(0.1, 0.0, 0.3)
    show morgan
    ml "It smells here too…"
    hide morgan
    jump fb_glitch

label fb_glitch:
    show breathing_darkness 
    pause 1.0

    $ flash_glitch = Pixellate(0.1, 7)

    show basement_clean with flash_glitch
    pause 0.2
    show basement_body with flash_glitch
    pause 0.2
    show right_dig with flash_glitch
    pause 0.2
    show footsteps-night with flash_glitch
    pause 0.2
    
    scene basement_present with flash_glitch
    show breathing_darkness 
    pause 0.5
    hide breathing_darkness with fade
    
    scene black-screen
    pause 0.5

    "{i}I murdered the whole family.{/i}"

    show charles
    cb "Morgan Lee? She thinks too highly of herself."
    cb "Don’t talk to her. I saw her cheating on the exams."
    cb "I'll get her scholarship revoked."
    hide charles
    
    "{i}You wanted to bury my future, so I decided to bury yours instead.{/i}"

    scene black 
    with Fade(0.1, 0.0, 0.3)
    "{i}I buried a body here...{i}"
    "{i}In this basement...{i}"
   
    call screen basement_puzzle

    "Morgan uses the tool to pull up the wood planks"
    scene basement_body
    with Fade(0.1, 0.0, 0.3)

    show miller_open
    dm "Detective Lee, we saw on the-"
    hide miller_open
    show miller
    dm "Another body… with a watch... the time they died..."
    hide miller
    show miller_open
    dm "Go back to the backyard, I’ll send someone to check this out."
    hide miller_open

    jump stay

label garden_path:
    scene gardener_shed
    with Fade(0.1, 0.0, 0.3)

    show morgan_open
    ml "What's that on the bushes...?"
    hide morgan_open

    menu: 
        "Search with bare hands":
            $ injury = True
            show morgan_open
            ml "I need to find it fast. I don't care about the pain."
            hide morgan_open
            show morgan
            ml "Ouch..."
            hide morgan

            jump bushes

        "Use the crowbar": 
            $ injury = False
            show morgan 
            "I use the crowbar to pry the branches. It’s slow, but my hands stay clean."
            hide morgan
            jump bushes

label bushes:
    scene garden_neighbor
    with Fade(0.1,0.0,0.3)

    show morgan
    nw "Searching for more secrets, Detective? Or just admiring the rot?"
    nw "I saw a shadow moving near those bushes the night they 'fled.' Short and fast. It was dragging something heavy."
    hide morgan
    show morgan_open
    ml "Why were you watching your neighbors late at night?"
    nw "I was throwing my trash."
    hide morgan_open
    show morgan
    ml "And yet, you didn't call the police that night, Mr. William. You just watched."
    ml "Perhaps you were waiting for them to leave so you could take what you wanted?"
    hide morgan
    nw "And I might have something you’ll need."

    scene gardener_shed
    with Fade(0.1,0.0,0.3)
    show hikaw
    "Pearl earrings..."
    hide hikaw

    scene gardener_shed
    with Fade(0.1,0.0,0.3)
    show morgan
    ml "Why do you have this?"
    hide morgan
    show morgan_open
    ml "You’ve been holding onto evidence for five years, William. That’s obstruction of justice. Why show it to me now?"
    hide morgan_open
    show morgan
    nw "I found that earring in the mud right after the scandal broke."
    nw "Here in these very bushes. It was sitting right where that shadow was digging near the tree."
    hide morgan

    scene gardener_shed
    with Fade(0.1, 0.0, 0.3)

    ml "I better take this to Miller."
    jump stay

label backyard: 
    scene patio
    with Fade(0.1, 0.0, 0.3)
    
    if injury:
        show miller
        dm "What happened to your arm?"
        hide miller
        menu:
            "This is no big deal.":
                $ suspicion += 1
                jump stayy
            "I didn't notice barbwire at the garden. I scratched my arm on it":
                $ suspicion -= 1
                jump stayy

    else:
        show miller_open
        dm "We identified the body, it was the father."
        hide miller_open
        show miller
        dm "What’s that on your hand?"
        hide miller
        menu: 
            "Nothing. Don't mind me":
                $ suspicion += 2
                jump stayy
            "I slipped in the garden, this is all dirt and mud":
                $ suspicion -= 1
                dm "Next time, be careful"
                jump stayy

label stay:
    jump investigation_hub

label story_progression:
    "Both areas have been searched. The truth is starting to surface..."
    jump backyard

label stayy: 
    scene patio
    with Fade(0.1,0.0,0.3)

    show miller
    dm "Do you wanna leave the site early? I’ll stay to investigate further. Do you want to stay or not?"
    hide miller

    menu: 
        "I’m going to stay.":
            jump vacation 

        "I’m going to call it a day.":
            jump shore 

label vacation: 

    scene black-screen
    with Fade(0.1,0.0,0.3)

    "{i}Morgan and Miller continue on the investigation...{/i}"
    jump nextday

label shore:

    scene shore
    pause 1.0
    
    scene black-screen
    with Fade(0.1,0.0,0.3)

    scene in_station
    with Fade(0.1,0.0,0.3)

    show morgan
    ml "I think we should arrest Silas."
    hide morgan
    show miller
    dm "And you're sure about that...?"
    hide miller
    show morgan_open
    ml "I am never wrong."
    hide morgan_open

    show miller_open
    dm "Right..."
    hide miller_open
    show miller
    dm "You know, Lee... while you were heading home yesterday, I took one last walk along the shore. "
    hide miller
    show miller_open
    dm "Near the spot where those kids found the motorboat."
    hide miller_open
    show morgan_open
    ml "Find anything interesting? Aside from the putrid smell?"
    hide morgan_open

    scene in_tag
    with Fade(0.1,0.0,0.3)

    show morgan
    dm "I found this. Half-buried in the silt, right under the edge of the dock. It’s a silver nametag."
    hide morgan
    show morgan
    dm "The pin is bent back... like it was ripped off someone's chest with a lot of force."
    hide morgan
    show morgan
    dm "You were his classmate…and as I have read, he reported you for reporting which revoked your scholarship."
    hide morgan
    show morgan
    dm "You killed them, Morgan."
    hide morgan

    scene in_station
    with Fade(0.1,0.0,0.3)

    menu: 
        "They buried my future, Miller. I just returned the favor.":
            $ suspicion += 2
            jump check_suspicion 

        "Too bad, Miller. I was always one step ahead of you.":
            show smirk face of morgan
            jump escape 

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

    call screen new_investigationboard
    
    scene inv_boardfill
    pause

    scene black-screen
    pause 0.5

    scene police-station
    with Fade(0.1,0.0,0.3) 

    show miller_open
    dm "You’ve been staring at Silas’s file for twenty minutes, Lee."
    dm "You really think a gardener has the precision to hide three bodies in three different ways?"
    hide miller_open
    show morgan
    ml "Precision comes from necessity, Miller."
    ml "He was underpaid. He was angry."
    hide morgan
    show miller
    dm "And what about the Broken Bottle you found in the bushes? Forensic says it matches the shards in the son’s skull. "
    dm "If Silas was the killer, why take the murder weapon from the dock all the way to the garden just to hide it in a bush?"
    hide miller
    show morgan_open
    ml "He panicked. He heard the mother scream, ran to silence her with whatever was in his hand, and then realized he couldn't be caught with the glass. It’s a logical chain of events, Miller."
    hide morgan_open
    show miller
    dm "Maybe. But the neighbor... William. "
    hide miller
    show miller_open
    dm "He mentioned a 'short, fast shadow.' Silas is over six feet tall. He doesn't exactly 'scoot' through thorns, Morgan."
    hide miller_open
    show morgan
    ml "Silas had access to the house. He knew Ariane’s jewelry collection. He didn't just kill them; he was looting them."
    hide morgan
    show miller
    dm "William had the earring for five years. Why wouldn't a 'thief' like Silas take both?"
    hide miller
    show morgan_open
    ml "Well…the fertilizer. It's a high-nitrogen rose fertilizer. Silas is the only one who ordered it. He used his own supplies as weights."
    hide morgan_open
    show morgan
    ml "Or someone used Silas’s shed to frame him. It’s too convenient. I think we have the suspects, Miller."
    hide morgan
    show miller
    dm "Okay, Morgan. Who do we bring in?"
    hide miller

    scene suspects
    with Fade(0.1,0.0,0.3)
    
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

label arrest1: 
    scene in_station
    with Fade(0.1,0.0,0.3)

    show morgan
    ml "Case closed. Our killer is greedy. You do this kind thing for money?"
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "CASE CLOSED"
    hide morgan
    jump end

label arrest2: 
    scene in_station
    with Fade(0.1,0.0,0.3)

    show miller
    dm "He has every reason to resent them but I don't think killing the whole family is reasonable."
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "CASE CLOSED"
    hide miller
    jump end

label arrest3: 
    scene in_station
    with Fade(0.1,0.0,0.3)
    
    show morgan
    ml "I do wonder, what kind of family is the Belmont for him to do this. "
    dm "Good job on the arrest, but don't think I've forgotten how you got there."
    dm "I'll be watching your reports very closely from now on."
    "CASE CLOSED"
    hide morgan
    jump end

label secrets: 
    scene policestation

    dm "Clean work, Lee. I haven't seen an investigation that tight in years."
    ml "Just doing my job, Miller."
    dm "Dinner is on me tonight. You earned it."
    "Legendary Detective."
    jump end

label escape:
    scene black 
    with fade 

    #HISS SOUND parang yung sa gas
    #insert image of smoke
    dm "DETECTIVE MORGAN"
    "MORGAN"

label end:

    scene black-screen
    with fade 

    "Some secrets are better left beneath…"
    "and Morgan Lee should never rests..."
    "{i}To be continued...{/i}"
    return
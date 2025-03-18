screen resentment_ryan():
    frame:
        xalign 0.01
        yalign 0.08
        text "Ryan's Resentment: [ryanres]"
screen sympathy_ryan():
    frame:
        xalign 0.01
        yalign 0.15
        text "Ryan's Sympathy: [ryansymp]"

screen resentment_jeremy():
    frame:
        xalign 0.01
        yalign 0.08
        text "Jeremy's Resentment: [jeremyres]"
screen sympathy_jeremy():
    frame:
        xalign 0.01
        yalign 0.15
        text "Jeremy's Sympathy: [jeremysymp]"

screen resentment_laney():
    frame:
        xalign 0.01
        yalign 0.08
        text "Laney's Resentment: [laneyres]"
screen sympathy_laney():
    frame:
        xalign 0.01
        yalign 0.15
        text "Laney's Sympathy: [laneysymp]"

screen resentment_carol():
    frame:
        xalign 0.01
        yalign 0.08
        text "Carol's Resentment: [carolres]"
screen sympathy_carol():
    frame:
        xalign 0.01
        yalign 0.15
        text "Carol's Sympathy: [carolsymp]"

screen resentment_town(): #this will be visible in the second arc, after talking to an old friend of Aunt Rachel's.
    frame:
        xalign 0.01
        yalign 0.01
        text "Town's Resentment: [townres]"
screen sympathy_town():
    frame:
        xalign 0.01
        yalign 0.07
        text "Town's Sympathy: [townsymp]"

screen inventory():
    frame:
        xalign 0.01
        yalign 0.01
        if inventory:
            text "Inventory: [','.join(inventory)],phone"
        else:
            text "Inventory: phone" #inventory items start effecting actions in the second arc.

screen intro_text():
    text "This game contains graphic discussions of the death of a child. Player discretion is advised." size 40 xalign 0.5 yalign 0.5


define m = Character("Maya")
define r = Character("Ryan")
define l = Character("Laney")
define j = Character("Jeremy")
define c = Character("Carol")
define n = Character("Newspaper", who_font= "newsreaderital.ttf", what_font= "newsreader.ttf")
define w = Character("Waitress")

default ryanres = 0
default ryansymp = 0
default jeremyres = 0
default jeremysymp = 0
default laneyres = 0
default laneysymp = 0
default carolres = 0
default carolsymp = 0
default inventory = []
default townsymp = 0
default townres = 0


# The game starts here.

label start:
    scene bg warnings
    play sound "audio/ocean.wav"
    show screen intro_text
    pause
    hide screen intro_text
    jump gamestart

label gamestart:
    scene bg flashback
    "My name is Maya Gold"

    "I am not happy to be home."
    jump gameintro

    label gameintro:
        window hide
        show bg gameint
        with dissolve
        play music "audio/intro_music.wav" volume 0.5
        pause
    jump houseintro

    label houseintro:
        show bg house
        with dissolve
        stop sound fadeout 3
        play music "audio/game music.wav" volume 0.25
        stop sound fadeout 3
        show screen inventory
        "The taxi drops me off in front of my great-aunt's house."
        "I hear a car door slam behind me."
        play sound "audio/car door.wav"
        show ryan neutral
        r "Maya!"
        "I'd known Ryan since kindergarten. Like most kids here, we'd gone to elementary through high school together."
        "(like most kids here, they'd stayed in town after graduation)."
        "They pull me into a hug. They don't seem to notice when I don't hug them back."

        r "It's been so long since I've seen you!"
        r "You never visit anymore!"
        r "How've you been?"
        show screen resentment_ryan
        show screen sympathy_ryan

        menu:
            "Not great.":
                $ryansymp += 1
                $townsymp += 1
                r "I guess makes sense, considering."
            "Just shrug.":
                hide ryan neutral
                show ryan annoyed
                $ryanres += 1
                $townres += 1
                r "Don't want to talk about it, huh?"
                r "What else is new."
                hide ryan annoyed
                show ryan sad
        show ryan sad
        r "Are you going to the memorial service?"
        "I hadn't thought about whether or not I wanted to go to Aunt Rachel's memorial"
        "I'd lived with her since I was 16, but we were never close."
        "I'd spent so much time fighting every authority figure after..."
        "My chest feels tight."
        "I know I should say yes, but..."

        menu:
            "I don't know.":
                r "I guess you'll be busy packing up the house."
            "I just... I can't":
                "Ryan sighs."
                r "I get it."
                $ryansymp += 1
                $townres += 1
        r "I mean, you haven't been to temple since..."
        "Ryan trails off, but I know what they're circling around."
        "I haven't been to temple since Monica Stein's service, over a decade ago."
        m "Let's go inside."
        hide ryan sad
        jump houseint
    
    label houseint:
        show bg houseinterior
        with dissolve
        show ryan neutral
        with dissolve
        "I glance around Aunt Rachel's living room."
        "Nothing's changed since the last time I visited."
        r "I came by twice a week to cook for her, and to clean the house."
        r "There's not much in the fridge, but you remember where the corner market is."
        hide ryan neutral
        show ryan sad
        r "At least, I assume..."
        m "Ryan..."

        menu:
            "Thank you for taking care of Aunt Rachel.":
                $ryanres += 1
                $townres += 1
                hide ryan sad
                show ryan annoyed
                r "Yeah, well, didn't have much of a choice."
                r "Not like you were around to do it."
                r "Speaking of people who {i}are{/i} around..."
            "I don't have a car.":
                $townsymp += 1
                r "Let me ask around, see if someone can drive you."
                r "Maybe Laney can do it."
                r "Speaking of..."
        r "Have you talked to Laney yet?"
        "Unbidden, a memory washes over me."
        jump laneyflash
    
    label laneyflash:
        stop music #yes this is supposed to be silent. Eventually I will build more flashbacks so it seems more purposeful.
        hide screen inventory
        hide ryan annoyed
        show bg flashback
        show laney child
        hide screen resentment_ryan
        hide screen sympathy_ryan

        l "You can't tell anyone we found her, okay?"
        l "Let's just wait until morning, someone will tell the Sisters by then."
        jump backhouse

    label backhouse:
        play music "audio/game music.wav" volume 0.25
        hide laney child
        show bg houseinterior
        show ryan annoyed
        show screen inventory
        show screen resentment_ryan
        show screen sympathy_ryan

        "I shake my head to dispell the memory."
        "This is why I left."
        "There's too much history here."
        m "Not yet, I just got in."
        "Ryan shrugs"
        hide ryan sad
        show ryan neutral
        r "Contact her at some point, yeah?"
        "Ryan stretches, then begins to move towards the door."
        r "Well, I should be heading out. Got a big project due at work."
        "I follow them, back to the front of the small house."
        m "Wait, Ryan..."
        "Ryan turns towards me."

        menu: 
            "Do you remember Monica Stein?":
                hide ryan neutral
                show ryan annoyed
                $ryanres += 1
                $townres += 3
                "Ryan's eyes dart towards the door."
                r "Yeah, the murder's still unsolved."
                "I open my mouth to say something, but they've already got the door half open."
                r "I really gotta go."
                "They leave without saying goodbye."
                hide ryan annoyed
    

            "Can we get dinner later?":
                $ryansymp += 1
                r "I'll be working late, but you could probably get food with Jeremy."
                r "Do you still have his number?"
                m "As long as it hasn't changed, yeah."
                r "It hasn't. He gets off work at five, but he has a lunch break soon. Shoot him a text, I'm sure he'll answer."
                r "He'll want to eat right after he gets off. He's still hungry all the time"
                m "That's what she said."
                $ryansymp += 1
                
                r "Some things don't change, huh?"
                "I smile back, but something in me cringes at her choice of words."
                "Nothing changes here."
                "Not even me."
                "Ryan steps towards the door."
                "They hesitate, as if they want to say something else."
                
                "Finally, they land on:"
                r "It's good to see you, Maya."
                hide ryan neutral
            
        jump desk

    label desk:
        hide screen resentment_ryan
        hide screen sympathy_ryan
        menu:
            "I decide to start going through Aunt Rachel's things.":
                jump desknews

    label desknews:
        show bg desk
        with dissolve
        "I start with her desk, which is stacked chest high with old newspapers."
        show paper one
        play audio "audio/newspaper sound.wav"
        "I flick through to a random date."
        stop audio
        n "TEN-YEAR-OLD DISCOVERED DEAD BY NUN AT CAMP HOLY SPIRIT: 'IT WAS HORRIFIC.'"
        "I continue reading"
        n "The body of ten year old Monica Stine was discovered in her bed at Camp Holy Spirit early this morning by Sister Mary Carter." 
        n "The girl’s head was beaten in completely. One onlooker described her appearance as 'unrecognizable.'"  
        n "Authorities say there are currently no suspects."
        n "Her family asks for privacy at this time."
        "The article then goes into more grizzly detail, interviewing campers and nuns."
        
        menu:
            "I flip to the next paper":
                jump nextpaper
    label nextpaper:
        hide paper one
        show paper two 
        play audio "audio/newspaper sound.wav" 
        n "FIVE YEAR RETROSPECTIVE: CASE OF MURDERED GIRL REMAINS UNSOLVED."
        stop audio
        n "Monica Stein was murdered five years ago this week. Her case remains open, but cold."
        "I skim a few lines down."
        n "Her family continues to assert that 'something' was not right at Camp Holy Spirit"
        n "Her mother asserts that 'I always knew something was wrong at that damn convent..."
        n "'...this proved it.'"
        "I roll my eyes. The convent was built to house mentally unstable kids."
        "Of course there was something wrong with it."
        "At least they spelled her name right in this one."

        menu:
            "pocket paper":
                $ inventory.append("newspaper")
                hide paper two
                play audio "audio/newspaper sound.wav"
                "I roll up the newspapers and shove them into my coat pocket"
                stop audio
                play sound "audio/texttone.wav" volume .5
                "My phone dings"
                show phone one
                j "Ry sd you were back n town wanna get dnnerr togeth?"
                "So Jeremy still can't type."
                "I guess I don't have anywhere else to be."
                hide phone one
                jump dinnerintro
            "recycle the paper":
                hide paper two
                play sound "audio/throw paper.wav"
                "I throw the paper to a corner in the room. That'll be my 'get rid of' pile."
                stop sound
                "I grimace. Aunt Rachel sure had a lot of crap."
                show phone two
                "I shoot off a quick text to Jeremy."
                m "Wanna get dinner tonight"
                play sound "audio/texttone.wav" volume .5
                j "sre meat u at siam thai?"
                "Fuck. I hate Siam Thai."
                hide phone two
                jump dinnerintro
                

    label dinnerintro:
        show bg flashback
        with dissolve
        "The resturaunt is walking distance from Aunt Rachel's house."
        "I thought I might need directions, but my feet carry me there automatically."
        "After years of post-Rosh Hashana service lunches and awkward dinner dates there, I couldn't forget the route. Not that I'd tried."
        "(Counsciously, at least)." 
        "By the time I reach the resturaunt, Jeremy is already there."
        play audio "audio/rustle flower.wav"
        show flower
        "There's still a vase of plastic flowers at the pay station up front. Might be the same ones since the last time I was here."

        menu:
            "Grab a flower":
                $ inventory.append("plastic flower")
                stop audio
                jump dinner 
            "Head to table":
                stop audio
                jump dinner

    label dinner:
        hide flower
        show bg resturaunt
        with dissolve
        show jeremy happy
        with dissolve
        j "Hey Maya!"
        j "It's good to see you!"
        j "How've you been?"
        menu:
            "Not great, Jer.":
                hide jeremy happy
                show jeremy neutral
                show screen resentment_jeremy
                with dissolve
                show screen sympathy_jeremy
                with dissolve
                $jeremysymp += 1
                $townsymp += 1
                "Jeremy's face falls"
        j "Shoot, I shouldn't have asked."
        j "I'm sorry for your loss."
        j "God, that was stupid of me."
        j "I'm so, so sorry."
        "Why do I now have to comfort Jeremy?"
        "Should I feel offended? Angry?"
        "How fucked is it that I just feel numb?"
        m "Please don't worry about it."
        j "I just—"
        m "It's fine Jeremy"
        "My voice comes out sharper than I mean it to."
        "Thankfully, Jeremy seems to get the message."
        j "Okay, okay."
        j "How has cleaning out the house been going?"
        j "Find anything cool?"
        j "Need any help?"
        "Jesus, I forgot how nosy he was."
        "Anything I tell him will get to half of town by the end of dinner."
        "I try to ignore the hungry look in his eyes."

        menu:
            "No and no.":
                $jeremyres += 1
                $townres += 1
                hide jeremy neutral
                show jeremy sad
                j "Okay, okay! Jeez, you don't gotta be agro about it!"
                j "Anything about Monica though?"
                "He {i}would{/i} be tactless enough to straight up ask."
                m "Yeah, actually."
            "Yeah, actually. Some old newspapers.":
                $townsymp += 1
                m "Mostly about Monica, actually."
                hide jeremy sad
                show jeremy happy
                $townsymp += 1
                j "Huh."
                j "Any idea why?"
                m "Guess she was still following along."
                hide jeremy happy
                show jeremy neutral
        j "You know, your Aunt Rachel was the only one that still talked about Monica."
        j "'Specially in the end, when her filter was going."
        menu:
            "What was she saying?":
                hide jeremy neutral
                show jeremy happy
                "Jeremy's face lights up."
                "He always did love gossip."
                $jeremysymp += 1
                j "Just the usual shit about a 'coverup.'"
                j "Honestly, we were scared she'd end up talking to a podcast or something."
                j "Some people were kinda relieved when she...."
                hide jeremy happy
                show jeremy sad
                j "Well...."
        "So people here are happy that she can't rock the boat anymore."
        "What else is new."
        "Jeremy looks awkward, like he didn't mean to let that last part slip."
        hide jeremy sad
        show jeremy neutral
        "I grew up with him. I know he's about to change..."
        j "Have you texted Laney yet?"
        "... the subject."
        menu:
            "Why does everyone keep asking that?":
                $jeremysymp += 1
                j "Ah, did Ryan ask you about her too?"
                j "Or anyone else since you've gotten back to town?"
                "Of course Jeremy knows I've been talking to Ryan."
                "He also surely knows I haven't talked to anyone else yet."
                m "Yep."
                j "Well, I guess it's cause you were such good..."
                j "...friends..."
                j "... so we figured you'd have texted her first thing."
            "I don't have her number anymore.":
                $townres += 1
        j "Did you delete her number or something?"
        "I absolutely did, but I can't tell him that."
        m "Must've lost it over the years."
        m "New phones and all."
        $jeremyres += 1
        $townres += 1
        j "Huh."
        "Too late, I remember telling Ryan I still had Jeremy's number, all these years later."
        "He's clearly suspicious."
        $jeremyres += 1
        $townres += 1
        j "Well, I can text it to you."
        m "That would be great."
        "Finally, a waitress wanders over."
        w "Welcome to Siam Thai. Do you know what you two'd like to eat?"
        hide jeremy neutral
        show jeremy happy
        "Jeremy looks at the menu."
        j "I'll have the California Rolls, please!"
        "He turns to me."
        j "Want to split some egg rolls? Or maybe a Pad Thai?"
        "Fuck, I hate it here."
        jump laneyconvo
    
    label laneyconvo:
        hide screen resentment_jeremy
        hide screen sympathy_jeremy
        hide jeremy neutral
        show bg flashback
        with dissolve
        "In the end, it's Ryan that sends me Laney's phone number."
        "She texts me back quickly."
        "By the next morning, I'm walking over to the new convent to see her."
        
        show bg nunnery
        with dissolve
        "I'm early."
        l "Maya! Hey!"
        show laney neutral
        with dissolve
        m "Hey Laney."
        "I take in her habit. I hadn't forgotten she'd become a nun, exactly."
        "I'd just put it from my mind."
        l "Actually, it's Sister Lauren now."
        "She says it kindly, but I know I won't be able to call her that."
        "(In my head, at least)."
        l "How're you feeling? Being back in town?"
        "Of course she'd know the real mindfuck isn't Aunt Rachel's death. That it's being back in St.____."
        menu:
            "It's weird.":
                show screen resentment_laney
                with dissolve
                show screen sympathy_laney
                with dissolve
                l "That makes sense."
                hide laney neutral
                show laney sad
                l "I know you didn't want to come back."
                "Of course she'd remember that too."
                $laneysymp += 1
            "Shrug.":
                show screen resentment_laney
                show screen sympathy_laney
                hide laney neutral
                show laney sad
                l "I'm sorry."
                l "I know you didn't want to come home."
                "I inhale sharply."
                m "It's not home anymore."
                $laneyres += 1
        l "Why are you here, anyways?"
        "Well that gives me pause."
        m "...because my Great Aunt died?"
        hide laney sad
        show laney mad
        l "I know that."
        l "I mean why're you here."
        l "Talking to me."
        menu:
            "Ryan and Jeremy kept bothering me.":
                $laneyres += 1
                "Laney scowls."
                l "Yeah well. They wouldn't shut up about you all week."
                l "Since they knew you were coming back."
            "I missed you.":
                $laneysymp += 1
                l "I missed you too."
                "She says it so softly."
        hide laney mad
        show laney sad
        l "I saw your Aunt one last time."
        l "Right before she died."
        l "Mother Superior wanted me to ask if she wanted any final rites."
        "I look at her, angry."
        m "You didn't, did you?"
        hide laney sad
        show laney mad
        l "Of course not!"
        "She looks angry that I even asked."
        $laneyres += 1
        m "Sorry."
        m "You never know in this town."
        hide laney mad
        show laney neutral
        $laneysymp += 1
        l "I know."
        "I take a deep breath."
        m "Did she say anything?"
        m "About me?"
        m "Before..."
        hide laney neutral
        show laney sad
        l "She said she missed you."
        "Unlike Ryan, she doesn't look like she blames me for not coming back."
        "She looks away."
        hide laney sad
        show laney eyes
        "For the first time, I feel a lump in my throat."
        "I blink tears away."
        menu:
            "Bring up the newspaper.":
                m "Lane—"
                m "Sorry, Lauren—"
                m "I found stacks of newspapers on Aunt Rachel's desk."
                m "They were all about Monica Stein."
                if laneysymp > 2 and laneyres < 2:
                    l "She got a bit obsessed, towards the end."
                    l "She kept demanding to visit Carol Johnson. Do you remember Carol?"
                    "I nod."
                    l "Of course you remember Carol, she was at your house all the time."
                    "Laney mutters to herself, then speaks up again."
                    l "Anyways."
                    l "Aunt Rachel claimed Carol knew something."
                    l "She didn't believe us when we told her they'd fallen out years ago..."
                    l "...and Carol wouldn't want to speak to her."
                    hide laney eyes
                    show laney neutral
                else:
                    "Laney eyes me suspiciouly."
                    hide laney eyes
                    show laney mad
                    l "Yes, well."
                    l "She got obsessed there, in the end."
                    $laneyres += 1
                    m "Jeremy said."
                    m "And that it upset people."
                    $laneysymp += 1
                    hide laney mad
                    show laney sad
                    l "We all talked to her."
                    l "Ryan visited. Jeremy and I called."
                    l "She wasn't alone, okay?"
                    "The lump in my throat grows bigger."
                    m "Thank you."
        "I take a deep breath."
        "There's another reason I came here."
        "It's not just that I wanted to see Laney."
        "I have to remind myself of that."
        m "Lauren...."
        show laney neutral
        m "I want to visit it."
        m "The old convent."
        m "Where {i}it{/i} happened."
        m "Can you get me in?"
        hide laney neutral
        show laney eyes
        l "Why?"
        menu:
            "For closure.":
                $laneysymp += 1
                l "God, Maya. We both know it won't do shit."
                "I look at her, surprised."
                l "What?"
                m "I didn't realize nuns could swear."
                hide laney eyes
                show laney happy
                l "Well..."
                l "... Maybe not in front of Mother Superior."
                l "But in front of old friends?"
                l "I think it's okay."
                menu: 
                    "Is that what we are?":
                        hide laney happy
                        show laney sad
                        menu:
                            "Friends?":
                                hide laney sad
                                show laney mad
                                l "Yes."
                                l "That's it."
            "I'm curious.":
                hide laney eyes
                show laney neutral
                l "Sure."
        l "Tell you what, I'll give you a key, and you can stop by tomorrow, okay?"
        show laney neutral
        menu:
            "Will you come with me?":
                $laneysymp += 1
                l "I can't."
                if laneysymp > 3 and laneyres < 3:
                    l "I wish I could."
                else:
                    l "I think you'll have to go by yourself."
                play sound "audio/key sound.wav"
                "Laney hands me the key."
                $ inventory.append("key")
            "Can I pick it up tomorrow?":
                $laneyres += 1
                "I might be busy, but I'll see what I can do."
        hide laney neutral
        jump outrotemp

    label outrotemp:
        play music "audio/key sound 2.wav"
        play sound "audio/ocean.wav"
        hide screen resentment_laney
        hide screen sympathy_laney
        hide screen inventory
        window hide
        show bg outrotemp
        with dissolve
        pause
    return









        
        


        












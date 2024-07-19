# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Goode")

# stat initialization

$ stat_tech = 0
$ stat_create = 0
$ stat_stam = 0
$ stat_cha = 0





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show goode default

    g "Hello, hello! Who is this?"

label name_selection:

menu:
    "What is your first name? (Click Here)":
        $ player_name_first = renpy.input("Type your first name.")
        $ player_name_first = player_name_first.strip()

        if player_name_first == "":
            $ player_name_first = "Ashley"

        $ player_name_last = renpy.input("Now type your last name.")
        $ player_name_last = player_name_last.strip()

        if player_name_last == "":
            $ player_name_last = "Jordan"

define p = Character("[player_name_first]")

p "It's me, %(player_name_first)s %(player_name_last)s."

g "%(player_name_first)s, you say? You're not calling from your mobile, so I'll have to confirm that it's you--"
    
g "by asking you a few questions."

p "Security questions?"

menu:
    "'Trust but verify', mate! First off, are you a bloke or a bird?"
    "Bloke.":
        $ player_gender = "male"
    "Bird.":
        $ player_gender = "female"
    "Bloke? Bird? What??":
        jump bloke_bird_explain
    "Why are you British?":
        jump british_explain

jump gender_confirmed

label bloke_bird_explain:

    g "Blokes are boys, and birds are girls."

menu:
    g "Now one more time: are you a bloke or a bird?"

    "Bloke.":
        $ player_gender = "male"
        jump gender_confirmed

    "Bird.":
        $ player_gender = "female"
        jump gender_confirmed

jump birth_date_choice

label british_explain:

    g "Just lucky, I suppose."

menu:
    g "Now answer the question, are you a bloke or a bird?"

    "Bloke.":
        $ player_gender = "male"
        jump gender_confirmed

    "Bird.":
        $ player_gender = "female"
        jump gender_confirmed

    "I don't speak British, mate. What do those two words even mean?":
        jump bloke_bird_explain

label gender_confirmed:

$ cockney_gender = ""

if player_gender == "male":
    $ cockney_gender = "bloke"
else:
    $ cockney_gender = "bird"

$ goode_pronoun = ""

if player_gender == "male":
    $ goode_pronoun = "mate"
else:
    $ goode_pronoun = "luv"

g "Hmmm.. that sounds about right."

g "Aaaand... your birth date?"


label birth_date_choice:

    $ birth_date = None
    while birth_date is None:
        $ birth_date = renpy.input("Enter your birth date (MM-DD):")

    $ month, day = map(int, birth_date.split('-'))

"You entered: [birth_date]"

"Month: [month], Day: [day]"

menu:
    "Is this correct?"
    "Yes.":
        jump more_questions
    "No.":
        jump birth_date_choice

g "I barely remember your party last year. Went a lil too heavy on the bevvies, if you know what I mean."

label more_questions:

menu:
    g "Next..."
    "What, more questions?":
        g "Gotta ask you more than just what's on your ID card, y'know?"
        jump background_choice
    "Go on...":
        jump background_choice

label background_choice:

menu:
    g "Would you say you grew up with a lot of money?"
    "Money? Nope.":
        $ background = "poor"
    "I didn't get all the brand name stuff in high-school, if that's what you mean.":
        $ background = "middle-class"
    "Money? I'd say we had enough to be comfortable.":
        $ background = "rich"

label previous_study_choice:

    g "Okay. Last question."

$ stat_tech = 0
$ stat_create = 0
$ stat_stam = 0
$ stat_cha = 0
$ previous_studies = ""

menu:
    g "Which uni program were you studying for last year?"
    "Computer science.":
        $ stat_tech += 10
        $ previous_studies = "studying computer science"
    "Creative writing.":
        $ stat_create += 10
        $ previous_studies = "studying creative writing"
    "Just taking classes to keep my sports scholarship.":
        $ stat_stam += 10
        $ previous_studies = "on an academic scholarship"
    "Performing arts.":
        $ stat_cha += 10
        $ previous_studies = "studying performing arts"

label char_creation_summary:

g "So lemme get this straight..."


g "You're a [cockney_gender] named [player_name_first] [player_name_last]. Your birth date is [month] [day]."

g "You grew up [background], and your were [previous_studies] last year."

menu:
    g "Is that your story?"
    "That's correct":
        jump confirm_character
    "I'd like to change my story.":
        g "Alright. Let's start from the top, then."
        jump name_selection


label confirm_character:

g "Alright. From the answers you provided..."

g "..."

g "You're either the real [player_name_first] [player_name_last] or a scammer with some wizard AI."

g "So what do you need?"

p "Let's meet up at the Pacific Centre food court."

g "Sure, [goode_pronoun], but why?"

p "I'll explain later. Just be there in 30 minutes."

g "Ok. I'll see you there."

show bg pacific_centre
with dissolve

label scene001_intro_meeting:

g "Hey [goode_pronoun]. Why'd you wanna meet up here?"

p "Lost my phone yesterday, so I..."



'''The gameplay / code loop should look like this:
1. There should be a section for each in-game day, from September 1st 2024 to September 1st 2025 (365 days).
2. Each day will have it's own flags, such as weather, day of the week, weekday vs weekend.
3. On each day, the choice between daytime and evening activities can be selected.
4. There are events that will occur on certain days. Some of them are mandatory, and some are optional, depending on which flags are set.

Events should be seperated away from the rest of the script: perhaps at the start or end of the script or secluded away in its own.
Events should have a flag to indicate whether they have triggered or not on any particular playthrough.

All stats and other variables should be initialized at the beginning fo the script before any events trigger.

'''





return
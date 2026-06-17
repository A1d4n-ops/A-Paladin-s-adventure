#RPG Continuous Game Play - Aidan Choon Dipsingh

#This program runs a text-based game which is based around a paladin's journey
#and the user gets to choose how the story plays out with user input



import sys  # Import the sys module for system-specific parameters and functions (not used explicitly here)
import time  # Import the time module for adding delays

def slow_reveal(text):  # Define a function to display text slowly character by character
    for char in text:  # Loop through each character in the input text
        print(char, end="", flush=True)  # Print the character without a newline, flush output immediately
        time.sleep(0.03)  # Pause for 0.03 seconds between characters
    print()  # Print a newline after the entire text is revealed

# Define the main story structure as a dictionary
journey = {
    "start": {
        "text": "\nWould you like to undertake the trials of the Paladin?",  # Starting scene text
        "choices": {  # Dictionary of choices in this scene
            "1": {
                "text": "You decide to take the challenge to give gods's grace to the people ",  # Choice 1 text
                "next": "village"  # Next scene if choice 1 is selected
            },
            "2": {
                "text": "You decide to live your own life",  # Choice 2 text
                "next": "lose"  # Next scene if choice 2 is selected
            }
        }
    },
    
    "village": {
        "text": "\nYou reach a village being attacked by bandits. What would you like to do?",  # Scene description
        "choices": {  # Choices in this scene
            "1": {
                "text": "Stay and fight off the bandits",  # Choice 1 text
                "next": "save_village"  # Next scene if choice 1
            },
            "2": {
                "text": "You ignore them and continue, thinking that this is their fight",  # Choice 2 text
                "next": "graveyard"  # Next scene if choice 2
            }
        }
    },

    "save_village": {  # Scene where the player saves the village
        "text": """\nYou save the village and the people are thankful.
They all want to express it in some way""",  # Multi-line scene description
        "choices": {  # Choices after saving the village
            "1": {
                "text": "Tell them of the religion of your god and make them believers",  # Choice 1
                "next": "spread_religion"  # Next scene
            },
            "2": {
                "text": "Accept the money that they decide to pool for you",  # Choice 2
                "next": "graveyard"  # Next scene
            }
        }
        },
    "spread_religion": {  # Scene where the player spreads religion
        "text": """\nYou decide to teach the villagers of your benevolent god.
You can feel that your god is pleased with your actions.\nIt is time to move on with your journey""",  # Scene description
        "choices": {  # Choices in this scene
            "1": {
                "text": "You choose your next destination to be the graveyard",  # Choice 1
                "next": "graveyard"  # Next scene
                },
            "2": {
                "text": "You choose your next destination to be the land of demons-Asabar",  # Choice 2
                "next": "asabar"  # Next scene
                }
            }
        },
    "graveyard": {  # Scene at the graveyard
        "text": """\nYou arrive at the graveyard, where the number of tombstones scatter as far as the eye can see.
Your light is the dimly-lit moon.""",  # Scene description
        "choices": {  # Choices in graveyard
            "1": {
                "text": "You decide to inspect the tombstones, and you find a cursed artifact that is on one of the graves",  # Choice 1
                "next": "artifact"  # Next scene
                },
            "2": {
                "text": "You decide to respect the dead and leave",  # Choice 2
                "next": "asabar_lose"  # Next scene
                }
            }
        },
    
    "asabar_lose": {  # Scene where the player chooses not to help in the holy war
        "text": """\nYou decided to head to Asabar.
There is currently a holy war is occuring involving the Holy Kingdom and the demons.""",  # Scene description
        "choices": {  # Choices in this scene
            "1": {
                "text": "You decide to help with the crusade and bring the judgment of God upon those who dare oppose them",  # Choice 1
                "next": "battle_lose"  # Next scene
                },
            "2": {
                "text": "You decide to leave, thinking that you do not need to join this fight",  # Choice 2
                "next": "adventurer"  # Next scene
                }
            }
        },
    
    
    "artifact": {  # Scene involving the cursed artifact
        "text": """\nThe artifact ,upon a closer inspection, seems to be a locket, which inside shows a picture of a family.
You hear the sounds of the souls tied to the locket.""",  # Scene description
        "choices": {  # Choices after examining the artifact
            "1": {
                "text": "You decide to relieve the souls from the locket by using divine power",  # Choice 1
                "next": "purified"  # Next scene
                },
            "2": {
                "text": "You decide to destroy the Amulet",  # Choice 2
                "next": "amulet_loss"  # Next scene
                }
            }
        },
    "purified": {  # Scene after purifying the artifact
        "text": """\nAfter purifying the locket, it gains the properties of a divine artifact.
You feel a great boost to your power when holding it.""",  # Scene description
        "choices": {  # Choices after purification
            "1": {
                "text": "You decide to take the locket, and go to Asabar, where a holy war is taking place",  # Choice 1
                "next": "asabar"  # Next scene
                },
            "2": {
                "text": "You decide to continue exploring the world",  # Choice 2
                "next": "adventurer"  # Next scene
                }
            }
        },
    "adventurer": {  # Scene where the player becomes an explorer
        "text": """\nNo longer concerning yourself with the will of the church, you explore the world.
You become an adventurer, making a name for yourself""",  # Scene description
        "choices": {  # Choices in adventurer scene
            "1": {
                "text": "Restart your journey",  # Choice 1
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Choice 2
                "next": "start"  # Restart at start
                }
            }
        },
    "asabar": {  # Scene heading to Asabar
        "text":"""\nYou decided to head to Asabar.
There is currently a holy war is occuring involving the Holy Kingdom and the demons.
You feel more confident as your divine power has a boost thanks to the locket.""",  # Scene description
        "choices": {
        "1": {
            "text": "You decide to bring judgement upon the demons who dare to stand against God",  # Choice 1
            "next": "battle"  # Next scene
            },
        "2": {
            "text": "You decide to leave, thinking that maybe this isn't for you, and that you should live a different life",  # Choice 2
            "next": "adventurer"  # Next scene
            }
        }
        },
        
    
    "lose":{  # Scene where the player dies
        "text": "You die a tragic death before you could venture into the world",  # Scene description
        "choices": {  # Choices after death scene
            "1": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                }
            }
        },
    "battle_lose": {  # Scene where the player loses a battle
        "text": """\nYou fought valiantly on the battle field, but your power is simply not enough.
You are swarmed by the sheer mass of the horde of demons and lose your life""",  # Scene description
        "choices": {  # Choices after losing battle
            "1": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                }
            }
        },
    "battle": {  # Scene where the player wins a battle
        "text": """\nYou charge at the swarm of enemies, your holy power enveloping your sword.
It's blinding light raises morale umong the troops, and they began to push back the demons.
It was thanks to the locket that you were able to bring forth such power.
The battle ends in a victory for the humans, and as a reward, you were given 2 options""",  # Scene description
        "choices": {  # Choices after victory
            "1": {
                "text": "You decide to become a bishop of the church",  # Choice 1
                "next": "bishop"  # Next scene
                },
            "2": {
                "text": "You decide to become a Viscount",  # Choice 2
                "next": "viscount"  # Next scene
                }
            }
        },
    "bishop": {  # Scene where the player becomes a bishop
        "text": """\nDue to having a large amount of holy power, you were given the option to become a bishop.
You accepted this, solidifying your determination to serving your god, who finally reveals their name to you.
Their name is Michael""",  # Scene description
        "choices": {  # Choices in bishop scene
            "1": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Restart option
                "next": "start"  # Restart at start
                }
            }
        },
    "viscount": {  # Scene where the player becomes a viscount
        "text": """\nDue to your huge contributions to the battle, you were given the title of Viscount.
In addition, you also received a patch of land in Asabar. How you choose to develop the viscounty is up to you.""",  # Scene description
        "choices": {  # Choices in viscount scene
            "1": {
                "text": "You decide to develop the religion of the viscounty",  # Choice 1
                "next": "holy_city"  # Next scene
                },
            "2": {
                "text": "You decide to develop the technology of the viscounty",  # Choice 2
                "next": "advanced_city"  # Next scene
                }
            }
        },
    "holy_city": {  # Scene focusing on religious development
        "text": """\nChoosing to focus on the development of religion of the viscounty, your connection with your God increases.
This caused fellow followerers as well to gain more holy power.
Because of this, people began to call the viscounty 'The true holy city'""",  # Scene description
        "choices": {  # Choices in holy city scene
            "1": {
                "text": "Restart your journey",  # Restart
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Restart
                "next": "start"  # Restart at start
                }
            }
        },
     "advanced_city": {  # Scene focusing on technological development
        "text": """\nChoosing to develop the technology, your city quickly grew.
This was thanks to what the demons left behind in Asabar before the battle.
Due to the quick development and advanced technology, people began to call this place 'Metropolis'.""",  # Scene description
        "choices": {  # Choices in city development scene
            "1": {
                "text": "Restart your journey",  # Restart
                "next": "start"  # Restart at start
                },
            "2": {
                "text": "Restart your journey",  # Restart
                "next": "start"  # Restart at start
                }
            }
        },
    }

current_scene = "start"  # Initialize current scene to 'start'

while True:  # Infinite loop to keep the game running
    scene = journey[current_scene]  # Get the current scene data from the journey dictionary

    print("\n" + scene["text"])  # Display the scene's main text

    # Display choices
    for number, choice in scene["choices"].items():  # Loop through each choice in the scene
        slow_reveal(f"{number}. {choice['text']}")  # Slowly reveal each choice with number and text

    slow_reveal("3. Quit game")  # Offer option to quit the game

    user_choice = input("\nWhat do you do?: ")  # Prompt the user for their decision

    # Quit game if user inputs '3'
    if user_choice == "3":
        slow_reveal("\nYou quit the game.")  # Display quit message
        exit()  # Exit the program

    # Continue game if user input matches one of the choices
    elif user_choice in scene["choices"]:
        current_scene = scene["choices"][user_choice]["next"]  # Move to the next scene

    else:  # If user input is invalid
        slow_reveal("Invalid choice.")  # Notify user of invalid input

# Display the last scene's text after the loop ends (though in this code, loop doesn't naturally end)
slow_reveal(scene["text"])

# Thank the player for playing
slow_reveal("\nThanks for playing!")               
        
   
    
    


    

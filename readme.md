Hi all - I hope you’re staying safe and weathering the Corona Virus storm as best you can… I’m just recovering from 8 days fighting the virus and now I can concentrate for more than 10 minutes at a time I have an idea for a community support app which I’d appreciate comments, ideas and feedback on please.
TLDR: I realised we have loads of items we’re not going to need during London’s lock-down period but which might be of great value to a neighbour (e.g. 60 cans of Ginger Beer and 20 tins of chopped tomatoes); if there were an app to tell me who’s most in need and within walking/driving distance, I could easily drop them off and do a good deed.
In particular, I’m looking for urgent and pragmatic comments about the following please:
1.	Does anyone know if something like this app already exists? No point reinventing the wheel…
2.	If not, is there something similar that could be built upon or re-purposed?
3.	If not, what do you think about the ‘stack’ I’m proposing below? Critical success factors are: it has to be simple enough for me to build (unless a better volunteer swoops in with expertise on a different stack); time is of the essence; it has to be easily usable and accessible to non-tech savy users.
Please read on if you have time and are able to offer your time/thoughts. My aim is to start sharing something within my own neighbours here in South London in a few days, so time is of the essence and I’d just appreciate a sanity check before charging off on my own Many thanks.
OVERALL GOAL
Create a web app which enables:
a) people in the same geographic to ‘advertise’ excess provisions, medicine, household goods and comfort items they’re willing to share (freely) with neighbours, and/or their ability to pick up/deliver such goods to those in need (vulnerable, locked-down, ill)
b) people in need to post urgent requests for such goods;
c) [Nice to have] people going a bit stir-crazy during lock-down to connect with neighbours and request social interaction via existing tools such as social media, text chats, old fashioned telephone, or video.
Think: Shared shopping list app with a little to-do list functionality (create, assign, accept, close jobs) made available online to hyper-local contacts only so as not to ‘swamp’ people with too much information (similar to the way https://nextdoor.co.uk/ creates hyperlocal groups).
WORKING TITLE
WGACA (“What goes around comes around”), since the idea is to enable and encourage positive community action and create "good karma’ during these unprecedented times specifically and literally by literally passing around goods and provisions to those more in need. An antidote to selfish panic-buying stimulated by some simple information sharing to match what can be spared with where it’s needed.
PROVISIONAL SOLUTION/TECHNOLOGY STACK
•	Python 3.8 - because it’s all I know and I’m planning to have to make this happen on my own initially.
•	https://anvil.works/ - because I don’t have time to learn and deploy a scalable web app with database, user authentication, email, and (nice to have) google maps integration and this seems like a fast route to getting something “out there” quickly.
That’s all - as few layers/dependencies as possible.
FYI I did consider setting up a simple discussion forum where people could interact with their offers/requests and may still do so for the social aspects of this but believe an app is better because the data can them be standardised, both for sharing with other charities/volunteers/government support teams and for down-stream automation (e.g. calculating optimum pick-up and drop-off delivery routes for volunteer drivers/walkers).
KEY RISKS / KNOWN INFORMATION GAPS
1.	Abuse of the system by selfish/criminal elements. I’m thinking about making each registered user’s “karma history” available for other registered users to view - including everything they’ve offered/donated, every delivery they offered/donated, “reviewers’ comments” and on the flip side everything they’ve asked for/received. Perhaps create a moderator role blocking/blacklisting abusers. Perhaps a human/physical authentication factor such as hand delivering invitation codes to real neighbours telling them about the app; perhaps cross-checking with the UK electoral roll.
2.	Taxonomy of objects. I can see non-standardisation becoming a problem (“toothpaste”, “tooth-paste”, “Tooth Paste”) and would appreciate any pointers towards supermarket style solutions or databases which may have already solved this problem. I think we can completely disregard brands but if there was an item/category heirarchy I could just pick up and present to users e.g. “Health & Hygeine | Dental | Toothpaste (child/adult/denture etc)” that would save a tonne of time.
3.	Without reaching out to the like of NextDoor.co.uk who already have a solution to this, it would also be a great time saver to find an existing database that breaks down streets to towns/boroughs and possibly postcodes, or at least estimated and limited walking/driving distance in order to define “local” areas and groups.
If you made it this far… apologies for the long rambling post and thank you in advance for any help or brain-power you can offer.
Best wishes,
Peter


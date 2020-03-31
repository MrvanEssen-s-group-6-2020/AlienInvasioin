Terms:
    
    Project:
        A script or group of scripts that are all associated.
        In our case, everything held within the folder Alien invasion.

    Personal project:
        This refers to the projects each editor will do themselves.
        This includes the code that they write while following the
        tutorial in the book, or code which goes beyond the book
        which they are developing.

    The group project:
        This refers to the project which will be submitted for the
        entire group. This project will be edited by each editor so that
        it meets all the spesifications which are layed out by the book
        regarding how the game should run and function. It will also
        include code added by each editor which goes beyond the scope
        of the book.

Intagrating personal projects into the group projects:
    
    Updating the code to keep up with the book:
        One or more persons in the group will be selected to modify the 
        group project's code by refactoring it and adding code so that 
        it is up to date with the code in the book.
    
    Adding your own ideas:
        If one editor intends to add special code to the group project
        which will change the functionality of the game, or they intend
        to refactor the code to make it easier to read or more efficent,
        they should first:
            Make it clear what they plan to do,
            Have a plan for how to do it,
        Then they should follow these steps.
            -Download the latest version of the group project.
            -Intagrate the changes they intend to make
            -Make sure the code is well comented
            -Report the changes they made in the version Report with a date
            https://docs.google.com/document/d/1D8m68YM8SNzEcUK5UvHE2F1jrYRUGz_RZIVXAIGyAoM/edit?usp=sharing
                Date format is MMMM-YY-DD
            -Bugtest and debug the Project
            -Update the version AND DATE in settings.py
            -Update the version in the name of the Project folder
            -Upload a zip file of the group project and pin it.
        When updating the group project, it is very important that when
        you upload an updated version of the group project it MUST NOT
        HAVE GAME CRASHING BUGS
    
    Other members in the group can choose to Veto a group project
    update if they feel it makes the code too chaotic or makes the
    game less playable


Updating Versions:
    In settings.py there is a variable called "self.version" when 
    updating the vesrion, you will simply be changing the string so it
    is clear that the code has been changed.

    The format:
        Refactoring or adding code will change the version by .1
        (Alpha 1.0 => Alpha 1.1)
        Simply changing spelling mistakes, or settings in settings.py
        which will have very little effect on the functionality of the
        proam will change the version by 0.0.1
        (Alpha 1.2 => Alpha 1.2.1)
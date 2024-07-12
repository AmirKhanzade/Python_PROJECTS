def your_story(word_type:str):
    user_input:str=input(f'Please enter your {word_type}')
    return user_input
noun1=your_story("noun1: ")
adjective1=your_story('adjective1: ')
verb1=your_story("verb1: ")
noun2=your_story('noun: ')
adjective2=your_story('adjective: ')
verb2=your_story('verb:  ')

story=f"""once upon a time there was a {adjective1} {noun1} who loved to {verb1} all day.
one day,{noun2} walked into room and caught the {noun1} in the act!
{noun2}:what are you doing?
{noun1}:I am just {verb1}ing , what's the big deal?
{noun2}:well, it is not every day that you see a {noun1} {verb1}ing in the middle of the day
{noun1}:I guess you are right maybe I should take a break.
{noun2}:probably good idea,why don't we go {verb2} instead?
{noun1}:sure,that  sounds like fun!

And so {noun1} and {noun2} went off to {verb2} and had agreat time.
THE END
"""
print(story)

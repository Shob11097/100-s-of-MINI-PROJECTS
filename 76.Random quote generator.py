#Random quote generator

from random import choice
quotes = "You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.",\
         "I’m selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can’t handle me at my worst, then you sure as hell don’t deserve me at my best." \
         "Life is what happens when you’re busy making other plans.", \
         "Get busy living or get busy dying" \
         "The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself.",\
         "When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.",\
         "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do." \
         "When I dare to be powerful – to use my strength in the service of my vision, then it becomes less and less important whether I am afraid."
print(choice(quotes))
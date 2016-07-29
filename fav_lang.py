# import OrderedDict class from the module collections
from collections import OrderedDict

# create an instance of the OrderedDict class and store this instance in fav_lang
# the call to OrderedDict() creates an empty ordered dictionary for us
# allows us to always get back the responses in the order that we gave them
fav_lang = OrderedDict()

fav_lang['jen'] = 'python'
fav_lang['sarah'] = 'c'
fav_lang['edward'] = 'ruby'
fav_lang['phil'] = 'python'

for name, language in fav_lang.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

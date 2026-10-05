import matplotlib.pyplot as plt
story_text="""Once on a time and twice on a time, and all times together as ever I heard
tell of, there was a tiny lassie who would weep all day to have the stars
in the sky to play with; she wouldn’t have this, and she wouldn’t have
that, but it was always the stars she would have. So one fine day off she
went to find them. And she walked and she walked and she walked, till by-
and-by she came to a mill-dam.
“Goode’en to ye,” says she, “I’m seeking the stars in the sky to play
with. Have you seen any?”
“Oh, yes, my bonnie lassie,” said the mill-dam. “They shine in my own face
o’ nights till I can’t sleep for them. Jump in and perhaps you’ll find
one.”
So she jumped in, and swam about and swam about and swam about, but ne’er
a one could she see. So she went on till she came to a brooklet.
“Goode’en to ye, Brooklet, Brooklet,” says she; “I’m seeking the stars in
the sky to play with. Have you seen any?”
“Yes, indeed, my bonny lassie,” said the Brooklet. “They glint on my banks
at night. Paddle about, and maybe you’ll find one.”
So she paddled and she paddled and she paddled, but ne’er a one did she
find. So on she went till she came to the Good Folk.
“Goode’en to ye, Good Folk,” says she; “I’m looking for the stars in the
sky to play with. Have ye seen e’er a one?”
“Why, yes, my bonny lassie,” said the Good Folk. “They shine on the grass
here o’ night. Dance with us, and maybe you’ll find one.”
And she danced and she danced and she danced, but ne’er a one did she see.
So down she sate; I suppose she wept.
“Oh dearie me, oh dearie me,” says she, “I’ve swam and I’ve paddled and
I’ve danced, and if ye’ll not help me I shall never find the stars in the
sky to play with.”
But the Good Folk whispered together, and one of them came up to her and
took her by the hand and said, “If you won’t go home to your mother, go
forward, go forward; mind you take the right road. Ask Four Feet to carry
you to No Feet at all, and tell No Feet at all to carry you to the stairs
without steps, and if you can climb that—”
“Oh, shall I be among the stars in the sky then?” cried the lassie.
“If you’ll not be, then you’ll be elsewhere,” said the Good Folk, and set
to dancing again.
So on she went again with a light heart, and by-and-by she came to a
saddled horse, tied to a tree.
“Goode’en to ye, Beast,” said she; “I’m seeking the stars in the sky to
play with. Will you give me a lift, for all my bones are an-aching.”
“Nay,” said the horse, “I know nought of the stars in the sky, and I’m
here to do the bidding of the Good Folk, and not my own will.”
“Well,” said she, “it’s from the Good Folk I come, and they bade me tell
Four Feet to carry me to No Feet at all.”
“That’s another story,” said he; “jump up and ride with me.”
So they rode and they rode and they rode, till they got out of the forest
and found themselves at the edge of the sea. And on the water in front of
them was a wide glistening path running straight out towards a beautiful
thing that rose out of the water and went up into the sky, and was all the
colours in the world, blue and red and green, and wonderful to look at.
“Now get you down,” said the horse; “I’ve brought ye to the end of the
land, and that’s as much as Four Feet can do. I must away home to my own
folk.”
“But,” said the lassie, “where’s No Feet at all, and where’s the stair
without steps?”
“I know not,” said the horse, “it’s none of my business neither. So
goode’en to ye, my bonny lassie;” and off he went.
So the lassie stood still and looked at the water, till a strange kind of
fish came swimming up to her feet.
“Goode’en to ye, big Fish,” says she, “I’m looking for the stars in the
sky, and for the stairs that climb up to them. Will ye show me the way?”
“Nay,” said the Fish, “I can’t unless you bring me word from the Good
Folk.”
“Yes, indeed,” said she. “They said Four Feet would bring me to No Feet at
all, and No Feet at all would carry me to the stairs without steps.”
“Get on my back and hold fast.”
“Ah, well,” said the Fish; “that’s all right then. Get on my back and hold
fast.”
And off he went—Kerplash!—into the water, along the silver path, towards
the bright arch. And the nearer they came the brighter the sheen of it,
till she had to shade her eyes from the light of it.
And as they came to the foot of it, she saw it was a broad bright road,
sloping up and away into the sky, and at the far, far end of it she could
see wee shining things dancing about.
“Now,” said the Fish, “here you are, and yon’s the stair; climb up, if you
can, but hold on fast. I’ll warrant you find the stair easier at home than
by such a way; ‘t was ne’er meant for lassies’ feet to travel;” and off he
splashed through the water.
So she clomb and she clomb and she clomb, but ne’er a step higher did she
get: the light was before her and around her, and the water behind her,
and the more she struggled the more she was forced down into the dark and
the cold, and the more she clomb the deeper she fell.
But she clomb and she clomb, till she got dizzy in the light and shivered
with the cold, and dazed with the fear; but still she clomb, till at last,
quite dazed and silly-like, she let clean go, and sank down—down—down.
And bang she came on to the hard boards, and found herself sitting,
weeping and wailing, by the bedside at home all alone.-----
The story is written by
Roger Federer &
Serina Williams
You can connect with the author at [rfederer@tennis.com] and
[swilliams@tennis.com]
Admin contact number: 1-888-111-2222"""


#1 Word and Character Count Using a List
#Find Character Count:
total_characters = len(story_text)
# Process words with a list
words_list =[]
for word in story_text.split():
    cleaned_word =word.strip("!?.,""-':;").lower()
    if cleaned_word:
        words_list.append(cleaned_word)
total_words = len(words_list)
print(f"Total Character Count: {total_characters}")
print(f"Total Word Count: {total_words}")
#Create a histogram:
unique_words=[]
word_counts=[]

for word in words_list:
    if word not in unique_words:
        unique_words.append(word)
        word_counts.append(words_list.count(word))

#Plotting the 5 most common words in the text
top_words= sorted(zip(unique_words, word_counts), key=lambda x: x[1], reverse=True)[:5]
plot_words, plot_counts = zip(*top_words)

plt.figure(figsize=(10,5))
plt.bar(plot_words, plot_counts)
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.title("Top 5 Words by Frequency in Story")
plt.savefig('word_histogram.png')

#2. Repeat with a Dictionary
word_counts_dict={}
for word in words_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1
print("\nQuestion 2: Repeating with a Dictionary")
print(f"Total Unique Words (Keys in Dictionary): :{len(word_counts_dict)}")

sorted_dict_items = sorted(word_counts_dict.items(), key=lambda x: x[1], reverse=True)[:5]
dict_words, dict_counts = zip(*sorted_dict_items)

plt.figure(figsize=(10,5))
plt.bar(dict_words, dict_counts)
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.title("Step 2: Top 5 Words by Frequency in Story Using a Dictionary")
plt.savefig('word_histogram_dictionary.png')

#3. Regular Expressions for Data Extraction

import re

#Phone Number Pattern:(1-xxx-xxx-xxxx)
phone_pattern = r'\d-\d{3}-\d{3}-\d{4}'

#Email Pattern:(xxxxxxxxx@xxxxxx.xxx)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

#Extract phone and emails using re.findall()
extracted_phones = re.findall(phone_pattern, story_text)
extracted_emails = re.findall(email_pattern, story_text)

#Store both in a separate list
extracted_contacts = extracted_phones + extracted_emails

#Show results:
print("\nQuestion 3: Extracted Contact Info")
print(f"Extracted Phone Numbers: {extracted_phones}")
print(f"Extracted Email Addresses: {extracted_emails}")
print(f"Combined List: {extracted_contacts}")

#4. Email Username Processing
#Extract usernames through email address:
usernames = [email.split('@')[0] for email in extracted_emails]

#Append @hotmail.com to each extracted username
hotmail_emails = [f"{user}@hotmail.com" for user in usernames]

#Show resulting username
print("\nQuestion 4: Email Usernames")
print(f"Extracted Usernames: {usernames}")
print(f"Hotmail Email Addresses: {hotmail_emails}")


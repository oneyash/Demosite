import os, sys
currentFileFolder = os.path.realpath(os.path.dirname(__file__))
edmarketRoot = os.path.realpath(os.path.join(currentFileFolder, '..'))
if edmarketRoot not in sys.path:
    sys.path.append(edmarketRoot)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Demosite.settings")
import django
django.setup()


from article.models import Articles

body_text = "The Da Vinci Code is a 2003 mystery-detective novel by Dan Brown. It follows symbologist Robert Langdon and" \
            " cryptologist Sophie Neveu after a murder in the Louvre Museum in Paris, when they become involved in a " \
            "battle between the Priory of Sion and Opus Dei over the possibility of Jesus Christ having been married to " \
            "Mary Magdalene. The title of the novel refers, among other things, to the finding of the first murder victim " \
            "in the Grand Gallery of the Louvre, naked and posed like Leonardo da Vinci's famous drawing, the Vitruvian Man, " \
            "with a cryptic message written beside his body and a pentagram drawn on his chest in his own blood. " \

"The novel explores an alternative religious history, whose central plot point is that the Merovingian kings of France were " \
"descended from the bloodline of Jesus Christ and Mary Magdalene, ideas derived from Clive Prince's The Templar Revelation (1997) " \
"and books by Margaret Starbird. The book also refers to The Holy Blood and the Holy Grail (1982) though Dan Brown has " \
"stated that it was not used as research material." \
"The Da Vinci Code provoked a popular interest in speculation concerning the Holy Grail legend and Mary Magdalene's role " \
"in the history of Christianity. The book has, however, been extensively denounced by many Christian denominations as an " \
"attack on the Roman Catholic Church, and consistently criticized for its historical and scientific inaccuracies. " \
"The novel nonetheless became a worldwide bestseller[1] that sold 80 million copies as of 2009[2] and has been translated " \
"into 44 languages. Combining the detective, thriller and conspiracy fiction genres, it is Brown's second novel to include the " \
"character Robert Langdon: the first was his 2000 novel Angels & Demons. In November 2004, Random House published a Special " \
"Illustrated Edition with 160 illustrations. In 2006, a film adaptation was released by Sony's Columbia Pictures."

author = "Dan Brown"
title = "The Da Vinci Code"
category= "fiction"
image = "davincicode.jpg"
image_small = "davincicode_small.jpg"
publication_date = "2003-03-16"


article_data = Articles(title=title, author=author, category=category, image=image, image_small=image_small,
                        publication_date=publication_date, bodytext =body_text)
article_data.save()

author = "Amish Tripathi"
title = "The Immortals of Meluha"
category= "Fiction"
image = "shiva.jpg"
image_small = "shiva_small.jpg"
publication_date = "2010-02-05"

body_text = "The Immortals of Meluha is the first novel of the Shiva trilogy series by Amish Tripathi. The story is set " \
            "in the land of Meluha and starts with the arrival of the Shiva. The Meluhan believe that Shiva is their " \
            "fabled saviour Neelkanth. Shiva decides to help the Meluhans in their war against the Chandravanshis, " \
            "who had joined forces with a cursed group called Nagas; however, in his journey and the resulting fight " \
            "that ensues, Shiva learns how his choices actually reflected who he aspires to be and how it led to dire consequences." \
"Tripathi had initially decided to write a book on the philosophy of evil, but was dissuaded by his family members, so " \
"he decided to write a book on Shiva, one of the Hindu Gods. He decided to base his story on a radical idea that all Gods" \
" were once human beings; it was their deeds in the human life that made them famous as Gods. After finishing writing The " \
"Immortals of Meluha, Tripathi faced rejection from many publication houses. Ultimately when his agent decided to publish " \
"the book himself, Tripathi embarked on a promotional campaign. It included posting a live-action video on YouTube, and " \
"making the first chapter of the book available as a free digital download, to entice readers."
"Ultimately, when the book was published in February 2010, it went on to become a huge commercial success. It had to be " \
"reprinted a number of times to keep up with the demand. Tripathi even changed his publisher and hosted a big launch for " \
"the book in Delhi. It was critically appreciated by some Indian reviewers, others noted that Tripathi's writing tended " \
"to lose focus at some parts of the story. With the launch of the third installment, titled The Oath of the Vayuputras, " \
"on February 2013, the Shiva Trilogy has become the fastest selling book series in the history of Indian publishing, " \
"with 2.5 million copies in print and over ₹60 crore (US$8.9 million) in sales."



article_data = Articles(title=title, author=author, category=category, image=image, image_small=image_small,
                        publication_date=publication_date, bodytext =body_text)
article_data.save()

author = "J. K Rowling"
title = "Harry Potter"
category= "Fiction"
image = "harry.jpg"
image_small = "harry_small.jpg"
publication_date = "2010-02-05"

body_text = "This article is about the series of seven novels. For its eponym, see Harry Potter (character). For the " \
            "film series, see Harry Potter (film series). For related topics, see List of Harry Potter related topics. " \
            "For other uses, see Harry Potter (disambiguation)." \
"Harry Potter"\
"The Harry Potter logo, used first in American editions of the novel series and later in films."\
"The Harry Potter logo first used for the American edition of the novel series (and some other edition\s worldwide), and then the film series."\
"Harry Potter and the Philosopher's Stone (1997)"\
"Harry Potter and the Chamber of Secrets (1998)"\
"Harry Potter and the Prisoner of Azkaban (1999)"\
"Harry Potter and the Goblet of Fire (2000)"\
"Harry Potter and the Order of the Phoenix (2003)"\
"Harry Potter and the Half-Blood Prince (2005)"\
"Harry Potter and the Deathly Hallows (2007)"\

"Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the life" \
" of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts " \
"School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, the Dark wizard who " \
"intends to become immortal, overthrow the Ministry of Magic, subjugate non-magic people and destroy anyone who stands in his way."

"Since the release of the first novel, Harry Potter and the Philosopher's Stone, on 30 June 1997, the books have gained " \
"immense popularity, critical acclaim and commercial success worldwide. They attracted a wide adult audience, and have " \
"remained one of the preeminent cornerstones of young adult literature.[3] The series has also had some share of criticism, " \
"including concern about the increasingly dark tone as the series progressed, as well as the often gruesome and graphic " \
"violence depicted in the series. As of July 2013, the books have sold more than 450 million copies worldwide, making the" \
" series the best-selling book series in history, and have been translated into seventy three languages.[4][5] The last " \
"four books consecutively set records as the fastest-selling books in history, with the final instalment selling roughly " \
"eleven million copies in the United States within twenty four hours of its release."
"A series of many genres, including fantasy, drama, coming of age and the British school story (which includes elements " \
"of mystery, thriller, adventure, horror and romance), it has many cultural meanings and references.[6] According to Rowling," \
" the main theme is death.[7] There are also many other themes in the series, such as prejudice, corruption, and madness."

"The series was originally published in English by two major publishers, Bloomsbury in the United Kingdom and Scholastic" \
" Press in the United States. The play Harry Potter and the Cursed Child will open in London on 30 July 2016 at the Palace " \
"Theatre and its script will be published by Little, Brown in the United Kingdom on 31 July 2016, who also published " \
"Rowling's adult novels and those written under her pen name Robert Galbraith.[9] The seven books were adapted into an" \
" eight-part film series by Warner Bros. Pictures, which is the second highest-grossing film series of all time as of " \
"August 2015. The series also originated much tie-in merchandise, making the Harry Potter brand worth in excess of $15 billion.[10]"

article_data = Articles(title=title, author=author, category=category, image=image, image_small=image_small,
                        publication_date=publication_date, bodytext =body_text)
article_data.save()


author = "Khaled Hosseini"
title = "Kite Runner"
category= "Historical drama"
image = "kite.jpg"
image_small = "kite_small.jpg"
publication_date = "2003-05-03"

body_text = "The Kite Runner is the first novel by Afghan-American author Khaled Hosseini.[1] Published in 2003 by Riverhead Books, " \
            "it tells the story of Amir, a young boy from the Wazir Akbar Khan district of Kabul, whose closest friend is Hassan, " \
            "his father's young Hazara servant. The story is set against a backdrop of tumultuous events, from the fall of " \
            "Afghanistan's monarchy through the Soviet military intervention, the exodus of refugees to Pakistan and the United States, " \
            "and the rise of the Taliban regime."

"Hosseini has commented that he considers The Kite Runner to be a father–son story, emphasizing the familial aspects of " \
"the narrative, an element that he continued to use in his later works. Themes of guilt and redemption feature prominently " \
"in the novel,[3] with a pivotal scene depicting an act of violence against Hassan that Amir fails to prevent. " \
"The latter half of the book centers on Amir's attempts to atone for this transgression by rescuing Hassan's son over two decades later."

"The Kite Runner became a bestseller after being printed in paperback and was popularized in book clubs. It was a number " \
"one New York Times bestseller for over two years,[4] with over seven million copies sold in the United States.[5] Reviews " \
"were generally positive, though parts of the plot drew significant controversy in Afghanistan[citation needed]. " \
"A number of adaptations were created following publication, including a 2007 film of the same name, several stage " \
"performances, and a graphic novel."

article_data = Articles(title=title, author=author, category=category, image=image, image_small=image_small,
                        publication_date=publication_date, bodytext =body_text)
article_data.save()

author = "Arthur Conan Doyle"
title = "Sherlok Holmes"
category= "Thriller"
image = "sherlock.jpg"
image_small = "sherlock_small.jpg"
publication_date = "1887-08-27"

body_text = "Sherlock Holmes (/ˈʃɜːrlɒk ˈhoʊmz/) is a fictional private detective created by British author Sir Arthur " \
            "Conan Doyle. Known as a consulting detective in the stories, Holmes is known for a proficiency with observation, " \
                                                          "forensic science, and logical reasoning that borders on the fantastic, " \
            "which he employs when investigating cases for a wide variety of clients, including Scotland Yard. First appearing " \
            "in print in 1887, the character's popularity became widespread with the first series of short stories in The Strand Magazine, " \
            "beginning with A Scandal in Bohemia in 1891; additional stories appeared from then to 1927, eventually " \
                                                 "totalling four novels and 56 short stories. All but one are set in the" \
                                                 " Victorian or Edwardian periods, taking place between about 1880 to 1914. " \
                                                 "Most are narrated by the character of Holmes's friend and biographer " \
                                                 "Dr. Watson, who usually accompanies Holmes during his investigations and " \
        "often shares quarters with him at the address of 221B Baker Street, London, where many of the stories begin."

"Though not the first fictional detective, Sherlock Holmes is arguably the most well-known, with Guinness World Records " \
"listing him as the most portrayed movie characterin history.[1] Holmes's popularity and fame are such that many have " \
                                                   "believed him to be not a fictional character but a real individual;[2][3][4] " \
                "numerous literary and fan societies have been founded that pretend to operate on this principle. The stories" \
" and character have had a profound and lasting effect on mystery writing and popular culture as a whole, with both the " \
"original tales as well as thousands written by authors other than Conan Doyle being adapted into stage and radio plays, " \
"television, films, video games, and other media for over one hundred years."


article_data = Articles(title=title, author=author, category=category, image=image, image_small=image_small,
                        publication_date=publication_date, bodytext =body_text)
article_data.save()
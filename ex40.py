# Modules, Classes, and Objects

import ex40_mystuff # importing module we wrote

ex40_mystuff.apple()
print ex40_mystuff.tangerine

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I'm a classy apple!"

thing = MyStuff() # instantiate class
thing.apple() # runs the function "apple" from the class
print thing.tangerine # prints the variable "tangerine" from the class

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
    "With pockets full of shells"])

shake_it_off = Song(["I stay out too late", "Got nothing in my brain"])

shake_it_off2_lyrics = ["That's what people say", "Mmmm"]
shake_it_off2 = Song(shake_it_off2_lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
shake_it_off.sing_me_a_song()
shake_it_off2.sing_me_a_song()

class DetailedSong(object):

    def __init__(self, input_lyrics, artist):
        self.lyrics = input_lyrics

    def sing_me_a_song(self, num_times):
        for x in range(num_times):
            for line in self.lyrics:
                print line
        print self

all_about_that_bass_lyrics = ["Because I'm all about that bass", "That bass", "No treble"]
all_about_that_bass_artist = "Meaghan Trainor"
all_about_that_bass = DetailedSong(all_about_that_bass_lyrics, all_about_that_bass_artist)

print all_about_that_bass
all_about_that_bass.sing_me_a_song(2)
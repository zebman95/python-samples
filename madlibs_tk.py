import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class MadLibsApp(tk.Tk):
    def __init__(self, stories):
        tk.Tk.__init__(self)
        self.title("Mad Libs Game")
        self.stories = stories
        self.selected_story = None
        self.user_name = ""

        # Create a label
        self.name_label = tk.Label(self, text="Enter your name:")
        self.name_label.pack()

        # Create an entry widget for user's name
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Create a label for theme selection
        self.theme_label = tk.Label(self, text="Choose a theme:")
        self.theme_label.pack()

        # Create a dropdown menu
        self.theme_var = tk.StringVar(self)
        self.theme_dropdown = ttk.Combobox(self, textvariable=self.theme_var)
        self.theme_dropdown['values'] = list(self.stories.keys())
        self.theme_dropdown.pack()

        # Create a button
        self.button = tk.Button(self, text="Generate Story", command=self.generate_story)
        self.button.pack()

    def generate_story(self):
        self.user_name = self.name_entry.get()
        if not self.user_name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        theme_id = self.theme_var.get()
        if theme_id in self.stories:
            self.selected_story = self.stories[theme_id]
            self.selected_story.set_variables()  # Set variables for the selected story
            generated_story = self.selected_story.generate_story()  # Generate the story
            messagebox.showinfo("Generated Story", generated_story)  # Display the generated story
            messagebox.showinfo("Thank You", f"Thanks {self.user_name} for playing!")  # Show thank you message with user's name
        else:
            messagebox.showerror("Error", "Please select a valid theme.")

class MadLibsStory:
    def __init__(self, title, story_template, variables):
        self.title = title
        self.story_template = story_template
        self.variables = variables
        self.story_variables = {}

    def set_variables(self):
        for variable in self.variables:
            self.story_variables[variable] = simpledialog.askstring(f"Enter {variable}", f"Enter {variable}:")

    def generate_story(self):
        story = self.story_template
        for key, value in self.story_variables.items():
            story = story.replace(f"<{key}>", value)
        return story

stories = {
    "1": MadLibsStory("American Anthem Rewrite", "O say you <verb> by the dawn's early <noun> , What so <adverb> we <verb_in_past_tense> at the twilight's last gleaming, Whose broad <plural_noun> and bright <plural_noun> through the <adjective> fight, O'er the <plural_noun> we watched, were so gallantly <verb_ending_in_ing> ? And the rockets' <color> glare, the <plural_noun> bursting in <noun> Gave proof through the night that our <noun> was still there; <interjection> does that <adjective> banner yet <verb>, O'er the land of the <adjective> and the home of the <adjective> ?",
                      ["verb", "noun", "adverb", "verb_in_past_tense", "plural_noun", "adjective", "verb_ending_in_ing", "color", "interjection"]),
    "2": MadLibsStory("All About Me", "Hi I am <name>. I am <age> years old. My birthday is on <date>. I am from <country>. I live in <city>. My family is big. I have got <number_sisters> sisters and <number_brothers> brothers. We have got <pet>. It's cute and likes eating <food>. My mom is <mom_profession>. My dad is <dad_profession>. I want to become <desired_profession>. I like <hobby_verb_with_ing> in my free time, but I hate <something_you_hate_verb_ing>. My parents think I am <self_noun>. My hobby is <hobby>. I am a <personal_adj1> and <personal_adj2> person.",
                      ["name", "age", "date", "country", "city", "number_sisters", "number_brothers", "pet", "food", "mom_profession", "dad_profession", "desired_profession", "hobby_verb_with_ing", "something_you_hate_verb_ing", "self_noun", "hobby", "personal_adj1", "personal_adj2"]),
    "3": MadLibsStory("Basketball Commentator", "Hi! This is <person_in_room>, speaking to you from the broadcasting <noun> at the <adjective> forum. In case you <verb_past_tense> in late, the score between the Los Angeles <plural_noun> is a squeaker, 141 to <number>. This has been the most <adjective> game these adjective> eyes have seen in years. First, one team scores a <noun>, then <exclamation>!-the other team comes right back. Okay. Time-out is over. Los Angeles brings in the ball at mid- <noun>, fakes the defender out of his <noun> and shoots a <number> handed shot. It goes right through the <noun>. He beat the <noun>! The game is over just as the <noun> goes off. []",
                      ["person_in_room", "noun", "adjective", "verb_past_tense", "plural_noun", "number", "exclamation"]),
    "4": MadLibsStory("Fun Facts about Sea Life", "Studies have shown that sharks have been <verb_ending_in_ing> in the oceans for well over four hundred million years. Today there are more than <number> known species of sharks throughout the <a place>. Young, <adjective> sharks are called pups. They are born with full sets of teeth in their <part of the body (plural)>, and soon after birth, they leave their mothers because they are able to feed and <verb> on their own. One unusual quality about sharks is that they lose teeth on a regular basis, and new <plural noun> grow in their mouths to replace them. Most shark species eat things like fish, crustaceans, plankton, <type of food (plural)>, and <plural noun>. Sharks have exceptionally <adjective> senses, especially their ability to smell they live and <verb> in a wide range of aquatic habitat, such as a warm waters of the <a place> or the cooler <type of liquid> near the <a place>. Some species are at risk of becoming extinct, which would be a/an <adverb> terrible loss as sharks are not just awesome. They’re totally <adjective>!",
                      ["verb_ending_in_ing", "number", "a place", "adjective", "part of the body (plural)", "verb", "plural noun", "type of food (plural)", "adjective", "verb", "a place", "type of liquid", "a place", "adverb", "adjective"]),
    "5": MadLibsStory("The Space Shuttle", "In 1981, the U.S launched the first real space <noun>. It was named Columbia and was piloted by two brave <plural_noun>. They had practiced <verb_ending_in_ing> for two years and were expert <plural_noun> and soared off into the <adjective> blue <noun> . At an altitude of <number> feet it went into orbit around the noun . For people watching from earth it was a/an <adjective> sight to <verb> ! Who could really <verb> that there were two <plural_noun> in space? It was mind <verb_ending_in_ing> . After <number> orbits, the shuttle landed <adverb> at an air force <noun> . It was a/an <adjective> day for the U.S program",
                      ["noun", "plural_noun", "verb_ending_in_ing", "adjective", "number", "verb", "adverb"]),
    "6": MadLibsStory("My Report about Pizza", "Pizza was invented by a <adjective> <nationality> chef named <person> to make a pizza you need to take a lump of <noun> and make a round <adjective> <noun>. Then you cover it with <adjective> sauce, <adjective> cheese, and fresh chopped <plural noun> next you have to bake it in a very hot <noun> when it is done cut it into shapes some kids like <food> pizza the best but my favorite is the <food> pizza if I could, I would eat pizza <number> times a day",
                      ["adjective", "nationality", "person", "noun", "adjective", "noun", "adjective", "adjective", "plural noun", "noun", "food", "food", "number"]),
}

if __name__ == "__main__":
    app = MadLibsApp(stories)
    app.mainloop()


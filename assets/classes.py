class Person:
    def __init__(self):
        self.name = None
        self.given = None
        self.surname = None
        self.sex = None
        self.birth = []
        self.death = []
        self.sources = []
        self.notes = []
        self.events = []
        self.facts = []
        self.immigration = []
        self.occupations = []
        self.education = []
        self.residences = []
        self.allEvents = []
        self.titles = []
        self.links = []
        self.id = None
        self.familyChildID = None
        self.familySpouseIDs = []
        self.familyChild = None
        self.familySpouses = []


class Family:
    def __init__(self):
        self.id = None
        self.members = []
        self.parentOne = None
        self.parentTwo = None
        self.wife = None
        self.children = []


class Tree:
    def __init__(self, name=None, path=None, numPeople=None, numSources=None, numMedia=None):
        self.name = name
        self.path = path
        self.numPeople = numPeople
        self.numSources = numSources
        self.numMedia = numMedia


class Source:
    def __init__(self):
        self.date = None
        self.name = None
        self.author = None
        self.publisher = None
        self.repository = None
        self.location = None
        self.link = None
        self.id = None
        self.note = None
        self.conc = None
        self.attachedTo = []

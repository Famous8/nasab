from calendar import month_abbr

from assets.classes import Person, Family, Source
from datetime import datetime, time

# Creating GEDCOMParse class
class gedcomParse:
    def __init__(self, file):
        # Storing file contents
        self.fileContents = open(file, encoding="utf8").readlines()

        # Setting variables of class
        self.fullGedcom = []  # To store list of all people as objects
        self.familyList = []  # To store list of all families as objects
        self.sourcesList = []  # To store list of all sources as objects

        self.familyIDList = []  # To store IDs of all families in GEDCOM (as string)
        self.familyStart = None

        self.terms = ["\n", "/", "@", "DATE", "PLAC", "TITL", "_APID", "_WLNK", "SEX",
                      "HUSB", "WIFE", "CHIL", "OCCU", "EDUC", "RETI", "INDI", "NAME",
                      "GIVN", "SURN", "FAMC", "FAMS", "EVEN", "FACT", "BIRT", "DEAT",
                      "TYPE", "DATE", "SOUR", "PUBL", "AUTH", "FAM", "REPO", "NOTE",
                      "CONC", "RESI"]

        person = Person()

        current_index = 0  # To store which line it is iterating over
        indi = False  # To define whether an individual has been identified yet

        termList = {"1 NAME": "name",
                    "2 GIVN": "given",
                    "2 SURN": "surname",
                    "1 FAMC": "familyChildID",
                    "1 SEX": "sex"}

        # List of terms which have multiple corresponding lines succeeding them
        corrTermList = {"1 BIRT": "birth",
                        "1 DEAT": "death",
                        "1 OCCU": "occupations",
                        "1 EDUC": "education",
                        "1 _WLNK": "links",
                        "1 RESI": "residences",
                        "1 NOTE": "notes",
                        "1 EVEN": "events",
                        "1 FACT": "facts",
                        "1 IMMI": "immigration",
                        "1 RETI": "events"}

        # List of terms which are appended to a list
        appendingList = {"1 SOUR": "sources",
                         "2 SOUR": "sources",
                         "1 FAMS": "familySpouseIDs"}

        # List of terms which succeed the terms in the previous list
        succeedingList = ["2 DATE", "2 PLAC", "2 NOTE", "2 TITL", "2 TYPE"]

        while self.familyStart is None:
            line = self.fileContents[current_index]

            if line.startswith("0"):
                if "INDI" in line:
                    indi = True  # Individual has been identified

                    if person.name != None:
                        person.allEvents = self.sortEvents(person)
                        self.fullGedcom.append(person)  # Appending person to list if person has a name stored

                    person = Person()  # Creating a new instance of a person
                    person.id = self.remExtra(line)  # Setting Person's ID

                else:
                    indi = False

            if indi:
                if line[:6] in termList:  # Adding names to person, if they are an individual
                    entry = termList[line[:6]]
                    setattr(person, entry, self.remExtra(line))

                elif line[:6] in corrTermList:  # Initialising creation of term
                    x, y = 1, 0  # Will be used to store iteration
                    details = []  # Storing details in list
                    for term in succeedingList:  # Going through each term
                        if self.fileContents[current_index + x].startswith(term):  # Checking if next line starts with term
                            details.append(self.remExtra(self.fileContents[current_index + x]))  # Appending contents to details list

                        else:
                            details.append('')

                        x += 1

                    if self.remExtra(line):
                        details.append(self.remExtra(line))
                        y = 1

                    else:
                        details.append('')

                    entry = corrTermList[line[:6]]

                    if not details[4]:
                        details[4] = entry.capitalize()

                    getattr(person, entry).append(details)  # Appending contents to person
                    # Changing next line accordingly, checking how many lines it skipped
                    skipped = 0

                    for x in details:  # Should be made a one-liner
                        if x != "":
                            skipped += 1

                    current_index += (skipped - y)

                elif line[:6] in appendingList:
                    entry = appendingList[line[:6]]

                    if self.remExtra(line) not in getattr(person, entry):
                        getattr(person, entry).append(self.remExtra(line))

            if line.startswith("0 @F"):  # Setting where families are defined
                self.familyStart = current_index

            current_index += 1  # Going to the next line

        person.allEvents = self.sortEvents(person)
        self.fullGedcom.append(person)  # Appending last person to list
        self.createFamilies()
        self.createSources()

    def findPersonByID(self, id):  # Returns persons object from their ID
        for person in self.fullGedcom:
            if person.id == id:
                return person

        return None

    def retrieveSourceFromPerson(self, source):
        sources = []

        for person in self.fullGedcom:
            if source.id in person.sources:
                sources.append(person)
                person.sources[person.sources.index(source.id)] = source

        return sources

    def getURLFromAPID(self, apid):
        apid = self.remExtra(apid).split(":")
        link = f"https://www.ancestry.com/discoveryui-content/view/{apid[2]}:{apid[0].split(',')[1]}"

        return link

    def createSources(self):
        source = Source()
        sourceTerms = {"1 TITL": "name",
                       "1 AUTH": "author",
                       "1 PUBL": "publisher",
                       "2 DATE": "date",
                       "2 PLAC": "location",
                       "1 _APID": "link",
                       "1 REPO": "repository",
                       "1 NOTE": "note",
                       "2 CONC": "conc"}

        for y in range(self.familyStart, len(self.fileContents)):
            line = self.fileContents[y]

            if line.startswith("0") and "SOUR" in line:
                if source.id is not None:
                    self.sourcesList.append(source)
                    source = Source()
                    source.id = line.split("@")[1]

                source.id = line.split("@")[1]
                source.attachedTo = self.retrieveSourceFromPerson(source)

                x = 1  # Will be used to store iteration

                for term in sourceTerms:  # Going through each term
                    if self.fileContents[y + x].startswith(term):
                        entry = sourceTerms[term]
                        if term == "1 _APID":
                            setattr(source, entry, self.getURLFromAPID(self.fileContents[y + x]))

                        else:
                            setattr(source, entry, self.remExtra(self.fileContents[y + x]))

                        x += 1

        self.sourcesList.append(source)

    def createFamilies(self):
        family = Family()

        for x in range(self.familyStart, len(self.fileContents)):  # Iterating from where families begin being defined to end of file
            line = self.fileContents[x]  # Defining line
            if line.startswith("0 @F"):  # Checking if new family is defined in GEDCOM
                if family.id is not None:  # Checking if current family has been defined in program
                    self.familyList.append(family)  # Appending family to family list
                    family = Family()
                    family.id = self.remExtra(line)  # Setting family ID

                family.id = self.remExtra(line)

            if line.startswith("1 HUSB"):  # Checking if Husband defined
                person = self.findPersonByID(self.remExtra(line))

                if person:
                    family.parentOne = person
                    person.familySpouses.append(family)

                next = self.fileContents[x + 1]  # Setting next line

                if next.startswith("1 WIFE") or next.startswith("1 HUSB"):  # Checking if next line is another spouse
                    person = self.findPersonByID(self.remExtra(next))

                    if person:
                        family.parentTwo = person
                        person.familySpouses.append(family)  # Adding spouse to family

            elif line.startswith("1 WIFE") and family.parentOne is None:  # Checking if wife is only known spouse
                person = self.findPersonByID(self.remExtra(line))
                if person:
                    family.parentOne = person
                    person.familySpouses.append(family)  # Adding wife as only known spouse and parent

            elif line.startswith("1 CHIL"):  # Checking if the person is a child
                person = self.findPersonByID(self.remExtra(line))

                if person:
                    family.children.append(person)
                    person.familyChild = family  # Adding child to family

        self.familyList.append(family)  # Appending family to family list

    def sortEvents(self, person):
        events = []
        eventsLists = person.birth + person.facts + person.immigration + person.occupations + person.education + person.residences + person.death

        for event in eventsLists:
            events.append(event)

        events.sort(key=lambda z: self.sortEventsKey(z[0]))

        return events

    def sortEventsKey(self, date):
        dateSplit = date.split()

        for word in dateSplit:
            if word.isalpha() and word not in month_abbr:
                date = date.replace(word, "").strip()
                dateSplit.remove(word)

        if len(dateSplit) == 3:
            if dateSplit[0].isalpha():
                return datetime.strptime(date, "%b %d %Y")

            elif dateSplit[0].isnumeric():
                return datetime.strptime(date, "%d %b %Y")

        elif len(dateSplit) == 2:
            if len(dateSplit[0]) <= 2 and dateSplit[1].isalpha():
                return datetime.strptime(date, "%d %b")

            elif dateSplit[0].isalpha() and dateSplit[1].isnumeric():
                return datetime.strptime(date, "%b %Y")

        elif len(dateSplit) == 1:
            if dateSplit[0].isalpha():
                return datetime.strptime(date, "%b")

            elif "-" in dateSplit[0]:
                return datetime.strptime(dateSplit[0].split("-")[0], "%Y")

            elif dateSplit[0].isnumeric():
                return datetime.strptime(date[:4], "%Y")

        return datetime(9999, 1, 1)

    def findFamily(self, id):  # Returns family object from its ID
        for family in self.familyList:
            if id == family.id:
                return family

        return None

    def remExtra(self, line):  # Removing all extra characters from line
        for char in self.terms:  # Removing characters
            if char in line:
                line = line.replace(char, "")

        line = line[1:].strip()

        return line

if __name__ == '__main__':
    gedcom = gedcomParse("D:\Genealogy\The Rizvi-Zaidi-Kazmi Family Tree.ged")
    for person in gedcom.fullGedcom:
        print(vars(person))

    for source in gedcom.sourcesList:
        print(vars(source))

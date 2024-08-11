famous_person=" Albert\t\n \t\nEinstein "
famous_person=famous_person.strip()
famous_person=famous_person.replace('\t','')
famous_person=famous_person.replace('\n','')
famous_person=famous_person.replace(' ','')
print(famous_person)
class TopPersonal:

    def __init__(self, position, name, age, experience):
        self.position = position
        self.name = name
        self.age = age
        self.experience = experience
        self.is_top_personal = True

    def move(self):
        print(self)
        return f' {self.name}  {self.is_top_personal} - is the owner of the Business trip package'


if __name__ == '__main__':
    print(" Company OOO RUSH EVA")
    general_director = TopPersonal("General Director", "Ruslan", 51, 21)
    executive_director = TopPersonal("Executive Director", "Olha", 48, 15)
    deputy_director_for_project = TopPersonal("Deputy Director for Project", "Oleh", 38, 9)
    deputy_director_for_economics = TopPersonal("Deputy Director for Economics", "Lily", 52, 8)
    deputy_director_for_marketing = TopPersonal("Deputy Director for Marketing", "Galina", 45, 12)
    project_engineer = TopPersonal("Project Engineer", "Vitaliy", 36, 6)
    print(general_director.move())
    print(executive_director.move())
    print(deputy_director_for_project.move())
    print(deputy_director_for_economics.move())
    print(deputy_director_for_marketing.move())
    print(project_engineer.move)

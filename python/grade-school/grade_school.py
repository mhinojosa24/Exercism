class School(object):
    def __init__(self):

        self.dict = {}
        for num in range(0, 12):
            if num not in self.dict:
                self.dict[num] = []



    def __repr__(self):
        """Return a string representation of this queue."""
        return '{}'.format(self.dict)

    def add_student(self, name, grade):
        if type(name) is str:
            if grade in self.dict:
                self.dict[grade].append(name)
        self.dict[grade].sort()


    def roster(self):
        result_arry = []
        for values in self.dict.values():
            result_arry.extend(values)

        return result_arry

    def grade(self, grade_number):
        result = self.dict[grade_number]
        # print(result)
        return sorted(result)

def main():
    school = School()
    for name, grade in [
        ('Peter', 2),
        ('Anna', 1),
        ('Barb', 1),
        ('Zoe', 2),
        ('Alex', 2),
        ('Jim', 3),
        ('Charlie', 1),
    ]:
        school.add_student(name, grade)
    result = school.roster()
    print(result)

if __name__ == '__main__':
    main()

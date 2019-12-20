#problem
# class Bird:
#     def fly(self):
#         print('i\'m fly')
#
#
# def go_fly(bird):
#     if isinstance(bird, Bird):
#         bird.fly()
#
# class Falcon(Bird):
#     pass
#
# falcon = Falcon()
# go_fly(falcon)
#
# class Ostrich(Bird):
#     pass
#
# ostrich = Ostrich()
# go_fly(ostrich)

#problem with before and after conditions
class Bird:
    def fly(self):
        print('i\'m fly')
        return '100 km'

def go_fly(bird):
    if isinstance(bird, Bird):
        distance = bird.fly()
        print(distance)

class Falcon(Bird):
    def fly(self):
        print('i\'m fly')
        # return 200

falcon = Falcon()
go_fly(falcon)
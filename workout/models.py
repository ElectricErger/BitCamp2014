from django.db import models

class ExerciseEvent(models.Model):
    woType = models.CharField(max_length=100) #Stores in the name of a workout type from the program
    startTime = models.DateTimeField() #Time functions are stored in from Python because they're cleaner
    endTime = models.DateTimeField() #Same as above
    elapsedTime = models.IntegerField(default=0) #The time it took to finish
    location = models.CharField(max_length=100) #City/Town name goes here
    calories = models.IntegerField(default=0) #Maybe
    #Link it to a user
    def duration(self):
        self.elapsedTime=int((self.endTime-self.startTime).total_seconds())

    def __unicode__(self):
        return "A " + self.woType + " in " + self.location + " on " + str(self.startTime.date()) + " at " + str(self.startTime.time())


class Goal(models.Model):
    event = models.ForeignKey(ExerciseEvent) #All goals need Events, but not all events need goals
    gType = models.CharField(max_length=20) #Stored in from the site (Types: Distance, Calories, Time)
    gValue = models.IntegerField(default=0) #What do you want your: Distance, Calories, Time to be
    gActual = models.IntegerField(default=0) #The value at the end of the workout
    gSuccess = models.BooleanField(default=0) #boolean. T if you met your goal
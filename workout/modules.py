from django.db import models

class ExerciseEvent(models.Model):
    woType = models.CharField(max_length=100) #Stores in the name of a workout type from the program
    startTime = models.BigIntegerField(default=0) #Time functions are stored in from Python because they're cleaner
    elapsedTime = models.BigIntegerField(default=0) #Same as above
    location = models.CharField(max_length=100) #City/Town name goes here
    calories = models.IntegerField(default=0) #Maybe


class Goal(models.Model):
    event = models.ForeignKey(ExerciseEvent) #All goals need Events, but not all events need goals
    gType = models.CharField(max_length=20) #Stored in from the site (Types: Distance, Calories, Time)
    gValue = models.IntegerField(default=0) #What do you want your: Distance, Calories, Time to be
    gActual = models.IntegerField(default=0) #The value at the end of the workout
    gSuccess = models.BooleanField(default=0) #boolean. T if you met your goal
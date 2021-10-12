from django.db import models



class UserProfile(models.Model):     

    email = models.EmailField(max_length=30)                                                                                                                    
    street = models.TextField()    
    stree2 = models.TextField()                                                                                                                
    name = models.CharField(max_length=30)                                                                                                                     
    city = models.CharField(max_length=30)                                                                                                                 
    country = models.CharField(max_length=30)    

    def __str__(self):
    	return self.name


class Measurement(models.Model):     

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)                                                                                                                    
    weight = models.FloatField()    
    height = models.FloatField()                                                                                                                
    width = models.FloatField()                                                                                                                     
    dateTime = models.DateTimeField()


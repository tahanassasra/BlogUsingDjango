from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   #if we delete user it will delete profile but if we delete profile it does not delete user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # the directory uploaded image profiles that will be saved to


    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kawrgs):  #overwrite the save mothed(already exists) to resize the profile photos
        super().save( *args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



    
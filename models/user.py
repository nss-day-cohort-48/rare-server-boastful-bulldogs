class User():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, first_name="", last_name="", email="", bio="", username="", password="", profile_image_url="", created_on="", active=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active

# Hi team! Remember that our initilaization doesn't care about order if a variable is definited with the empty string above.
# If something doesn't work, please note that these are out of order!

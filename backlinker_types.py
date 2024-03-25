
class Customer():
    def __init__(self, email, position, name, website, existing_backlink_url, business_name, linkedin):
        self.email = email
        self.position = position
        self.name = name
        self.website = website
        self.existing_backlink_url = existing_backlink_url
        self.business_name = business_name
        self.linkedin = linkedin

    def to_str(self):
        return f"""Customer details:
    - Name: {self.name}
    - Position: {self.position}
    - Email: {self.email}
    - Business name: {self.business_name}
    - Website: {self.website}
    - Existing backlink: {self.existing_backlink_url}
    - LinkedIn profile: {self.linkedin}"""

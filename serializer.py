
# --------------------------------- EXAMPLE CLASS ----------------------------------------
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.age}, {self.email}"


# --------------------------------- SERIALIZER CLASS ----------------------------------------

class PersonSerializer:
    def __init__(self, instance=None, data=None):
        self.instance = instance
        self.data = data
        self.validated_data = {}
        self.errors = {}

    def is_valid(self):
        if self.data is None:
            self.errors['data'] = 'No data provided.'
            return False

        if 'name' not in self.data:
            self.errors['name'] = 'This field is required.'
        elif not isinstance(self.data['name'], str):
            self.errors['name'] = 'Must be a string.'

        if 'age' not in self.data:
            self.errors['age'] = 'This field is required.'
        elif not isinstance(self.data['age'], int):
            self.errors['age'] = 'Must be an integer.'

        if 'email' not in self.data:
            self.errors['email'] = 'This field is required.'
        elif not isinstance(self.data['email'], str):
            self.errors['email'] = 'Must be a string.'

        if self.errors:
            return False

        self.validated_data = {
            'name': self.data['name'],
            'age': self.data['age'],
            'email': self.data['email']
        }
        return True

    def save(self):
        if not self.validated_data:
            raise ValueError("Cannot save without validated data.")

        self.instance = Person(**self.validated_data)
        return self.instance

    def serialize(self):
        if self.instance is None:
            return None

        return {
            'name': self.instance.name,
            'age': self.instance.age,
            'email': self.instance.email
        }

# --------------------------------- USE CASE ----------------------------------------
# SERIALIZED; --------------------------------------------------------


# Create a new Person object
person = Person(name="Alice", age=30, email="alice@example.com")

# Initialize the serializer with the person instance
serializer = PersonSerializer(instance=person)

# Serialize the person object
serialized_data = serializer.serialize()

print("SERIALIZED DATA IN JSON FORMAT:  \n", f'>>| {serialized_data} |')

# DESERIALIZED; --------------------------------------------------------

# Data to be deserialized
data = {
    'name': 'Bob',
    'age': 25,
    'email': 'bob@example.com'
}

# Initialize the serializer with the data
serializer = PersonSerializer(data=data)

# Validate the data
if serializer.is_valid():
    # Save the data to create a new Person object
    person = serializer.save()
    print(person)
else:
    print(serializer.errors)


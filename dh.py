# use the class for individual object with the same behaviour 
class DH_Endpoint(object):
    # Calling the Initialization constructor as object is created from cthe class
    # call self for easy accessing of instances created within class
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
    # def to define the function created to generate Partial Key
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    # def to define the function created to generate Full Key
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    
u1_public=1257
u1_private=1999
u2_public= 1357
u2_private=1577
user1 = DH_Endpoint(u1_public, u2_public, u1_private)
user2 = DH_Endpoint(u1_public, u2_public, u2_private)

u1_partial=user1.generate_partial_key()
print("user1 partial key:",u1_partial) #1123

u2_partial=user2.generate_partial_key()
print("user2 partial key:",u2_partial)#1102

u1_full=user1.generate_full_key(u2_partial)
print("user1 full key:",u1_full) #986

u2_full=user2.generate_full_key(u1_partial)
print("user2 full key:",u2_full) #986



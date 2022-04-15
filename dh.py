# use the class for individual object with the same behaviour 
class DH_Endpoint(object):
    # Calling the Initialization constructor as object is created from cthe class
    # call self for easy accessing of instances created within class
    def __init__(self, pub_key1, pub_key2, priv_key):
        self.pub_key1 = pub_key1
        self.pub_key2 = pub_key2
        self.priv_key = priv_key
        self.full_key = None
    # def to define the function created to generate Partial Key
    def generate_partialkey(self):
        partialkey = self.pub_key1**self.priv_key
        partialkey = partialkey%self.pub_key2
        return partialkey
    
    # def to define the function created to generate Full Key
    def generate_full_key(self, partial_key_n):
        full_key = partial_key_n**self.priv_key
        full_key = full_key%self.pub_key2
        self.full_key = full_key
        return full_key
    
    
u1_public=1257
u1_private=1999
u2_public= 1357
u2_private=1577
user1 = DH_Endpoint(u1_public, u2_public, u1_private)
user2 = DH_Endpoint(u1_public, u2_public, u2_private)

u1_partial=user1.generate_partialkey()
print("user1 partial key:",u1_partial) #1123

u2_partial=user2.generate_partialkey()
print("user2 partial key:",u2_partial)#1102

u1_full=user1.generate_full_key(u2_partial)
print("user1 full key:",u1_full) #986

u2_full=user2.generate_full_key(u1_partial)
print("user2 full key:",u2_full) #986



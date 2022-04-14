class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message
    
    
u1_public=1257
u1_private=1999
u2_public= 1357
u2_private=1577
user1 = DH_Endpoint(u1_public, u2_public, u1_private)
user2 = DH_Endpoint(u1_public, u2_public, u2_private)

u1_partial=user1.generate_partial_key()
print("user1 partial key:",u1_partial) #147

u2_partial=user2.generate_partial_key()
print("user2 partial key:",u2_partial)

u1_full=user1.generate_full_key(u2_partial)
print("user1 full key:",u1_full) #75

u2_full=user2.generate_full_key(u1_partial)
print("user2 full key:",u2_full) #75



import hashlib
import time

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
def check(s):
    file = open("password_file.txt", "r")
    #read each line at a time
    read = file.readlines()
    for line in read:
      #splits each element into list
      array = line.split(",")
      user = array[0]
      salt = array[1]
      hashed = array[2].replace('\n', '')
      #Concatanate the password with the salt value
      newhash = concat(s, salt)
      newhash = hash_with_sha256(newhash)
      #Check if the passwords match
      if (newhash == hashed):
        print("You found the password.", user, s)
        return
    file.close()
    
def concat(s,salt):
    return s + salt

def brute_force(s,n):
    #checks if the string is length of the password we will try
    if (len(s) == n):
        #Goes to check password method if length is correct
        (check(s))
        return
    #Checks digits 0-9 and adds to string
    for i in range(10):  
        brute_force(s+str(i),n)

        
def main():
    s = ""
    for n in range(3,8):
        brute_force(s,n)
        
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
# --------------
##File path for the file 
def read_file(path):
    file=open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence
sample_message = read_file(file_path)

#Code starts here


# --------------
#Code starts here
def read_file(path1,path2):
    file1=open(path1,'r')
    file2=open(path2,'r')
    sen1=file1.readline()
    sen2=file2.readline()
    return sen1,sen2
    file1.close()
    file2.close()
message_1,message_2 =read_file(file_path_1,file_path_2)


def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return quotient
secret_msg_1 = str(fuse_msg(message_1,message_2))
print(secret_msg_1)




# --------------
#Code starts here
def read_file(path):
    file = open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence
message_3 = read_file(file_path_3)
print(message_3)


def substitute_msg(message_c):
    if(message_c=='Red'):
        sub ='Army General'
        return sub
    elif(message_c=='Green'):
        sub = 'Data Scientist'
        return sub
    else:
        sub='Marine Biologist'
        return sub
secret_msg_2 = str(substitute_msg(message_3))
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def read_file(path1,path2):
    file2=open(path1,'r')
    file1=open(path2,'r')
    sentence1 = file1.readline()
    sentence2 = file2.readline()
    file1.close()
    file2.close()
    return sentence1,sentence2

message_5,message_4 = read_file(file_path_4,file_path_5)
print(message_4,message_5)


def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[x for x in b_list if not x in  a_list]
    final_msg= ' '.join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_5,message_4)
print(secret_msg_3)








# --------------
#Code starts here
def read_file(path):
    file=open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence

message_6 = read_file(file_path_6)
print(message_6)


def extract_msg(message_f):
    a_list = message_6.split()
    b_list = list(filter(lambda x:len(x)%2==0,a_list))
    final_msg=' '.join(b_list)
    return final_msg

secret_msg_4 =str(extract_msg(message_6))
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=" ".join(message_parts)
print(secret_msg)
def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()
write_file(secret_msg,final_path)



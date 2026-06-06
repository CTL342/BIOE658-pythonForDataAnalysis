filepath = "/Users/christopherlee/Desktop/UMD/Courses/ENBC 311/ENBC 311 - Bonus Questions/"
username = input("Please enter your username: ")
password = input("Please enter your password: ")

def add_username_password_file(username, password, filename):
    with open(filename, 'w') as file:
        file.write(f"{username},{password}")
    file.close()

add_username_password_file(username, password, filepath + "database.txt")
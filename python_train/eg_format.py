import getpass
template_name = "my name"
user_name = getpass.getuser()
#
template_menu = 'Toolkit/{!r}/{}'.format(user_name,template_name)
print template_menu

# def A():
#     for i in range(4):
#         if i>2:
#             print i
#         A()
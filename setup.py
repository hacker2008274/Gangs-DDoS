import os

print("""
\x1b[38;2;255;20;147m╔═╗┌─┐┌┐┌┌─┐┌─┐  ╔╦╗┌─┐┬─┐┬┌─┌─┐
\x1b[38;2;255;20;147m║ ╦├─┤││││ ┬└─┐───║║├─┤├┬┘├┴┐└─┐
\x1b[38;2;255;20;147m╚═╝┴ ┴┘└┘└─┘└─┘  ═╩╝┴ ┴┴└─┴ ┴└─┘\x1b[38;2;0;255;58m>(setup)""")
print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install os")
    os.system("pip install socket")
    os.system("pip install os")
    os.system("pip install colorama")
    os.system("pip install Fore")
    os.system("pip install sys")

elif c == "1":
    os.system("pip3 install os")
    os.system("pip3 install socket")
    os.system("pip3 install os")
    os.system("pip3 install colorama")
    os.system("pip3 install Fore")
    os.system("pip3 install sys")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")

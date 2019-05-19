import subprocess

cmd = '"{nuke_path}" -t "{py_path}" "{str1}" "{str2}"'.format(
    nuke_path = "C:\Program Files\Nuke10.0v3/Nuke10.0.exe",
    py_path = "C:\Users\86131\Desktop/test2.py",
    str1 = "hello",
    str2 = "world",
)

subprocess.call(cmd,shell=True)
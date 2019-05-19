line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print re.split(r'[;,\s]\s*', line)
print re.split(r'[;,\s]*', line)
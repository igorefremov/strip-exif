# Copyright 2018 Igor Efremov
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import sys

from PIL import Image

def is_image(filepath):
    lfp = filepath.lower()
    return (lfp.endswith('.jpg') or lfp.endswith('.jpeg') or lfp.endswith('.png'))

def strip_file(filepath):
    print ('stripping %s... ' % filepath),
    sys.stdout.flush()
    
    try:
        Image.open(filepath).save(filepath)
        print 'done'
    except:
        print 'error - stopping!'
        sys.exit(-3)

def strip_dir(dirpath):
    if not dirpath.endswith('/'):
        dirpath += '/'
    
    for entry in os.listdir(dirpath):
        filepath = dirpath + entry
        if (not os.path.isfile(filepath)) or (not is_image(filepath)):
            continue
        strip_file(filepath)

if len(sys.argv) < 2:
    print 'usage: python %s file1.jpg file2.jpg dir1 dir2 ...' % sys.argv[0]
    sys.exit(-1)

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if os.path.isfile(arg) and is_image(arg):
        strip_file(arg)
    elif os.path.isdir(arg):
        strip_dir(arg)
    else:
        print 'invalid input: %s' % arg
        sys.exit(-2)

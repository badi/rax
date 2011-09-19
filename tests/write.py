
import fax

import sys
import os

mydirname = os.path.dirname(sys.argv[0])
inroot    = os.path.join(mydirname, 'relaxation-data')
outroot   = os.path.join(mydirname, 'test-write-project')
nprocs    = 1
pool      = fax.Pool(nprocs)

print 'Loading project from', inroot
project = fax.load_project(inroot, gens=[0], pool=pool)
print 'Read description:',  project.description
project.set_description('Hello World')
project.set_extrafiles([os.path.join(outroot,'README')])


print 'Writing project to', outroot
project.write(outroot, pool=pool)

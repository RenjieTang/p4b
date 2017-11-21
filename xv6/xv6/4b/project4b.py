import sys, os, inspect
import collections
import toolspath
from testing import Xv6Test, Xv6Build

curdir = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
def get_description(name):
  cfile = os.path.join(curdir, 'tests', name+'.c')
  with open(cfile, 'r') as f:
    desc = f.readline()
  desc = desc.strip()
  desc = desc[2:]
  if desc[-2:] == '*/':
    desc = desc[:-2]
  return desc.strip()

test_values = [
  ['create', 10],
  ['create2', 10],
  ['create3', 10],

  ['join', 10],
  ['join2', 10],
  ['join3', 10],

  ['recursion', 10],
  ['recursion2', 10],
  ['fork_clone', 10],
  ['clone_clone', 10],
  ['two_threads', 10],
  ['many_threads', 10],

  ['locks', 10],
  ['size', 10],

  ['cond', 10],
  ['cond2', 10],
  ['cond3', 10],
  ['cond4', 10],

]

hidden_tests = []#'create3', 'cond3', 'cond4', 'fork_clone', 'file', 'join3', 'many_threads', 'recursion2', 'size']
all_tests = []
build_test = Xv6Build
for testname, point_value in test_values:
  if testname in hidden_tests:
    continue
  members = {
      'name': testname,
      'tester': 'tests/' + testname + '.c',
      'description': get_description(testname),
      'timeout': 10,
      'point_value' : point_value
      }
  newclass = type(testname, (Xv6Test,), members)
  all_tests.append(newclass)
  setattr(sys.modules[__name__], testname, newclass)

class usertests(Xv6Test):
  name = 'usertests'
  tester = 'tests/usertests.c'
  description = get_description('usertests')
  timeout = 240

#all_tests.append(usertests)

from testing.runtests import main
main(build_test, all_tests)

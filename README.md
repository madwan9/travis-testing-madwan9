# travistest
Testing Travis CI

This repository is setup for students to do a first ditch effort at using github
AND using travis-ci to test code.  FYI the CI stands for "continuous integration" and it provides a way to constantly
test your code as your writing to make sure it is meeting your needs.

Read about the meaning of the various general files below and then read the assignment that follows:

There are a variety of files in the repository:

1)  README.md  -> this is the readme file for the repository.  It gives information on what is in the
                  repository and how to use it.  This is where your assignment would be described (like it is below).
                  A README.md can be expected for any GITHUB Repository (fancy way to say a place to store your code).
2)  .travis.cl -> this is the file that tells travis-ci to run a set of test code on a python file.
                  You should open this file up and take a look at what is in it to understand what
                  is happening within that particular file.  It basically gives travis-ci a set of commands that tell
                  it what language your using and what file contains some test codes for you to run.
3)  test.py    -> this file has a set of python commands/scripts that automatically run some tests on whatever code
                  is submitted.  This particular test.py file will run the function in testadd.py using 
                  the numbers 1 and 1.  It tests to make sure that the testadd.py code runs and yields an answer of 2.

As near as I can figure, the above three files will be in every repository where you are putting code to run AND that
has tests that you automatically want to run.  I will be providing these files for you and you shouldn't have to edit them.
There may be other files included that you, likewise, do not need to be concerned with.  The important files in your
GITHUB repositories will be some python file with helper code that you'll be editing and, possibly, some data file(s) 
that you may need to access to run the code.  

testadd.py -> this is the ACTUAL python code that you should edit in order to then test your code.
                  Edit the code so that it does what the docstring says.  The filename will vary in a given repository.  
                  For example, a problem set may have a title PS4.py (because XBOX sucks - videogame reference for those
                  who didn't catch it)

ASSIGNMENT
1)  You should have setup a github account and already cloned the travistest repository to your own account.
2)  Edit the code testadd.py so that it does what the docstring says.  
3)  Login to: travis-ci.com
4)  Link your github account to travis-ci.com by SIGNING UP WITH GITHUB
5)  Once you are signed up with GITHUB, you should be on the homepage of travis-ci.com
6)  In the upper left of the screen you should see a list of:
    MyRepositories     Running     +
7)  Hit the + button to add a repository
8)  Choose your repository named "travistest"
9)  You should receive the option to BUILD or RESTART BUILD
    - if you DON'T see this option to build (i.e. it shows you a picture of a road cone and says NO BUILDS AVAILABLE or
    something of that sort, it means you DON'T have a travis.cl file in your repository.  That file is what clues
    travis-ci.com into what to do to test your code).
10) Go ahead and run your build to see if you've edited testadd.py correctly.  You will see a few things popup to tell you that the 
    program is going to run a "virtual machine".  Travis is creating a virtual computer to load your code and run it through python for 
    you!  How kind of it :)
11) If your build is successful, the code will turn GREEN and you will see the line:
    test.py::FILENAME TESTED  PASSED in green
12) If your build is NOT successful, the code will turn RED and you will see the line:
    test.py::FILENAME TESTED FAILED in red
    If it fails, you can see error messages, use those to figure out your problem and go back to your github repository and make    
    changes, push those changes through to your travistest repository and restart your build once you think you've fixed your 
    problem(s).  
13) Good luck!  I'd value your opinion of if you prefer this method of turnin over canvas.

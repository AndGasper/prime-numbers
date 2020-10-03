# Check for Dependency Changes 

- Why?
- Because one should separate underlying dependency management logic/handling from say handling cached versions of test runners or some such.


## Note: probably excessive/hmmm? to have this pre-commit hook specify its own Pipfile/dependency for  


### Note: this definitely ain't it, chief. Should find a way to leverage the additional_dependencies = ['pre-commit:3.2'] and just figure out the path.
# DS Deloitte 0212 Checkpoints

This is a repository that will contain all the checkpoints of the Deloitte 0212 cohorts. Here are the steps to get this repo locally:

1. FORK this repository, creating a copy on your own GitHub account

2. Then clone your fork down to your local computer
```
git clone https://github.com/[yourusername]/DS-Deloitte-0212-Checkpoints.git
```
3. Add the ```/flatiron-school/``` version as the upstream (to pull future changes)
```
git remote add upstream https://github.com/flatiron-school/DS-Deloitte-0212-Checkpoints.git
```
4.You can make changes to the notebooks now! Remember to push your changes to your forked version of the repo (to put your local changes up online):
```
git add [filename]
git commit -m 'message here'
git push
```

Whenever you want to get updated notes:

5. Grab the changes from the upstream repo
```
git fetch upstream
```
6. Merge new changes onto your local repo
```
git merge upstream/main -m "meaningful message about what you're updating"
```

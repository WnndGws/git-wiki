File is located in `.git/hooks/pre-commit`

The git hook itself is only two lines…

```zsh
./auto_toc.py
git add .
```

Now when I do a git commit git will automatically run the Python script, generating the super index, and then adding these changes to the staging area and of course being lumped into the commit that kicked off the hook in the first place.

# My cheatsheet

- I try to use "Trunk-based" development where I can.
  - Key to this is using feat-flags
  - feat-flags should reference an issue somehow to allow tracking

## From the start

- Authenticate with `gh auth login`
- Choose a repo from `gh repo list`
- Clone repo with `gh repo clone repon-name`

## Making changes

- check encryption with `git-crypt status`
  - can unlock the repo using gpg key assuming it was locked using `git-crypt add-gpg-user KEY` (which is what I use, just make sure to use the E key)

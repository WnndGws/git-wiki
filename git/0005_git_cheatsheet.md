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

### Trunk-based in a team

- Use `git clone REPO` to get the repo initially
- Start adding changes to files, just make sure to use feature flags
  - Feature flags basically means lots of `if-then` statements in the code, and read a local config file, or system state etc
- Every now and then run `git fetch --all --prune` to see what changes have been made to `origin/main` since the last time I pulled or pushed to it
  - You will likely see something like `98169c3..6b4ca35  master -> origin/master` in the output telling me that I am on commit `98169c3` but the latest commit to main is `6b4ca35`
  - I want to rebase my changes on-top of the changes already made using `git rebase --autostash origin/main`
  - I have essentially now updated my git log to match the current state of `origin/main` and my commits I made since the last pull are then tacked onto the end
  - Autostash just stashes any uncommited work, and then pops it back after the rebase
  - When done adding complete change, add a tag to denote that this is where we are up to

### Trunk-based alone

- Use `gh repo clone REPO` to get the repo
- Make all changes
- Use `git add` and `git push` etc, when full feature is complete add a new release using `gh release create`

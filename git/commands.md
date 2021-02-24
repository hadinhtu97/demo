# Git commands basic

## Commit
* `git add` : stage change
  * `git add <file>`
  * `git add .`
* `git commit -m 'subject'` : commit stage changed . previous commit is prrent of this commit
  * `git commit -m 'subject' -m 'description'`
  * ![commit](images/commit.png)

## Branch
* `git branch` : view all branch
  * `git branch <name>` : create new branch
  * `git branch -d <name>` : delete a branch
  * `git checkout <name>` : move to branch name
  * `git checkout -b <name>` : create and move to new branch

## Combine branch
* `git merge <branchName>` : merge a branch into current branch. In practive, we work in a develop branch, then go back to main branch, then merge main branch with develop branch. Merge with create a new commit has two parent, first is a previous commit in main branch, second is a previous commit in develop branch
  * ![before merge](images/before-merge.png)
  * `git merge bugFix`
  * ![merged](images/merged.png)
* `git rebase <branchName>` : rebase a branch into current branch.
  * ![before rebase](images/before-rebase.png)
  * `git rebase main`
  * ![rebased](images/rebased.png)
* `git cherry-pick <commit1> <commit2> ...` : move commits into current branch
  * ![img](images/before-cherry-pick.png)
  * `git cherry-pick C2 C4`
  * ![img](images/cherry-pick.png)

## Move
* HEAD: is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of. HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD. Normally HEAD points to a branch name (like bugFix). When you commit, the status of bugFix is altered and this change is visible through HEAD.
  * ![main](images/main.png)
  * `git checkout C1`
  * ![head](images/head.png)
* Relative refs: `^` : moving upwards one commit or `~number` : moving upwards number commit
  * ![before moving](images/before-moving.png)
  * `git checkout main^`
  * ![moving](images/moving.png)

## Reverse
* `git reset` : reverts changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;". git reset will move a branch backwards as if the commit had never been made in the first place.
  * ![img](images/before-reset.png)
  * `git reset HEAD^`
  * ![img](images/reset.png)
* `git revert` : resetting works great for local branches on your own machine, its method of "rewriting history" doesn't work for remote branches that others are using. In order to reverse changes and share those reversed changes with others, we need to use git revert. Let's see it in action.
  * ![img](images/before-reset.png)
  * `git revert HEAD`
  * ![img](images/revert.png)
  * new commit C2' introduces changes -- it just happens to introduce changes that exactly reverses the commit of C2.
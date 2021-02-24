# A Successful Git Branching Model
Gitflow is a Git workflow. The Gitflow defines a strict branching model designed around the project release. This provides a robust framework for managing larger projects.
> [Source](https://nvie.com/posts/a-successful-git-branching-model/)

![img](images/a-successful-git-branching-model.png)

## Main branches
The central repo holds two main branches with an infinite lifetime:
* `master`
* `develop`
* ![img](images/main-branches.png)


`origin/master` is the main branch where the source code of HEAD always reflects a production-ready state.

`origin/develop` is the main branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release.

When the source code in the `develop` branch reaches a stable point and is ready to be released, all of the changes should be merged back into `master` somehow and then tagged with a release number.

Therefore, each time when changes are merged back into master, this is a new production release by definition.

## Supporting branches
Unlike the main branches, these branches always have a limited life time, since they will be removed eventually :
* `feature`
* `release` 
* `hotfix`

Each of these branches have a specific purpose and are bound to strict rules as to which branches may be their originating branch and which branches must be their merge targets.

### Feature branches
* May branch off from: `develop`
* Must merge back into: `develop`
* Branch naming convention:anything except `master`, `develop`, `release-*`, or `hotfix-*`
* ![img](images/feature-branch.png)

`feature` branches (or sometimes called topic branches) are used to develop new features for the upcoming or a distant future release.

The essence of a `feature` branch is that it exists as long as the feature is in development, but will eventually be merged back into `develop` (to definitely add the new feature to the upcoming release) or discarded (in case of a disappointing experiment).
* Create a new feature branch: `git checkout -b myfeature develop`
* Finishes a feature branch: 
  * `git checkout develop`
  * `git merge --no-ff myfeature`  (--no-ff flag causes the merge to always create a new commit object, even if the merge could be performed with a fast-forward)
  * `git branch -d myfeature`
  * `git push origin develop`

### Release branches
* May branch off from: `develop`
* Must merge back into: `develop` and `master`
* Branch naming convention: `release-*`

`release` branches support preparation of a new production release. They allow for minor bug fixes and preparing meta-data for a release (version number, build dates, etc.). By doing all of this work on a release branch, the develop branch is cleared to receive features for the next big release.

The key moment to branch off a new `release` branch from `develop` is when `develop` (almost) reflects the desired state of the new release. 

For example, say version 1.2 is the current production release running live and causing troubles due to a severe bug. But changes on develop are yet unstable. We may then branch off a hotfix branch and start fixing the problem:
* Creating a release branch : `git checkout -b release-1.2 develop`
* This new branch may exist there for a while, until the release may be rolled out definitely. During that time, bug fixes may be applied in this branch (rather than on the develop branch). Adding large new features here is strictly prohibited. They must be merged into develop, and therefore, wait for the next big release.
* Finishing a release branch : 
  * `git checkout master` 
  * `git merge --no-ff release-1.2` : the release branch is merged into `master` (since every commit on master is a new release by definition, remember)
  * `git tag -a 1.2` :  that commit on master must be tagged for easy future reference to this historical version
  * `git checkout develop`
  * `git merge --no-ff release-1.2` : Finally, the changes made on the release branch need to be merged back into `develop`, so that future releases also contain these bug fixes.
  * `git branch -d release-1.2`

### Hotfix branches
* May branch off from: `master`
* Must merge back into: `develop` and `master`
* Branch naming convention: `hotfix-*`
* ![img](images/hotfix-branch.png)

`hotfix` branches are very much like `release` branches in that they are also meant to prepare for a new production release, albeit unplanned. They arise from the necessity to act immediately upon an undesired state of a live production version.

When a critical bug in a production version must be resolved immediately, a `hotfix` branch may be branched off from the corresponding tag on the `master` branch that marks the production version. The essence is that work of team members (on the develop branch) can continue, while another person is preparing a quick production fix.

For example, say version 1.2 is the current production release running live and causing troubles due to a severe bug. But changes on develop are yet unstable. We may then branch off a hotfix branch and start fixing the problem:
* Creating the hotfix branch: `git checkout -b hotfix-1.2.1 master`
* Finishing a hotfix branch:
  * `git checkout master`
  * `git merge --no-ff hotfix-1.2.1`
  * `git tag -a 1.2.1`
  * `git checkout develop`
  * `git merge --no-ff hotfix-1.2.1`
  *  __when a `release` branch currently exists, the `hotfix` changes need to be merged into that `release` branch, instead of `develop`__
  *  `git branch -d hotfix-1.2.1`
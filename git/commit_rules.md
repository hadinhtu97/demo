# Rules of great git commit message

## Types of commit: 
* feat : The new feature you're adding to a particular application
* fix : A bug fix
* docs : Documentation only changes
* style : Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* refactor : A code change that neither fixes a bug nor adds a feature
* pert : A code change that improves performance
* test : Adding missing tests or correcting existing tests
* build : A code change that improves performance
* ci : Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
* chore : Regular code maintenance.
  
You can also use emojis to represent commit types
## Separate subject from body with a blank line
```
Derezz the master control program

MCP turned out to be evil and had become intent on world domination.
This commit throws Tron's disc into MCP (causing its deresolution)
and turns it back into a chess game.
```
## Limit the subject title in 50 characters
## Capitalize the subject line
## Do not end the subject title with the period (.)
## Use the imperative mood in the subect title

Wrong:
* Fixed bug with Y
* Changing behavior of X
* More fixes for broken stuff
* Sweet new API methods

A properly formed Git commit subject line should always be able to complete the following sentence:
> If applied, this commit will `your subject line here`.

Exam : 
* If applied, this commit will `refactor subsystem X for readability`
* If applied, this commit will `update getting started documentation`
* If applied, this commit will `remove deprecated methods`
* If applied, this commit will `release version 1.0.0`
* If applied, this commit will `merge pull request #123 from user/branch`

## Limit the body in 72 characters
## Use the body to explain what changes you have made and why you made them.
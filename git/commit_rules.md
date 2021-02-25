# Rules of great git commit message

## Format of commit
__<type><scope>: <message>__

__Type__
* `feat` : The new feature you're adding to a particular application
* `fix` : A bug fix
* `docs` : Documentation only changes
* `style` : Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* `refactor` : A code change that neither fixes a bug nor adds a feature
* `test` : Adding missing tests or correcting existing tests
* `chore` : Updating grunt tasks etc; no production code change

__Scope__
* `init`
* `runner`
* `watcher`
* `config`
* `web-server`
* `proxy`
* etc.

__Examples__ 
> `feat: add login page`
> `fix: make links open in new tab`
> `docs: add documentation of project`
> `style: add missing semi-colons`
> `refactor: change name function getUser to getUserData`
> `test: test valid data when fech from database`
> `chore: ignore env to .gitignore`

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
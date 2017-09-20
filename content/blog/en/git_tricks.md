Title: Useful git tricks
Date: 2017-04-15
Slug: git-tricks
lang: en
tags: git

Following some useful tricks for `git` and related remote hosts (`github`, `gitlab`, etc.)

## Difference of a file **after** `git pull`
If you want to see the differences of a file after you have pulled just type:

    $ git pull
    $ git diff HEAD@{1} file

## Checking out a Pull Request locally
Checkout a Pull Request is not only useful but almost mandatory before merging
the changes to the production branch.

The process is super easy:

    # find the PR ID on github

    # fetch the changes of the pull request into a new branch
    $ git fetch origin pull/ID/head:BRANCHNAME

    # checkout to the branch
    $ git checkout BRANCHNAME


after testing the Pull Request code it can be merged with github.

For more information just have a look to the [github docs](https://help.github.com/articles/checking-out-pull-requests-locally/)

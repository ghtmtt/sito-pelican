Title: Checkout a Pull Request locally
Date: 2017-08-24
Slug: checkout-pr-github
lang: en
tags: git, github

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

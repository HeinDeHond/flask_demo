### How to use this repository
## Git Basics for Beginners

### Create your own fork and clone it to your local machine

1. **Create your own fork:** Forking a repository means making a personal copy of someone else's project. In this case, you'll create your own copy of the repository you want to work with.

2. **Clone the fork to your local machine:** Cloning means downloading a copy of the repository to your computer so that you can work on it locally. To do this, you'll need to use the `git clone` command followed by the URL of your forked repository. This will create a local copy on your machine.

3. **Open folder containing a project with Pycharm IDE**: After having this folder locally, open it with pycharm using "File -> Open ..." item from a top menu.

### Working with Chapters and Branches

- Each chapter in the exercises is split into a separate branch in the repository. For example, there may be branches like `chapter_1`, `chapter_2`, and so on. A branch is like a separate line of development that allows you to work on different features or modifications independently.

- To navigate to a specific chapter, you can use the `git checkout` command followed by the name of the chapter/branch. For example, if you want to work on `chapter_1`, you would run the command `git checkout chapter_1`. This will switch your working directory to that particular chapter/branch.

### Making Changes and Committing

1. **Edit your code and make changes:** Once you are inside the repository and on the desired chapter/branch, you can make edits and changes to your code using any code editor or IDE of your choice. This could involve writing new code, modifying existing code, or fixing bugs.

2. **Add changes to Git and create a commit:** After you've made the necessary changes to your code, you need to tell Git to track those changes. You can use the `git add` command to add specific files or `git add .` to add all the changes in the current directory. After that, you can create a commit using the `git commit` command. A commit is like a snapshot of your code at a specific point in time and acts as a record of the changes you've made.

### Pushing Your Changes

1. **Push your changes back:** Once you've created a commit, you can push your changes back to your forked repository. Pushing means uploading your commits to the remote repository. You can use the `git push` command to do this. After pushing, your changes will be visible in your forked repository.

Remember, this is just a simplified explanation of the process. Git offers many more features and commands, but understanding these steps should give you a good starting point for working with Git and version control.


### How to run
Install flask with:
```shell
pip install flask
```

After this run app.py either with your IDE or:
```shell
python app.py
```

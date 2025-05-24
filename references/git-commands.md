# Git Commands Used on Day 1

## Initial Configuration Commands

### `git config --global user.email "baobind1@gmail.com"`
**Purpose:** Sets your email address for all Git repositories on your computer. This email appears in your commit history and helps identify who made changes.

### `git config --global user.name "Baobin"`
**Purpose:** Sets your name for all Git repositories. This name appears alongside your email in commit messages.

### `git config --list`
**Purpose:** Shows all your Git configuration settings. Useful to verify your setup is correct.

## Repository Setup Commands

### `git init`
**Purpose:** Initializes a new Git repository in the current directory. Creates a hidden `.git` folder that tracks all changes.

### `git remote add origin https://github.com/Baobin878/infrastructure-journey.git`
**Purpose:** Links your local repository to a remote repository on GitHub. "origin" is the default name for your main remote repository.

### `git remote set-url origin https://github.com/Baobin878/infrastructure-journey.git`
**Purpose:** Changes the URL of an existing remote repository. We used this to fix the username issue (Baobin → Baobin878).

## Basic Workflow Commands

### `git add .`
**Purpose:** Stages all changed files in the current directory for commit. The dot (.) means "all files." You can also add specific files with `git add filename`.

### `git commit -m "Day 1: Created system info collector script"`
**Purpose:** Creates a snapshot of your staged changes with a descriptive message. The -m flag lets you add the message inline.

### `git push -u origin main`
**Purpose:** Uploads your commits to the remote repository. The -u flag sets up tracking between your local and remote branches. After first use, you can just use `git push`.

## Branch Management

### `git branch -M main`
**Purpose:** Renames the current branch to "main". We used this because GitHub now uses "main" as the default branch name instead of "master".

## Status and Information Commands

### `git status`
**Purpose:** Shows the current state of your repository - which files are modified, staged, or untracked. Always useful to check before committing.

### `git log`
**Purpose:** Shows the commit history. Use `git log --oneline` for a condensed view.

### `git remote -v`
**Purpose:** Shows all remote repositories connected to your local repo with their URLs. The -v flag means "verbose".

## Synchronization Commands

### `git pull`
**Purpose:** Downloads changes from the remote repository and merges them into your current branch. Essential when working across multiple machines.

### `git push`
**Purpose:** Uploads your local commits to the remote repository. After initial setup with -u flag, this simpler version works.

## Common Git Workflow

```bash
# 1. Check what's changed
git status

# 2. Add changes to staging
git add .                    # Add everything
# OR
git add filename.py          # Add specific file

# 3. Commit with message
git commit -m "Descriptive message about what changed"

# 4. Push to GitHub
git push

# 5. On different machine, pull changes
git pull
```

## Troubleshooting Commands We Used

### When authentication failed:
- Created Personal Access Token on GitHub
- Used token as password instead of GitHub password

### When remote repository wasn't found:
- Created repository on GitHub.com first
- Used correct username (Baobin878 not Baobin)

### When branch name was wrong:
- Used `git branch -M main` to rename from master to main

## Pro Tips

1. **Always pull before starting work** on a different machine
2. **Commit often** with clear messages
3. **Use `.gitignore`** to exclude files you don't want to track
4. **Check `git status`** before committing to see what you're about to commit

## Next Git Commands to Learn

- `git clone` - Copy a repository from GitHub to your computer
- `git branch` - Create and manage branches
- `git checkout` - Switch between branches
- `git merge` - Combine branches
- `git diff` - See what changed in files
- `git reset` - Undo changes
- `git stash` - Temporarily save changes

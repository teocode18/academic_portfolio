
## **Git Branching Simple Guide**

Working with branches is key to team development with Git, but also has risks.  
Keep your working pattern as simple as possible.  
Avoid working on the same part of the code as your teammates.  
Agree on work to complete and communicate regularly.  
Don’t leave hanging branches (apologies for the pun!).

---

## **Check-up**

- `git status` — **Check current repository status**

---

## **Creating a Branch (from main)**

- `git branch` — **List branches**  
- `git branch "my_name"` — **Create a new branch with name "my_name"**  
- `git branch -d "my_name"` — **Delete the branch with name "my_name"**

---

## **Working in That Branch**

- `git checkout "my_name"` — **Switch to the named branch**  
- `git commit` — **Commits now apply in that branch**  
- `git push` — **Push your work before attempting to merge**

---

## **Merging From Your Branch to Main**  
*(must be on the `main` branch first)*

- `git checkout main` — **Switch to the main branch (the destination)**  
- `git pull` — **Update the main branch (others may have made changes)**  
- `git merge "my_name"` — **Merge the named branch into main**  
- `git branch -d "my_name"` — **Delete the branch after successful merge**

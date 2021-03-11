import subprocess as cmd
def git_push_automation():
    try:
        cmd.run("git init", check=True, shell=True)
        no_of_ex=int(input("Enter no of extension : "))
        ex=""
        for i in range(no_of_ex):
            kk=input(f"Enter Extension {i} : ")
            ex=ex+("*"+kk+" ")
        cmd.run(f"git add {ex}", check=True, shell=True)
        cmd.run('git commit -m "first commit"', check=True, shell=True)
        cmd.run("git branch -M main", check=True, shell=True)
        git_repo=input("Enter repo : ")
        cmd.run(f'git remote add origin {git_repo}', check=True, shell=True)
        cmd.run("git push -u origin main", check=True, shell=True)
        print("Success")
        return True
    except Exception as e:
        print(e)
        return False

git_push_automation()





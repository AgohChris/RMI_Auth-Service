import subprocess
import datetime

commit_message=input("Entre un méssage pour le commit : ")

if commit_message=="":
    msgDate = datetime.datetime.now().strftime('%d-%m-%Y à %H:%M:%S')
    commit_message = f"Auto-commit du : {msgDate}"

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    
    branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
    
    subprocess.run(["git", "push", "origin", branch], check=True)

    print(f"✅ Commit et push effectués sur la branche '{branch}' message : {commit_message}")

except subprocess.CalledProcessError as e:
    print(f"❌ Erreur lors de l'exécution de Git : {e}")

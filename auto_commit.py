import subprocess
import datetime


def autoCommit(succes=""):
    commit_message = input("Entre un méssage pour le commit : ")
        
    if commit_message == "":
        commit_message = f"Auto-commit du : {datetime.datetime.now().strftime('%d-%m-%Y à %H:%M:%S')}"

    try:
        # Vérifie si des modifications sont présentes
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
        if not status:
            print("❌ Aucun changement détecté, rien à valider.")
            return "❌ Aucun changement détecté, rien à valider."

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
        
        subprocess.run(["git", "push", "origin", branch], check=True)

        succes = f"✅ Commit et push effectués sur la branche '{branch}' message : {commit_message}"
        print(succes)

    except subprocess.CalledProcessError as e:
        succes = f"❌ Erreur lors de l'exécution de Git : {e}"
        print(succes)
        
    return succes


if __name__ == "__main__":
    autoCommit()